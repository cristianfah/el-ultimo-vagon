#!/usr/bin/env python3
"""Corre el lote v1c paso a paso con tools/fal_gen.py (FAL_KEY del entorno; nunca se imprime).

  python3 run_lote_v1c.py --list                 # estado de cada paso
  python3 run_lote_v1c.py --run V01              # genera (1 toma); no acepta nada
  python3 run_lote_v1c.py --accept V01 <png>     # copia la toma revisada a v1c/frames/<plano>.png
  python3 run_lote_v1c.py --flag V01 "motivo"    # 2.º fallo: se marca y se sigue

Antes de --accept, abrir el PNG y revisarlo contra «Estado del mundo» (cap01_v10.md) y revision_v1.md §5.
Tope del trabajo: 12 USD; máximo 2 tomas por paso (una + un reintento).
"""
import argparse, json, pathlib, shutil, subprocess, sys, urllib.request
HERE = pathlib.Path(__file__).resolve().parent
PREVIS = HERE.parent
REPO = HERE.parents[4]
LOTE = json.loads((HERE / "lote_v1c.json").read_text())
URLS = json.loads((REPO / "produccion/assets/fal_urls_v1.json").read_text())
REG = HERE / "registro_v1c.json"
CACHE = HERE / ".refs_cache"; RAW = HERE / "raw"; FR = HERE / "frames"
TOPE = LOTE["tope_trabajo_usd"]
reg = json.loads(REG.read_text()) if REG.exists() else {"gastado_usd": 0.0, "pasos": {}}

def save(): REG.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n")
def step(sid): return next(s for s in LOTE["pasos"] if s["paso"] == sid)
def resolve(x):
    kind, v = x.split(":", 1)
    if kind == "frame":
        p = FR / f"{v}.png"
        return p if p.exists() else PREVIS / "frames" / f"{v}.png"
    if kind == "file": return PREVIS / v
    if kind == "ref":
        CACHE.mkdir(exist_ok=True); p = CACHE / pathlib.Path(v).name
        if not p.exists(): urllib.request.urlretrieve(URLS[v], p)
        return p
    raise ValueError(x)

ap = argparse.ArgumentParser(); g = ap.add_mutually_exclusive_group(required=True)
g.add_argument("--list", action="store_true"); g.add_argument("--run"); g.add_argument("--accept", nargs=2); g.add_argument("--flag", nargs=2)
a = ap.parse_args()
if a.list:
    for s in LOTE["pasos"]:
        r = reg["pasos"].get(s["paso"], {})
        print(s["paso"], s["plano"], s["modelo"], r.get("estado", "pendiente"), r.get("tomas", 0), "deps:", ",".join(s["depende_de"]) or "-")
    print("gastado", round(reg["gastado_usd"], 2), "de", TOPE); sys.exit()
if a.run:
    s = step(a.run); r = reg["pasos"].setdefault(s["paso"], {"tomas": 0, "estado": "pendiente"})
    for d in s["depende_de"]:
        if reg["pasos"].get(d, {}).get("estado") not in ("aceptado", "marcado"): sys.exit(f"{s['paso']} espera {d}")
    if r["tomas"] >= 2: sys.exit("ya hubo 2 tomas: aceptar una o --flag")
    if reg["gastado_usd"] + s["costo_est_usd"] > TOPE + 1e-9: sys.exit(f"PARAR: pasaría el tope de {TOPE} USD")
    imgs = [str(resolve(s["base"]))] + [str(resolve(x)) for x in s["refs"]]
    out = RAW / f"{s['paso']}_{s['plano']}_t{r['tomas']}"; RAW.mkdir(exist_ok=True)
    cmd = [sys.executable, str(REPO / "tools/fal_gen.py"), "--prompt", str(HERE / s["prompt"]), "--images", *imgs,
           "--out", str(out), "--models", s["modelo"], "--ar", "9:16"]
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO)
    print(res.stdout[-2000:], res.stderr[-2000:])
    ok = "ERROR" not in res.stdout and res.returncode == 0
    r["tomas"] += 1; reg["gastado_usd"] = round(reg["gastado_usd"] + (s["costo_est_usd"] if ok else 0), 4)
    r.setdefault("salidas", []).append(f"{out}_{s['modelo']}_0.png" if ok else "ERROR"); save()
if a.accept:
    sid, png = a.accept; s = step(sid); FR.mkdir(exist_ok=True)
    shutil.copy(png, FR / f"{s['plano']}.png"); reg["pasos"][sid]["estado"] = "aceptado"; reg["pasos"][sid]["aceptada"] = png; save()
if a.flag:
    sid, why = a.flag; reg["pasos"].setdefault(sid, {"tomas": 0})["estado"] = "marcado"; reg["pasos"][sid]["motivo"] = why; save()
