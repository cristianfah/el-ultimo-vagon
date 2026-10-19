#!/usr/bin/env python3
"""Regenera planos en GPT Image 2.5 sunburst, desde el PNG original, en paralelo.

No edita una salida ya editada. num_images=1. Imprime request_id y claves de
respuesta que no sean la imagen. No imprime la clave.
"""
import json, os, pathlib, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

import fal_client

HERE = pathlib.Path(__file__).resolve().parent
ORIG = HERE.parent / "frames"
RAW = HERE / "raw"
CACHE = HERE / ".refs_cache"
URLS = json.loads((HERE.parents[4] / "produccion/assets/fal_urls_v1.json").read_text())
REG = HERE / "registro_v1c.json"
TOPE = 12.0
# Tope de reserva por toma hasta leer el costo real. Sunburst high sale más caro que NBP.
RESERVA = 0.40

JOBS = {
    "b0_p2": ["b0_p2.png", "F08_v2_ambar_bajo.png", "PROP_maletin_v2.png", "HOJA_martina.png"],
    "b0_p3": ["b0_p3.png", "F08_v2_ambar_bajo.png", "HOJA_martina.png", "HOJA_extra_pareja_camisa_azul.png"],
    "b3_p6": ["b3_p6.png", "F08_v2_ambar_bajo.png", "b0_p4.png"],
    "b4_p6": ["b4_p6.png", "HOJA_tomas.png", "HOJA_martina.png", "F05_rojo_tres_cuartos_hacia_puerta.png"],
    "b5_p6": ["b5_p6.png", "HOJA_hugo.png", "PROP_llave_y_cerradura.png", "F05_rojo_tres_cuartos_hacia_puerta.png"],
    "b5_p8": ["b5_p8.png", "HOJA_hugo.png", "PROP_llave_y_cerradura.png"],
    "b2_p4": ["b2_p4.png", "HOJA_martina.png", "F09_ambar_asiento_pareja.png"],
    "b6_p2": ["b6_p2.png", "HOJA_carmen.png", "ESTADO_carmen_palma_v2_palma.png", "F05_rojo_tres_cuartos_hacia_puerta.png"],
    "b3_p1": ["b0_p2.png", "F08_v2_ambar_bajo.png", "PROP_maletin_v2.png"],
    "b6_p1": ["b6_p1.png", "HOJA_ivan.png", "HOJA_hugo.png", "F05_rojo_tres_cuartos_hacia_puerta.png"],
    "b6_p3": ["b6_p3.png", "F02_rojo_ultimo_vagon_hacia_fondo_cabina.png", "HOJA_martina.png", "HOJA_tomas.png"],
    "b7_p1": ["b7_p1.png", "F05_rojo_tres_cuartos_hacia_puerta.png"],
    "b7_p2": ["b7_p2.png", "HOJA_diego.png", "F05_rojo_tres_cuartos_hacia_puerta.png"],
    "b7_p5": ["b7_p5.png", "HOJA_diego.png", "F05_rojo_tres_cuartos_hacia_puerta.png"],
    "b7_p3": ["b7_p3.png", "F02_rojo_ultimo_vagon_hacia_fondo_cabina.png", "HOJA_martina.png", "HOJA_ivan.png"],
    "b7_p4": ["b7_p4.png", "F02_rojo_ultimo_vagon_hacia_fondo_cabina.png", "HOJA_tomas.png", "HOJA_martina.png"],
    "b7_p6": ["b7_p6.png", "F02_rojo_ultimo_vagon_hacia_fondo_cabina.png", "HOJA_martina.png", "HOJA_hugo.png"],
}

REF_KEY = {
    "F08_v2_ambar_bajo.png": "set/F08_v2_ambar_bajo.png",
    "F05_rojo_tres_cuartos_hacia_puerta.png": "set/F05_rojo_tres_cuartos_hacia_puerta.png",
    "F02_rojo_ultimo_vagon_hacia_fondo_cabina.png": "set/F02_rojo_ultimo_vagon_hacia_fondo_cabina.png",
    "F09_ambar_asiento_pareja.png": "set/F09_ambar_asiento_pareja.png",
    "PROP_maletin_v2.png": "props/PROP_maletin_v2.png",
    "PROP_llave_y_cerradura.png": "props/PROP_llave_y_cerradura.png",
    "HOJA_martina.png": "personajes/HOJA_martina.png",
    "HOJA_tomas.png": "personajes/HOJA_tomas.png",
    "HOJA_carmen.png": "personajes/HOJA_carmen.png",
    "HOJA_hugo.png": "personajes/HOJA_hugo.png",
    "HOJA_ivan.png": "personajes/HOJA_ivan.png",
    "HOJA_diego.png": "personajes/HOJA_diego.png",
    "HOJA_extra_pareja_camisa_azul.png": "personajes/HOJA_extra_pareja_camisa_azul.png",
    "ESTADO_carmen_palma_v2_palma.png": "personajes/ESTADO_carmen_palma_v2_palma.png",
    "ESTADO_diego_mojado_herido_v3.png": "personajes/ESTADO_diego_mojado_herido_v3.png",
}


def local(name):
    if name.startswith("b"):
        return ORIG / name
    CACHE.mkdir(exist_ok=True)
    p = CACHE / name
    if not p.exists():
        urllib.request.urlretrieve(URLS[REF_KEY[name]], p)
    return p


def gastado():
    reg = json.loads(REG.read_text())
    return float(reg["gastado_usd"])


def one(plano, toma):
    prompt = (HERE / "prompts" / f"SB_{plano}.txt").read_text().strip()
    paths = [str(local(n)) for n in JOBS[plano]]
    t0 = time.time()
    urls = [fal_client.upload_file(p) for p in paths]
    handle = fal_client.submit(
        "openai/gpt-image-2.5/sunburst/edit",
        arguments={
            "prompt": prompt,
            "image_urls": urls,
            "image_size": {"width": 1152, "height": 2048},
            "quality": "high",
            "num_images": 1,
            "output_format": "png",
        },
    )
    result = handle.get()
    meta = {k: v for k, v in result.items() if k != "images"}
    meta["request_id"] = handle.request_id
    meta["latency_s"] = round(time.time() - t0, 2)
    meta["started_unix"] = round(t0, 3)
    meta["prompt_file"] = f"prompts/SB_{plano}.txt"
    meta["prompt"] = prompt
    meta["images"] = paths
    out = RAW / f"SB_{plano}_t{toma}_sunburst_0.png"
    urllib.request.urlretrieve(result["images"][0]["url"], out)
    (RAW / f"SB_{plano}_t{toma}_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1))
    return plano, str(out), handle.request_id, list(meta.keys())


def next_toma(plano):
    n = 0
    while (RAW / f"SB_{plano}_t{n}_sunburst_0.png").exists():
        n += 1
    return str(n)


def main():
    planes = sys.argv[1:]
    if not planes:
        sys.exit("falta el plano")
    need = RESERVA * len(planes)
    if gastado() + need > TOPE + 1e-9:
        sys.exit(f"PARAR: {gastado():.2f} + reserva {need:.2f} pasa {TOPE}")
    RAW.mkdir(exist_ok=True)
    ok = 0
    with ThreadPoolExecutor(max_workers=min(6, len(planes))) as pool:
        futs = {pool.submit(one, p, next_toma(p)): p for p in planes}
        for f in as_completed(futs):
            try:
                plano, out, rid, keys = f.result()
                print("OK", plano, out, rid, ",".join(keys), flush=True)
                ok += 1
            except Exception as e:
                print("ERROR", futs[f], str(e)[:400], flush=True)
    if ok < len(planes):
        sys.exit(1)


if __name__ == "__main__":
    main()
