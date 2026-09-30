#!/usr/bin/env python3
"""Cliente mínimo de la cola de fal.ai. Lee FAL_KEY del entorno; nunca del repo.

Uso:
  python3 tools/fal_run.py <endpoint> <input.json> <carpeta_salida>
"""
import json
import os
import sys
import time
import urllib.request

KEY = os.environ["FAL_KEY"]
HEAD = {"Authorization": f"Key {KEY}", "Content-Type": "application/json"}


def call(url, data=None):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None, headers=HEAD)
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


def run(endpoint, payload, poll=3, timeout=900):
    job = call(f"https://queue.fal.run/{endpoint}", payload)
    t0 = time.time()
    while time.time() - t0 < timeout:
        st = call(job["status_url"])
        if st["status"] == "COMPLETED":
            return call(job["response_url"])
        time.sleep(poll)
    raise TimeoutError(job["request_id"])


def download(url, path):
    urllib.request.urlretrieve(url, path)


if __name__ == "__main__":
    endpoint, inp, out = sys.argv[1:4]
    os.makedirs(out, exist_ok=True)
    res = run(endpoint, json.load(open(inp)))
    json.dump(res, open(os.path.join(out, "resultado.json"), "w"), indent=2)
    items = res.get("images") or ([res["video"]] if "video" in res else [])
    for i, f in enumerate(items):
        ext = os.path.splitext(f["url"])[1] or (".mp4" if "video" in res else ".png")
        download(f["url"], os.path.join(out, f"{i}{ext}"))
    print(json.dumps({k: v for k, v in res.items() if k not in ("images",)}, indent=1)[:600])
