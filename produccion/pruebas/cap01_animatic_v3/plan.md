# Animatic v3 del capítulo 1 · plan

18-oct-2026. Sale de `guion/cap01/cap01_v10.md` y de las notas de Cristian sobre el v1 y el v2 (`produccion/pruebas/cap01_animatic/revision_v1.md`). Se llama v3 porque el v2 ya existe (el v1 con las voces montadas).

**Objetivo:** que el animatic llegue a Cristian bien a la primera: con ritmo, cámara dirigida, continuidad sin errores y voces que calzan. Antes de mostrarlo, cada bot revisa su parte contra la lista de fallas de `revision_v1.md` (sección 5).

**Antes de empezar:** fusionar a `main` los PR #11 (assets, `fal_urls_v1.json`, tomas) y #12 (prompts del productor), para que todos trabajen sobre lo mismo.

## Presupuesto: tope de 40 USD en fal (techo, no meta; Cristian, 19-oct-2026)

| Partida | Detalle | Costo aproximado |
| --- | --- | --- |
| Assets nuevos | 5 assets × 2 tomas (GPT Image 2.5 y Nano Banana Pro) | ~1,5 USD |
| Previsualización | ~40 fotogramas en GPT Image 2.5, más una pasada de correcciones | ~10 USD |
| Video | 16 llamadas, unos 88 s pedidos × 2 semillas: ~52 s a 480p y ~36 s a 768p | ~10,9 USD a precio de lista (~7 con el descuento hasta el 31-oct) |
| Margen | Retomas y cobro real a 768p | ~10 USD |
| **Tope** | | **40 USD** |

Si el cobro real a 768p es distinto de 0,05 USD/s, último vagón avisa después de la primera llamada, antes de seguir.

## Fases, responsables y entregas

Cada fase tiene una entrega y una revisión. Ninguna fase empieza sin que la anterior pase su revisión.

| # | Fase | Responsable | Entrega | Revisión antes de pasar |
| --- | --- | --- | --- | --- |
| 1 | Voz de Don Hugo y su línea | Claude (diseño) · Cristian (elige) | Toma de «¡Al último vagón! ¡Rápido!» en `produccion/voces.md` | Cristian |
| 2 | Pistas de diálogo | Último vagón | `pistas/c02.mp3`, `c04b.mp3`, `c07a.mp3`, `c07b.mp3` con los tiempos de la tabla de abajo | Guionista: cada línea en su segundo |
| 3 | Assets nuevos | Productor (prompts) · Último vagón (corre) | Los 5 assets de imagen de la tabla «Assets que faltan» del guion v10 (incluida `F08_v2_ambar_bajo`) | Midjourney: look y luz; Guionista: lado de la herida, cinta, sin texto |
| 4 | Previsualización | Director (prompts) · Último vagón (corre y monta) | Un fotograma por plano (`previs/b0_p1.png`…) y `cap01_previs_v1.mp4`: imágenes fijas con los tiempos del guion y las pistas | Guionista contra «Estado del mundo»; Métricas, prueba sin sonido. **Después, Cristian aprueba** |
| 5 | Prompts de video | Productor | `prompts/c00a.md` … `c07b.md`, H3 a 768p | Lista de la skill `director-de-prompts` y de `revision_v1.md` |
| 6 | Generación | Último vagón | Dos semillas por llamada; `tomas.json` con prompt, referencias, semilla, costo y URL | Último vagón elige con la lista de `revision_v1.md` (ritmo, cámara, continuidad, actuación) |
| 7 | Montaje | Último vagón | `cap01_animatic_v3.mp4`, cortado en la acción y en los cortes reales; pistas limpias encima | Métricas (sin sonido) y Guionista (continuidad) |
| 8 | Aprobación | Cristian | Notas o OK para la versión final en Kling 4.0 | — |

## La previsualización (fase 4)

- **Un fotograma por plano** del guion v10, en GPT Image 2.5 (`openai/gpt-image-2.5/flare/edit`; `sunburst/edit` para el P1 del bloque 0), 9:16, con las hojas de los personajes en cuadro y la plancha del set como referencias.
- **Cada prompt de fotograma describe el instante más representativo del plano:** tamaño, altura de cámara, lente, quién está dónde y mirando a qué, la luz y las filas de «Estado del mundo» que aplican. Sin texto en la imagen.
- **b0_p2 (decisión de Cristian, 19-oct):** manga del abrigo gris carbón, con el puño del suéter avena asomando y cubriéndole los nudillos. Prompt en `previs/prompts/b0_p2.txt`.
- **Montaje de `cap01_previs_v1`:** EDL y audio en `previs/montaje.md`. `c04b.mp3`: Hugo toma A (2,3 s) entra a los 2,5 s; pitazo como efecto en post a los 2,1 s.
- **El video de la previsualización** son los fotogramas fijos con la duración de cada plano y las pistas de diálogo encima, más un efecto de sonido simple donde ayude a entender (golpes, grito). Sirve para aprobar encuadres, continuidad y ritmo antes de gastar en video.
- **Los fotogramas aprobados** son el primer fotograma de cada llamada (`image_url`) y la referencia de composición de los demás planos.

## Llamadas de video (fase 6)

H3 Max `minimax/h3-max/reference-to-video` · resolución mixta (decisión de Cristian del 18-oct-2026): **480P** en las 12 llamadas sin diálogo y **768P** en las 4 con pista de voces (c02, c04b, c07a y c07b), porque a 480p H3 no respeta la pista · `aspect_ratio: 9:16` · `prompt_expansion_mode: disabled` · dos semillas por llamada. Cada llamada pide 0,5 s de colchón al inicio y al final. Primer fotograma: el de la previsualización del primer plano de la llamada.

| Llamada | Bloque y planos | Planos en el montaje | Duración pedida | Audio 1 |
| --- | --- | --- | --- | --- |
| c00a | 0 · P1–P2 | 3,0 s | 4,0 s | — |
| c00b | 0 · P3–P4 | 3,0 s | 4,0 s | — |
| c01 | 1 · P1 y P2, en el tren. Una sola acción continua (se apoya, cierra los ojos, los abre, se estira la manga, empuja la puerta); el montaje usa el inicio y el final | 1,8 s | 3,5 s | — |
| c01f | 1 · F1–F2, cuarto del rapto | 1,4 s | 2,5 s | — |
| F3 | 1 · pantalla | 0,8 s | Imagen fija (`PANTALLA_tomas_anden`) con empuje leve en post. Si la toma a01 del v1 trae la pantalla legible, se puede usar | — |
| c02 | 2 · P1–P4 | 11,5 s | 12,5 s | `c02.mp3` |
| c03a | 3 · P1–P3 | 5,0 s | 6,0 s | — |
| c03b | 3 · P4–P6 | 4,0 s | 5,0 s | — |
| c04a | 4 · P1–P3 | 4,5 s | 5,5 s | — |
| c04b | 4 · P4–P6 | 6,5 s | 7,5 s | `c04b.mp3` |
| c05a | 5 · P1–P3 | 3,8 s | 4,8 s | — |
| c05b | 5 · P4, P6 y P7 (el inserto P5 va entre P4 y P6 en el montaje) | 4,2 s | 5,2 s | — |
| c05i | 5 · P5, inserto de la palma | 1,0 s | 2,0 s | — |
| c06a | 5 · P8–P9 y 6 · P1 (dentro del último vagón) | 4,3 s | 5,3 s | — |
| c06b | 6 · P2–P3 | 3,5 s | 4,5 s | — |
| c07a | 7 · P1–P3 | 7,3 s | 8,3 s | `c07a.mp3` |
| c07b | 7 · P4–P6 | 6,5 s | 7,5 s | `c07b.mp3` |

En total, unos 88 s pedidos por semilla.

## Pistas de diálogo (fase 2)

Tiempos medidos desde el segundo 0 de la llamada (incluyen el colchón de 0,5 s del inicio). Antes de la primera línea y entre líneas va silencio; la pista dura lo mismo que la llamada. Las tomas empiezan sin silencio (medido el 18-oct-2026) y están en `produccion/pruebas/cap01_animatic/voces/`.

| Pista | Línea y toma | Entra en | Plano (en la llamada) | Duración de la pista |
| --- | --- | --- | --- | --- |
| `c02.mp3` | Tomás 1C `tomas_b2_1` | 0,8 s | P1 (0,5–4,0 s) | 12,5 s |
| | Martina 2B `martina_b2_1` | 2,5 s | P1 | |
| | Tomás 3C `tomas_b2_2` | 5,2 s | P3 (5,0–8,0 s) | |
| | Martina 4D `martina_b2_2` | 8,2 s | P4 (8,0–12,0 s) | |
| `c04b.mp3` | Hugo A `hugo_b4_1` (2,3 s). **Ya armada en `pistas/c04b.mp3`.** El pitazo va como efecto en post, a los 2,1 s | 2,5 s | P5 (2,0–5,0 s) | 7,5 s |
| `c07a.mp3` | Diego 5C `diego_b7_1` | 1,5 s | P2 (1,3–4,9 s) | 8,3 s |
| | Diego 6C `diego_b7_2` | 5,0 s | P3 (4,9–7,8 s) | |
| `c07b.mp3` | Tomás 7B `tomas_b7_1` | 0,7 s | P4 (0,5–3,2 s) | 7,5 s |

## Reparto de lectura

Todos leen `guion/cap01/cap01_v10.md` y `produccion/pruebas/cap01_animatic/revision_v1.md`. Además:
- **Productor:** `produccion/prompting/guia_direccion_video.md` (secciones 10 a 13) y la skill `director-de-prompts`.
- **Director:** la sección «La previsualización» de este plan y la guía (secciones 6, 10, 11 y 13).
- **Último vagón:** `produccion/metodo.md` (sección 8), las tablas de llamadas y pistas de este plan.
- **Guionista y Métricas:** la lista de fallas de `revision_v1.md` (sección 5).
