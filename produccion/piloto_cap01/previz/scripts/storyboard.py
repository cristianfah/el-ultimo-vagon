#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""storyboard.py - del gris a los stills A/B/C, la planta, el chequeo y las paginas de storyboard (07, 17-nov-2026).

  python3 storyboard.py armar   --json ../shots/c05b.json        # set+elenco (si falta) y la llamada (.blend + datos)
  python3 storyboard.py stills  --json ../shots/c05b.json [--samples 16] [--rapido]   # A/B/C + planta por plano
  python3 storyboard.py revisar --json ../shots/c05b.json        # tiempos, miradas al lente, lados, choques
  python3 storyboard.py todo    --json ../shots/c05b.json        # armar + stills + revisar
  python3 storyboard.py pagina  --bloque 5                        # paginas 3300x2550 del bloque
  python3 storyboard.py video   --json ../shots/c05b.json [--samples 6] [--workbench]   # cuadros + MP4 de referencia

Variables de entorno (o argumentos): PREVIZ_TRABAJO (carpeta de trabajo), BLENDER (ejecutable), FFMPEG.
Stills: cuadros reales de la camara del plano. A = inicio, B = momento clave, C = final (07: nunca angulos extra).
Se definen en la ficha por plano: "stills": {"A": {"t": 3.6, "desc": "..."}, "B": {...}, "C": {...}}. Si faltan,
A/B/C = primer cuadro, medio y ultimo de la ventana de montaje.
"""
import argparse
import glob
import json
import math
import os
import shutil
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PREVIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import previz_tiempos as T  # noqa: E402

TRABAJO = os.environ.get("PREVIZ_TRABAJO", os.path.join(PREVIZ, "_trabajo"))
BLENDER = os.environ.get("BLENDER", "blender")
FFMPEG = os.environ.get("FFMPEG", "ffmpeg")
FUENTE = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
FUENTE_B = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
RADIO = 0.16   # previz_lib.CILINDRO["radio"]
UMBRAL_CASI = 22.0   # nariz entre 14 y 22 grados del lente: aviso (se lee de frente aunque no mire al lente)

# copia de previz_lib.COLORES (este script corre fuera de Blender); se verifica contra previz_lib en armar()
COLORES = {
    "martina": (0.90, 0.74, 0.42), "tomas": (0.10, 0.20, 0.55), "diego": (0.74, 0.72, 0.62),
    "carmen": (0.45, 0.74, 0.90), "ivan": (0.42, 0.25, 0.12), "hugo": (0.72, 0.52, 0.14),
    "hombre_azul": (0.05, 0.40, 1.00), "esposa": (0.78, 0.55, 0.52), "enmascarado": (0.58, 0.58, 0.60),
    "infectado": (0.10, 0.10, 0.11), "extra": (0.30, 0.30, 0.33),
}
NOMBRE_COLOR = {
    "martina": "avena", "tomas": "azul marino", "diego": "piedra clara", "carmen": "celeste", "ivan": "café oscuro",
    "hugo": "bronce", "hombre_azul": "azul fuerte", "esposa": "beige rosado", "enmascarado": "gris liso",
    "infectado": "casi negro", "extra": "gris oscuro",
}
NOMBRE = {"martina": "Martina", "tomas": "Tomás", "diego": "Diego", "carmen": "Carmen", "ivan": "Iván", "hugo": "Hugo",
          "hombre_azul": "Hombre azul", "esposa": "Esposa", "enmascarado": "Figura con máscara",
          "infectado": "Infectados", "extra": "Pasajeros"}


def base(n):
    return n.rsplit("_", 1)[0] if n.startswith(("infectado_", "extra_")) else n


def correr(cmd, mostrar=("[", "Error", "Traceback", "  File ")):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for ln in p.stdout.splitlines():
        if any(ln.startswith(m) or m in ln for m in mostrar) and "EGL" not in ln:
            print(ln)
    if p.returncode != 0:
        print(p.stdout[-4000:])
        raise SystemExit("Fallo (%d): %s" % (p.returncode, " ".join(cmd[:5])))
    return p.stdout


def tiempos():
    with open(os.path.join(PREVIZ, "llamadas_tiempos.json"), encoding="utf-8") as fh:
        return {c["call_id"]: c for c in json.load(fh)["llamadas"]}


def rutas(cid):
    r = os.path.join(TRABAJO, "render", cid)
    return {"dir": r, "blend": os.path.join(r, cid + ".blend"), "datos": os.path.join(r, cid + "_datos.json"),
            "stills": os.path.join(TRABAJO, "stills", cid), "set": os.path.join(TRABAJO, "set", "tren_blockout.blend")}


# ------------------------------------------------------------------------------------------- armar

def armar(json_ficha, reconstruir_set=False):
    ficha = T.leer_ficha(json_ficha)
    R = rutas(ficha["call_id"])
    bl = [BLENDER, "-b", "--python-exit-code", "1"]
    if reconstruir_set or not os.path.isfile(R["set"]):
        os.makedirs(os.path.dirname(R["set"]), exist_ok=True)
        correr(bl + ["-P", os.path.join(AQUI, "build_set.py"), "--", "--out", R["set"]])
        correr(bl + [R["set"], "-P", os.path.join(AQUI, "build_cast.py"), "--", "--save"], ("[build_cast] OK", "Error", "Traceback"))
    os.makedirs(R["dir"], exist_ok=True)
    correr(bl + [R["set"], "-P", os.path.join(AQUI, "shot_from_json.py"), "--", "--json", os.path.abspath(json_ficha),
                 "--out", R["blend"], "--datos", R["datos"]])
    return ficha, R


# ------------------------------------------------------------------------------------------- geometria

def sub(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def norm(a):
    n = math.sqrt(dot(a, a)) or 1.0
    return [a[0] / n, a[1] / n, a[2] / n]


def proyectar(cuadro, lens, res, p):
    """Punto de mundo -> (u, v) en [0,1] de la imagen 9:16 (sensor vertical de 36 mm), o None si esta detras."""
    c = cuadro["cam"]
    fw, up = norm(c["dir"]), norm(c["up"])
    der = cross(fw, up)
    v = sub(p, c["pos"])
    z = dot(v, fw)
    if z <= 0.05:
        return None
    k = lens / 36.0
    W, H = res
    return 0.5 + dot(v, der) / z * k * H / W, 0.5 - dot(v, up) / z * k


def frames_stills(sh, plano, fps, ventana):
    """{letra: (cuadro, desc)} dentro del plano. Por defecto A/B/C en la ventana de montaje."""
    f0, f1 = plano["f0"], plano["f1"]
    lo = max(f0, int(round(ventana[0] * fps))) if ventana else f0
    hi = min(f1 - 1, int(round(ventana[1] * fps)) - 1) if ventana else f1 - 1
    spec = sh.get("stills")
    out = {}
    if spec:
        for letra in sorted(spec):
            s = spec[letra]
            out[letra] = (min(f1 - 1, max(f0, int(round(s["t"] * fps)))), s.get("desc", ""), s.get("lados"))
    else:
        out = {"A": (lo, "", None), "B": ((lo + hi) // 2, "", None), "C": (hi, "", None)}
    return out


# ------------------------------------------------------------------------------------------- stills

def stills(json_ficha, samples=16, rapido=False):
    ficha = T.leer_ficha(json_ficha)
    cid, fps, res = ficha["call_id"], int(ficha.get("fps", 24)), ficha.get("resolution", [720, 1280])
    R = rutas(cid)
    if not os.path.isfile(R["blend"]):
        armar(json_ficha)
    datos = json.load(open(R["datos"], encoding="utf-8"))
    tt = tiempos().get(cid, {})
    vent = {p["id"]: (p["de_s"], p["a_s"]) for p in tt.get("planos", [])}
    n, planos = T.planos_en_cuadros(ficha)
    por_id = {s["id"]: s for s in ficha["shots"]}
    if os.path.isdir(R["stills"]):
        shutil.rmtree(R["stills"])
    os.makedirs(R["stills"])
    pedido, indice = [], {"call_id": cid, "planos": []}
    for p in planos:
        fs = frames_stills(por_id[p["id"]], p, fps, vent.get(p["id"]))
        indice["planos"].append({"id": p["id"], "stills": {k: {"f": v[0], "t": round(v[0] / fps, 3), "desc": v[1],
                                                               "cam_z": round(datos["cuadros"][v[0]]["cam"]["pos"][2], 2)}
                                                           for k, v in fs.items()}})
        pedido += [v[0] for v in fs.values()]
    pedido = sorted(set(pedido))
    tmp = os.path.join(R["stills"], "_cuadros")
    motor = ["--engine", "BLENDER_WORKBENCH"] if rapido else ["--engine", "EEVEE", "--samples", str(samples)]
    correr([BLENDER, "-b", R["blend"], "-P", os.path.join(AQUI, "render_shot.py"), "--", "--out",
            os.path.join(tmp, "f_"), "--still"] + [str(f) for f in pedido] + motor)
    for pl in indice["planos"]:
        for letra, s in pl["stills"].items():
            dst = os.path.join(R["stills"], "%s_%s_%s.png" % (cid, pl["id"], letra))
            shutil.copy(os.path.join(tmp, "f_%04d.png" % s["f"]), dst)
            s["png"] = os.path.basename(dst)
    shutil.rmtree(tmp)
    # planta por plano (en el cuadro de B)
    for pl, p in zip(indice["planos"], planos):
        fb = pl["stills"].get("B", list(pl["stills"].values())[len(pl["stills"]) // 2])["f"]
        region = region_plano(datos, p)
        png = os.path.join(R["stills"], "%s_%s_planta.png" % (cid, p["id"]))
        correr([BLENDER, "-b", R["blend"], "-P", os.path.join(AQUI, "cenital.py"), "--", "--plano", p["id"], "--frame",
                str(fb), "--region"] + ["%.3f" % v for v in region] + ["--px", "900", "--out", png])
        dibujar_planta(png, region, datos, p, fb, ficha, por_id[p["id"]])
        pl["planta"] = os.path.basename(png)
        pl["region"] = region
    with open(os.path.join(R["stills"], "indice.json"), "w", encoding="utf-8") as fh:
        json.dump(indice, fh, ensure_ascii=False, indent=1)
    print("[storyboard] stills %s -> %s" % (cid, R["stills"]))
    return indice


def region_plano(datos, p):
    """Region de la planta: camara y personajes con nombre (infectados y pasajeros solo si no hay nadie mas)."""
    xs, ys = [], []
    cuadros = datos["cuadros"][p["f0"]:p["f1"]]
    principales = any(not n.startswith(("infectado_", "extra_")) for c in cuadros for n in c["actores"])
    for c in cuadros:
        xs.append(c["cam"]["pos"][0])
        ys.append(c["cam"]["pos"][1])
        for n, a in c["actores"].items():
            if principales and n.startswith(("infectado_", "extra_")):
                continue
            xs.append(a["pies"][0])
            ys.append(a["pies"][1])
    m = 0.9
    x0, x1, y0, y1 = min(xs) - m, max(xs) + m, min(ys) - m, max(ys) + m
    # al menos 3,2 m de ancho y proporcion vertical parecida al panel (9:16)
    w, h = max(3.2, x1 - x0), max(3.2, y1 - y0)
    if h < w * 1.2:
        h = w * 1.2
    if w < h / 1.9:
        w = h / 1.9
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]


def dibujar_planta(png, region, datos, p, fb, ficha, sh):
    from PIL import Image, ImageDraw, ImageFont
    im = Image.open(png).convert("RGB")
    W, H = im.size
    x0, y0, x1, y1 = region
    px = lambda q: ((q[0] - x0) / (x1 - x0) * W, (y1 - q[1]) / (y1 - y0) * H)   # noqa: E731
    d = ImageDraw.Draw(im, "RGBA")
    f = ImageFont.truetype(FUENTE_B, 26)
    fs = ImageFont.truetype(FUENTE, 20)
    cuadros = datos["cuadros"][p["f0"]:p["f1"]]
    # recorridos de los personajes
    for nombre in cuadros[0]["actores"]:
        pts = [px(c["actores"][nombre]["pies"]) for c in cuadros if nombre in c["actores"]]
        col = tuple(int(255 * v) for v in COLORES.get(base(nombre), (0.5, 0.5, 0.5)))
        if len(pts) > 1 and math.dist(pts[0], pts[-1]) > 8:
            d.line(pts, fill=col + (255,), width=5)
            flecha(d, pts[-2] if len(pts) > 2 else pts[0], pts[-1], col + (255,), 18)
    # camara: recorrido y cuna del campo de vision en B
    lens = next(pl["lens_mm"] for pl in datos["planos"] if pl["id"] == p["id"])
    cpts = [px(c["cam"]["pos"]) for c in cuadros]
    if math.dist(cpts[0], cpts[-1]) > 6:
        d.line(cpts, fill=(255, 255, 255, 255), width=4)
        flecha(d, cpts[-2], cpts[-1], (255, 255, 255, 255), 20)
    cb = datos["cuadros"][fb]["cam"]
    hfov = 2 * math.atan(36.0 * 9 / 16 / 2 / lens)
    ang = math.atan2(cb["dir"][1], cb["dir"][0])
    largo = 2.2
    o = px(cb["pos"])
    a1 = px([cb["pos"][0] + largo * math.cos(ang + hfov / 2), cb["pos"][1] + largo * math.sin(ang + hfov / 2)])
    a2 = px([cb["pos"][0] + largo * math.cos(ang - hfov / 2), cb["pos"][1] + largo * math.sin(ang - hfov / 2)])
    d.polygon([o, a1, a2], fill=(255, 255, 255, 50), outline=(255, 255, 255, 230))
    d.ellipse([o[0] - 11, o[1] - 11, o[0] + 11, o[1] + 11], fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=2)
    # nombres sobre la marca A
    for nombre, a in cuadros[0]["actores"].items():
        if nombre.startswith(("infectado_", "extra_")):
            continue
        q = px(a["pies"])
        txt = NOMBRE.get(nombre, nombre)
        d.text((q[0] + 16, q[1] - 34), txt, font=f, fill=(255, 255, 255, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))
    # escala y orientacion
    m1 = W / (x1 - x0)
    d.line([(20, H - 30), (20 + m1, H - 30)], fill=(255, 255, 255, 255), width=4)
    d.text((24, H - 62), "1 m", font=fs, fill=(255, 255, 255, 255))
    d.text((W - 230, 14), "↑ cabeza del tren", font=fs, fill=(255, 255, 255, 230))
    im.save(png)


def flecha(d, a, b, col, tam):
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    p1 = (b[0] - tam * math.cos(ang - 0.45), b[1] - tam * math.sin(ang - 0.45))
    p2 = (b[0] - tam * math.cos(ang + 0.45), b[1] - tam * math.sin(ang + 0.45))
    d.polygon([b, p1, p2], fill=col)


# ------------------------------------------------------------------------------------------- revisar

def revisar(json_ficha, umbral_deg=14.0):
    """Chequeos que mide el script (no opina un agente): tiempos, miradas al lente, lados de cuadro y choques."""
    ficha = T.leer_ficha(json_ficha)
    cid, fps, res = ficha["call_id"], int(ficha.get("fps", 24)), ficha.get("resolution", [720, 1280])
    R = rutas(cid)
    if not os.path.isfile(R["datos"]):
        armar(json_ficha)
    datos = json.load(open(R["datos"], encoding="utf-8"))
    tt = tiempos().get(cid)
    prob, avisos = [], []
    n, planos = T.planos_en_cuadros(ficha)
    if tt:
        if ficha["duration_s"] != tt["duration_s"]:
            prob.append("duration_s %s != %s de llamadas_tiempos.json" % (ficha["duration_s"], tt["duration_s"]))
        ids_f = [p["id"] for p in planos]
        ids_t = [p["id"] for p in tt["planos"]]
        if ids_f != ids_t:
            prob.append("planos %s != %s" % (ids_f, ids_t))
        for p, q in zip(planos, tt["planos"]):
            if p["id"] != q["id"]:
                continue
            if q["de_s"] < p["t0"] - 1e-6 or q["a_s"] > p["t1"] + 1e-6:
                prob.append("%s: la ventana de montaje %.2f-%.2f no cabe en el plano %.2f-%.2f" % (p["id"], q["de_s"], q["a_s"], p["t0"], p["t1"]))
    else:
        avisos.append("la llamada no esta en llamadas_tiempos.json")
    por_id = {s["id"]: s for s in ficha["shots"]}
    lens = {pl["id"]: pl["lens_mm"] for pl in datos["planos"]}
    vent = {p["id"]: (p["de_s"], p["a_s"]) for p in (tt or {}).get("planos", [])}
    for p in planos:
        sh = por_id[p["id"]]
        lo, hi = vent.get(p["id"], (p["t0"], p["t1"]))
        malos, casi = {}, {}
        for c in datos["cuadros"][p["f0"]:p["f1"]]:
            t = c["f"] / fps
            if t < lo - 1e-6 or t >= hi:
                continue
            for nombre, a in c["actores"].items():
                uv = proyectar(c, lens[p["id"]], res, a["cabeza"])
                if uv is None or not (0.0 <= uv[0] <= 1.0 and 0.0 <= uv[1] <= 1.0):
                    continue
                hacia = norm(sub(c["cam"]["pos"], a["cabeza"]))
                dist = math.sqrt(dot(sub(c["cam"]["pos"], a["cabeza"]), sub(c["cam"]["pos"], a["cabeza"])))
                ang = math.degrees(math.acos(max(-1.0, min(1.0, dot(norm(a["mira"]), hacia)))))
                if ang < umbral_deg and dist < 7.0 and not nombre.startswith("infectado_"):
                    malos.setdefault(nombre, []).append((c["f"], round(ang, 1)))
                elif ang < UMBRAL_CASI and dist < 4.0 and not nombre.startswith(("infectado_", "extra_")):
                    casi.setdefault(nombre, []).append((c["f"], round(ang, 1)))
        for nombre, lista in malos.items():
            prob.append("%s: %s mira al lente (nariz a < %.0f° de la camara) en %d cuadros de montaje, p. ej. cuadro %d (%.1f°)"
                        % (p["id"], nombre, umbral_deg, len(lista), lista[0][0], lista[0][1]))
        for nombre, lista in casi.items():   # 14-22°: en cuadro se lee como una cara de frente (revision del 18-nov)
            if nombre in malos:
                continue
            peor = min(lista, key=lambda x: x[1])
            avisos.append("%s: %s casi de frente al lente (nariz a < %.0f°) en %d cuadros de montaje; el peor, cuadro %d (%.1f°)"
                          % (p["id"], nombre, UMBRAL_CASI, len(lista), peor[0], peor[1]))
        # lados declarados en los stills
        for letra, s in (sh.get("stills") or {}).items():
            lados = s.get("lados")
            if not lados:
                continue
            f = min(p["f1"] - 1, max(p["f0"], int(round(s["t"] * fps))))
            c = datos["cuadros"][f]
            for nombre, lado in lados.items():
                if nombre not in c["actores"]:
                    prob.append("%s %s: %s no esta en el plano" % (p["id"], letra, nombre))
                    continue
                uv = proyectar(c, lens[p["id"]], res, c["actores"][nombre]["cabeza"])
                if uv is None:
                    prob.append("%s %s: %s queda detras de la camara" % (p["id"], letra, nombre))
                    continue
                real = "izq" if uv[0] < 0.5 else "der"
                if real != lado:
                    prob.append("%s %s: %s deberia estar a la %s del cuadro y esta a la %s (u=%.2f)" % (p["id"], letra, nombre, lado, real, uv[0]))
        # choques entre cilindros (gente fundida)
        choques = {}
        for c in datos["cuadros"][p["f0"]:p["f1"]]:
            ac = c["actores"]
            ns = sorted(ac)
            for i, a in enumerate(ns):
                for b in ns[i + 1:]:
                    dd = math.hypot(ac[a]["pies"][0] - ac[b]["pies"][0], ac[a]["pies"][1] - ac[b]["pies"][1])
                    if dd < 2 * RADIO - 0.03:
                        choques.setdefault((a, b), c["f"])
        for (a, b), f in choques.items():
            avisos.append("%s: %s y %s se tocan (cilindros superpuestos) desde el cuadro %d" % (p["id"], a, b, f))
    print("[revisar] %s: %d problemas, %d avisos" % (cid, len(prob), len(avisos)))
    for x in prob:
        print("  PROBLEMA", x)
    for x in avisos:
        print("  aviso", x)
    return prob, avisos


# ------------------------------------------------------------------------------------------- paginas

def envolver(d, txt, fuente, ancho):
    out = []
    for parrafo in txt.split("\n"):
        linea = ""
        palabras = []
        for pal in parrafo.split():            # una palabra mas ancha que la columna se parte por letras
            while d.textlength(pal, font=fuente) > ancho and len(pal) > 1:
                k = len(pal)
                while k > 1 and d.textlength(pal[:k], font=fuente) > ancho:
                    k -= 1
                palabras.append(pal[:k])
                pal = pal[k:]
            palabras.append(pal)
        for pal in palabras:
            prueba = (linea + " " + pal).strip()
            if d.textlength(prueba, font=fuente) <= ancho:
                linea = prueba
            else:
                if linea:
                    out.append(linea)
                linea = pal
        out.append(linea)
    return out


def pagina(bloque, salida=None):
    from PIL import Image, ImageDraw, ImageFont
    with open(os.path.join(PREVIZ, "bloques.json"), encoding="utf-8") as fh:
        bloques = json.load(fh)
    B = bloques[str(bloque)]
    tt = tiempos()
    with open(os.path.join(PREVIZ, "llamadas_tiempos.json"), encoding="utf-8") as fh:
        orden = json.load(fh)["orden_montaje"]
    unidades = []          # (call, plano, sh, stills_idx)
    elenco = set()
    for cid in B["llamadas"]:
        fj = os.path.join(PREVIZ, "shots", cid + ".json")
        ficha = T.leer_ficha(fj)
        idx = json.load(open(os.path.join(TRABAJO, "stills", cid, "indice.json"), encoding="utf-8"))
        por_id = {s["id"]: s for s in ficha["shots"]}
        for pl in idx["planos"]:
            if pl["id"] not in B.get("planos", [pl["id"]]):
                continue
            sh = por_id[pl["id"]]
            unidades.append((cid, pl, sh, ficha))
            elenco |= {base(a) for a in sh.get("actors", {})}
    unidades.sort(key=lambda u: orden.index(u[1]["id"]) if u[1]["id"] in orden else 999)
    PW, PH = 3300, 2550
    M, GAP_U = 40, 60
    UW = (PW - 2 * M - GAP_U) // 2
    PNW, PNH = 315, 560
    TX = UW - 4 * PNW - 3 * 10 - 20          # columna derecha: camara y montaje
    ABAJO = 150                               # texto bajo los paneles: A/B/C y que hay en cuadro
    ROW_H = 46 + PNH + ABAJO
    por_pag = 6
    paginas = [unidades[i:i + por_pag] for i in range(0, len(unidades), por_pag)]
    f_tit = ImageFont.truetype(FUENTE_B, 46)
    f_lay = ImageFont.truetype(FUENTE, 30)
    f_pl = ImageFont.truetype(FUENTE_B, 30)
    f_tx = ImageFont.truetype(FUENTE, 21)
    f_txb = ImageFont.truetype(FUENTE_B, 21)
    f_let = ImageFont.truetype(FUENTE_B, 40)
    f_pie = ImageFont.truetype(FUENTE, 24)
    salidas = []
    out_dir = salida or os.path.join(TRABAJO, "paginas")
    os.makedirs(out_dir, exist_ok=True)
    for k, us in enumerate(paginas):
        im = Image.new("RGB", (PW, PH), (243, 241, 236))
        d = ImageDraw.Draw(im)
        tit = "EUV · CAP01 · BLOQUE %s · %s" % (bloque, B["titulo"])
        if len(paginas) > 1:
            tit += "   (página %d de %d)" % (k + 1, len(paginas))
        d.text((M, 30), tit, font=f_tit, fill=(20, 20, 22))
        y = 96
        for ln in envolver(d, "Layout: " + B["layout"], f_lay, PW - 2 * M):
            d.text((M, y), ln, font=f_lay, fill=(40, 40, 44))
            y += 40
        y0 = y + 14
        # los paneles se achican si la nota de layout es larga: las filas nunca pisan la leyenda del pie
        filas_pag = (len(us) + 1) // 2
        alto_disp = (PH - 175) - y0
        PNH = min(560, int(alto_disp / max(1, filas_pag)) - 46 - ABAJO - 8)
        PNW = int(round(PNH * 9 / 16))
        TX = UW - 4 * PNW - 3 * 10 - 20
        ROW_H = 46 + PNH + ABAJO + 8
        for i, (cid, pl, sh, ficha) in enumerate(us):
            col, fila = i % 2, i // 2
            ux, uy = M + col * (UW + GAP_U), y0 + fila * ROW_H
            cam = sh["camera"]
            nom_cam = "CAM_%s_%s" % (sh["id"], (cam.get("tag") or ("MANO" if cam.get("handheld") else "FIJA")).upper())
            vent = next((q for q in tt[cid]["planos"] if q["id"] == sh["id"]), None)
            titulo = "%s · %s" % (sh["id"], sh.get("titulo", sh.get("descripcion", "")[:60]))
            d.text((ux, uy), titulo, font=f_pl, fill=(15, 15, 18))
            py = uy + 46
            letras = sorted(pl["stills"])
            for j, letra in enumerate(letras[:3]):
                s = pl["stills"][letra]
                th = Image.open(os.path.join(TRABAJO, "stills", cid, s["png"])).convert("RGB").resize((PNW, PNH), Image.LANCZOS)
                px_ = ux + j * (PNW + 10)
                im.paste(th, (px_, py))
                d.rectangle([px_, py, px_ + PNW - 1, py + PNH - 1], outline=(30, 30, 30), width=2)
                d.rectangle([px_ + 8, py + 8, px_ + 58, py + 58], fill=(15, 15, 15))
                d.text((px_ + 18, py + 10), letra, font=f_let, fill=(255, 255, 255))
                d.text((px_ + 66, py + 20), "%.2f s" % s["t"], font=f_tx, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))
            # planta
            px_ = ux + 3 * (PNW + 10)
            pi = Image.open(os.path.join(TRABAJO, "stills", cid, pl["planta"])).convert("RGB")
            esc = min(PNW / pi.width, PNH / pi.height)
            pi = pi.resize((max(1, int(pi.width * esc)), max(1, int(pi.height * esc))), Image.LANCZOS)
            d.rectangle([px_, py, px_ + PNW - 1, py + PNH - 1], fill=(20, 20, 22))
            im.paste(pi, (px_ + (PNW - pi.width) // 2, py + (PNH - pi.height) // 2))
            d.rectangle([px_, py, px_ + PNW - 1, py + PNH - 1], outline=(30, 30, 30), width=2)
            d.text((px_ + 10, py + PNH - 34), "PLANTA (en B)", font=f_txb, fill=(255, 255, 255))
            # columna derecha: camara (nombre, lente, altura, hacia donde mira, movimiento) y montaje
            tx, ty = ux + 4 * (PNW + 10) + 10, py
            sB = pl["stills"].get("B") or pl["stills"][letras[len(letras) // 2]]
            der = [("b", nom_cam), ("n", "%d mm · altura %.2f m" % (int(round(cam.get("lens_mm", 35))), sB.get("cam_z", 0.0))),
                   ("n", "Mira: " + (cam.get("mira", "").strip() or "—")), ("n", "Mov.: " + (cam.get("mov", "").strip() or "—"))]
            if vent:
                der.append(("n", "Montaje %.1f s · %s %.2f–%.2f s" % (vent["a_s"] - vent["de_s"], cid, vent["de_s"], vent["a_s"])))
            for tipo, txt in der:
                fnt = f_txb if tipo == "b" else f_tx
                for ln in envolver(d, txt, fnt, TX):
                    if ty > py + PNH - 4:
                        break
                    d.text((tx, ty), ln, font=fnt, fill=(25, 25, 28))
                    ty += 27
                ty += 8
            # debajo de los paneles: una linea por cuadro y que hay en cuadro
            ty = py + PNH + 8
            abajo = ["%s · %s" % (l_, pl["stills"][l_]["desc"]) for l_ in letras if pl["stills"][l_].get("desc")]
            if sh.get("en_cuadro"):
                abajo.append("En cuadro: " + sh["en_cuadro"])
            for txt in abajo:
                for ln in envolver(d, txt, f_tx, UW):
                    if ty > py + PNH + ABAJO - 24:
                        break
                    d.text((ux, ty), ln, font=f_tx, fill=(25, 25, 28))
                    ty += 26
        # pie: leyenda de cilindros
        yl = PH - 130
        d.line([(M, yl - 16), (PW - M, yl - 16)], fill=(150, 150, 150), width=2)
        xl = M
        d.text((xl, yl), "Cilindros (solo posición, mirada y recorrido; la nariz marca hacia dónde mira):", font=f_pie, fill=(20, 20, 22))
        xl, yl2 = M, yl + 40
        for n in ["martina", "tomas", "diego", "carmen", "ivan", "hugo", "hombre_azul", "esposa", "enmascarado", "extra", "infectado"]:
            if n not in elenco:
                continue
            c = tuple(int(255 * v) for v in COLORES[n])
            d.rectangle([xl, yl2 + 2, xl + 30, yl2 + 32], fill=c, outline=(0, 0, 0))
            txt = "%s · %s" % (NOMBRE[n], NOMBRE_COLOR[n])
            d.text((xl + 40, yl2 + 2), txt, font=f_pie, fill=(20, 20, 22))
            xl += 40 + int(d.textlength(txt, font=f_pie)) + 40
        d.text((M, yl2 + 46), "Cada número nuevo es un corte. A = inicio, B = momento clave, C = final; cuadros reales de la cámara del plano. "
                              "Gris de previz: el cuerpo, la cara y el look salen solo de las hojas de personaje.",
               font=f_pie, fill=(60, 60, 64))
        nombre = "pagina_bloque%s%s.jpg" % (bloque, ("_%d" % (k + 1)) if len(paginas) > 1 else "")
        ruta = os.path.join(out_dir, nombre)
        im.save(ruta, quality=90)
        salidas.append(ruta)
        print("[storyboard] pagina ->", ruta)
    return salidas


# ------------------------------------------------------------------------------------------- video

def video(json_ficha, samples=6, workbench=False):
    ficha = T.leer_ficha(json_ficha)
    cid = ficha["call_id"]
    R = rutas(cid)
    if not os.path.isfile(R["blend"]):
        armar(json_ficha)
    fdir = os.path.join(R["dir"], "cuadros")
    for v in glob.glob(os.path.join(fdir, "frame_*.png")):
        os.remove(v)
    motor = ["--engine", "BLENDER_WORKBENCH"] if workbench else ["--engine", "EEVEE", "--samples", str(samples)]
    correr([BLENDER, "-b", R["blend"], "-P", os.path.join(AQUI, "render_shot.py"), "--", "--out",
            os.path.join(fdir, "frame_")] + motor)
    correr([sys.executable, os.path.join(AQUI, "encode.py"), "--ffmpeg", FFMPEG, "--json", os.path.abspath(json_ficha),
            "--frames-dir", fdir, "--work", TRABAJO, "--font", FUENTE, "--tira", "4"])
    correr([sys.executable, os.path.join(AQUI, "check_ref.py"), "--ffmpeg", FFMPEG, "--json", os.path.abspath(json_ficha),
            "--ref", os.path.join(TRABAJO, "out", cid + "_ref.mp4"), "--frames-dir", fdir])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("accion", choices=["armar", "stills", "revisar", "todo", "pagina", "video"])
    ap.add_argument("--json")
    ap.add_argument("--bloque")
    ap.add_argument("--samples", type=int, default=None)
    ap.add_argument("--rapido", action="store_true", help="stills en Workbench (luz plana), para iterar rapido")
    ap.add_argument("--workbench", action="store_true")
    ap.add_argument("--set", action="store_true", help="reconstruye set y elenco")
    a = ap.parse_args()
    if a.accion == "armar":
        armar(a.json, a.set)
    elif a.accion == "stills":
        stills(a.json, a.samples or 16, a.rapido)
    elif a.accion == "revisar":
        prob, _ = revisar(a.json)
        sys.exit(1 if prob else 0)
    elif a.accion == "todo":
        armar(a.json, a.set)
        stills(a.json, a.samples or 16, a.rapido)
        revisar(a.json)
    elif a.accion == "pagina":
        pagina(a.bloque)
    elif a.accion == "video":
        video(a.json, a.samples or 6, a.workbench)


if __name__ == "__main__":
    main()
