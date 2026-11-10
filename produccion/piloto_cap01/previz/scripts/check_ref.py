#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_ref.py - control del video de referencia antes de subirlo (no hay ffprobe: se lee la salida de ffmpeg).

  python3 check_ref.py --ffmpeg <ffmpeg> --ref <trabajo>/out/c05a_ref.mp4 --json shots/c05a.json [--frames-dir <render>/c05a]

Verifica: codec H.264, yuv420p, tamano, fps, duracion EXACTA (cuadros decodificados = duration_s * fps), sin audio,
sin cuadros repetidos seguidos (congelados) y, con --frames-dir, que tampoco haya PNG repetidos seguidos.
Tambien compara contra los limites de Kling 4.0 Omni-Ref para video_1 (3-30 s, lado menor >= 720 px).
Sale con codigo 1 si algo falla. El texto en cuadro no se puede detectar aqui: el ref se codifica sin drawtext.
"""
import argparse
import hashlib
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import previz_tiempos as T  # noqa: E402


def salida(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    return r.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ffmpeg", required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("--json", default=None, help="ficha de la llamada (de ahi salen duracion, fps y tamano esperados)")
    ap.add_argument("--duration", type=int, default=None)
    ap.add_argument("--fps", type=int, default=24)
    ap.add_argument("--size", type=int, nargs=2, default=[720, 1280])
    ap.add_argument("--frames-dir", default=None)
    ap.add_argument("--prefix", default="frame_")
    a = ap.parse_args()

    fps, size, dur = a.fps, list(a.size), a.duration
    if a.json:
        ficha = T.leer_ficha(a.json)
        fps, size, dur = int(ficha.get("fps", 24)), list(ficha.get("resolution", [720, 1280])), int(ficha["duration_s"])
    if dur is None:
        raise SystemExit("Falta --json o --duration")
    n_esp = dur * fps

    info = salida([a.ffmpeg, "-hide_banner", "-i", a.ref])
    video = [l for l in info.splitlines() if "Stream #" in l and "Video:" in l]
    audio = [l for l in info.splitlines() if "Stream #" in l and "Audio:" in l]
    otros = [l for l in info.splitlines() if "Stream #" in l and "Video:" not in l and "Audio:" not in l]
    res = []

    def chk(nombre, ok, detalle):
        res.append((nombre, ok, detalle))

    chk("un solo stream de video", len(video) == 1, "%d" % len(video))
    v = video[0] if video else ""
    m = re.search(r"Video: (\w+)", v)
    chk("codec h264", bool(m) and m.group(1) == "h264", m.group(1) if m else "?")
    chk("pix_fmt yuv420p", "yuv420p" in v, "yuv420p" if "yuv420p" in v else v[:80])
    m = re.search(r"\b(\d{3,5})x(\d{3,5})\b", v)
    tam = [int(m.group(1)), int(m.group(2))] if m else None
    chk("tamano %dx%d" % tuple(size), tam == size, "%sx%s" % tuple(tam) if tam else "?")
    m = re.search(r"([\d.]+) fps", v)
    chk("fps %d" % fps, bool(m) and abs(float(m.group(1)) - fps) < 1e-6, m.group(1) if m else "?")
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", info)
    d_cont = (int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))) if m else -1.0
    chk("duracion del contenedor %d.00 s" % dur, abs(d_cont - dur) < 0.011, "%.2f s" % d_cont)
    chk("sin audio", len(audio) == 0, "%d stream(s) de audio" % len(audio))
    chk("sin otros streams (subtitulos, datos)", len(otros) == 0, "%d" % len(otros))

    # cuadros decodificados y congelados: md5 de cada cuadro decodificado
    md5 = salida([a.ffmpeg, "-hide_banner", "-v", "error", "-i", a.ref, "-map", "0:v:0", "-f", "framemd5", "-"])
    hashes = [l.split(",")[-1].strip() for l in md5.splitlines() if l and not l.startswith("#")]
    chk("cuadros = %d (duracion exacta)" % n_esp, len(hashes) == n_esp, "%d" % len(hashes))
    rep = [i for i in range(1, len(hashes)) if hashes[i] == hashes[i - 1]]
    chk("sin cuadros repetidos seguidos (mp4)", not rep, "ninguno" if not rep else "repetidos en %s" % rep[:10])
    if a.frames_dir:
        hp = []
        for k in range(n_esp):
            ruta = os.path.join(a.frames_dir, "%s%04d.png" % (a.prefix, k))
            if not os.path.isfile(ruta):
                hp.append(None)
                continue
            with open(ruta, "rb") as fh:
                hp.append(hashlib.md5(fh.read()).hexdigest())
        falt = [k for k, x in enumerate(hp) if x is None]
        chk("PNG completos", not falt, "faltan %d" % len(falt))
        rep = [i for i in range(1, len(hp)) if hp[i] is not None and hp[i] == hp[i - 1]]
        chk("sin PNG repetidos seguidos", not rep, "ninguno" if not rep else "repetidos en %s" % rep[:10])
    # limites del modelo (Kling 4.0 Omni-Ref, video_1)
    chk("Kling video_1: 3-30 s", 3 <= dur <= 30, "%d s" % dur)
    chk("Kling video_1: lado menor >= 720 px", bool(tam) and min(tam) >= 720, "%s" % (min(tam) if tam else "?"))

    ok = all(r[1] for r in res)
    print("[check_ref] %s" % a.ref)
    for nombre, bien, det in res:
        print("  %-4s %-44s %s" % ("OK" if bien else "FALLA", nombre, det))
    print("[check_ref] RESULTADO: %s" % ("OK" if ok else "FALLA"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
