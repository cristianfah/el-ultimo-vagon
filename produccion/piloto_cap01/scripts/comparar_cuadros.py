#!/usr/bin/env python3
"""Arma una comparación lado a lado de varios cuadros, con una etiqueta bajo cada uno.
Uso: python3 -I comparar_cuadros.py salida.jpg "etiqueta=ruta.png" "etiqueta=ruta.png" ...
"""
import os, sys
p = os.path.expanduser("~/Library/Python/3.9/lib/python/site-packages")
if os.path.isdir(p) and p not in sys.path: sys.path.append(p)
from PIL import Image, ImageDraw, ImageFont
out, items = sys.argv[1], [a.split("=", 1) for a in sys.argv[2:]]
H, pad, lab = 1280, 16, 64
ims = []
for etiqueta, ruta in items:
    im = Image.open(ruta).convert("RGB"); w = int(im.width * H / im.height)
    ims.append((etiqueta, im.resize((w, H), Image.LANCZOS)))
W = sum(im.width for _, im in ims) + pad * (len(ims) + 1)
lienzo = Image.new("RGB", (W, H + lab + pad * 2), (14, 14, 14)); d = ImageDraw.Draw(lienzo)
try: f = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 34)
except Exception: f = ImageFont.load_default()
x = pad
for etiqueta, im in ims:
    lienzo.paste(im, (x, pad)); d.text((x + 4, H + pad + 14), etiqueta, fill=(235, 235, 235), font=f); x += im.width + pad
lienzo.save(out, quality=90); print(out, lienzo.size)
