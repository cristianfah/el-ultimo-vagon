#!/usr/bin/env python3
"""Genera keyframes o bloques de video leyendo solo el guion técnico (produccion/shotlists/capNN.yaml).

Uso:
  python3 tools/generar_desde_yaml.py keyframe c01_p03 [keyframe|keyframe_entrada]
  python3 tools/generar_desde_yaml.py video c01_b03

Los keyframes aprobados se leen de renders/<cap>/aprobados.json ({"c01_p03": "<url>"}). FAL_KEY viene del entorno.
"""
import json
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(__file__))
from fal_run import download, run  # noqa: E402

YAML = "produccion/shotlists/cap01.yaml"
OUT = "renders/cap01"
ENDPOINTS = {
    "gpt_image_2_5_edit": "openai/gpt-image-2.5/flare/edit",
    "nano_banana_pro_edit": "fal-ai/nano-banana-pro/edit",
}


def resolver(ref, assets, aprobados):
    m = re.match(r"Image \d+ = (.+)", ref)
    nombre = m.group(1).strip()
    k = re.match(r"keyframe (c\d+_p\d+\w*)", nombre)
    if k:
        return aprobados[k.group(1)]
    clave = nombre.split(" ")[0]
    for grupo in assets.values():
        if clave in grupo:
            a = grupo[clave]
            return a.get("hoja") or a.get("ref")
    raise KeyError(nombre)


def main():
    tipo, ident = sys.argv[1], sys.argv[2]
    d = yaml.safe_load(open(YAML, encoding="utf-8"))
    apr_path = os.path.join(OUT, "aprobados.json")
    aprobados = json.load(open(apr_path)) if os.path.exists(apr_path) else {}
    if tipo == "keyframe":
        campo = sys.argv[3] if len(sys.argv) > 3 else "keyframe"
        plano = next(p for p in d["planos"] if p["id"] == ident)
        pr = plano["prompts"][campo]
        payload = dict(pr["params"])
        payload["prompt"] = pr["texto"]
        payload["image_urls"] = [resolver(r, d["assets"], aprobados) for r in pr["referencias"]]
        endpoint = ENDPOINTS[pr["motor"]]
        destino = os.path.join(OUT, "keyframes", f"{ident}_{campo}")
    else:
        bloque = next(b for b in d["bloques"] if b["id"] == ident)
        pv = bloque["prompt_video"]
        payload = dict(pv["params"])
        payload["prompt"] = pv["texto"]
        for campo, refs in pv["entradas"].items():
            urls = [resolver(r, d["assets"], aprobados) for r in (refs if isinstance(refs, list) else [refs])]
            payload[campo] = urls if campo.endswith("urls") else urls[0]
        endpoint = pv["endpoint"]
        destino = os.path.join(OUT, "video", ident)
    os.makedirs(destino, exist_ok=True)
    json.dump({"endpoint": endpoint, "payload": payload}, open(os.path.join(destino, "solicitud.json"), "w"), indent=2, ensure_ascii=False)
    res = run(endpoint, payload)
    json.dump(res, open(os.path.join(destino, "resultado.json"), "w"), indent=2)
    items = res.get("images") or [res["video"]]
    for i, f in enumerate(items):
        ext = ".mp4" if "video" in res else ".png"
        download(f["url"], os.path.join(destino, f"{i}{ext}"))
    print(destino, len(items))


if __name__ == "__main__":
    main()
