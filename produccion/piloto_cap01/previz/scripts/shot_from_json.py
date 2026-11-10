# -*- coding: utf-8 -*-
"""shot_from_json.py - arma una llamada de previz a partir de su ficha shots/<id>.json.

  blender -b <set>/tren_blockout.blend -P shot_from_json.py -- --json shots/c05a.json --out <trabajo>/render/c05a/c05a.blend

Que hace:
  - Varios PLANOS dentro de una llamada, con CORTE SECO en el cuadro exacto: una camara por plano (CAM_<plano>),
    ligada a un marcador de la linea de tiempo en su primer cuadro. Cuadro k <-> t = k / fps. Cuadros 0 .. N-1.
  - Camara con sensor de 36 mm en encaje vertical (9:16), focal en mm, posicion / objetivo por claves con
    aceleracion y frenada, temblor de operador (ruido con semilla por plano), respiracion, vibracion,
    vaiven del tren y sacudidas con retardo en cuadros respecto de un impacto.
  - Figuras (posicion, giro, inclinacion, cabeza, postura), barras-brazo, bota, props, puertas y vidrios que revientan.
  - Todo queda horneado: una clave por cuadro y por canal. El .blend resultante se puede abrir y revisar.

Formato de la ficha: ver README.md de esta carpeta. Las coordenadas son relativas al ancla "origin" (un vacio ANC_*
del set), con los ejes del mundo: +Y hacia la cabeza del tren, +X derecha mirando adelante, +Z arriba.
Los tiempos "t" son segundos desde el inicio de la LLAMADA (no del plano).
"""
import argparse
import json
import math
import os
import random
import sys

import bpy
from mathutils import Euler, Matrix, Quaternion, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import previz_lib as L      # noqa: E402
import previz_tiempos as T  # noqa: E402

TAU = 2.0 * math.pi

# ------------------------------------------------------------------------------------------------ curvas

def suavizar(u, tipo="inout"):
    """Curva de llegada a una clave. Nada es lineal por defecto: el movimiento arranca y frena."""
    u = 0.0 if u < 0.0 else 1.0 if u > 1.0 else u
    if tipo == "linear":
        return u
    if tipo == "in":          # arranca lento y llega con velocidad
        return u ** 2.4
    if tipo == "out":         # sale rapido y frena
        return 1.0 - (1.0 - u) ** 2.4
    if tipo == "snap":        # golpe: casi quieto y descarga al final (el impacto cae en la clave)
        return u ** 4.0
    if tipo == "hold":        # salta en la clave
        return 1.0 if u >= 1.0 else 0.0
    if tipo == "back":        # llega, se pasa un poco y vuelve
        c1 = 1.70158
        c3 = c1 + 1.0
        return 1.0 + c3 * (u - 1.0) ** 3 + c1 * (u - 1.0) ** 2
    return u * u * u * (u * (6.0 * u - 15.0) + 10.0)   # inout


_RUIDO = {}


def ruido(t, semilla, hz, octavas=3):
    """Ruido suave y determinista en [-1, 1]: suma de senos con frecuencias y fases sorteadas por semilla."""
    clave = (semilla, round(hz, 4), octavas)
    par = _RUIDO.get(clave)
    if par is None:
        rnd = random.Random(str(clave))   # str: semilla estable entre corridas (sin hash aleatorio)
        par = [(hz * (1.93 ** i) * rnd.uniform(0.8, 1.25), 1.0 / (1.7 ** i), rnd.uniform(0.0, TAU)) for i in range(octavas)]
        _RUIDO[clave] = par
    s = sum(a * math.sin(TAU * f * t + ph) for f, a, ph in par)
    return s / sum(a for _, a, _ in par)


def semilla_de(texto):
    return sum((i + 1) * ord(c) for i, c in enumerate(texto)) % 100000


# ------------------------------------------------------------------------------------------------ claves

def completar(claves):
    """Cada clave hereda de la anterior los campos que no declara."""
    out, prev = [], {}
    for k in sorted(claves, key=lambda k: k.get("t", 0.0)):
        full = dict(prev)
        full.update(k)
        if "ease" not in k:
            full.pop("ease", None)
        out.append(full)
        prev = {a: b for a, b in full.items() if a != "ease"}
    return out


def _mezcla(a, b, e):
    if isinstance(a, Vector):
        return a.lerp(b, e)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + (b - a) * e
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)) and len(a) == len(b):
        return [x + (y - x) * e for x, y in zip(a, b)]
    return b if e >= 1.0 else a


def valor_en(claves, t, resolver=None, campos_ref=()):
    """Interpola una lista de claves completas en t. Los campos de campos_ref se resuelven a punto de mundo."""
    def val(k):
        d = {}
        for c, v in k.items():
            if c in ("t", "ease"):
                continue
            d[c] = resolver(v) if (resolver and c in campos_ref) else v
        return d
    if t <= claves[0]["t"]:
        return val(claves[0])
    if t >= claves[-1]["t"]:
        return val(claves[-1])
    for a, b in zip(claves, claves[1:]):
        if a["t"] <= t <= b["t"]:
            u = (t - a["t"]) / max(1e-9, b["t"] - a["t"])
            e = suavizar(u, b.get("ease", "inout"))
            va, vb = val(a), val(b)
            return {c: _mezcla(va.get(c, vb.get(c)), vb.get(c, va.get(c)), e) for c in set(va) | set(vb)}
    return val(claves[-1])


# ------------------------------------------------------------------------------------------------ contexto

class Llamada:
    def __init__(self, ficha):
        self.ficha = ficha
        self.fps = int(ficha.get("fps", 24))
        self.n, self.planos = T.planos_en_cuadros(ficha)
        self.por_id = {sh["id"]: sh for sh in ficha["shots"]}
        ancla = bpy.data.objects.get(ficha["origin"])
        if ancla is None:
            raise KeyError("No existe el ancla %r en el set" % ficha["origin"])
        self.origen = ancla.matrix_world.translation.copy()
        v = ficha.get("train_sway", {})
        self.vaiven = {"m": v.get("m", 0.006), "deg": v.get("deg", 0.30), "hz": v.get("hz", 0.45)}
        self._memo = {}
        self._claves = {}

    # ---- claves completas, cacheadas por objeto de la ficha
    def claves(self, lista):
        c = self._claves.get(id(lista))
        if c is None:
            c = completar(lista)
            self._claves[id(lista)] = c
        return c

    # ---- vaiven del tren: ruido de muy baja frecuencia, con fase propia por objeto
    def vaiven_en(self, t, quien, escala=1.0):
        s = semilla_de(quien)
        dx = self.vaiven["m"] * escala * ruido(t, 7000 + s, self.vaiven["hz"], 2)
        rol = self.vaiven["deg"] * escala * ruido(t, 7100 + s, self.vaiven["hz"] * 0.8, 2)
        return dx, rol

    # ---- referencias a puntos del mundo
    def punto(self, ref, t, plano):
        if isinstance(ref, Vector):
            return ref
        if isinstance(ref, (list, tuple)):
            z = ref[2] if len(ref) > 2 else 0.0
            return self.origen + Vector((ref[0], ref[1], z))
        if isinstance(ref, str):
            return bpy.data.objects[ref].matrix_world.translation.copy()
        if isinstance(ref, dict):
            des = Vector(ref.get("offset", (0, 0, 0)))
            tt = t - ref.get("lag_s", 0.0)
            if "actor" in ref:
                return self.actor(plano, ref["actor"], tt)[ref.get("part", "cabeza")] + des
            if "prop" in ref:
                return self.prop(plano, ref["prop"], tt)["pos"] + des
            if "set" in ref:
                return bpy.data.objects[ref["set"]].matrix_world.translation.copy() + des
        raise ValueError("Referencia de punto no entendida: %r" % (ref,))

    # ---- estado de una figura en t (matrices de mundo y puntos utiles)
    def actor(self, plano, nombre, t):
        clave = ("a", plano["id"], nombre, round(t, 5))
        if clave in self._memo:
            return self._memo[clave]
        spec = plano["actors"][nombre]
        raiz = bpy.data.objects["FIG_" + nombre]
        d = L.dims_figura(raiz["altura"], raiz["ancho"])
        v = valor_en(self.claves(spec["keys"]), t, lambda r: self.punto(r, t, plano), ("pos",))
        postura = spec.get("pose", "de_pie")
        y_off, cad_z = d["posturas"][postura]
        pos = v["pos"].copy()
        dx, rol = self.vaiven_en(t, nombre, spec.get("sway", 1.0))
        pos.x += dx
        tr = spec.get("tremor")
        if tr:   # temblor del cuerpo (forcejeo, miedo): amplitud chica, frecuencia alta
            s = tr.get("seed", semilla_de(nombre))
            for i in range(3):
                pos[i] += tr.get("m", 0.004) * ruido(t, s + i, tr.get("hz", 6.0), 2) * (0.4 if i == 2 else 1.0)
        m_raiz = (Matrix.Translation(pos) @ Matrix.Rotation(math.radians(rol), 4, "Y")
                  @ Matrix.Rotation(math.radians(v.get("yaw", 0.0)), 4, "Z"))
        l_cad = (Matrix.Translation((0, y_off, cad_z + v.get("dz", 0.0)))
                 @ Matrix.Rotation(-math.radians(v.get("lean", 0.0)), 4, "X")
                 @ Matrix.Rotation(math.radians(v.get("side", 0.0)), 4, "Y"))
        l_cue = (Matrix.Translation((0, 0, d["torso_h"]))
                 @ Matrix.Rotation(math.radians(v.get("head_yaw", 0.0)), 4, "Z")
                 @ Matrix.Rotation(-math.radians(v.get("head_pitch", 0.0)), 4, "X")
                 @ Matrix.Rotation(math.radians(v.get("head_roll", 0.0)), 4, "Y"))
        m_cad = m_raiz @ l_cad
        m_cue = m_cad @ l_cue
        hx = d["ancho"] / 2 + 0.03
        st = {
            "m_raiz": m_raiz, "l_cad": l_cad, "l_cue": l_cue, "postura": postura, "d": d,
            "pies": m_raiz.translation.copy(),
            "cadera": m_cad.translation.copy(),
            "torso": m_cad @ Vector((0, 0, d["torso_h"] * 0.5)),
            "pecho": m_cad @ Vector((0, d["fondo"] / 2, d["torso_h"] * 0.75)),
            "espalda": m_cad @ Vector((0, -d["fondo"] / 2, d["torso_h"] * 0.80)),
            "hombro_R": m_cad @ Vector((hx, 0, d["torso_h"] - 0.07)),
            "hombro_L": m_cad @ Vector((-hx, 0, d["torso_h"] - 0.07)),
            "cabeza": m_cue @ Vector((0, 0, d["cuello"] + d["cabeza_r"])),
            "frente": m_cue.to_3x3() @ Vector((0, 1, 0)),
        }
        self._memo[clave] = st
        return st

    def prop(self, plano, nombre, t):
        clave = ("p", plano["id"], nombre, round(t, 5))
        if clave in self._memo:
            return self._memo[clave]
        spec = plano["props"][nombre]
        v = valor_en(self.claves(spec["keys"]), t, lambda r: self.punto(r, t, plano), ("pos",))
        pos = v["pos"].copy()
        rot = list(v.get("rot", (0, 0, 0)))
        tr = spec.get("tremor")
        if tr:
            s = tr.get("seed", semilla_de(nombre))
            for i in range(3):
                pos[i] += tr.get("m", 0.0) * ruido(t, s + i, tr.get("hz", 7.0), 2)
                rot[i] += tr.get("deg", 0.0) * ruido(t, s + 10 + i, tr.get("hz", 7.0), 2)
        st = {"pos": pos, "rot": Euler([math.radians(a) for a in rot], "XYZ")}
        self._memo[clave] = st
        return st


# ------------------------------------------------------------------------------------------------ horneado

class Horno:
    """Escribe claves por cuadro. Lleva el ultimo estado de visibilidad y el ultimo cuaternion por objeto."""

    def __init__(self):
        self.vis = {}
        self.quat = {}

    def visible(self, ob, v, f):
        if self.vis.get(ob.name) == v:
            return
        self.vis[ob.name] = v
        ob.hide_render = not v
        ob.hide_viewport = not v
        ob.keyframe_insert("hide_render", frame=f)
        ob.keyframe_insert("hide_viewport", frame=f)

    def loc(self, ob, p, f):
        ob.location = p
        ob.keyframe_insert("location", frame=f)

    def rot_q(self, ob, q, f):
        ob.rotation_mode = "QUATERNION"
        prev = self.quat.get(ob.name)
        if prev is not None and prev.dot(q) < 0.0:
            q = -q
        self.quat[ob.name] = q.copy()
        ob.rotation_quaternion = q
        ob.keyframe_insert("rotation_quaternion", frame=f)

    def matriz_local(self, ob, m, f):
        loc, q, _ = m.decompose()
        self.loc(ob, loc, f)
        self.rot_q(ob, q, f)

    def barra(self, ob, a, b, f):
        """Barra unitaria (crece en +Z) desde el punto a hasta el punto b."""
        v = b - a
        largo = max(0.02, v.length)
        self.loc(ob, a, f)
        self.rot_q(ob, v.normalized().to_track_quat("Z", "Y"), f)
        ob.scale = (1.0, 1.0, largo)
        ob.keyframe_insert("scale", frame=f)


def en_rango(spec, t):
    return spec.get("from_t", -1e9) <= t < spec.get("to_t", 1e9)


def hornear_camara(ll, h, cam, plano, t, f):
    c = plano["camera"]
    lag = c.get("lag_s", 0.0)

    def res(r):
        tt = t - lag if isinstance(r, dict) and ("actor" in r or "prop" in r) else t
        return ll.punto(r, tt, plano)

    v = valor_en(ll.claves(c["keys"]), t, res, ("pos", "look_at"))
    pos = v["pos"].copy()
    obj = v["look_at"]
    sid = c.get("handheld", {}).get("seed", semilla_de(plano["id"]))
    rx = ry = rz = 0.0

    hh = c.get("handheld")
    if hh:   # temblor de operador: deriva lenta + temblor fino cuya fuerza tambien respira (no es ruido parejo)
        hz, amp, tre = hh.get("hz", 0.7), hh.get("rot_deg", 0.4), hh.get("tremor", 0.18)
        env = 0.65 + 0.35 * ruido(t, sid + 50, 0.35, 2)
        rx += amp * (ruido(t, sid + 1, hz) + tre * env * ruido(t, sid + 11, hz * 8.0, 2))
        ry += amp * (ruido(t, sid + 2, hz * 0.9) + tre * env * ruido(t, sid + 12, hz * 7.3, 2))
        rz += amp * 0.45 * ruido(t, sid + 3, hz * 0.6)
        pm = hh.get("pos_m", 0.0)
        pos += Vector((ruido(t, sid + 21, hz * 0.8), ruido(t, sid + 22, hz * 0.7), ruido(t, sid + 23, hz * 1.1))) * pm
    br = c.get("breath")
    if br:   # respiracion: sube y baja lento
        ph = math.sin(TAU * br.get("hz", 0.3) * t + (sid % 7))
        pos.z += br.get("m", 0.003) * ph
        rx += br.get("deg", 0.08) * ph
    vb = c.get("vibration")
    if vb:   # vibracion del tren en una camara apoyada: amplitud muy chica, frecuencia alta
        rx += vb.get("deg", 0.05) * ruido(t, sid + 31, vb.get("hz", 9.0), 2)
        ry += vb.get("deg", 0.05) * 0.7 * ruido(t, sid + 32, vb.get("hz", 9.0) * 1.13, 2)
        pos.z += vb.get("m", 0.0008) * ruido(t, sid + 33, vb.get("hz", 9.0), 2)
    for i, sk in enumerate(c.get("shakes", [])):   # sacudida: parte delay_f cuadros DESPUES del impacto y decae
        t0 = sk["impact_t"] + sk.get("delay_f", 3) / float(ll.fps)
        tau = t - t0
        if tau >= 0.0:
            dur = sk.get("dur_s", 0.4)
            env = math.exp(-4.0 * tau / dur)
            if env > 0.003:
                hz, s2 = sk.get("hz", 9.0), sk.get("seed", sid + 100 + i)
                rnd = random.Random(s2)
                fa = [rnd.uniform(0.0, TAU) for _ in range(6)]
                rx += sk.get("deg", 1.5) * env * math.cos(TAU * hz * tau + fa[0] * 0.15)
                ry += sk.get("deg", 1.5) * 0.7 * env * math.sin(TAU * hz * 1.21 * tau + fa[1])
                rz += sk.get("deg", 1.5) * 0.5 * env * math.sin(TAU * hz * 0.83 * tau + fa[2])
                k = Vector(sk.get("kick", (0, 0, 0)))
                pos += k * env * math.cos(TAU * hz * 0.5 * tau)
                pos += Vector((math.sin(TAU * hz * tau + fa[3]), math.sin(TAU * hz * 1.3 * tau + fa[4]),
                               math.sin(TAU * hz * 0.9 * tau + fa[5]))) * sk.get("m", 0.01) * env
    if c.get("sway", True):
        dx, rol = ll.vaiven_en(t, "cam_" + plano["id"], c.get("sway_scale", 1.0))
        pos.x += dx
        rz += rol
    d = obj - pos
    if d.length < 1e-6:
        d = Vector((0, 1, 0))
    q = d.normalized().to_track_quat("-Z", "Y")
    q = q @ Quaternion((0, 0, 1), math.radians(v.get("roll", 0.0)))
    q = q @ Euler((math.radians(rx), math.radians(ry), math.radians(rz)), "XYZ").to_quaternion()
    h.loc(cam, pos, f)
    h.rot_q(cam, q, f)


def crear_esquirlas(col, vidrio, spec, n_cuadros, fps, f_rotura, h):
    """Esquirlas que salen del vidrio en el cuadro de la rotura (vidrio roto en trozos, no gotas)."""
    rnd = random.Random(spec.get("seed", 5))
    mw = vidrio.matrix_world
    w, alto = vidrio.get("ancho", 0.42), vidrio.get("alto", 0.55)
    centro = mw @ (sum((Vector(c) for c in vidrio.bound_box), Vector()) / 8.0)
    ejex = (mw.to_3x3() @ Vector((1, 0, 0))).normalized()
    direc = Vector(spec.get("dir", (0, -1, 0))).normalized()
    vel = spec.get("speed", 3.0)
    mat = bpy.data.materials["FX_esquirla"]
    for i in range(int(spec.get("n", 16))):
        s = rnd.uniform(0.02, 0.05)
        me = bpy.data.meshes.new("FX_esquirla_%02d" % i)
        me.from_pydata([(-s, 0, -s * 0.6), (s * 0.8, 0, -s * 0.3), (0, 0, s), (0, 0.006, 0)], [],
                       [(0, 1, 2), (0, 3, 1), (1, 3, 2), (2, 3, 0)])
        me.update()
        me.materials.append(mat)
        ob = bpy.data.objects.new("FX_esquirla_%02d" % i, me)
        col.objects.link(ob)
        ob.rotation_mode = "XYZ"
        p0 = centro + ejex * rnd.uniform(-w / 2, w / 2) + Vector((0, 0, rnd.uniform(-alto / 2, alto / 2)))
        v0 = direc * vel * rnd.uniform(0.45, 1.3) + ejex * rnd.uniform(-1.1, 1.1) + Vector((0, 0, rnd.uniform(-0.4, 1.6)))
        giro = Vector((rnd.uniform(-14, 14), rnd.uniform(-14, 14), rnd.uniform(-14, 14)))
        r0 = Vector((rnd.uniform(0, TAU), rnd.uniform(0, TAU), rnd.uniform(0, TAU)))
        h.visible(ob, False, 0)
        t_suelo = None
        for f in range(f_rotura, n_cuadros):
            tau = (f - f_rotura) / float(fps)
            p = p0 + v0 * tau + Vector((0, 0, -4.9 * tau * tau))
            if p.z <= 0.012:
                if t_suelo is None:
                    t_suelo = tau
                    p_suelo = Vector((p.x, p.y, 0.012))
                p, tau_r = p_suelo, t_suelo
            else:
                tau_r = tau
            if f == f_rotura:
                h.visible(ob, True, f)
            h.loc(ob, p, f)
            ob.rotation_euler = Euler(r0 + giro * tau_r, "XYZ")
            ob.keyframe_insert("rotation_euler", frame=f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", required=True, help="ficha de la llamada (shots/<id>.json)")
    ap.add_argument("--out", required=True, help=".blend de salida de la llamada")
    a = ap.parse_args(L.args_script())

    ficha = T.leer_ficha(a.json)
    fps = int(ficha.get("fps", 24))
    res = ficha.get("resolution", [720, 1280])
    sc = L.preparar_escena(fps, res)
    L.aplicar_luz(ficha.get("set_light", "neutro"))
    bpy.context.view_layer.update()
    try:
        bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"
    except Exception:
        pass

    ll = Llamada(ficha)
    h = Horno()
    sc.frame_start, sc.frame_end = 0, ll.n - 1
    sc["call_id"] = ficha["call_id"]

    col_cam = L.coleccion("CAMARAS")
    col_fx = L.coleccion("FX")
    figuras = [ob.name[4:] for ob in bpy.data.objects if ob.get("es_figura")]
    props = [ob.name[5:] for ob in bpy.data.objects if ob.get("es_prop")]

    # validacion temprana: nombres de la ficha contra el .blend
    for sh in ficha["shots"]:
        for n in sh.get("actors", {}):
            if n not in figuras:
                raise KeyError("Plano %s: no existe la figura %r (corre build_cast.py o revisa el nombre)" % (sh["id"], n))
        for n in sh.get("props", {}):
            if n not in props:
                raise KeyError("Plano %s: no existe el prop %r" % (sh["id"], n))

    # una camara por plano, ligada a un marcador en su primer cuadro (corte seco)
    camaras = {}
    for p in ll.planos:
        sh = ll.por_id[p["id"]]
        cd = bpy.data.cameras.new("CAM_" + p["id"])
        cd.sensor_fit = "VERTICAL"          # 9:16: los 36 mm del sensor van en el alto del cuadro
        cd.sensor_height = 36.0
        cd.sensor_width = 36.0 * res[0] / float(res[1])
        cd.lens = float(sh["camera"].get("lens_mm", ficha.get("lens_mm", 35)))
        cd.clip_start, cd.clip_end = 0.01, 200.0
        cam = bpy.data.objects.new("CAM_" + p["id"], cd)
        col_cam.objects.link(cam)
        cam.rotation_mode = "QUATERNION"
        camaras[p["id"]] = cam
        mk = sc.timeline_markers.new(p["id"], frame=p["f0"])
        mk.camera = cam
    sc.camera = camaras[ll.planos[0]["id"]]

    # puertas y vidrios: animacion de set a nivel de llamada (su estado se conserva entre planos)
    sa = ficha.get("set_anim", {})
    puertas = [(bpy.data.objects[d["object"]], completar(d["keys"])) for d in sa.get("doors", [])]
    for g in sa.get("glass_break", []):
        vid = bpy.data.objects[g["object"]]
        fb = T.cuadro(g["t"], fps)
        # el vidrio se evalua con la puerta en su estado del cuadro de rotura
        for ob, claves in puertas:
            ob.rotation_euler.z = ob["signo"] * math.radians(valor_en(claves, fb / float(fps))["open_deg"])
        bpy.context.view_layer.update()
        h.visible(vid, True, 0)
        h.visible(vid, False, fb)
        crear_esquirlas(col_fx, vid, g, ll.n, fps, fb, h)

    # "pared movil": objetos del set que un plano oculta para poder poner la camara donde iria la pared
    ocultables = sorted({n for sh in ficha["shots"] for n in sh.get("hide_set", [])})
    for n in ocultables:
        if bpy.data.objects.get(n) is None:
            raise KeyError("hide_set: no existe el objeto %r en el set" % n)

    plano_de = {}
    for p in ll.planos:
        for f in range(p["f0"], p["f1"]):
            plano_de[f] = p["id"]

    for f in range(ll.n):
        t = f / float(fps)
        sh = ll.por_id[plano_de[f]]
        visibles = set()

        for nombre, spec in sh.get("actors", {}).items():
            st = ll.actor(sh, nombre, t)
            h.matriz_local(bpy.data.objects["FIG_" + nombre], st["m_raiz"], f)
            h.matriz_local(bpy.data.objects[nombre + "_cadera"], st["l_cad"], f)
            h.matriz_local(bpy.data.objects[nombre + "_cuello"], st["l_cue"], f)
            visibles |= {nombre + "_" + L.PARTES_POSTURA[st["postura"]], nombre + "_torso", nombre + "_cabeza", nombre + "_nariz"}
            for lado, bs in spec.get("arms", {}).items():       # barra-brazo: solo si la mano es la accion
                if not en_rango(bs, t):
                    continue
                mano = valor_en(ll.claves(bs["keys"]), t, lambda r: ll.punto(r, t, sh), ("to",))["to"].copy()
                tm = bs.get("tremor_m", 0.0)
                if tm:
                    s = semilla_de(nombre + lado)
                    mano += Vector((ruido(t, s, 7.0, 2), ruido(t, s + 1, 6.3, 2), ruido(t, s + 2, 8.1, 2))) * tm
                h.barra(bpy.data.objects["%s_brazo_%s" % (nombre, lado)], st["hombro_" + lado], mano, f)
                visibles.add("%s_brazo_%s" % (nombre, lado))
            bt = spec.get("boot")
            if bt and en_rango(bt, t):
                vb = valor_en(ll.claves(bt["keys"]), t, lambda r: ll.punto(r, t, sh), ("pos",))
                bota = bpy.data.objects[nombre + "_bota"]
                h.loc(bota, vb["pos"], f)
                bota.rotation_euler = Euler((0, 0, math.radians(vb.get("yaw", 0.0))), "XYZ")
                bota.keyframe_insert("rotation_euler", frame=f)
                h.barra(bpy.data.objects[nombre + "_cana"], vb["pos"] + Vector((0, 0, 0.09)), st["cadera"], f)
                visibles |= {nombre + "_bota", nombre + "_cana"}

        for nombre in sh.get("props", {}):
            st = ll.prop(sh, nombre, t)
            ob = bpy.data.objects["PROP_" + nombre]
            h.loc(ob, st["pos"], f)
            ob.rotation_euler = st["rot"]
            ob.keyframe_insert("rotation_euler", frame=f)
            visibles.add("PROP_" + nombre)
            visibles |= {c.name for c in ob.children_recursive}

        for ob, claves in puertas:
            ob.rotation_euler.z = ob["signo"] * math.radians(valor_en(claves, t)["open_deg"])
            ob.keyframe_insert("rotation_euler", index=2, frame=f)

        hornear_camara(ll, h, camaras[sh["id"]], sh, t, f)

        for n in ocultables:
            h.visible(bpy.data.objects[n], n not in sh.get("hide_set", []), f)
        for n in figuras:
            for parte in L.partes_figura(n):
                ob = bpy.data.objects.get(parte)
                if ob is not None:
                    h.visible(ob, parte in visibles, f)
        for n in props:
            ob = bpy.data.objects["PROP_" + n]
            for o2 in [ob] + list(ob.children_recursive):
                h.visible(o2, o2.name in visibles, f)

    out = os.path.abspath(a.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=out)
    print("[shot_from_json] %s: %d cuadros a %d fps" % (ficha["call_id"], ll.n, fps))
    for p in ll.planos:
        print("[shot_from_json]   %-8s cuadros %3d-%3d  (%.3f-%.3f s)  %s mm" %
              (p["id"], p["f0"], p["f1"] - 1, p["f0"] / fps, p["f1"] / fps, ll.por_id[p["id"]]["camera"].get("lens_mm", "?")))
    print("[shot_from_json] OK ->", out)


if __name__ == "__main__":
    main()
