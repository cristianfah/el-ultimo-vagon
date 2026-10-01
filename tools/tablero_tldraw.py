#!/usr/bin/env python3
"""Arma un tablero .tldr (tldraw) con todas las imágenes y el story del proyecto.

Uso:
  python3 tools/tablero_tldraw.py --src /tmp/fin /tmp/fin2 /tmp/finp /tmp/final /tmp/h /tmp/kf /tmp/up/mj \
      --out /tmp/tablero/el_ultimo_vagon.tldr

Las imágenes se buscan por nombre en las carpetas de --src y se incrustan reducidas.
Necesita Node con @tldraw/tlschema instalado en --node-modules (por defecto /tmp/tl):
  mkdir -p /tmp/tl && cd /tmp/tl && npm i @tldraw/tlschema
"""
import argparse
import base64
import io
import json
import os
import subprocess
import sys

from PIL import Image

STORY = [
    ("0:00", "COLD OPEN. Una mano golpea la ventanita. Martina, casi sin voz: «Diego…». 20 MINUTOS ANTES.", ["F03_rojo_puerta_desde_dentro_0-45"]),
    ("0:03", "Martina y Tomás, juntos sin tocarse. «Este viaje es para arreglarlo, ¿cierto?» «Sí.»", ["KF01_0-03_pareja_ambar", "F09_ambar_asiento_pareja"]),
    ("0:08", "INSERTO: mensaje de «D»: Estoy en el tren. Ella da vuelta el celular.", ["PROP_celular_martina"]),
    ("0:11", "Carmen dormita, Iván observa, Hugo revisa boletos: se ve la culata del revólver.", ["F08_ambar_pasajeros_hacia_puerta"]),
    ("0:16", "Gritos desde adelante. Las luces pasan a rojo de emergencia.", ["F10_rojo_pasajeros_hacia_puerta"]),
    ("0:19", "LA REGLA DEL CONTAGIO. El hombre de camisa azul: «fue un rasguño». Iván lo ve todo.", ["HOJA_extra_pareja_camisa_azul", "F11_rojo_pasajeros_hacia_atras"]),
    ("0:23", "«¡Al último vagón!» Hugo gira la llave vieja, se traba, la fuerza.", ["F12_rojo_detalle_llave_0-23"]),
    ("0:28", "Por la ventanita ven cómo los infectados se llevan al resto.", ["F07_rojo_fuelle_vestibulo"]),
    ("0:31", "Seis personas bajo la luz roja. Iván: «Nadie abre esa puerta.» Carmen: «Hay gente viva allá afuera.»", ["F01_rojo_ultimo_vagon_hacia_puerta"]),
    ("0:37", "INSERTO: Hugo abre el tambor a escondidas. Dos balas.", ["F06_rojo_esquina_trasera_0-37", "PROP_revolver_dos_balas"]),
    ("0:40", "Tomás abraza a Martina; ella mira el celular. «D»: ¿Dónde estás?", ["F05_rojo_tres_cuartos_hacia_puerta"]),
    ("0:45", "Golpes de persona. Diego en la ventanita: «¡Martina, ábreme!»", ["KF02_0-45_diego_ventanita", "F04_rojo_puerta_desde_fuelle"]),
    ("0:49–1:04", "Tomás: «¿Quién es?» Iván: «¿Te mordieron?» Carmen no puede ver el brazo. «Si fuera tu hijo…»", ["F05_rojo_tres_cuartos_hacia_puerta"]),
    ("1:08", "Detrás de Diego, los infectados doblan la esquina.", ["F07_rojo_fuelle_vestibulo"]),
    ("1:10", "Hugo saca el revólver, le tiembla la mano. Le pone la llave a Martina en la mano.", ["PROP_llave_y_cerradura", "F02_rojo_ultimo_vagon_hacia_fondo_cabina"]),
    ("1:16", "Tomás, frío: «Ábrele. Quiero saber quién es.»", []),
    ("1:19", "Martina con la llave. Tomás detrás, el revólver al lado, Diego en el vidrio. CORTE A NEGRO.", ["KF03_1-19_martina_llave"]),
    ("1:23", "ENCUESTA: ¿MARTINA LE ABRE LA PUERTA A DIEGO?  SÍ · NO", []),
]

KEYFRAMES = [
    ("KF01_0-03_pareja_ambar", "KF01 · 0:03 · Flare · 50 mm"),
    ("KF02_0-45_diego_ventanita", "KF02 · 0:45 · Flare · 35 mm"),
    ("KF03_1-19_martina_llave", "KF03 · 1:19 · Flare · 40 mm"),
]

PERSONAJES = [
    ("Martina", "martina"), ("Tomás", "tomas"), ("Diego", "diego"), ("Carmen", "carmen"),
    ("Iván", "ivan"), ("Don Hugo", "hugo"), ("Pareja extra", "extra_pareja_camisa_azul"),
]

SET_LOOK = ["look_ambar_plancha_heroe", "look_rojo_plancha_heroe"]
SET_VISTAS = ["set_v01_base_hacia_puerta", "set_v02_eje_inverso_cabina", "set_v03_puerta_interior",
              "set_v04_puerta_exterior_fuelle", "set_v05_lateral_asientos"]
SET_FINALES = [
    "F01_rojo_ultimo_vagon_hacia_puerta", "F02_rojo_ultimo_vagon_hacia_fondo_cabina",
    "F03_rojo_puerta_desde_dentro_0-45", "F04_rojo_puerta_desde_fuelle", "F05_rojo_tres_cuartos_hacia_puerta",
    "F06_rojo_esquina_trasera_0-37", "F07_rojo_fuelle_vestibulo", "F08_ambar_pasajeros_hacia_puerta",
    "F09_ambar_asiento_pareja", "F10_rojo_pasajeros_hacia_puerta", "F11_rojo_pasajeros_hacia_atras",
    "F12_rojo_detalle_llave_0-23",
]
PROPS = ["PROP_llave_y_cerradura", "PROP_freno_emergencia", "PROP_revolver_dos_balas", "PROP_celular_martina"]
MJ = ["cara_martina_mj01", "cara_tomas_mj01", "cara_diego_mj01", "cara_carmen_mj01", "cara_ivan_mj01",
      "cara_hugo_mj01", "extra_pareja_mj01", "vest_tomas_mj01", "vest_diego_mj01", "vest_carmen_mj01",
      "vest_ivan_mj01", "vest_hugo_mj01", "set_ultimo_vagon_look_mj01", "set_ultimo_vagon_look_mj02",
      "set_ultimo_vagon_look_mj03", "set_puerta_mj01", "set_pasillo_exterior_mj01", "set_pasillo_exterior_mj02"]

PENDIENTES = [
    "Aprobar F01–F12, los 4 props, las 7 referencias de personaje, el estado de Diego y KF01–KF03.",
    "Tomás se ve algo atlético y más guapo que Diego: ajustar contextura, no cara.",
    "El cuello de Iván se lee como cuero en planos cercanos.",
    "Bajo luz roja, el abrigo de Martina la oscurece y la camisa azul se vuelve negra (0:19).",
    "Decidir «South American» o «Chilean» en los prompts.",
    "1:10: pedir la placa de bronce de la llave. La cinta de la fila 5 izquierda aún no aparece.",
]

GAP = 40
LABEL_H = 70
PAD = 80
HEADER_H = 120


class Board:
    def __init__(self, srcs, max_side):
        self.srcs = srcs
        self.max_side = max_side
        self.assets = {}
        self.shapes = []
        self.n = 0

    def _id(self, prefix):
        self.n += 1
        return f"{prefix}:s{self.n:04d}"

    def find(self, name):
        for d in self.srcs:
            p = os.path.join(d, name + ".png")
            if os.path.exists(p):
                return p
        return None

    def asset(self, name):
        if name in self.assets:
            return self.assets[name]
        path = self.find(name)
        if not path:
            print(f"falta {name}", file=sys.stderr)
            return None
        im = Image.open(path).convert("RGB")
        im.thumbnail((self.max_side, self.max_side))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=82)
        aid = f"asset:{name}"
        self.assets[name] = (aid, im.width, im.height, {
            "id": aid, "typeName": "asset", "type": "image", "meta": {},
            "props": {"name": name + ".jpg", "src": "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode(),
                      "w": im.width, "h": im.height, "mimeType": "image/jpeg", "isAnimated": False,
                      "fileSize": buf.tell()},
        })
        return self.assets[name]

    def shape(self, type_, x, y, props, parent="page:page"):
        sid = self._id("shape")
        self.shapes.append({"id": sid, "typeName": "shape", "type": type_, "x": x, "y": y, "rotation": 0,
                            "isLocked": False, "opacity": 1, "meta": {}, "parentId": parent, "props": props})
        return sid

    @staticmethod
    def rich(text):
        paras = []
        for line in text.split("\n"):
            paras.append({"type": "paragraph", "content": [{"type": "text", "text": line}]} if line else {"type": "paragraph"})
        return {"type": "doc", "content": paras}

    def text(self, x, y, s, w, size="s", parent="page:page", color="black", font="sans"):
        return self.shape("text", x, y, {"color": color, "size": size, "font": font, "textAlign": "start", "w": w,
                                         "richText": self.rich(s), "scale": 1, "autoSize": False}, parent)

    def note(self, x, y, s, color="yellow", parent="page:page", size="s", scale=1.8):
        return self.shape("note", x, y, {"color": color, "labelColor": "black", "size": size, "font": "sans",
                                         "fontSizeAdjustment": 0, "align": "start", "verticalAlign": "start",
                                         "growY": 0, "url": "", "richText": self.rich(s), "scale": scale,
                                         "textLastEditedBy": None}, parent)

    def image(self, name, x, y, h=None, w=None, parent="page:page", label=None):
        a = self.asset(name)
        if not a:
            return 0, 0
        aid, iw, ih, _ = a
        if h is not None:
            w = round(iw * h / ih)
        else:
            h = round(ih * w / iw)
        self.shape("image", x, y, {"w": w, "h": h, "playing": True, "url": "", "assetId": aid, "crop": None,
                                   "flipX": False, "flipY": False, "altText": name}, parent)
        self.text(x, y + h + 8, label if label is not None else name, w, "s", parent)
        return w, h

    def frame(self, x, y, w, h, name):
        return self.shape("frame", x, y, {"w": w, "h": h, "name": name, "color": "black"})

    def fit_frames(self):
        frames = {s["id"]: s for s in self.shapes if s["type"] == "frame"}
        ext = {fid: [0, 0] for fid in frames}
        for s in self.shapes:
            if s["parentId"] not in ext:
                continue
            p = s["props"]
            if s["type"] == "note":
                w = h = 200 * p["scale"]
            elif s["type"] == "text":
                w, h = min(p["w"], 600), 40
            else:
                w, h = p["w"], p["h"]
            e = ext[s["parentId"]]
            e[0], e[1] = max(e[0], s["x"] + w), max(e[1], s["y"] + h)
        y = next(iter(frames.values()))["y"] if frames else 0
        for fid, (w, h) in ext.items():
            frames[fid]["props"]["w"] = round(w + PAD)
            frames[fid]["props"]["h"] = round(h + PAD)
            frames[fid]["y"] = y
            y += frames[fid]["props"]["h"] + 200

    def records(self):
        self.fit_frames()
        from_index = indices(len(self.shapes))
        for s, idx in zip(self.shapes, from_index):
            s["index"] = idx
        base = [
            {"id": "document:document", "typeName": "document", "gridSize": 10, "name": "EL ÚLTIMO VAGÓN", "meta": {}},
            {"id": "page:page", "typeName": "page", "name": "Visor del proyecto", "index": "a1", "meta": {}},
        ]
        return base + [a[3] for a in self.assets.values()] + self.shapes


def indices(n):
    out, i = [], 0
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(n):
        out.append("b" + alphabet[i // 62 % 62] + alphabet[i % 62])
    return out


def row(b, fid, x, y, names, h, labels=None):
    for i, n in enumerate(names):
        w, _ = b.image(n, x, y, h=h, parent=fid, label=(labels[i] if labels else None))
        x += w + GAP
    return x


def build(b):
    y = 0
    b.text(0, y, "EL ÚLTIMO VAGÓN · visor del proyecto", 3000, "xl")
    b.text(0, y + 110, "Microserie vertical 9:16 de zombies donde el público decide. Seis pasajeros encerrados en el último vagón "
                       "de un tren nocturno, el primer día del brote. Triángulo: Martina, Tomás y Diego.\n"
                       "Guion vigente: guion/cap01/cap01_v3.md · Fuente de verdad: biblia/ · Imágenes: Drive, imagenes/03_para_aprobacion",
           3000, "m")
    y += 360

    col_w, img_h = 380, 560
    fw = PAD * 2 + len(STORY) * (col_w + GAP)
    fh = HEADER_H + 300 + 2 * (img_h + LABEL_H + GAP) + PAD
    fid = b.frame(0, y, fw, fh, "STORY · Capítulo 1 (guion v3) · keyframes en verde")
    for i, (tc, txt, imgs) in enumerate(STORY):
        x = PAD + i * (col_w + GAP)
        b.note(x, HEADER_H - 40, f"{tc}\n{txt}", "light-green" if any(n.startswith("KF") for n in imgs) else "yellow", fid)
        yy = HEADER_H + 380
        for n in imgs:
            w, h = b.image(n, x, yy, h=img_h if not n.startswith(("PROP", "HOJA")) else None,
                           w=col_w if n.startswith(("PROP", "HOJA")) else None, parent=fid)
            yy += h + LABEL_H + GAP
    y += fh + 200

    kh = 1300
    fid = b.frame(0, y, PAD * 2 + 3 * (round(kh * 9 / 16) + GAP), HEADER_H + kh + LABEL_H + PAD, "KEYFRAMES DE PRUEBA · para aprobación")
    row(b, fid, PAD, HEADER_H, [k for k, _ in KEYFRAMES], kh, [l for _, l in KEYFRAMES])
    y += HEADER_H + kh + LABEL_H + PAD + 200

    rh, hh = 700, 700
    fid_y = y
    x = PAD
    cols = []
    for nombre, key in PERSONAJES:
        cols.append((nombre, key, x))
        x += round(rh * 9 / 16) + GAP + round(hh * 16 / 9) + GAP * 3
    fw = x + PAD
    fh = HEADER_H + 60 + rh + LABEL_H + PAD + rh + LABEL_H + 60
    fid = b.frame(0, fid_y, fw, fh, "PERSONAJES · referencia + hoja")
    for nombre, key, cx in cols:
        b.text(cx, HEADER_H - 20, nombre, 800, "l", fid)
        w, _ = b.image("REF_" + key, cx, HEADER_H + 60, h=rh, parent=fid)
        b.image("HOJA_" + key, cx + w + GAP, HEADER_H + 60, h=hh, parent=fid)
    b.text(PAD, HEADER_H + 60 + rh + LABEL_H + 40, "Estados", 800, "l", fid)
    b.image("ESTADO_diego_mojado_herido", PAD, HEADER_H + 60 + rh + LABEL_H + 120, h=rh - 120, parent=fid)
    y += fh + 200

    sh = 700
    fw = PAD * 2 + 12 * (round(sh * 9 / 16) + GAP) + 200
    fh = HEADER_H + 3 * (60 + sh + LABEL_H + GAP) + PAD
    fid = b.frame(0, y, fw, fh, "SET · último vagón, fuelle y vagón de pasajeros")
    yy = HEADER_H
    for titulo, names in [("Look (ámbar y rojo)", SET_LOOK), ("Vistas técnicas · luz neutra = plano técnico", SET_VISTAS),
                          ("Planchas finales F01–F12", SET_FINALES)]:
        b.text(PAD, yy - 10, titulo, 2000, "l", fid)
        row(b, fid, PAD, yy + 60, names, sh)
        yy += 60 + sh + LABEL_H + GAP
    y += fh + 200

    ph = 600
    fw = PAD * 2 + 4 * (round(ph * 16 / 9) + GAP)
    fid = b.frame(0, y, fw, HEADER_H + ph + LABEL_H + PAD, "PROPS")
    row(b, fid, PAD, HEADER_H, PROPS, ph)
    y += HEADER_H + ph + LABEL_H + PAD + 200

    mh = 500
    fid = b.frame(0, y, PAD * 2 + len(MJ) * (mh + GAP), HEADER_H + mh + LABEL_H + PAD, "EXPLORACIÓN MIDJOURNEY · solo referencia")
    row(b, fid, PAD, HEADER_H, MJ, mh)
    y += HEADER_H + mh + LABEL_H + PAD + 200

    fid = b.frame(0, y, PAD * 2 + len(PENDIENTES) * 400, HEADER_H + 400, "PENDIENTES / NOTAS PARA CRISTIAN")
    for i, p in enumerate(PENDIENTES):
        b.note(PAD + i * 400, HEADER_H, p, "orange", fid)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--max-side", type=int, default=1280)
    ap.add_argument("--node-modules", default="/tmp/tl")
    a = ap.parse_args()

    b = Board(a.src, a.max_side)
    build(b)
    recs = b.records()
    tmp = a.out + ".records.json"
    with open(tmp, "w") as f:
        json.dump(recs, f)
    js = r"""
const fs=require('fs');const t=require('@tldraw/tlschema');
const [tmp,out]=process.argv.slice(1);
const recs=JSON.parse(fs.readFileSync(tmp,'utf8'));const s=t.createTLSchema();
for(const r of recs){s.types[r.typeName].validate(r);}
fs.writeFileSync(out,JSON.stringify({tldrawFileFormatVersion:1,schema:s.serialize(),records:recs}));
console.log('ok',recs.length,'registros');
"""
    subprocess.run(["node", "-e", js, tmp, a.out], check=True, cwd=a.node_modules)
    os.remove(tmp)
    print(a.out, f"{os.path.getsize(a.out) / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
