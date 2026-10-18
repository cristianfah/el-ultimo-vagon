# Animatic del capítulo 1 · plan del 18-oct-2026

**Objetivo de hoy:** el capítulo 1 completo (`guion/cap01/cap01_v9.md`, 85 s) en H3 Max a 480p, armado con los tiempos del guion, para que Cristian lo apruebe antes de la versión final en Kling 4.0.

**Además del animatic, el objetivo es que el equipo aprenda el flujo** (`produccion/metodo.md`) para manejar los próximos capítulos con menos intervención. Cada bot deja por escrito lo que funcionó y lo que no en `produccion/pruebas/cap01_animatic/notas.md`.

## Presupuesto (necesita el OK de Cristian antes de gastar)

| Partida | Detalle | Costo aproximado |
| --- | --- | --- |
| Assets mínimos | Maletín, Diego con el brazo derecho, fotograma guía del cuarto del rapto con los captores | ~1 USD (Nano Banana Pro / GPT Image 2.5) |
| Video | 10 llamadas de H3 Max a 480p, 97 s en total | ~5 USD |
| Margen | Una retoma por bloque como máximo, solo si hace falta | ~2 USD |
| **Tope del día** | | **10 USD en fal** |

## Qué se usa en el animatic y qué no

- **Sí:** hojas de personaje y planchas aprobadas, el maletín, Diego con el brazo derecho y el fotograma guía del rapto.
- **Solo descrito en el prompt (sin asset nuevo):** la marca de la muñeca, el hombre de camisa azul convertido, la palma de Carmen y la pantalla con la foto de Tomás. Se hacen como assets para la versión final.
- **Audio:** el que genera H3. Las voces de ElevenLabs son para la versión final.
- **Sin sobreimpresiones:** ni subtítulos ni tarjetas. Las pone Cristian en post.

## URLs de referencia en fal

Ya están en `produccion/assets/fal_urls_v1.json`: las hojas de Martina, Tomás, Diego, Carmen, Iván y Hugo; `ESTADO_diego_mojado_herido` (brazo equivocado, se reemplaza); F01, F03, F04, F08 y F09.

**Faltan subir a fal** (desde Drive, `imagenes/04_aprobados`): `HOJA_extra_pareja_camisa_azul`, F02, F05, F07, F10, F12, `PROP_llave_y_cerradura` y `direccion_arte/referencias/ref_infectados.jpg`. Se agregan al mismo JSON.

## Llamadas del animatic

| Llamada | Bloque | Duración | Referencias (orden) |
| --- | --- | --- | --- |
| a00 | 0 · El maletín | 8 s | HOJA_martina · maletín · F08 · HOJA_extra_pareja_camisa_azul |
| a01 | 1 · Flashes del rapto | 6 s | HOJA_martina · fotograma guía del rapto · maletín |
| a02 | 2 · El regreso | 14 s | HOJA_martina · HOJA_tomas · F09 (prompt listo en `produccion/prompting/guia_direccion_video.md`, sección 8.2) |
| a03 | 3 · El maletín se abre | 10 s | HOJA_extra_pareja_camisa_azul · maletín · F08 · ref_infectados |
| a04 | 4 · El grito | 12 s | HOJA_martina · HOJA_tomas · HOJA_hugo · F09 · F10 (Carmen e Iván solo descritos, para no pasar de 5 imágenes) |
| a05 | 5 · La huida | 12 s | HOJA_hugo · HOJA_carmen · HOJA_ivan · F07 · F04 · F12 |
| a05i | Inserto de la palma de Carmen | 5 s | HOJA_carmen · F07 |
| a06 | 6 · El encierro | 8 s | HOJA_carmen · HOJA_tomas · HOJA_martina · F01 · F02 |
| a07a | 7 · Diego, planos 1–3 | 10 s | Diego brazo derecho (nuevo) · HOJA_martina · HOJA_tomas · F03 · F01 |
| a07b | 7 · Diego, planos 4–6 | 12 s | Diego brazo derecho (nuevo) · HOJA_tomas · HOJA_martina · HOJA_hugo · F03 · F05 |

Todas con `aspect_ratio: 9:16`, `resolution: 480P`, `prompt_expansion_mode: disabled`. Cada toma se registra en `produccion/pruebas/cap01_animatic/tomas.json` (llamada, prompt, referencias, semilla, costo, URL).

## Reparto de tareas

| # | Quién | Tarea | Entrega | Depende de |
| --- | --- | --- | --- | --- |
| 1 | Cristian | OK de gasto (tope 10 USD en fal) y revisar este plan | Un mensaje | — |
| 2 | Último vagón → agente de Cursor | Subir a fal las referencias que faltan y generar los 3 assets mínimos (maletín, Diego con el brazo derecho, fotograma guía del rapto) con `tools/fal_gen.py`, una variable por edición | URLs en `fal_urls_v1.json` y los prompts de imagen en `produccion/assets/prompts_fal/` | 1 |
| 3 | Midjourney | Dirección de arte de lo nuevo: maletín, máscaras de la secta y cuarto del rapto. Para hoy, una descripción en texto que el agente de Cursor pueda usar; los frames de estilo de Midjourney quedan para la versión final | Texto de look de los tres assets | — |
| 4 | Productor | Escribir los 9 prompts que faltan (todas las llamadas menos a02) en formato H3 Ref2VA, con la guía de dirección. Cada prompt con su costo y su lista de referencias | `produccion/pruebas/cap01_animatic/prompts/aNN.md` | Guía |
| 5 | Último vagón → agente de Cursor | Correr las 10 llamadas con `tools/fal_run.py`, registrar cada toma y armar el animatic con ffmpeg según los tiempos del guion (los flashes del bloque 1 se intercalan en el bloque 0) | `renders/cap01/animatic/cap01_animatic_v1.mp4` y subida a Drive | 2, 4 |
| 6 | Productor | Revisar cada toma con la lista de `produccion/metodo.md` (sección 7). Si un bloque falla, corregir su prompt y pedir una sola retoma | Notas por toma en `notas.md` | 5 |
| 7 | Guionista | Revisar que las líneas del guion suenen a cada personaje y escribir el caption y la encuesta del reel. Si propone cambios de guion, van como propuesta de v10, sin editar la v9 | Propuesta en `notas.md` | — |
| 8 | Métricas | Ver el animatic: ¿el gancho se entiende en 2 s sin sonido?, ¿hay tramos muertos?, ¿la encuesta invita a comentar? Sin inventar números | Notas en `notas.md` | 5 |
| 9 | Director | Juntar las notas y traerle a Cristian un solo siguiente paso | Un mensaje | 6, 7, 8 |
| 10 | Cristian | Aprobar el animatic (o pedir cambios por bloque) | — | 9 |

**Después de la aprobación:** voces en ElevenLabs y versión final en Kling 4.0 (Cristian y Claude), con los mismos prompts en formato Kling.

## Mensajes listos para cada bot

**Director:**
> Hoy sacamos el animatic del capítulo 1 en H3 Max a 480p. El plan y el reparto están en `produccion/pruebas/cap01_animatic/plan.md`. Coordina el orden de las tareas y, cuando estén las notas de productor, guionista y métricas, tráeme un solo siguiente paso. Tope de gasto: 10 USD en fal.

**Último vagón:**
> Lee `AGENTS.md`, `produccion/metodo.md` y `produccion/pruebas/cap01_animatic/plan.md`. Encarga a un agente de Cursor las tareas 2 y 5 del plan: subir las referencias que faltan, generar los 3 assets mínimos, correr las 10 llamadas de H3 Max cuando el productor deje los prompts y armar el animatic con ffmpeg. Todo se registra en `tomas.json`. Tope: 10 USD en fal.

**Productor:**
> Lee `produccion/prompting/guia_direccion_video.md` y `guion/cap01/cap01_v9.md`. El prompt del bloque 2 (llamada a02) está escrito como ejemplo en la sección 8.2. Escribe los otros 9 (tabla «Llamadas del animatic» del plan) en el mismo formato H3 Ref2VA, con emociones escritas como conducta, miradas con destino, manos con lado y cámara con motivo. Déjalos en `produccion/pruebas/cap01_animatic/prompts/` con su costo. Después revisa cada toma con la lista de la sección 7 del método.

**Guionista:**
> Lee `biblia/premisa.md`, `biblia/personajes.md` y `guion/cap01/cap01_v9.md`. Revisa que las siete líneas suenen a cada personaje y escribe el caption y la encuesta del reel («Si fueras Martina, ¿le abres?»). Si propones cambios, van como propuesta de v10 en `produccion/pruebas/cap01_animatic/notas.md`.

**Midjourney:**
> Para el capítulo 1 hay tres assets nuevos: el maletín (negro, esquinas metálicas, dos cierres, sin marca), las máscaras de la secta (lisas, grises, sin rasgos, diseño original) y el cuarto del rapto (concreto, una silla, luz cenital dura, una pantalla). Para hoy, escribe su look en texto para que el agente de Cursor los genere con Nano Banana Pro. Los frames de estilo en Midjourney quedan para la versión final.

**Métricas:**
> Cuando esté el animatic del capítulo 1, revisa si el gancho se entiende en 2 s sin sonido, dónde hay tramos muertos y si la encuesta invita a comentar. Deja tus notas en `produccion/pruebas/cap01_animatic/notas.md`. Sin inventar números.
