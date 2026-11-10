# Previz en Blender · scripts

Motor de previz gris (headless, Blender 4.5 LTS + ffmpeg). Blender manda la cámara, el lente, el blocking y los tiempos; el video que sale se sube como **video de referencia**. Nada llama a una API ni a un modelo. Ningún script tiene rutas fijas: todo entra por argumentos.

| Script | Corre con | Qué hace |
|---|---|---|
| `build_set.py` | Blender | Tren en bloques grises: último vagón, fuelle, vagón 5 y vagón 2 (el mismo módulo paramétrico), props (maletín, llave) y anclas `ANC_*`. Escribe `set_info.json` |
| `build_cast.py` | Blender | Elenco de tres bloques con color y altura por personaje. Barras-brazo y bota ocultas, solo se muestran si la ficha las pide |
| `shot_from_json.py` | Blender | Lee `shots/<id>.json` y arma la llamada: una cámara por plano ligada a un marcador (corte seco), claves horneadas por cuadro |
| `render_shot.py` | Blender | Workbench, luz plana, 720×1280, 24 fps → `frame_0000.png …` (cuadro k = archivo k) |
| `encode.py` | python3 | PNG → `out/<id>_ref.mp4` (sin texto ni audio, duración exacta), `qa/<id>_qa.mp4`, `qa/<id>_hoja.jpg`, `qa/<id>_tira.jpg` |
| `check_ref.py` | python3 | Tamaño, fps, duración exacta, sin audio, sin cuadros repetidos, límites de Kling |
| `previz_llamada.py` | python3 | Encadena los cuatro pasos de una llamada |
| `previz_lib.py`, `previz_tiempos.py` | (módulos) | Mallas, materiales, figuras, luz del set · tiempos → cuadros |

## Uso

```bash
BLENDER="<ruta>/Blender"; FFMPEG="<ruta>/ffmpeg"; TRABAJO="<carpeta de trabajo>/previz"; FUENTE="<una .ttf para el texto de QA>"

# 1) Set y elenco (una vez; de nuevo solo si cambian medidas, colores o alturas)
"$BLENDER" -b --python-exit-code 1 -P build_set.py -- --out "$TRABAJO/set/tren_blockout.blend"
"$BLENDER" -b --python-exit-code 1 "$TRABAJO/set/tren_blockout.blend" -P build_cast.py -- --save

# 2) Una llamada completa desde su ficha
python3 previz_llamada.py --blender "$BLENDER" --ffmpeg "$FFMPEG" --work "$TRABAJO" \
        --json ../shots/c05a.json --font "$FUENTE" --tira 3

# 2b) O paso a paso
"$BLENDER" -b --python-exit-code 1 "$TRABAJO/set/tren_blockout.blend" -P shot_from_json.py -- \
        --json ../shots/c05a.json --out "$TRABAJO/render/c05a/c05a.blend"
"$BLENDER" -b --python-exit-code 1 "$TRABAJO/render/c05a/c05a.blend" -P render_shot.py -- --out "$TRABAJO/render/c05a/frame_"
python3 encode.py    --ffmpeg "$FFMPEG" --json ../shots/c05a.json --frames-dir "$TRABAJO/render/c05a" --work "$TRABAJO" --font "$FUENTE"
python3 check_ref.py --ffmpeg "$FFMPEG" --json ../shots/c05a.json --ref "$TRABAJO/out/c05a_ref.mp4" --frames-dir "$TRABAJO/render/c05a"

# Probar una composición sin renderizar todo: solo algunos cuadros
"$BLENDER" -b "$TRABAJO/render/c05a/c05a.blend" -P render_shot.py -- --out "<carpeta temporal>/prueba_" --still 0 43 84
```

## Ficha `shots/<id>.json`

- `duration_s` (entero), `fps`, `resolution`, `set_light` (`neutro`, `ambar`, `ambar_bajo`, `rojo`), `train_sway`.
- `origin`: un ancla del set (`ANC_fuelle`, `ANC_vagon2_fila_12`, …; la lista está en `set/set_info.json`). Todas las coordenadas son metros relativos a esa ancla. **+Y = hacia la cabeza del tren, +X = derecha mirando hacia adelante, +Z = arriba.** Giro `yaw` 0 = mira a +Y; positivo = hacia la izquierda.
- Todos los `t` son **segundos desde el inicio de la llamada**. Un plano ocupa los cuadros `round(t0·fps)` a `round(t1·fps) − 1`; el primero parte en 0 y el último termina en `duration_s`.
- `shots[]`: `id`, `t0`, `t1`, `camera`, `actors`, `props`, `hide_set` (objetos del set que ese plano oculta, «pared móvil»).
- `camera`: `lens_mm` (sensor de 36 mm en vertical), `keys` con `pos` y `look_at`, `handheld` (`rot_deg`, `pos_m`, `hz`, `seed`), `breath`, `vibration`, `lag_s`, `shakes` (`impact_t` + `delay_f` cuadros).
- `actors.<nombre>`: `pose` (`de_pie`, `sentado`, `agachado`), `keys` (`pos`, `yaw`, `lean`, `side`, `head_yaw`, `head_pitch`, `head_roll`, `dz`), `tremor`, `arms.R/L` (barra del hombro hasta `to`), `boot`.
- Un punto (`pos`, `look_at`, `to`) puede ser `[x, y, z]`, el nombre de un objeto, o `{"actor": "carmen", "part": "cabeza", "offset": [..]}` / `{"prop": "llave", "offset": [..]}`.
- Cada clave hereda de la anterior lo que no declara. `ease` es la curva de llegada: `inout` (por defecto), `in`, `out`, `snap` (golpe), `back`, `hold`, `linear`.
- `set_anim`: `doors` (`open_deg` por clave) y `glass_break` (el vidrio desaparece en el cuadro de `t` y salen esquirlas).

## Reglas que el motor hace cumplir

- El ref sale de los PNG, sin texto ni audio, con `duration_s × fps` cuadros exactos. Si falta un cuadro, `encode.py` falla: no rellena.
- Sin quietud al inicio: el primer plano parte en `t0 = 0` con la acción en marcha.
- Colores y alturas del elenco: `previz_lib.COLORES` y `previz_lib.ALTURAS`. Medidas del set: `build_set.DEF`.
