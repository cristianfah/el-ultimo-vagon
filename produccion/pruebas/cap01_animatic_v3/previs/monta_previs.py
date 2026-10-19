#!/usr/bin/env python3
"""Monta cap01_previs_v1.mp4: fotogramas fijos 9:16 480x832 24 fps + 4 pistas."""
from __future__ import annotations

import json
import pathlib
import subprocess

ROOT = pathlib.Path("/workspace/produccion/pruebas/cap01_animatic_v3")
PACK = ROOT / "previs" / "prompts_previs_v1.json"
FRAMES = ROOT / "previs" / "frames"
OUT = ROOT / "previs" / "cap01_previs_v1.mp4"
MONTAJE = ROOT / "previs" / "montaje.md"
PAD = 0.5
W, H, FPS = 480, 832, 24

CALL_AUDIO = {
    "c02": ROOT / "pistas" / "c02.mp3",
    "c04b": ROOT / "pistas" / "c04b.mp3",
    "c07a": ROOT / "pistas" / "c07a.mp3",
    "c07b": ROOT / "pistas" / "c07b.mp3",
}
# Primer plano de cada llamada de VIDEO (plan.md), no el campo `call` del pack:
# b4_p4 está etiquetado c04a en el pack, pero c04b.mp3 cubre P4–P6.
CALL_FIRST = {
    "c02": "b2_p1",
    "c04b": "b4_p4",
    "c07a": "b7_p1",
    "c07b": "b7_p4",
}


def ffprobe_dur(path: pathlib.Path) -> float:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nk=1:nw=1", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(r.stdout.strip())


def main():
    pack = json.loads(PACK.read_text())
    shots = pack["shots"]
    missing = [s["id"] for s in shots if not (FRAMES / f"{s['id']}.png").exists()]
    if missing:
        raise SystemExit(f"faltan fotogramas: {missing}")

    t = 0.0
    edl = []
    shot_in = {}
    for s in shots:
        rec = {
            "id": s["id"],
            "call": s["call"],
            "in": round(t, 3),
            "dur": s["duration_s"],
            "out": round(t + s["duration_s"], 3),
        }
        edl.append(rec)
        shot_in[s["id"]] = rec["in"]
        t += s["duration_s"]
    total = round(t, 3)
    call_start = {call: shot_in[sid] for call, sid in CALL_FIRST.items()}

    work = pathlib.Path("/tmp/previs_montaje")
    work.mkdir(exist_ok=True)
    concat = work / "concat.txt"
    lines = ["ffconcat version 1.0"]
    for rec in edl:
        p = (FRAMES / f"{rec['id']}.png").resolve()
        lines.append(f"file '{p}'")
        lines.append(f"duration {rec['dur']}")
    last = (FRAMES / f"{edl[-1]['id']}.png").resolve()
    lines.append(f"file '{last}'")
    concat.write_text("\n".join(lines) + "\n")

    silent = work / "silence.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
         "-t", str(total), "-c:a", "pcm_s16le", str(silent)],
        check=True, capture_output=True,
    )

    trimmed = {}
    audio_edl = []
    for call, src in CALL_AUDIO.items():
        if call not in call_start:
            raise SystemExit(f"no hay planos para {call}")
        dur = ffprobe_dur(src)
        trim_dur = max(0.05, dur - 2 * PAD)
        dest = work / f"{call}_trim.wav"
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(src), "-ss", str(PAD), "-t", str(trim_dur),
             "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(dest)],
            check=True, capture_output=True,
        )
        start = call_start[call]
        trimmed[call] = dest
        audio_edl.append({
            "pista": call,
            "src": str(src.relative_to(ROOT.parent.parent.parent)),
            "entra_s": start,
            "pad_recortado_s": PAD,
            "duracion_trim_s": round(trim_dur, 3),
            "nota": "Colchón 0,5 s de cada extremo de la llamada recortado; overlay al primer plano de la llamada.",
        })

    # build ffmpeg mix
    inputs = ["-i", str(concat), "-i", str(silent)]
    for call in ("c02", "c04b", "c07a", "c07b"):
        inputs += ["-i", str(trimmed[call])]

    # adelay in ms
    delays = []
    mix_labels = ["[1:a]"]
    fc = []
    for i, call in enumerate(("c02", "c04b", "c07a", "c07b"), start=2):
        ms = int(round(call_start[call] * 1000))
        delays.append(ms)
        lab = f"a{i}"
        fc.append(f"[{i}:a]adelay={ms}|{ms},volume=-6dB[{lab}]")
        mix_labels.append(f"[{lab}]")
    fc.append(
        "".join(mix_labels)
        + f"amix=inputs={len(mix_labels)}:duration=first:dropout_transition=0:normalize=0[aout]"
    )
    vf = f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps={FPS},format=yuv420p"
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", *inputs,
        "-filter_complex", ";".join(fc),
        "-map", "0:v", "-map", "[aout]",
        "-vf", vf,
        "-r", str(FPS), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20",
        "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart",
        "-t", str(total),
        str(OUT),
    ]
    print("ffmpeg", " ".join(cmd[:8]), "...", flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-4000:])
        raise SystemExit(r.returncode)

    vdur = ffprobe_dur(OUT)
    md = []
    md.append("# Montaje de `cap01_previs_v1.mp4`")
    md.append("")
    md.append("19-oct-2026. Fotogramas fijos, duraciones del pack de previs (no el colchón de 0,5 s de las llamadas H3). 9:16, 480×832, 24 fps.")
    md.append("")
    md.append(f"- **Archivo:** `produccion/pruebas/cap01_animatic_v3/previs/cap01_previs_v1.mp4`")
    md.append(f"- **Duración:** {vdur:.2f} s (suma de planos {total:.2f} s)")
    md.append("- **Pistas:** c02, c04b, c07a, c07b. Colchón de 0,5 s recortado en cada extremo; overlay al primer plano de la llamada; mezcla −6 dB.")
    md.append("- **Pitazo de Hugo:** no está en `c04b.mp3`; va en post a los 2,1 s de la llamada (1,6 s del bloque c04b en este corte).")
    md.append("- **c05i:** primer fotograma = `ESTADO_carmen_palma.png` (dorso). **c06b / b6_p2:** estado = `ESTADO_carmen_palma_v2_palma.png` (palma).")
    md.append("")
    md.append("## EDL")
    md.append("")
    md.append("| t in | t out | dur | id | llamada |")
    md.append("| ---: | ---: | ---: | --- | --- |")
    for rec in edl:
        md.append(f"| {rec['in']:.2f} | {rec['out']:.2f} | {rec['dur']:.2f} | `{rec['id']}` | {rec['call']} |")
    md.append("")
    md.append("## Audio")
    md.append("")
    md.append("| pista | entra (s del corte) | trim |")
    md.append("| --- | ---: | --- |")
    for a in audio_edl:
        md.append(f"| `{a['pista']}` | {a['entra_s']:.2f} | {a['duracion_trim_s']:.2f} s (pad {PAD} s × 2) |")
    md.append("")
    md.append("Hugo (toma A) entra a los 2,5 s de la pista original = 2,0 s del bloque c04b en este corte (0,5 s dentro de P5 / `b4_p5`).")
    md.append("")
    MONTAJE.write_text("\n".join(md) + "\n")
    print(json.dumps({
        "out": str(OUT),
        "dur": vdur,
        "n": len(edl),
        "audio": audio_edl,
        "size": OUT.stat().st_size,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
