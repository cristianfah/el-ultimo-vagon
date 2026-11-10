# Scripts del piloto cap. 1

Sin claves ni llamadas pagas. Se ejecutan con `python3 -I` y reciben todas las rutas por argumento. Necesitan `numpy`, `opencv` y `Pillow`, y un `ffmpeg` cuya ruta se pasa con `--ffmpeg` donde hace falta.

| Script | Qué hace |
|---|---|
| `medir_lipsync.py` | Mide una toma con diálogo contra la pista limpia: correlación y desfase del audio, movimiento de boca por personaje dentro y fuera de su línea, y una tira de recortes de boca con la onda de la pista para revisión humana. Las cajas de boca se dan a mano, en fracción del cuadro |
| `comparar_cuadros.py` | Arma una comparación lado a lado de varios cuadros con una etiqueta bajo cada uno |
| `hoja_antes_despues.py` | Hoja de contacto de pares antes → nuevo |

El previz en Blender tiene sus propios scripts y su README en `../previz/scripts/`.
