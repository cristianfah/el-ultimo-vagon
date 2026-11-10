#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""previz_llamada.py - una llamada completa desde su ficha: armar -> renderizar -> codificar -> verificar.

  python3 previz_llamada.py --blender <Blender> --ffmpeg <ffmpeg> --work <trabajo/previz> --json shots/c05a.json \
                            [--font <fuente.ttf>] [--tira 3] [--engine BLENDER_WORKBENCH] [--set <otro.blend>]

Usa <work>/set/tren_blockout.blend (lo construyen build_set.py + build_cast.py; con --build-set los corre antes).
Deja: <work>/render/<id>/<id>.blend y frame_####.png, <work>/out/<id>_ref.mp4, <work>/qa/<id>_qa.mp4 y _hoja.jpg.
"""
import argparse
import glob
import os
import subprocess
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import previz_tiempos as T  # noqa: E402


def correr(cmd, filtro=None):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for linea in p.stdout:
        if filtro is None or any(f in linea for f in filtro):
            sys.stdout.write(linea)
    if p.wait() != 0:
        raise SystemExit("Fallo (%d): %s" % (p.returncode, " ".join(cmd[:4]) + " ..."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--blender", required=True)
    ap.add_argument("--ffmpeg", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--json", required=True)
    ap.add_argument("--set", default=None, help=".blend del set con elenco (por defecto <work>/set/tren_blockout.blend)")
    ap.add_argument("--build-set", action="store_true", help="reconstruye set y elenco antes")
    ap.add_argument("--engine", default="BLENDER_WORKBENCH")
    ap.add_argument("--font", default=None)
    ap.add_argument("--tira", type=int, default=0)
    a = ap.parse_args()

    work = os.path.abspath(a.work)
    ficha = T.leer_ficha(a.json)
    cid = ficha["call_id"]
    set_blend = os.path.abspath(a.set) if a.set else os.path.join(work, "set", "tren_blockout.blend")
    rdir = os.path.join(work, "render", cid)
    os.makedirs(rdir, exist_ok=True)
    marcas = ("[build_", "[shot_", "[render_", "Error", "Traceback", "  File ")
    bl = [a.blender, "-b", "--python-exit-code", "1"]
    t0 = time.time()
    if a.build_set or not os.path.isfile(set_blend):
        correr(bl + ["-P", os.path.join(AQUI, "build_set.py"), "--", "--out", set_blend], marcas)
        correr(bl + [set_blend, "-P", os.path.join(AQUI, "build_cast.py"), "--", "--save"], ("[build_cast] OK", "Error", "Traceback"))
    for viejo in glob.glob(os.path.join(rdir, "frame_*.png")):      # nunca mezclar cuadros de una version anterior
        os.remove(viejo)
    shot_blend = os.path.join(rdir, cid + ".blend")
    correr(bl + [set_blend, "-P", os.path.join(AQUI, "shot_from_json.py"), "--", "--json", a.json, "--out", shot_blend], marcas)
    t1 = time.time()
    correr(bl + [shot_blend, "-P", os.path.join(AQUI, "render_shot.py"), "--", "--out", os.path.join(rdir, "frame_"),
                 "--engine", a.engine], marcas)
    t2 = time.time()
    enc = [sys.executable, os.path.join(AQUI, "encode.py"), "--ffmpeg", a.ffmpeg, "--json", a.json,
           "--frames-dir", rdir, "--work", work]
    if a.font:
        enc += ["--font", a.font]
    if a.tira:
        enc += ["--tira", str(a.tira)]
    correr(enc)
    t3 = time.time()
    correr([sys.executable, os.path.join(AQUI, "check_ref.py"), "--ffmpeg", a.ffmpeg, "--json", a.json,
            "--ref", os.path.join(work, "out", cid + "_ref.mp4"), "--frames-dir", rdir])
    print("[previz_llamada] %s: armar %.1f s, render %.1f s, encode %.1f s, total %.1f s" %
          (cid, t1 - t0, t2 - t1, t3 - t2, time.time() - t0))


if __name__ == "__main__":
    main()
