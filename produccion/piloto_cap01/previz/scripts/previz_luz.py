# -*- coding: utf-8 -*-
"""previz_luz.py - luz del gris solo desde fuentes que existen en el set (05: "luz solo de fuentes reales").

Se usa dentro de Blender (shot_from_json.py la monta y la hornea; render_shot.py la usa con EEVEE).
Workbench ignora estas luces: ahi sigue valiendo el tinte plano de previz_lib.aplicar_luz().

Fuentes, todas con objeto visible en el set:
  - apliques ambar: una luz puntual bajo cada lampara de lectura encendida (<vagon>_lampara_<fila>_<lado>).
    No son todas iguales: cada lampara trae su "factor" desde build_set.py.
  - rojo de emergencia: luces de area a lo largo de cada tira del cielo (<vagon>_tira, fuelle_tira).
  - tubo frio: solo dentro del ultimo vagon, sobre la puerta (ultimo_tubo_frio). Se enciende con el rojo.
  - cuarto del rapto: un solo foco duro y frio desde arriba (rapto_lampara).
Nada de relleno: el mundo queda casi negro. Los personajes (cilindros) llevan emision propia para leerse igual.

EL ROJO SE AJUSTA AQUI (pendiente de Cristian, 05): LUZ["rojo"]["color"] y LUZ["rojo"]["w_por_m"].
"""
import math

import bpy
from mathutils import Vector

LUZ = {
    "mundo": {"neutro": 0.05, "ambar": 0.0045, "ambar_bajo": 0.0032, "rojo": 0.0030, "negro": 0.0, "rapto": 0.0010},
    "mundo_color": {"neutro": (1, 1, 1), "ambar": (1.0, 0.8, 0.6), "ambar_bajo": (1.0, 0.8, 0.6),
                    "rojo": (1.0, 0.25, 0.22), "negro": (0, 0, 0), "rapto": (0.8, 0.9, 1.0)},
    "ambar": {"color": (1.0, 0.58, 0.24), "w": 75.0, "radio": 0.03, "emision": 9.0},
    "ambar_bajo_factor": 0.62,
    "rojo": {"color": (1.0, 0.035, 0.02), "w_por_m": 3.2, "paso_m": 1.0, "emision": 1.4},
    "tubo": {"color": (0.72, 0.86, 1.0), "w": 5.0, "emision": 2.0},
    "rapto": {"color": (0.86, 0.93, 1.0), "w": 700.0, "angulo_deg": 42.0, "emision": 12.0},
}
# Que grupo esta encendido en cada estado (factor sobre su potencia)
ESTADOS = {
    "neutro":     {"ambar": 1.0, "rojo": 0.0, "tubo": 0.0, "rapto": 1.0},
    "ambar":      {"ambar": 1.0, "rojo": 0.0, "tubo": 0.0, "rapto": 0.0},
    "ambar_bajo": {"ambar": LUZ["ambar_bajo_factor"], "rojo": 0.0, "tubo": 0.0, "rapto": 0.0},
    "rojo":       {"ambar": 0.0, "rojo": 1.0, "tubo": 1.0, "rapto": 0.0},
    "negro":      {"ambar": 0.0, "rojo": 0.0, "tubo": 0.0, "rapto": 0.0},
    "rapto":      {"ambar": 0.0, "rojo": 0.0, "tubo": 0.0, "rapto": 1.0},
}


def _col():
    col = bpy.data.collections.get("LUCES_SET")
    if col is None:
        col = bpy.data.collections.new("LUCES_SET")
        bpy.context.scene.collection.children.link(col)
    return col


def _luz(nombre, tipo, color, pos, rot=(0.0, 0.0, 0.0), **kw):
    ld = bpy.data.lights.new(nombre, tipo)
    ld.color = color
    ld.energy = 0.0
    for k, v in kw.items():
        setattr(ld, k, v)
    ob = bpy.data.objects.new(nombre, ld)
    ob.location = pos
    ob.rotation_euler = rot
    _col().objects.link(ob)
    return ob


def _bbox(ob):
    pts = [ob.matrix_world @ Vector(c) for c in ob.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return lo, hi


def _emisor(mat_nombre, color):
    """Devuelve el input de fuerza de emision del material (lo crea si falta). None si no existe el material."""
    mat = bpy.data.materials.get(mat_nombre)
    if mat is None:
        return None
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    ec = bsdf.inputs.get("Emission Color") or bsdf.inputs.get("Emission")
    ec.default_value = (color[0], color[1], color[2], 1.0)
    return bsdf.inputs["Emission Strength"]


def montar():
    """Crea las luces del set una sola vez. Devuelve {grupo: [(objeto_o_input, potencia_base), ...]}."""
    bpy.context.view_layer.update()
    grupos = {"ambar": [], "rojo": [], "tubo": [], "rapto": [], "emision": {}}
    A, R, Tb, Rp = LUZ["ambar"], LUZ["rojo"], LUZ["tubo"], LUZ["rapto"]
    for ob in bpy.data.objects:
        if ob.type != "MESH":
            continue
        n = ob.name
        if "_lampara_" in n and ob.get("es_lampara"):
            lo, hi = _bbox(ob)
            c = (lo + hi) / 2
            luz = _luz("LUZ_" + n, "POINT", A["color"], (c.x, c.y, lo.z - 0.05), shadow_soft_size=A["radio"])
            grupos["ambar"].append((luz, A["w"] * float(ob.get("factor", 1.0))))
        elif n.endswith("_tira"):
            lo, hi = _bbox(ob)
            largo = hi.y - lo.y
            k = max(1, int(round(largo / R["paso_m"])))
            for i in range(k):
                y = lo.y + (i + 0.5) * largo / k
                luz = _luz("LUZ_%s_%02d" % (n, i), "AREA", R["color"], ((lo.x + hi.x) / 2, y, lo.z - 0.02),
                           shape="RECTANGLE", size=0.08, size_y=largo / k * 0.9)
                grupos["rojo"].append((luz, R["w_por_m"] * largo / k))
        elif n == "ultimo_tubo_frio":
            lo, hi = _bbox(ob)
            c = (lo + hi) / 2
            luz = _luz("LUZ_tubo_frio", "AREA", Tb["color"], (c.x, lo.y - 0.03, lo.z - 0.02),
                       rot=(math.radians(-25), 0.0, 0.0), shape="RECTANGLE", size=hi.x - lo.x, size_y=0.05)
            grupos["tubo"].append((luz, Tb["w"]))
        elif n == "rapto_lampara":
            lo, hi = _bbox(ob)
            c = (lo + hi) / 2
            luz = _luz("LUZ_rapto", "SPOT", Rp["color"], (c.x, c.y, lo.z - 0.03), spot_size=math.radians(Rp["angulo_deg"]),
                       spot_blend=0.08, shadow_soft_size=0.02)
            grupos["rapto"].append((luz, Rp["w"]))
    grupos["emision"] = {
        "ambar": [(_emisor("SET_lampara_on", A["color"]), A["emision"])],
        "rojo": [(_emisor("SET_tira", R["color"]), R["emision"])],
        "tubo": [(_emisor("SET_tubo", Tb["color"]), Tb["emision"])],
        "rapto": [(_emisor("SET_rapto_lampara", Rp["color"]), Rp["emision"])],
    }
    return grupos


def estado_en(ficha, t):
    """Estado de luz en el segundo t de la llamada. "light_keys": [{"t": 0, "estado": "ambar"}, ...] (escalones)."""
    claves = ficha.get("light_keys")
    if not claves:
        return ficha.get("set_light", "neutro")
    est = claves[0]["estado"]
    for k in sorted(claves, key=lambda k: k["t"]):
        if t + 1e-6 >= k["t"]:
            est = k["estado"]
    return est


def hornear(grupos, ficha, n_cuadros, fps):
    """Una clave por cambio de estado, con interpolacion constante (las luces se cortan de golpe)."""
    mundo = bpy.context.scene.world
    bg = mundo.node_tree.nodes.get("Background") if mundo and mundo.use_nodes else None
    previo = None
    for f in range(n_cuadros):
        est = estado_en(ficha, f / float(fps))
        if est == previo:
            continue
        previo = est
        if est not in ESTADOS:
            raise ValueError("estado de luz desconocido: %r (opciones: %s)" % (est, ", ".join(ESTADOS)))
        fac = ESTADOS[est]
        for g in ("ambar", "rojo", "tubo", "rapto"):
            for luz, w in grupos[g]:
                luz.data.energy = w * fac[g]
                luz.data.keyframe_insert("energy", frame=f)
            for inp, e in grupos["emision"][g]:
                if inp is not None:
                    inp.default_value = e * fac[g]
                    inp.keyframe_insert("default_value", frame=f)
        if bg is not None:
            v, c = LUZ["mundo"][est], LUZ["mundo_color"][est]
            bg.inputs[0].default_value = (c[0] * v, c[1] * v, c[2] * v, 1.0)
            bg.inputs[1].default_value = 1.0
            bg.inputs[0].keyframe_insert("default_value", frame=f)
    # interpolacion constante en todo lo horneado aqui
    datos = [l.data for g in ("ambar", "rojo", "tubo", "rapto") for l, _ in grupos[g]]
    datos += [m for m in bpy.data.materials if m.name in ("SET_lampara_on", "SET_tira", "SET_tubo", "SET_rapto_lampara")]
    for d in datos + ([mundo] if mundo else []):
        ad = getattr(d, "animation_data", None)
        nt = getattr(d, "node_tree", None)
        for fuente in (ad, nt.animation_data if nt is not None else None):
            if fuente and fuente.action:
                for fc in fuente.action.fcurves:
                    for kp in fc.keyframe_points:
                        kp.interpolation = "CONSTANT"
