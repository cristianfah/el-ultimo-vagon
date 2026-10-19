#!/usr/bin/env python3
"""Arma log_generaciones_v1c.json desde el registro, los PNG y los meta de sunburst.

Los costos de fal no vinieron en la respuesta. Quedan marcados como estimados.
"""
import hashlib, json, os, pathlib, urllib.request
from datetime import datetime, timezone

HERE = pathlib.Path(__file__).resolve().parent
ORIG = HERE.parent / "frames"
RAW = HERE / "raw"
REG = json.loads((HERE / "registro_v1c.json").read_text())
LOTE = json.loads((HERE / "lote_v1c.json").read_text())
URLS = json.loads((HERE.parents[4] / "produccion/assets/fal_urls_v1.json").read_text())

# Tabla publicada en fal (página sunburst/edit, bloque actualizado 2026-09-09):
# high, una imagen de entrada. 1920×1080 = 0.03960; 2560×1440 = 0.05529.
# 1152×2048 = 2.359 MP, interpolado entre 2.074 MP y 3.686 MP → 0.0424.
# Cada referencia extra: +0.008, cifra del 8-sep-2026 en prompts_previs_v1.md, no remedida.
# Texto: ~0.004 (orden de 800 tokens a 5 USD / 1M). Todo es estimado.
SUN_BASE = 0.0424
SUN_EXTRA = 0.008
SUN_TEXT = 0.004

ROLES = {
    "F08_v2_ambar_bajo.png": "referencia de luz ámbar baja del vagón 2",
    "F05_rojo_tres_cuartos_hacia_puerta.png": "referencia de luz roja del último vagón",
    "F02_rojo_ultimo_vagon_hacia_fondo_cabina.png": "referencia de la pared trasera, sin segunda puerta",
    "F09_ambar_asiento_pareja.png": "referencia de la banca de dos, sin divisor central",
    "PROP_maletin_v2.png": "referencia del maletín cerrado",
    "PROP_llave_y_cerradura.png": "referencia de la llave antigua y la placa",
    "HOJA_martina.png": "hoja de Martina: cara, pelo, suéter avena, abrigo",
    "HOJA_tomas.png": "hoja de Tomás: pelo corto con partidura, anteojos, campera",
    "HOJA_carmen.png": "hoja de Carmen",
    "HOJA_hugo.png": "hoja de Hugo",
    "HOJA_ivan.png": "hoja de Iván",
    "HOJA_diego.png": "hoja de Diego",
    "HOJA_extra_pareja_camisa_azul.png": "hoja de la pareja de camisa azul",
    "ESTADO_carmen_palma_v2_palma.png": "estado de la palma derecha de Carmen",
    "ESTADO_diego_mojado_herido_v3.png": "estado de Diego mojado, manga derecha oscura",
    "b0_p4.png": "fotograma original de la lectora, para copiar cara, moño y bufanda",
    "lectora_b0_p4.png": "recorte de la lectora tomado de b0_p4",
}

# Prompts de tomas cuyo .txt se reescribió después. El resto se lee del archivo o del meta.
HIST = {}

def _p(name):
    return (HERE / "prompts" / name).read_text().strip()

# b0_p2 t0: primer prompt, antes de endurecer la posición del maletín.
HIST[("b0_p2", 0)] = _p("SB_b0_p2.txt").replace(
    "Slide the briefcase backward, toward the window, until the blue cushion covers two thirds of it. Only the front brass corner stays visible, low, in the shadow under the rail. The body of the briefcase is hidden by the seat. It is not standing on the open aisle floor.",
    "The closed hard-shell briefcase sits fully UNDER the blue seat, on the AISLE side, tucked into the shadow beneath the cushion, its back edge on the seat's metal rail. It is not out in the aisle.",
)
HIST[("b0_p2", 1)] = _p("SB_b0_p2.txt").replace(
    "Slide the briefcase backward, toward the window, until the blue cushion covers two thirds of it. Only the front brass corner stays visible, low, in the shadow under the rail. The body of the briefcase is hidden by the seat. It is not standing on the open aisle floor.",
    "The closed hard-shell briefcase is entirely in the shadow UNDER the blue cushion, aisle side. The cushion hides the top of the briefcase. Only its front face and brass corner peek out below the seat rail. It does not sit on the open floor of the aisle.",
)
HIST[("b3_p6", 0)] = _p("SB_b3_p6.txt").replace(
    "foreground left, the blue-shirt man is on his feet and lunging onto his wife. Their bodies tangle in shadow, motion blur, shapes only, nothing graphic, neither looking at the camera. They are not asleep and not sitting calmly.",
    "foreground left is a dark struggling tangle in shadow, the blue-shirt man lunging onto his wife. Shapes only, motion blur, nothing graphic, neither of them looking at the camera.",
)
HIST[("b6_p2", 0)] = _p("SB_b6_p2.txt").replace(
    "Her chin is down. Her RIGHT hand is a closed fist already inside the brown coat, between the lapels, so the knuckles disappear into the cloth. The palm faces her own chest, not the camera. A dark, almost black smear is still visible on the edge of that palm as it goes in. Her eyes are on the hand. The bag strap stays on her left shoulder. Her other hand holds the coat open just enough.",
    "Her chin is down. She looks at her own RIGHT palm, held close to her chest, the palm turned toward HER face and not toward the camera. We only glimpse the edge of that dark smear. Her fingers are curling into a fist and the fist is already slipping inside the opening of the brown coat. Her eyes stay on the hand. The bag strap stays on her left shoulder.",
)

SUN_VER = {
    ("b0_p2", 0): ("retry", "Puño de avena y luz baja correctos, ventanita seca. El maletín sigue en el piso del pasillo, al lado del asiento, no debajo del cojín."),
    ("b0_p2", 1): ("retry", "Misma falla de posición: el maletín sigue apoyado en el piso del pasillo. El puño cubre los nudillos y la luz sigue baja."),
    ("b0_p2", 2): ("accept", "Tercera toma. Puño, luz de dos o tres lámparas y ventanita seca. El maletín sigue fuera, contra el riel, no metido bajo el cojín. Se acepta con esa falla: tres regeneraciones no lo movieron y el original ya lo tenía así."),
    ("b0_p3", 0): ("accept", "Martina mira hacia abajo a la izquierda, al hombre de camisa azul. La esposa sigue dormida. Luz ámbar baja. Caras nítidas."),
    ("b3_p6", 0): ("retry", "Lectora con moño y bufanda, ventanita oscura y pocas lámparas. El primer término izquierdo está sentado y caído, no es un forcejeo."),
    ("b3_p6", 1): ("accept", "El hombre de azul está de pie abalanzado sobre la mujer. La lectora grita con moño, bufanda roja y el libro cayendo. Ventanita oscura, sin cielo."),
    ("b4_p6", 0): ("accept", "Pelo corto con partidura, manos tomadas, fuelle rojo detrás de las siluetas, sin cielo. El brazo de Martina sale de su abrigo."),
    ("b5_p6", 0): ("accept", "La llave está en la cerradura, a mitad de giro, en la mano derecha. La otra mano afirma la placa. Media cara en sombra. Sin tubo de neón largo."),
    ("b5_p8", 0): ("accept", "Plano cerrado: hombro contra la puerta, llave girando por dentro, mano gris atorada en el vano, ventanita seca. Las uñas de esa mano salieron largas. Se acepta con esa falla."),
    ("b2_p4", 0): ("accept", "Banca compartida: el lugar vacío se ve a su derecha, sin divisor. La mano sola en el apoyabrazos, ventana a la izquierda, mirada al frente. Quedó más abierto que un primer plano y con más de dos lámparas."),
    ("b6_p2", 0): ("accept", "Puño cerca del pecho, mirada baja, bolso al hombro izquierdo, media cara en sombra, piel nítida. La mancha no se lee y el puño no llega a entrar en el abrigo. No se reintentó: el presupuesto se usó en planos que no tenían toma."),
    ("b6_p3", 0): ("accept", "Pared trasera, ventanita negra sin vías ni cielo, puerta de cabina a la izquierda. Tomás a la izquierda mira a la derecha; Martina a la derecha mira el piso. El pelo no es una partidura estricta y la tira roja del techo es larga."),
    ("b7_p1", 0): ("accept", "Puerta cerrada, fuelle oscuro detrás del vidrio, sin cielo. Manchas de manos en el vidrio, más rojas que negras. El grupo está de espaldas."),
    ("b7_p3", 0): ("accept", "Martina a la derecha, enfocada, media cara en sombra. Detrás, pared con ventanita negra y puerta de cabina a la izquierda, sin vías. Iván queda grande en el primer término izquierdo, no solo en el borde."),
    ("b7_p4", 0): ("accept", "Tomás a la izquierda mira a la derecha, pelo corto con partidura, anteojos. Ventanita trasera negra, sin segunda puerta."),
    ("b7_p5", 0): ("retry", "Mira hacia atrás y el fuelle está oscuro, pero las dos manos están en el vidrio y la chaqueta tiene manchas rojo vivo en el pecho y la manga."),
    ("b7_p5", 1): ("accept", "La palma izquierda está en el vidrio y mira hacia atrás. El fuelle está oscuro. Queda una marca rojo vivo en la manga derecha, no una manga apenas más oscura."),
    ("b7_p6", 0): ("retry", "La mano de Hugo está en la manija, sin llave, y Martina mira a la izquierda. Detrás de ella hay una puerta con ventanita: es la segunda puerta que no debía estar."),
    ("b7_p6", 1): ("accept", "Pared ciega con una ventanita negra, sin puerta ni vías. La mano de Hugo, vacía, está en la manija abajo a la derecha. Martina mira a la izquierda. Cara nítida."),
    ("b3_p1", 0): ("accept", "Nadie en el pasillo, trabas abiertas y un hilo de niebla. El hombre sigue sentado. El maletín sigue al lado del asiento, no debajo: la misma falla que b0_p2."),
    ("b6_p1", 0): ("accept", "Iván de espaldas a la puerta, de frente a cámara, brazos abiertos contra el marco. Hugo al lado, manos vacías. El vidrio tiene palmas y no muestra cielo."),
    ("b7_p2", 0): ("retry", "El encuadre de la ventanita y la mirada hacia atrás sirven, pero la espalda y el vidrio tienen marcas rojo vivo. La regla es manga derecha y marcas oscuras."),
    ("b7_p2", 1): ("accept", "Ventanita ancha, mira hacia atrás, fuelle oscuro, tubo blanco arriba. La chaqueta es clara con manchas oscuras, ya no rojo vivo. Siguen marcas en la espalda, no solo en la manga derecha."),
}

FAILS = [
    {
        "id": "SB_b5_p6_fallo_carga",
        "paso": "SB_b5_p6",
        "plano": "b5_p6",
        "toma": 0,
        "timestamp": "2026-10-19T02:56:30Z",
        "timestamp_fuente": "aproximado: el lote de las 02:56 UTC; esta llamada no dejó PNG",
        "modelo": "sunburst",
        "endpoint": "openai/gpt-image-2.5/sunburst/edit",
        "params": {"image_size": {"width": 1152, "height": 2048}, "quality": "high", "aspect": "9:16", "num_images": 1, "seed": None, "output_format": "png", "resolution": None},
        "prompt_file": "prompts/SB_b5_p6.txt",
        "prompt": _p("SB_b5_p6.txt"),
        "referencias": [],
        "fal_request_id": "01a15216-809f-7271-95e9-dfef6c0d122a",
        "output": None,
        "costo_usd": None,
        "costo_tipo": "estimado",
        "latencia_s": 6.629,
        "latencia_tipo": "inference_time de fal (status COMPLETED pese al 422)",
        "veredicto": "retry",
        "motivo_visual": "422 image_load_error al leer HOJA_hugo.png subida (2752×1536). No hubo PNG. Se achicó la hoja a 1536 px y se reintentó.",
        "en_montaje": False,
        "nota_costo": "fal no devolvió un monto. Se estima igual que una toma sunburst con 4 referencias porque el status quedó COMPLETED. No está confirmado que se haya cobrado.",
    }
]


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def rel(p):
    p = pathlib.Path(p)
    try:
        return str(p.resolve().relative_to(HERE))
    except ValueError:
        try:
            return str(p.resolve().relative_to(HERE.parent))
        except ValueError:
            return str(p)


def rol(path):
    name = pathlib.Path(path).name
    if name in ROLES:
        return ROLES[name]
    if name.startswith("b") and name.endswith(".png"):
        return "fotograma original de ese plano"
    return "referencia"


def costo_sun(n):
    return round(SUN_BASE + SUN_EXTRA * max(0, n - 1) + SUN_TEXT, 4)


def inference(rid):
    key = os.environ.get("FAL_KEY")
    if not key or not rid:
        return None
    url = f"https://queue.fal.run/openai/gpt-image-2.5/requests/{rid}/status"
    req = urllib.request.Request(url, headers={"Authorization": f"Key {key}"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.loads(r.read().decode())
        return (d.get("metrics") or {}).get("inference_time")
    except Exception:
        return None


def main():
    frames = {p.name: sha(p) for p in (HERE / "frames").glob("*.png")}
    records = []
    # --- llamadas del corredor V01–V35 y el FIX ---
    by = {s["paso"]: s for s in LOTE["pasos"]}
    for paso, r in REG["pasos"].items():
        s = by[paso]
        prompt = (HERE / s["prompt"]).read_text().strip()
        for i, out in enumerate(r.get("salidas", [])):
            if out == "ERROR":
                continue
            p = pathlib.Path(out)
            if not p.exists():
                p = RAW / pathlib.Path(out).name
            aceptada = pathlib.Path(r.get("aceptada", "")).name
            if r.get("estado") == "marcado":
                ver, mot = "flag", r.get("motivo", "")
            elif r.get("estado") == "pendiente":
                ver, mot = "retry", "No se aceptó. En b6_p3 la ventanita trasera muestra vías y cielo."
            elif p.name == aceptada:
                ver, mot = "accept", "Aceptada en la pasada secuencial. Criterio del lote: " + s["revisar"]
            else:
                ver, mot = "retry", "Esta toma no se aceptó. Criterio que se volvió a pedir: " + s["revisar"]
            base_note = "fotograma que se edita"
            if s["depende_de"]:
                base_note = "salida ya editada del paso " + ",".join(s["depende_de"]) + " (v1c/frames), no el PNG original"
            refs = [{"orden": 1, "path": f"según resolve(): {s['base']}", "rol": base_note}]
            for n, ref in enumerate(s["refs"], start=2):
                refs.append({"orden": n, "path": ref, "rol": rol(ref.split(":", 1)[-1])})
            en = False
            if p.exists() and f"{s['plano']}.png" in frames and sha(p) == frames[f"{s['plano']}.png"]:
                en = True
            rec = {
                "id": f"{paso}_t{i}",
                "paso": paso,
                "plano": s["plano"],
                "toma": i,
                "timestamp": iso(p.stat().st_mtime) if p.exists() else None,
                "timestamp_fuente": "mtime del PNG de salida, UTC" if p.exists() else None,
                "modelo": s["modelo"],
                "endpoint": {"nbp": "fal-ai/nano-banana-pro/edit", "flare": "openai/gpt-image-2.5/flare/edit"}[s["modelo"]],
                "params": {
                    "resolution": "2K" if s["modelo"] == "nbp" else None,
                    "quality": "high" if s["modelo"] == "flare" else None,
                    "aspect": "9:16",
                    "image_size": {"width": 1152, "height": 2048} if s["modelo"] == "flare" else None,
                    "num_images": 1,
                    "seed": None,
                    "output_format": "png",
                },
                "prompt_file": s["prompt"],
                "prompt": prompt,
                "referencias": refs,
                "fal_request_id": None,
                "output": rel(p) if p.exists() else out,
                "costo_usd": s["costo_est_usd"],
                "costo_tipo": "estimado",
                "nota_costo": "Cifra del lote (NBP 0.15, flare 0.08). fal_gen.py no guarda el monto ni el request_id. El corredor sumó esta cifra a gastado_usd.",
                "latencia_s": None,
                "latencia_tipo": "no medida",
                "veredicto": ver,
                "motivo_visual": mot,
                "en_montaje": en,
            }
            records.append(rec)
    # FIX, fuera del corredor
    for i, name in enumerate(["FIX_b2_p4_asiento_t0_nbp_0.png", "FIX_b2_p4_asiento_t1_nbp_0.png", "FIX_b2_p4_asiento_t2_nbp_0.png"]):
        p = RAW / name
        motivos = [
            "accept", "Se ve la banca de dos, pero el plano quedó más abierto que el primer plano.",
            "retry", "No abrió el lugar de al lado: seguía leyéndose como asiento individual.",
            "retry", "No cerró el encuadre.",
        ]
        ver, mot = motivos[i * 2], motivos[i * 2 + 1]
        prompt_file = ["prompts/FIX_b2_p4_asiento.txt", "prompts/FIX_b2_p4_asiento_t1.txt", "prompts/FIX_b2_p4_asiento_t2.txt"][i]
        records.append({
            "id": f"FIX_b2_p4_t{i}",
            "paso": "FIX_b2_p4",
            "plano": "b2_p4",
            "toma": i,
            "timestamp": iso(p.stat().st_mtime),
            "timestamp_fuente": "mtime del PNG, UTC",
            "modelo": "nbp",
            "endpoint": "fal-ai/nano-banana-pro/edit",
            "params": {"resolution": "2K", "quality": None, "aspect": "9:16", "image_size": None, "num_images": 1, "seed": None, "output_format": "png"},
            "prompt_file": prompt_file,
            "prompt": (HERE / prompt_file).read_text().strip(),
            "referencias": [
                {"orden": 1, "path": "frames/b2_p4.png en ese momento (salida de V18, ya editada)" if i == 0 else f"raw/FIX_b2_p4_asiento_t{i-1}_nbp_0.png", "rol": "imagen ya editada, no el original"},
                {"orden": 2, "path": ".refs_cache/F09_ambar_asiento_pareja.png", "rol": ROLES["F09_ambar_asiento_pareja.png"]},
            ],
            "fal_request_id": None,
            "output": rel(p),
            "costo_usd": 0.15,
            "costo_tipo": "estimado",
            "nota_costo": "Misma tarifa estimada de NBP. No está dentro de gastado_usd del corredor; el registro la anota aparte como 0.45 por las tres tomas.",
            "latencia_s": None,
            "latencia_tipo": "no medida",
            "veredicto": ver,
            "motivo_visual": mot,
            "en_montaje": sha(p) == frames.get("b2_p4.png"),
        })
    # sunburst
    for meta_path in sorted(RAW.glob("SB_*_meta.json")):
        if meta_path.name.startswith("_"):
            continue
        # SB_b0_p2_t0_meta.json
        stem = meta_path.name.replace("_meta.json", "")
        parts = stem.split("_t")
        plano = parts[0][3:]
        toma = int(parts[1].split("_")[0])
        meta = json.loads(meta_path.read_text())
        png = RAW / f"SB_{plano}_t{toma}_sunburst_0.png"
        prompt = meta.get("prompt") or HIST.get((plano, toma)) or _p(f"SB_{plano}.txt")
        prompt_fuente = "meta de la llamada" if meta.get("prompt") else ("texto reconstruido de antes de reescribir el archivo" if (plano, toma) in HIST else "archivo vigente; no se reescribió después de esta toma")
        imgs = meta.get("images") or []
        if not imgs:
            imgs = ["previs/frames (original) + refs del job; el meta de las primeras tomas no guardó la lista"]
        refs = [{"orden": n, "path": rel(x) if pathlib.Path(str(x)).exists() else str(x), "rol": rol(x)} for n, x in enumerate(imgs, start=1)]
        if refs:
            refs[0]["rol"] = "fotograma original, PNG limpio, no una salida ya editada"
        rid = meta.get("request_id")
        lat = meta.get("latency_s")
        lat_tipo = "reloj de pared del runner, incluye la subida" if lat else "inference_time de fal, sin la subida"
        if lat is None:
            lat = inference(rid)
        ver, mot = SUN_VER[(plano, toma)]
        records.append({
            "id": f"SB_{plano}_t{toma}",
            "paso": f"SB_{plano}",
            "plano": plano,
            "toma": toma,
            "timestamp": iso(meta["started_unix"]) if meta.get("started_unix") else (iso(png.stat().st_mtime) if png.exists() else None),
            "timestamp_fuente": "started_unix del runner" if meta.get("started_unix") else "mtime del PNG, UTC",
            "modelo": "sunburst",
            "endpoint": "openai/gpt-image-2.5/sunburst/edit",
            "params": {"resolution": None, "quality": "high", "aspect": "9:16", "image_size": {"width": 1152, "height": 2048}, "num_images": 1, "seed": None, "output_format": "png"},
            "prompt_file": meta.get("prompt_file") or f"prompts/SB_{plano}.txt",
            "prompt_fuente": prompt_fuente,
            "prompt": prompt,
            "referencias": refs,
            "fal_request_id": rid,
            "output": rel(png) if png.exists() else None,
            "costo_usd": costo_sun(max(1, len(imgs))),
            "costo_tipo": "estimado",
            "nota_costo": "Estimado: 0.0424 (tabla fal high, 2026-09-09, interpolada a 1152×2048 con 1 referencia) + 0.008 por referencia extra (nota del 8-sep-2026, no remedida) + 0.004 de texto. fal no devolvió monto.",
            "latencia_s": round(lat, 3) if isinstance(lat, float) else lat,
            "latencia_tipo": lat_tipo,
            "veredicto": ver,
            "motivo_visual": mot,
            "en_montaje": png.exists() and sha(png) == frames.get(f"{plano}.png"),
        })
    # fallo de carga, sin meta
    fail = FAILS[0]
    fail["costo_usd"] = costo_sun(4)
    fail["referencias"] = [
        {"orden": 1, "path": "previs/frames/b5_p6.png", "rol": "fotograma original"},
        {"orden": 2, "path": ".refs_cache/HOJA_hugo.png (entonces 2752×1536)", "rol": ROLES["HOJA_hugo.png"]},
        {"orden": 3, "path": ".refs_cache/PROP_llave_y_cerradura.png", "rol": ROLES["PROP_llave_y_cerradura.png"]},
        {"orden": 4, "path": ".refs_cache/F05_rojo_tres_cuartos_hacia_puerta.png", "rol": ROLES["F05_rojo_tres_cuartos_hacia_puerta.png"]},
    ]
    records.append(fail)
    # fallo de política, sin request_id
    records.append({
        "id": "SB_b7_p2_fallo_politica",
        "paso": "SB_b7_p2",
        "plano": "b7_p2",
        "toma": -1,
        "timestamp": "2026-10-19T03:07:30Z",
        "timestamp_fuente": "aproximado: dentro del lote que terminó 03:08:20Z; no hubo meta",
        "modelo": "sunburst",
        "endpoint": "openai/gpt-image-2.5/sunburst/edit",
        "params": {"resolution": None, "quality": "high", "aspect": "9:16", "image_size": {"width": 1152, "height": 2048}, "num_images": 1, "seed": None, "output_format": "png"},
        "prompt_file": "prompts/SB_b7_p2.txt",
        "prompt_fuente": "primer texto, reemplazado después. Pedía manga rasgada y manchas dark reddish black, y usaba ESTADO_diego_mojado_herido_v3.",
        "prompt": "FILM STILL, vertical 9:16. Rebuild this shot clean, in one pass, from Image 1. Image 1 is Diego at the door window. Image 2 is Diego's face. Image 3 is Diego soaked: pale stone canvas jacket, only the RIGHT sleeve torn and stained dark reddish black. Image 4 is the red carriage.\n\nMOMENT: the wired-glass window fills about 60 percent of the frame width, with riveted metal door visible on all sides. Diego's wet face is pressed to the glass, hair stuck to his forehead. He looks back over his shoulder into the gangway. The handprints on the glass are dark, almost black, matte. His jacket is soaked and clean except the right sleeve.\n\nBEHIND HIM: the gangway falls almost to black, a faint red cast only. No lit corridor, no doors, no sky, no rain.\n\nLIGHT: the cold white tube above the door, on our side, lights the glass from above. Half his face is in real shadow. No second fill.\n\nTEXTURE: sharp wet skin, separate fingers, fine 35mm grain. No waxy skin, no crunchy sharpening, no compression mush, no text.",
        "referencias": [
            {"orden": 1, "path": "previs/frames/b7_p2.png", "rol": "fotograma original"},
            {"orden": 2, "path": "personajes/HOJA_diego.png", "rol": ROLES["HOJA_diego.png"]},
            {"orden": 3, "path": "personajes/ESTADO_diego_mojado_herido_v3.png", "rol": ROLES["ESTADO_diego_mojado_herido_v3.png"]},
            {"orden": 4, "path": "set/F05_rojo_tres_cuartos_hacia_puerta.png", "rol": ROLES["F05_rojo_tres_cuartos_hacia_puerta.png"]},
        ],
        "fal_request_id": None,
        "output": None,
        "costo_usd": costo_sun(4),
        "costo_tipo": "estimado",
        "nota_costo": "content_policy_violation antes de haber PNG. No hay request_id en el log del runner. El monto es la misma estimación; no está confirmado que se haya cobrado.",
        "latencia_s": None,
        "latencia_tipo": "no medida",
        "veredicto": "retry",
        "motivo_visual": "El checker de contenido rechazó el prompt (manga rasgada, manchas, estado herido). Se reescribió sin esas palabras y sin la hoja de estado.",
        "en_montaje": False,
    })
    records.sort(key=lambda r: (r["timestamp"] or "", r["id"]))
    est = round(sum(r["costo_usd"] or 0 for r in records), 4)
    out = {
        "lote": "previs_v1c",
        "nota": "Un registro por llamada a fal. Ningún monto es una factura: fal no devolvió costo. costo_tipo dice estimado en todas.",
        "estimado_usd": est,
        "gastado_usd_corredor": REG["gastado_usd"],
        "llamadas": len(records),
        "records": records,
    }
    dest = HERE / "log_generaciones_v1c.json"
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({"llamadas": len(records), "estimado_usd": est, "en_montaje": sum(1 for r in records if r["en_montaje"]), "sin_png": sum(1 for r in records if not r["output"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
