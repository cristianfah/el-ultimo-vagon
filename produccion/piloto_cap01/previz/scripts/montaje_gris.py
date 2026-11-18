#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""montaje_gris.py - la pelicula en gris: corta cada plano en su ventana de montaje, pone las voces y mide el ritmo.

  python3 montaje_gris.py [--version v1] [--pistas <carpeta con c02a.wav c02b.wav c04b.mp3 c07a_v2.wav c07b_v2.wav>]

Entra: llamadas_tiempos.json (orden de montaje y ventana de cada plano), <trabajo>/out/<llamada>_ref.mp4 (el gris de cada
llamada) y las pistas de voz de las llamadas con dialogo (la pista arranca en el segundo 0 de su llamada).
Sale, en <trabajo>/montaje/:
  cap01_gris_<v>.mp4      el corte limpio con voces (720x1280, 24 fps)
  cap01_gris_<v>_qa.mp4   el mismo, con plano, segundo de montaje y llamada sobreimpresos (para revisar)
  ritmo_gris_<v>.md       tabla de ritmo: duracion de cada plano, accion, regla «accion + 0,5 s» y entrada de cada linea
b1_f3 (la pantalla) es una imagen fija de post: va como carton negro con su nombre. Al final, la encuesta en negro.
"""
import argparse
import json
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PREVIZ = os.path.dirname(AQUI)
REPO = os.path.abspath(os.path.join(PREVIZ, "..", "..", ".."))
TRABAJO = os.environ.get("PREVIZ_TRABAJO", os.path.join(PREVIZ, "_trabajo"))
FFMPEG = os.environ.get("FFMPEG", "ffmpeg")
FUENTE = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
FPS, W, H, SR = 24, 720, 1280, 48000
PISTAS = {"c02a": "c02a.wav", "c02b": "c02b.wav", "c04b": "c04b.mp3", "c07a": "c07a_v2.wav", "c07b": "c07b_v2.wav"}


def correr(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    if r.returncode != 0:
        print(r.stdout[-3000:])
        raise SystemExit("ffmpeg fallo")
    return r.stdout


def leer_audio(ruta):
    import numpy as np
    raw = subprocess.run([FFMPEG, "-v", "error", "-i", ruta, "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                         stdout=subprocess.PIPE, check=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32)


def main():
    import numpy as np
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default="v1")
    ap.add_argument("--pistas", default=os.path.join(os.path.dirname(TRABAJO), "pistas_v3"))
    a = ap.parse_args()
    tt = json.load(open(os.path.join(PREVIZ, "llamadas_tiempos.json"), encoding="utf-8"))
    v3 = json.load(open(os.path.join(REPO, "produccion/pruebas/cap01_animatic_v3/tiempos_montaje_v3.json"), encoding="utf-8"))
    accion = {p["id"]: p for p in v3["planos"]}
    plano_llamada = {}
    for c in tt["llamadas"]:
        for p in c["planos"]:
            plano_llamada[p["id"]] = (c, p)
    segs = []
    for pid in tt["orden_montaje"]:
        if pid == "b1_f3":
            segs.append({"id": pid, "carton": "b1_f3 · la pantalla (imagen fija de post)", "dur": accion[pid]["dur_s"]})
            continue
        c, p = plano_llamada[pid]
        f0, f1 = int(round(p["de_s"] * FPS)), int(round(p["a_s"] * FPS))
        segs.append({"id": pid, "call": c["call_id"], "f0": f0, "f1": f1, "de": p["de_s"], "a": p["a_s"], "dur": (f1 - f0) / FPS})
    segs.append({"id": "encuesta", "carton": "Si fueras Martina, ¿lo dejas entrar?   SÍ · NO", "dur": 2.0})

    out_dir = os.path.join(TRABAJO, "montaje")
    os.makedirs(out_dir, exist_ok=True)
    # --- video: un filtro con todos los tramos
    entradas, fc, labels = [], [], []
    vistos = {}
    for s in segs:
        if "call" in s and s["call"] not in vistos:
            ref = os.path.join(TRABAJO, "out", s["call"] + "_ref.mp4")
            if not os.path.isfile(ref):
                raise SystemExit("Falta %s (corre storyboard.py video)" % ref)
            vistos[s["call"]] = len(vistos)
            entradas += ["-i", ref]
    t = 0.0
    for i, s in enumerate(segs):
        if "carton" in s:
            fc.append("color=c=black:s=%dx%d:r=%d:d=%.4f,drawtext=fontfile=%s:text='%s':fontsize=34:fontcolor=white:"
                      "x=(w-text_w)/2:y=(h-text_h)/2,format=yuv420p,setsar=1[s%d]"
                      % (W, H, FPS, s["dur"], FUENTE, s["carton"].replace(":", "\\:").replace("'", ""), i))
        else:
            k = vistos[s["call"]]
            fc.append("[%d:v]trim=start_frame=%d:end_frame=%d,setpts=PTS-STARTPTS,scale=%d:%d,format=yuv420p,setsar=1[s%d]"
                      % (k, s["f0"], s["f1"], W, H, i))
        s["t_montaje"] = round(t, 3)
        t += s["dur"]
        labels.append("[s%d]" % i)
    fc.append("%sconcat=n=%d:v=1:a=0[v]" % ("".join(labels), len(segs)))
    total = t
    # --- audio: cada tramo toma su pedazo de la pista de su llamada (o silencio)
    pistas = {cid: leer_audio(os.path.join(a.pistas, f)) for cid, f in PISTAS.items()
              if os.path.isfile(os.path.join(a.pistas, f))}
    trozos = []
    for s in segs:
        n = int(round(s["dur"] * SR))
        x = np.zeros(n, dtype=np.float32)
        if s.get("call") in pistas:
            pa = pistas[s["call"]]
            i0 = int(round(s["de"] * SR))
            y = pa[i0:i0 + n]
            x[:len(y)] = y
        trozos.append(x)
    audio = np.concatenate(trozos)
    wav = os.path.join(out_dir, "voces_%s.wav" % a.version)
    import wave
    with wave.open(wav, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes(np.clip(audio, -32768, 32767).astype(np.int16).tobytes())
    base = os.path.join(out_dir, "cap01_gris_%s" % a.version)
    x264 = ["-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart"]
    correr([FFMPEG, "-y", "-hide_banner"] + entradas + ["-i", wav, "-filter_complex", ";".join(fc), "-map", "[v]",
           "-map", "%d:a" % len(vistos), "-c:a", "aac", "-b:a", "160k", "-shortest"] + x264 + [base + ".mp4"])
    # QA: plano y segundo sobreimpresos
    txt = []
    for s in segs:
        e0, e1 = s["t_montaje"], s["t_montaje"] + s["dur"]
        etiqueta = "%s  %s" % (s["id"], s.get("call", "")) if "call" in s else s["id"]
        txt.append("drawtext=fontfile=%s:text='%s':x=18:y=20:fontsize=30:fontcolor=white:box=1:boxcolor=black@0.6:"
                   "boxborderw=8:enable='between(t,%.3f,%.3f)'" % (FUENTE, etiqueta, e0, e1 - 0.001))
    txt.append("drawtext=fontfile=%s:text='%%{pts\\:flt}':x=w-tw-18:y=20:fontsize=30:fontcolor=white:box=1:"
               "boxcolor=black@0.6:boxborderw=8" % FUENTE)
    correr([FFMPEG, "-y", "-hide_banner", "-i", base + ".mp4", "-vf", ",".join(txt), "-c:a", "copy"] + x264 + [base + "_qa.mp4"])
    # --- ritmo
    lineas = []
    for c in tt["llamadas"]:
        for ln in (c.get("pista") or {}).get("lineas", []):
            lineas.append((c["call_id"], ln))
    filas = ["| Plano | Llamada | Entra en el montaje | Dura | Acción (v1c) | ¿≤ acción + 0,5 s? | Línea que entra | Entra después del corte |",
             "|---|---|---:|---:|---:|---|---|---:|"]
    fallas = []
    for s in segs:
        if s["id"] == "encuesta":
            continue
        ac = accion.get(s["id"], {}).get("accion_s")
        ok = "sí" if ac is None or s["dur"] <= ac + 0.5 + 0.05 else "**no**"
        entra, dl = "", ""
        if "call" in s:
            for cid, (quien, texto, t0, t1) in lineas:
                if cid == s["call"] and s["de"] - 1e-6 <= t0 < s["a"]:
                    d = t0 - s["de"]
                    entra = "%s: «%s»" % (quien, texto)
                    marca = "" if d <= 0.3 + 1e-6 else " **(> 0,3 s)**"
                    dl = "%.2f s%s" % (d, marca)
                    if d > 0.3 + 1e-6 and d < 1.0:
                        fallas.append("%s: «%s» entra %.2f s después del corte (tope 0,3 s)" % (s["id"], texto, d))
        if ok != "sí":
            fallas.append("%s dura %.2f s y su acción %.2f s (+0,5 s)" % (s["id"], s["dur"], ac))
        filas.append("| %s | %s | %.2f s | %.2f s | %s | %s | %s | %s |" % (
            s["id"], s.get("call", "post"), s["t_montaje"], s["dur"], ("%.2f s" % ac) if ac is not None else "—", ok, entra, dl))
    md = ["# Ritmo del gris %s" % a.version, "",
          "Duración total sin la encuesta: **%.2f s**. Regla de Cristian (05): se recorta solo un plano que dura más que su acción "
          "+ 0,5 s, nunca dentro de una línea, sin relleno; cada línea entra a 0,3 s o menos después del corte." % (total - 2.0), "",
          "Las duraciones salen de `llamadas_tiempos.json` (v1c). La acción es la estimada en `tiempos_montaje_v3.json`; "
          "en el gris se verifica a ojo que la acción de cada plano quepa en su ventana.", ""] + filas + ["", "## No cumplen", ""]
    md += ["- " + f for f in fallas] or ["- Ninguno."]
    with open(os.path.join(out_dir, "ritmo_gris_%s.md" % a.version), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md) + "\n")
    print("[montaje_gris] %s.mp4 (%.2f s), _qa.mp4 y ritmo_gris_%s.md" % (base, total, a.version))
    for f in fallas:
        print("  NO CUMPLE", f)


if __name__ == "__main__":
    main()
