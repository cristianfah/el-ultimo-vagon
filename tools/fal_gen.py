"""Genera o edita imágenes en fal.ai con las referencias del proyecto.

Uso:
    python tools/fal_gen.py --prompt prompts/set_base.txt --images a.png b.png \
        --out salidas/set_base --models nbp flare --ar 9:16

Corre el mismo prompt en cada modelo pedido y guarda los resultados como
<out>_<modelo>_<n>.png. Necesita la variable de entorno FAL_KEY.
"""

import argparse
import pathlib
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import fal_client

ENDPOINTS = {
    "nbp": "fal-ai/nano-banana-pro/edit",
    "flare": "openai/gpt-image-2.5/flare/edit",
    "sunburst": "openai/gpt-image-2.5/sunburst/edit",
}

TEXT_ENDPOINTS = {"nbp": "fal-ai/nano-banana-pro"}

# GPT Image 2.5 pide tamaños en múltiplos de 16.
GPT_SIZES = {
    "9:16": {"width": 1152, "height": 2048},
    "16:9": {"width": 2048, "height": 1152},
    "4:5": {"width": 1632, "height": 2048},
    "1:1": {"width": 2048, "height": 2048},
}


def build_args(model, prompt, urls, ar, n):
    if model == "nbp":
        return {"prompt": prompt, "image_urls": urls, "aspect_ratio": ar,
                "resolution": "2K", "num_images": n, "output_format": "png"}
    return {"prompt": prompt, "image_urls": urls, "image_size": GPT_SIZES[ar],
            "quality": "high", "num_images": n, "output_format": "png"}


def run(model, prompt, urls, ar, n, out):
    endpoint = ENDPOINTS[model]
    args = build_args(model, prompt, urls, ar, n)
    if not urls:
        if model not in TEXT_ENDPOINTS:
            raise ValueError("sin imágenes de referencia solo funciona con nbp")
        endpoint = TEXT_ENDPOINTS[model]
        args.pop("image_urls")
    result = fal_client.subscribe(endpoint, arguments=args)
    paths = []
    for i, img in enumerate(result["images"]):
        path = pathlib.Path(f"{out}_{model}_{i}.png")
        path.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(img["url"], path)
        paths.append(str(path))
    return paths


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt", required=True, help="archivo .txt con el prompt")
    p.add_argument("--images", nargs="*", default=[], help="referencias locales, en orden (image 1, image 2…)")
    p.add_argument("--out", required=True, help="prefijo de salida")
    p.add_argument("--models", nargs="+", default=["nbp", "flare"], choices=ENDPOINTS)
    p.add_argument("--ar", default="9:16", choices=GPT_SIZES)
    p.add_argument("-n", type=int, default=1)
    a = p.parse_args()

    prompt = pathlib.Path(a.prompt).read_text().strip()
    urls = [fal_client.upload_file(f) for f in a.images]
    with ThreadPoolExecutor() as pool:
        futures = {m: pool.submit(run, m, prompt, urls, a.ar, a.n, a.out) for m in a.models}
        for m, f in futures.items():
            try:
                print(m, *f.result())
            except Exception as e:
                print(m, "ERROR", e)


if __name__ == "__main__":
    main()
