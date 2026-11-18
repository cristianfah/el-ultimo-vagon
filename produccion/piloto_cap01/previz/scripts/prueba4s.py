#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prueba4s.py - deja lista (en borrador, sin correr) la prueba de 4 s de un plano dificil (07: «probar 4 s antes de gastar»).

  python3 prueba4s.py --llamada c05b --desde 2.0 [--dur 4]

Sale en <trabajo>/pruebas4s/<llamada>_<desde>-<hasta>/:
  video_1.mp4         los 4 s del gris (corte exacto por cuadro, sin audio): referencia de video del brazo A
  hoja_storyboard.jpg los stills A/B/C de los planos que caen en esos 4 s, en una hoja: referencia de imagen del brazo B
  planos.json         que planos entran, con sus segundos dentro de la prueba
El prompt y el payload se escriben a mano (van en el repo, en previz/pruebas4s/). Nada de esto llama a un motor.
"""
import argparse
import json
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PREVIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import previz_tiempos as T  # noqa: E402

TRABAJO = os.environ.get("PREVIZ_TRABAJO", os.path.join(PREVIZ, "_trabajo"))
FFMPEG = os.environ.get("FFMPEG", "ffmpeg")
FUENTE_B = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"


def main():
    from PIL import Image, ImageDraw, ImageFont
    ap = argparse.ArgumentParser()
    ap.add_argument("--llamada", required=True)
    ap.add_argument("--desde", type=float, required=True)
    ap.add_argument("--dur", type=int, default=4)
    a = ap.parse_args()
    ficha = T.leer_ficha(os.path.join(PREVIZ, "shots", a.llamada + ".json"))
    fps = int(ficha.get("fps", 24))
    n, planos = T.planos_en_cuadros(ficha)
    f0 = int(round(a.desde * fps))
    f1 = f0 + a.dur * fps
    if f1 > n:
        raise SystemExit("La prueba pasa el final de la llamada (%d > %d cuadros)" % (f1, n))
    hasta = f1 / fps
    out = os.path.join(TRABAJO, "pruebas4s", "%s_%.1f-%.1f" % (a.llamada, a.desde, hasta))
    os.makedirs(out, exist_ok=True)
    ref = os.path.join(TRABAJO, "out", a.llamada + "_ref.mp4")
    r = subprocess.run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error", "-i", ref, "-vf",
                        "trim=start_frame=%d:end_frame=%d,setpts=PTS-STARTPTS" % (f0, f1), "-an", "-c:v", "libx264",
                        "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(fps), os.path.join(out, "video_1.mp4")])
    if r.returncode:
        raise SystemExit("ffmpeg fallo")
    idx = json.load(open(os.path.join(TRABAJO, "stills", a.llamada, "indice.json"), encoding="utf-8"))
    dentro = []
    for p in planos:
        ini, fin = max(p["f0"], f0), min(p["f1"], f1)
        if ini < fin:
            dentro.append({"id": p["id"], "en_prueba_s": [round((ini - f0) / fps, 3), round((fin - f0) / fps, 3)]})
    # hoja: una fila por plano con sus stills A/B/C (solo los que caen dentro de la prueba)
    filas = []
    for d in dentro:
        pl = next(x for x in idx["planos"] if x["id"] == d["id"])
        ims = []
        for letra in sorted(pl["stills"]):
            s = pl["stills"][letra]
            if f0 <= s["f"] < f1:
                ims.append((letra, Image.open(os.path.join(TRABAJO, "stills", a.llamada, s["png"])).convert("RGB")))
        if not ims:     # si ningun still cae dentro, el B del plano
            s = pl["stills"].get("B") or list(pl["stills"].values())[0]
            ims.append(("B", Image.open(os.path.join(TRABAJO, "stills", a.llamada, s["png"])).convert("RGB")))
        d["stills"] = [l_ for l_, _ in ims]
        filas.append((d["id"], ims))
    pw, ph, g = 360, 640, 16
    cols = max(len(f[1]) for f in filas)
    W = g + cols * (pw + g)
    H = g + len(filas) * (ph + 50 + g)
    hoja = Image.new("RGB", (W, H), (18, 18, 20))
    dr = ImageDraw.Draw(hoja)
    fnt = ImageFont.truetype(FUENTE_B, 30)
    y = g
    for k, (pid, ims) in enumerate(filas):
        dr.text((g, y + 6), "%d · %s" % (k + 1, pid), font=fnt, fill=(235, 235, 235))
        for j, (letra, im) in enumerate(ims):
            x = g + j * (pw + g)
            hoja.paste(im.resize((pw, ph), Image.LANCZOS), (x, y + 50))
            dr.text((x + 10, y + 58), letra, font=fnt, fill=(255, 255, 255), stroke_width=3, stroke_fill=(0, 0, 0))
        y += ph + 50 + g
    hoja.save(os.path.join(out, "hoja_storyboard.jpg"), quality=92)
    with open(os.path.join(out, "planos.json"), "w", encoding="utf-8") as fh:
        json.dump({"llamada": a.llamada, "desde_s": a.desde, "hasta_s": hasta, "planos": dentro}, fh, ensure_ascii=False, indent=1)
    print("[prueba4s] %s %.2f-%.2f s -> %s  planos: %s" % (a.llamada, a.desde, hasta, out, [d["id"] for d in dentro]))


if __name__ == "__main__":
    main()
