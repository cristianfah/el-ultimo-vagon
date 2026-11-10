#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""encode.py - PNG -> video de referencia, copia de QA y hoja de contacto (Python del sistema + ffmpeg).

  python3 encode.py --ffmpeg <ffmpeg> --json shots/c05a.json --frames-dir <trabajo>/render/c05a \
                    --work <trabajo> [--font <fuente.ttf>] [--tira 3] [--crf 16]

Salidas (dentro de --work):
  out/<id>_ref.mp4   LO QUE SE SUBE: H.264 yuv420p, 24 fps, SIN audio, SIN texto, cuadros = duration_s * fps exactos.
  qa/<id>_qa.mp4     la misma imagen con contador de cuadro, id de plano y tiempo (solo para humanos; necesita --font).
  qa/<id>_hoja.jpg   hoja de contacto: 3 cuadros por plano (primero, medio, ultimo).
  qa/<id>_tira.jpg   opcional (--tira N): un cuadro cada N, para revisar el movimiento.
El ref y el qa salen de los PNG, no uno del otro. Sin --font no se dibuja texto (este ffmpeg no trae fontconfig).
"""
import argparse
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import previz_tiempos as T  # noqa: E402

ESCALA = "scale=%d:%d:flags=lanczos:out_color_matrix=bt709:out_range=tv,setsar=1,format=yuv420p"
X264 = ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "slow", "-g", "24",
        "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-movflags", "+faststart", "-an"]


def correr(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    if r.returncode != 0:
        sys.stderr.write(r.stdout[-3000:] + "\n")
        raise SystemExit("ffmpeg fallo (%d): %s" % (r.returncode, " ".join(cmd[:6]) + " ..."))
    return r.stdout


def texto(font, txt, tam, y, extra=""):
    return ("drawtext=fontfile='%s':text='%s':x=16:y=%s:fontsize=%d:fontcolor=white:box=1:boxcolor=black@0.6:boxborderw=6%s"
            % (font, txt, y, tam, extra))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ffmpeg", required=True)
    ap.add_argument("--json", required=True, help="ficha de la llamada")
    ap.add_argument("--frames-dir", required=True, help="carpeta con frame_0000.png ...")
    ap.add_argument("--work", required=True, help="carpeta de trabajo del previz (se crean out/ y qa/)")
    ap.add_argument("--prefix", default="frame_")
    ap.add_argument("--font", default=None, help="archivo .ttf/.ttc para el texto de QA")
    ap.add_argument("--crf", type=int, default=16)
    ap.add_argument("--tira", type=int, default=0, help="si > 0, tira de revision con un cuadro cada N")
    a = ap.parse_args()

    ficha = T.leer_ficha(a.json)
    cid = ficha["call_id"]
    fps = int(ficha.get("fps", 24))
    w, h = ficha.get("resolution", [720, 1280])
    n, planos = T.planos_en_cuadros(ficha)
    fdir = os.path.abspath(a.frames_dir)
    faltan = [k for k in range(n) if not os.path.isfile(os.path.join(fdir, "%s%04d.png" % (a.prefix, k)))]
    if faltan:
        raise SystemExit("Faltan %d cuadros en %s (primero: %d). No se rellena con congelados." % (len(faltan), fdir, faltan[0]))
    sobran = os.path.isfile(os.path.join(fdir, "%s%04d.png" % (a.prefix, n)))
    if sobran:
        print("[encode] aviso: hay cuadros mas alla del %d; se ignoran" % (n - 1))
    out_dir, qa_dir = os.path.join(a.work, "out"), os.path.join(a.work, "qa")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(qa_dir, exist_ok=True)
    patron = os.path.join(fdir, a.prefix + "%04d.png")
    entrada = ["-framerate", str(fps), "-start_number", "0", "-i", patron]
    esc = ESCALA % (w, h)

    # 1) referencia: sin texto, sin audio, duracion exacta
    ref = os.path.join(out_dir, cid + "_ref.mp4")
    correr([a.ffmpeg, "-y", "-hide_banner"] + entrada + ["-frames:v", str(n), "-r", str(fps), "-vf", esc,
                                                       "-crf", str(a.crf)] + X264 + [ref])
    print("[encode] ref  ->", ref)

    # 2) QA: contador de cuadro, id de plano y tiempo
    qa = os.path.join(qa_dir, cid + "_qa.mp4")
    vf = [esc]
    if a.font:
        vf.append(texto(a.font, cid + "  cuadro %{eif\\:n\\:d\\:3}  t=%{pts\\:flt} s", 30, "16"))
        for p in planos:
            vf.append(texto(a.font, "%s  (cuadros %d-%d)" % (p["id"], p["f0"], p["f1"] - 1), 30, "62",
                            ":enable='between(n,%d,%d)'" % (p["f0"], p["f1"] - 1)))
    else:
        print("[encode] aviso: sin --font el QA sale sin texto")
    correr([a.ffmpeg, "-y", "-hide_banner"] + entrada + ["-frames:v", str(n), "-r", str(fps), "-vf", ",".join(vf),
                                                       "-crf", "20"] + X264 + [qa])
    print("[encode] qa   ->", qa)

    # 3) hoja de contacto: primero, medio y ultimo cuadro de cada plano
    hoja = os.path.join(qa_dir, cid + "_hoja.jpg")
    tw, th = 360, int(round(360.0 * h / w))
    ins, fc, filas = [], [], []
    i = 0
    for r, p in enumerate(planos):
        celdas = []
        for k in (p["f0"], (p["f0"] + p["f1"] - 1) // 2, p["f1"] - 1):
            ins += ["-i", os.path.join(fdir, "%s%04d.png" % (a.prefix, k))]
            f = "[%d:v]scale=%d:%d:flags=lanczos" % (i, tw, th)
            if a.font:
                f += "," + texto(a.font, "%s  c%d  %.3f s" % (p["id"], k, k / float(fps)), 20, "10")
            f += ",pad=%d:%d:2:2:black[c%d]" % (tw + 4, th + 4, i)
            fc.append(f)
            celdas.append("[c%d]" % i)
            i += 1
        fc.append("%shstack=inputs=3[r%d]" % ("".join(celdas), r))
        filas.append("[r%d]" % r)
    fc.append("%svstack=inputs=%d[o]" % ("".join(filas), len(filas)) if len(filas) > 1 else "%scopy[o]" % filas[0])
    correr([a.ffmpeg, "-y", "-hide_banner"] + ins + ["-filter_complex", ";".join(fc), "-map", "[o]",
                                                   "-frames:v", "1", "-q:v", "3", hoja])
    print("[encode] hoja ->", hoja)

    # 4) tira de revision opcional
    if a.tira and a.tira > 0:
        tira = os.path.join(qa_dir, cid + "_tira.jpg")
        cols = 10
        cant = (n + a.tira - 1) // a.tira
        rows = (cant + cols - 1) // cols
        f = ""
        if a.font:                                   # el numero se dibuja antes del select: es el cuadro real
            f = texto(a.font, "%{eif\\:n\\:d}", 72, "16") + ","
        f += "select='not(mod(n\\,%d))',scale=216:-2,tile=%dx%d:padding=2" % (a.tira, cols, rows)
        correr([a.ffmpeg, "-y", "-hide_banner", "-start_number", "0", "-i", patron, "-frames:v", "1", "-vsync", "0",
                "-vf", f, "-q:v", "4", tira])
        print("[encode] tira ->", tira)


if __name__ == "__main__":
    main()
