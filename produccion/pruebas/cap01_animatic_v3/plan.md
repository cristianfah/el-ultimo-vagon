# Animatic v3 del capítulo 1 · plan

18-oct-2026. Sale de `guion/cap01/cap01_v10.md` y de las notas de Cristian sobre el v1 y el v2 (`produccion/pruebas/cap01_animatic/revision_v1.md`). Se llama v3 porque el v2 ya existe (el v1 con las voces montadas).

**Objetivo:** que el animatic llegue a Cristian bien a la primera: con ritmo, cámara dirigida, continuidad sin errores y voces que calzan. Antes de mostrarlo, cada bot revisa su parte contra la lista de fallas de `revision_v1.md` (sección 5).

**Antes de empezar:** fusionar a `main` los PR #11 (assets, `fal_urls_v1.json`, tomas) y #12 (prompts del productor), para que todos trabajen sobre lo mismo.

## Presupuesto: tope de 40 USD en fal (propuesto; Cristian confirma)

| Partida | Detalle | Costo aproximado |
| --- | --- | --- |
| Assets nuevos | 4 assets × 2 tomas en GPT Image 2.5 | ~1,5 USD |
| Previsualización | ~40 fotogramas en GPT Image 2.5, más una pasada de correcciones | ~10 USD |
| Video | 16 llamadas, 86 s pedidos × 2 semillas, H3 Max a 768p | ~9 USD a precio de lista |
| Margen | Retomas y cobro real a 768p | ~10 USD |
| **Tope** | | **40 USD** |

Si el cobro real a 768p es distinto de 0,05 USD/s, último vagón avisa después de la primera llamada, antes de seguir.

## Fases, responsables y entregas

Cada fase tiene una entrega y una revisión. Ninguna fase empieza sin que la anterior pase su revisión.

| # | Fase | Responsable | Entrega | Revisión antes de pasar |
| --- | --- | --- | --- | --- |
| 1 | Voz de Don Hugo y su línea | Claude (diseño) · Cristian (elige) | Toma de «¡Al último vagón! ¡Rápido!» en `produccion/voces.md` | Cristian |
| 2 | Pistas de diálogo | Último vagón | `pistas/c02.mp3`, `c04b.mp3`, `c07a.mp3`, `c07b.mp3` con los tiempos de la tabla de abajo | Guionista: cada línea en su segundo |
| 3 | Assets nuevos | Productor (prompts) · Último vagón (corre) | Los 4 assets de la tabla «Assets que faltan» del guion v10 | Midjourney: look y luz; Guionista: lado de la herida, cinta, sin texto |
| 4 | Previsualización | Director (prompts) · Último vagón (corre y monta) | Un fotograma por plano (`previs/b0_p1.png`…) y `cap01_previs_v1.mp4`: imágenes fijas con los tiempos del guion y las pistas | Guionista contra «Estado del mundo»; Métricas, prueba sin sonido. **Después, Cristian aprueba** |
| 5 | Prompts de video | Productor | `prompts/c00a.md` … `c07b.md`, H3 a 768p | Lista de la skill `director-de-prompts` y de `revision_v1.md` |
| 6 | Generación | Último vagón | Dos semillas por llamada; `tomas.json` con prompt, referencias, semilla, costo y URL | Último vagón elige con la lista de `revision_v1.md` (ritmo, cámara, continuidad, actuación) |
| 7 | Montaje | Último vagón | `cap01_animatic_v3.mp4`, cortado en la acción y en los cortes reales; pistas limpias encima | Métricas (sin sonido) y Guionista (continuidad) |
| 8 | Aprobación | Cristian | Notas o OK para la versión final en Kling 4.0 | — |

## La previsualización (fase 4)

- **Un fotograma por plano** del guion v10, en GPT Image 2.5 (`openai/gpt-image-2.5/flare/edit`; `sunburst/edit` para el P1 del bloque 0), 9:16, con las hojas de los personajes en cuadro y la plancha del set como referencias.
- **Cada prompt de fotograma describe el instante más representativo del plano:** tamaño, altura de cámara, lente, quién está dónde y mirando a qué, la luz y las filas de «Estado del mundo» que aplican. Sin texto en la imagen.
- **El video de la previsualización** son los fotogramas fijos con la duración de cada plano y las pistas de diálogo encima, más un efecto de sonido simple donde ayude a entender (golpes, grito). Sirve para aprobar encuadres, continuidad y ritmo antes de gastar en video.
- **Los fotogramas aprobados** son el primer fotograma de cada llamada (`image_url`) y la referencia de composición de los demás planos.

## Llamadas de video (fase 6)

H3 Max `minimax/h3-max/reference-to-video` · `resolution: 768P` · `aspect_ratio: 9:16` · `prompt_expansion_mode: disabled` · dos semillas por llamada. Cada llamada pide 0,5 s de colchón al inicio y al final. Primer fotograma: el de la previsualización del primer plano de la llamada.

| Llamada | Bloque y planos | Duración pedida | Audio 1 |
| --- | --- | --- | --- |
| c00a | 0 · P1–P2 | 3,5 s | — |
| c00b | 0 · P3–P4 | 3,5 s | — |
| c01 | 1 · P1 y P2 (en el tren; el montaje usa el inicio y el final) | 4 s | — |
| c01f | 1 · F1–F2 (cuarto del rapto) | 4 s | — |
| F3 | 1 · pantalla | Imagen fija (`PANTALLA_tomas_anden`) con empuje leve en post. Si la toma a01 del v1 trae la pantalla legible, se puede usar | — |
| c02 | 2 · P1–P4 | 12 s | `c02.mp3` |
| c03a | 3 · P1–P3 | 5,5 s | — |
| c03b | 3 · P4–P6 | 4,5 s | — |
| c04a | 4 · P1–P3 | 5 s | — |
| c04b | 4 · P4–P6 | 7 s | `c04b.mp3` |
| c05a | 5 · P1–P3 | 4,5 s | — |
| c05b | 5 · P4, P6, P7 (el inserto P5 va entre P4 y P6 en el montaje) | 6 s | — |
| c05i | 5 · P5, inserto de la palma | 3 s | — |
| c06a | 5 · P8 y 6 · P1–P2 | 5 s | — |
| c06b | 6 · P3 | 2,5 s | — |
| c07a | 7 · P1–P3 | 8 s | `c07a.mp3` |
| c07b | 7 · P4–P6 | 8 s | `c07b.mp3` |

## Pistas de diálogo (fase 2)

Tiempos medidos desde el segundo 0 de la llamada (incluyen el colchón de 0,5 s). Antes de la primera línea y entre líneas va silencio. Las tomas están en `produccion/pruebas/cap01_animatic/voces/`.

| Pista | Línea y toma | Entra en | Duración total de la pista |
| --- | --- | --- | --- |
| `c02.mp3` | Tomás 1C `tomas_b2_1` | 0,8 s | 12 s |
| | Martina 2B `martina_b2_1` | 2,5 s | |
| | Tomás 3C `tomas_b2_2` | 4,9 s | |
| | Martina 4D `martina_b2_2` | 7,7 s | |
| `c04b.mp3` | Hugo (toma nueva; el pitazo del silbato va como efecto en post, a los 2,1 s) | 2,6 s | 7 s |
| `c07a.mp3` | Diego 5C `diego_b7_1` | 1,5 s | 8 s |
| | Diego 6C `diego_b7_2` | 5,0 s | |
| `c07b.mp3` | Tomás 7B `tomas_b7_1` | 0,7 s | 8 s |

## Reparto de lectura

Todos leen `guion/cap01/cap01_v10.md` y `produccion/pruebas/cap01_animatic/revision_v1.md`. Además:
- **Productor:** `produccion/prompting/guia_direccion_video.md` (secciones 10 a 13) y la skill `director-de-prompts`.
- **Director:** la sección «La previsualización» de este plan y la guía (secciones 6, 10, 11 y 13).
- **Último vagón:** `produccion/metodo.md` (sección 8), las tablas de llamadas y pistas de este plan.
- **Guionista y Métricas:** la lista de fallas de `revision_v1.md` (sección 5).
