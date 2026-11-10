#!/usr/bin/env python3
"""Hoja de contacto antes/después. Uso: python3 -I hoja_antes_despues.py salida.jpg columnas "id=antes.png=despues.png" ..."""
import os, sys
p = os.path.expanduser("~/Library/Python/3.9/lib/python/site-packages")
if os.path.isdir(p) and p not in sys.path: sys.path.append(p)
from PIL import Image, ImageDraw, ImageFont
out, cols = sys.argv[1], int(sys.argv[2]); items = [a.split("=") for a in sys.argv[3:]]
w, h, pad, lab = 270, 480, 10, 34
try: f = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
except Exception: f = ImageFont.load_default()
filas = (len(items) + cols - 1) // cols; cw = w * 2 + pad * 3; chh = h + lab + pad * 2
L = Image.new("RGB", (cw * cols, chh * filas), (14, 14, 14)); d = ImageDraw.Draw(L)
for k, (i, a, b) in enumerate(items):
    x0, y0 = (k % cols) * cw, (k // cols) * chh
    for j, r in enumerate((a, b)):
        im = Image.open(r).convert("RGB").resize((w, h), Image.LANCZOS); L.paste(im, (x0 + pad + j * (w + pad), y0 + pad))
    d.text((x0 + pad, y0 + h + pad + 4), i + "   antes  →  nuevo", fill=(235, 235, 235), font=f)
L.save(out, quality=88); print(out, L.size)
