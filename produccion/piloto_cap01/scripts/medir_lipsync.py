#!/usr/bin/env python3
"""Mide una toma con diálogo contra la pista limpia.

1) Audio: correlación y desfase entre la envolvente del audio de la toma y la pista limpia.
2) Boca: energía de movimiento en la zona de la boca de cada personaje, dentro y fuera
   de las ventanas en que le toca hablar.
3) Tira de recortes de boca por cuadro, con la onda de la pista debajo, para revisión humana.

Uso:
  python3 -I medir_lipsync.py --ffmpeg RUTA --video toma.mp4 --pista c02a.wav --out carpeta \
     --boca "tomas:0.55,0.30,0.22,0.10" --boca "martina:0.14,0.33,0.22,0.10" \
     --linea "tomas:0.80-1.84" --linea "martina:2.56-3.20" --hasta 3.7
Las cajas van en fracción del cuadro: x,y,ancho,alto.
No usa claves ni red. Requiere numpy, opencv y Pillow.
"""
import argparse, json, os, subprocess, sys, wave
for p in (os.path.expanduser("~/Library/Python/3.9/lib/python/site-packages"),):
    if os.path.isdir(p) and p not in sys.path: sys.path.append(p)
import numpy as np, cv2
from PIL import Image, ImageDraw

def wav_mono(ffmpeg, src, dst, sr=16000):
    subprocess.run([ffmpeg, "-y", "-v", "error", "-i", src, "-vn", "-ac", "1", "-ar", str(sr), "-c:a", "pcm_s16le", dst], check=False)
    if not os.path.exists(dst) or os.path.getsize(dst) < 1000: return None, sr
    with wave.open(dst) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    return x, sr

def envolvente(x, sr, ms=25):
    n = max(1, int(sr * ms / 1000)); k = np.ones(n) / n
    e = np.convolve(np.abs(x), k, mode="same")
    return e[:: n // 2 or 1], sr / (n // 2 or 1)

def correlacion(a, b, fs, max_lag_s=1.0):
    n = min(len(a), len(b)); a = a[:n] - a[:n].mean(); b = b[:n] - b[:n].mean()
    mejor = (-2, 0); L = int(max_lag_s * fs)
    for lag in range(-L, L + 1):
        if lag >= 0: x, y = a[lag:], b[: n - lag]
        else: x, y = a[: n + lag], b[-lag:]
        if len(x) < fs: continue
        d = (np.linalg.norm(x) * np.linalg.norm(y)) or 1e-9
        c = float(np.dot(x, y) / d)
        if c > mejor[0]: mejor = (c, lag)
    return mejor[0], mejor[1] / fs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ffmpeg", required=True); ap.add_argument("--video", required=True)
    ap.add_argument("--pista", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--boca", action="append", default=[]); ap.add_argument("--linea", action="append", default=[])
    ap.add_argument("--hasta", type=float, default=0.0)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    nombre = os.path.splitext(os.path.basename(a.video))[0]
    res = {"toma": nombre}
    # --- audio
    xt, sr = wav_mono(a.ffmpeg, a.video, os.path.join(a.out, nombre + "_audio.wav"))
    xp, _ = wav_mono(a.ffmpeg, a.pista, os.path.join(a.out, "pista_ref.wav"))
    if xt is None: res["audio"] = {"tiene_audio": False}
    else:
        et, fs = envolvente(xt, sr); ep, _ = envolvente(xp, sr)
        c, lag = correlacion(et, ep, fs)
        res["audio"] = {"tiene_audio": True, "correlacion": round(c, 3), "desfase_s": round(lag, 3),
                        "nota": "desfase > 0: la toma va atrasada respecto de la pista"}
    # --- video
    cap = cv2.VideoCapture(a.video); fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)); H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cajas = {}
    for b in a.boca:
        n, v = b.split(":"); x, y, w, h = [float(t) for t in v.split(",")]
        cajas[n] = (int(x * W), int(y * H), int(w * W), int(h * H))
    lineas = {}
    for l in a.linea:
        n, v = l.split(":"); t0, t1 = [float(t) for t in v.split("-")]
        lineas.setdefault(n, []).append((t0, t1))
    cuadros = []; ok, f = cap.read()
    while ok:
        cuadros.append(f); ok, f = cap.read()
    cap.release()
    dur = len(cuadros) / fps; hasta = a.hasta or dur
    res["video"] = {"ancho": W, "alto": H, "fps": round(fps, 3), "cuadros": len(cuadros), "duracion_s": round(dur, 3)}
    res["boca"] = {}
    for n, (x, y, w, h) in cajas.items():
        g = [cv2.cvtColor(c[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY).astype(np.float32) for c in cuadros]
        mov = np.array([0.0] + [float(np.mean(np.abs(g[i] - g[i - 1]))) for i in range(1, len(g))])
        t = np.arange(len(mov)) / fps
        dentro = np.zeros(len(mov), bool)
        for (t0, t1) in lineas.get(n, []): dentro |= (t >= t0) & (t <= t1 + 0.1)
        valido = t <= hasta
        md = float(mov[dentro & valido].mean()) if (dentro & valido).any() else 0.0
        mf = float(mov[~dentro & valido].mean()) if (~dentro & valido).any() else 0.0
        res["boca"][n] = {"mov_hablando": round(md, 3), "mov_callado": round(mf, 3),
                          "razon": round(md / mf, 2) if mf > 0 else None,
                          "lineas": lineas.get(n, [])}
    # --- tira para revisión humana: bandas de 24 cuadros (2 s a 12 cuadros por segundo)
    paso = max(1, int(round(fps / 12))); idx = [i for i in range(0, len(cuadros), paso) if i / fps <= hasta]
    cw, ch, margen, por_banda = 150, 84, 90, 24; filas = list(cajas.items())
    alto_banda = (ch + 12) * len(filas) + 64
    bandas = [idx[k:k + por_banda] for k in range(0, len(idx), por_banda)]
    img = Image.new("RGB", (margen + cw * por_banda, alto_banda * len(bandas)), (18, 18, 18)); d = ImageDraw.Draw(img)
    ep = None
    if xp is not None:
        ep, fse = envolvente(xp, 16000); emax = ep.max() or 1
    for nb, banda in enumerate(bandas):
        yb0 = nb * alto_banda
        for r, (n, (x, y, w, h)) in enumerate(filas):
            y0 = yb0 + r * (ch + 12); d.text((4, y0 + ch // 2 - 6), n, fill=(230, 230, 230))
            for k, i in enumerate(banda):
                rec = cv2.cvtColor(cuadros[i][y:y + h, x:x + w], cv2.COLOR_BGR2RGB)
                img.paste(Image.fromarray(rec).resize((cw, ch)), (margen + k * cw, y0))
                ti = i / fps; habla = any(t0 <= ti <= t1 + 0.1 for (t0, t1) in lineas.get(n, []))
                d.rectangle([margen + k * cw, y0 + ch, margen + (k + 1) * cw - 1, y0 + ch + 7], fill=(60, 200, 90) if habla else (70, 70, 70))
        yp = yb0 + (ch + 12) * len(filas)
        d.text((4, yp + 16), "pista", fill=(230, 230, 230))
        for k, i in enumerate(banda):
            ti = i / fps
            if ep is not None:
                j = min(len(ep) - 1, int(ti * fse)); hh = int(36 * ep[j] / emax)
                d.rectangle([margen + k * cw + 2, yp + 40 - hh, margen + (k + 1) * cw - 3, yp + 40], fill=(240, 190, 60))
            if k % 3 == 0: d.text((margen + k * cw + 2, yp + 44), "%.2f s" % ti, fill=(200, 200, 200))
    tira = os.path.join(a.out, nombre + "_bocas.png"); img.save(tira); res["tira"] = tira
    json.dump(res, open(os.path.join(a.out, nombre + "_medicion.json"), "w"), ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False))

if __name__ == "__main__":
    main()
