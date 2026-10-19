# Montaje de `cap01_previs_v1`

Imágenes fijas con las duraciones del guion v10 y las pistas de `pistas/`. Los fotogramas (`previs/b0_p1.png` …) se generan en la fase 4; este archivo fija el EDL para cuando existan.

## Audio de diálogo (tiempos de `pistas/tiempos.json`)

Colocar cada pista al inicio del bloque de la **llamada** (con el colchón de 0,5 s). En el montaje del capítulo (sin colchón) recortar 0,5 s al inicio y al final de la pista, o retrasar la pista −0,5 s respecto del primer plano del bloque.

| Pista | Bloque | En el archivo (llamada) | En el capítulo (sin colchón) |
| --- | --- | --- | --- |
| `pistas/c02.mp3` | 2 · P1–P4 | Tomás 0,8 · Martina 2,5 · Tomás 5,2 · Martina 8,2 | iguales menos 0,5 s |
| `pistas/c04b.mp3` | 4 · P4–P6 | **Hugo toma A (2,3 s) entra a los 2,5 s.** Pitazo **no va en la pista**: efecto en post a los **2,1 s** | P5 del capítulo empieza en 0:36,5. Hugo a 0:37,0 (0,5 s dentro de P5). Pitazo a 0:36,6 (0,1 s dentro de P5) |
| `pistas/c07a.mp3` | 7 · P1–P3 | Diego 1,5 · Diego 5,0 | iguales menos 0,5 s |
| `pistas/c07b.mp3` | 7 · P4–P6 | Tomás 0,7 | iguales menos 0,5 s |

`c04b.mp3` dura 7,5 s (P4 1,5 + P5 3,0 + P6 2,0 + 0,5 + 0,5). Onset medido de Hugo en el archivo: 2,63 s (la toma A trae ~0,13 s de aire; la tabla manda 2,5 s).

## Fotograma b0_p2 (decisión de Cristian, 19-oct-2026)

Prompt en `previs/prompts/b0_p2.txt`: manga del abrigo gris carbón, con el puño del suéter avena asomando y cubriéndole los nudillos. Mano derecha.

## ffmpeg (cuando existan los fotogramas)

9:16, 24 fps, 480×832 para la previs. Cada `bN_pM.png` se congela `duracion_s` del guion. Las pistas se mezclan a −6 dB sobre silencio. El pitazo de Hugo se agrega como efecto a los 2,1 s de `c04b`, no se genera en fal.
