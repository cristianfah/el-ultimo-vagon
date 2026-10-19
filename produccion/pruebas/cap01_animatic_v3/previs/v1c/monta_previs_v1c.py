#!/usr/bin/env python3
"""Monta cap01_previs_v1c.mp4 con los tiempos de ../../tiempos_montaje_v3.json.

Cada still se normaliza a 480×832 (escala para cubrir y recorte al centro, sin barras) antes del concat:
así no hay saltos de fotogramas por PNG de distinta resolución. Fotograma: v1c/frames/<id>.png si existe,
si no previs/frames/<id>.png. b4_p3 lleva 0,5 s de negro al inicio (post). Pistas con colchón de 0,5 s recortado.
"""
import json, math, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent; PREVIS = HERE.parent; V3 = PREVIS.parent
T = json.loads((V3 / "tiempos_montaje_v3.json").read_text())
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else PREVIS / "cap01_previs_v1c.mp4"
W, H, FPS, PAD = 480, 832, 24, T["colchon_llamada_s"]
WORK = pathlib.Path("/tmp/previs_v1c"); (WORK / "st").mkdir(parents=True, exist_ok=True)
VF = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,format=rgb24"
def run(c): r = subprocess.run(c, capture_output=True, text=True); r.returncode and sys.exit(r.stderr[-3000:]); return r
edl = []; t = 0.0
for s in T["planos"]:
    src = HERE / "frames" / f"{s['id']}.png"; src = src if src.exists() else PREVIS / "frames" / f"{s['id']}.png"
    dst = WORK / "st" / f"{s['id']}.png"; run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-vf", VF, str(dst)])
    # cuadros enteros acumulados para que cada corte caiga en el fotograma exacto
    f_in, f_out = round(t * FPS), round((t + s["dur_s"]) * FPS)
    if s["id"] == "b4_p3":
        blk = WORK / "st" / "negro.png"; run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"color=black:s={W}x{H}", "-frames:v", "1", str(blk)])
        fb = round((t + 0.5) * FPS); edl += [(str(blk), f_in, fb, "b4_p3_negro"), (str(dst), fb, f_out, s["id"])]
    else: edl.append((str(dst), f_in, f_out, s["id"]))
    t += s["dur_s"]
N = round(t * FPS)
lines = ["ffconcat version 1.0"]
for p, a, b, _ in edl: lines += [f"file '{p}'", f"duration {(b - a) / FPS:.6f}"]
lines.append(f"file '{edl[-1][0]}'"); (WORK / "c.txt").write_text("\n".join(lines) + "\n")
run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(WORK / "c.txt"), "-vf", f"fps={FPS},format=yuv420p",
     "-frames:v", str(N), "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-an", str(WORK / "v.mp4")])
first = {c["llamada"]: c["planos"][0] for c in T["llamadas"] if "audio1" in c}
start = {s["id"]: s["entra_montaje_s"] for s in T["planos"]}
calls = {c["llamada"]: c for c in T["llamadas"]}
ins = ["-i", str(WORK / "v.mp4"), "-f", "lavfi", "-t", f"{N / FPS:.6f}", "-i", "anullsrc=r=48000:cl=stereo"]; fc = []; labs = ["[1:a]"]
for i, (call, sid) in enumerate(first.items(), start=2):
    src = V3 / calls[call]["audio1"]["pista"]; dur = calls[call]["montaje_s"]
    ins += ["-ss", str(PAD), "-t", f"{dur:.3f}", "-i", str(src)]
    ms = int(round(start[sid] * 1000)); fc.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms},volume=-6dB[a{i}]"); labs.append(f"[a{i}]")
fc.append("".join(labs) + f"amix=inputs={len(labs)}:duration=first:normalize=0[aout]")
run(["ffmpeg", "-y", "-v", "error", *ins, "-filter_complex", ";".join(fc), "-map", "0:v", "-map", "[aout]", "-c:v", "copy",
     "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", "-t", f"{N / FPS:.6f}", str(OUT)])
(WORK / "edl.json").write_text(json.dumps([{"id": e[3], "f_in": e[1], "f_out": e[2], "file": e[0]} for e in edl], indent=1))
print(json.dumps({"out": str(OUT), "frames": N, "dur_s": N / FPS, "planos": len(T["planos"]), "segmentos": len(edl),
                  "audio": {c: start[s] for c, s in first.items()}}, ensure_ascii=False))
