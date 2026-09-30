# Investigación: referencias, duración mínima y continuidad

Fecha: 2026-09-30. Fuentes: fichas de fal.ai de `minimax/h3-max/*` y especificaciones publicadas de Kling 4.0 y 4.0 Flash. **Todo lo de esta página está pendiente de confirmarse con pruebas reales** (ver plan al final).

## 1. El problema: planos de 1 s y modelos de 3–5 s mínimo

| Modelo | Duración mínima | Máxima |
|---|---|---|
| H3 Max (todas las rutas) | **5 s** | 15 s |
| Kling 4.0 Flash | 3 s | 20 s |
| Kling 4.0 (oficial, octubre) | 3 s | 30 s |

Ningún modelo hace un clip de 1 s. La solución es **separar dos ideas que el guion técnico tenía mezcladas**:

- **Plano** = lo que ve el público entre dos cortes (1–3 s). Es una unidad de **montaje**.
- **Bloque de generación** = lo que se le pide al modelo en una llamada (5–15 s). Es una unidad de **producción**.

Un bloque puede contener varios planos. Hay tres estrategias:

| Estrategia | Cómo | Cuándo | Costo relativo |
|---|---|---|---|
| **A · Bloque multi-beat** | Una llamada de 5–15 s con varios planos como beats (`0.0 to 2.0s: … CUT. 2.0 to 5.0s: …`), mismos personajes, misma locación y luz. Se corta en el montaje | Escenas de diálogo y reacciones; la mayor parte del capítulo | Bajo: 10 s ≈ 1 llamada en vez de 4–5 |
| **B · Plano suelto recortado** | Un keyframe exacto → clip de 5 s → se usa 1–2 s | Insertos que exigen encuadre exacto (mano en el vidrio, celular, culata del revólver) | Medio: se paga el clip completo |
| **C · Encadenado** | El último fotograma de un bloque (o el video mismo) es la entrada del siguiente | Continuidad entre bloques de una misma escena | Sin costo extra |

La documentación de fal confirma que H3 Max **mantiene la identidad del personaje entre cortes dentro de una misma generación** (a condición de describir al personaje igual en cada beat). Es la base de la estrategia A.

## 2. Lo que permiten las referencias

### H3 Max · `reference-to-video`
- Hasta **12 archivos**: imágenes, videos y audios juntos.
- **Imágenes** (`reference_image_urls`): el prompt las nombra «Image 1», «Image 2»… (personaje, locación, prop).
- **Videos** (`reference_video_urls`): clips de 2–15 s (15 s en total), «Video 1»… Sirven para guiar movimiento, ritmo y actuación. **Se puede usar una toma anterior ya aprobada como referencia**, lo que da continuidad de espacio, luz y personaje.
- **Audios** (`reference_audio_urls`): clips de 2–15 s, «Audio 1»… Fijan la voz. Un audio necesita al menos una imagen o video con él.
- `aspect_ratio: 9:16` disponible. Resolución 480P, 768P y **1080P** (refinado desde 768P, 0,16 USD/s).
- **Costo de las referencias:** cada solicitud incluye 4.096 tokens gratis. Una imagen de 1024×1024 son 1.024 tokens: **hasta 4 imágenes cuadradas de 1024 salen gratis**. Cada imagen extra cuesta ~0,02 USD; una referencia de video es cara (0,21 a 2,16 USD según largo y resolución). Conclusión: **imágenes, sí; video de referencia, solo cuando aporte algo que la imagen no da.**

### H3 Max · `image-to-video`
- `image_url` = primer fotograma; `end_image_url` = último. Con los dos, el modelo interpola (**primer y último fotograma**, o solo último).
- **`target_audio_url`:** fija la banda sonora del clip con un audio propio (2–15 s). Si el diálogo se genera antes en ElevenLabs, el clip nace con esa voz y esa duración.
- El lienzo sigue a la imagen: el keyframe debe ser 9:16.

### Kling 4.0 Flash (disponible hoy, acceso anticipado)
- 3–20 s, **solo 720p**, 8-bit.
- Entradas: texto, imagen de primer fotograma y referencias (Omni). **No hay primer y último fotograma ni multi-keyframe** (eso es del 4.0 completo) y no acepta referencias de voz.
- Uso en el proyecto: exploración de planos clave (ya decidido).

### Kling 4.0 (oficial, octubre)
- Hasta 30 s, **10 keyframes** (un plano con varios puntos fijos), 15 referencias (10 imágenes, 5 videos, 7 personajes/elements, hasta 3 voces), 4K. Cuando salga, es el motor natural para bloques multi-beat con keyframes.

## 3. Modelo de continuidad propuesto: la «pila de referencias»

La continuidad deja de depender de que el prompt describa bien, y pasa a depender de **qué se le pasa al modelo**. Cada bloque de generación recibe una pila fija, en este orden:

| Posición | Contenido | Origen |
|---|---|---|
| Image 1..n | Hoja de cada personaje presente (piel seca, luz neutra) | Assets de Weavy |
| Image n+1 | Placa de la locación con la luz de la escena (ámbar o rojo) | Assets de Weavy o primer bloque aprobado |
| Image n+2 | Prop crítico, si es el protagonista del bloque (revólver, celular) | Assets de Weavy |
| Video 1 (opcional) | Toma aprobada anterior de la misma escena | Bloque previo |
| Audio 1 (opcional) | Voz del personaje que habla | ElevenLabs |

Reglas:
- **Máximo 4 imágenes de 1024×1024** por bloque, para no pagar tokens de referencia. Si hay más personajes, se compone una hoja con dos personajes en una sola imagen.
- **Una placa de locación por combinación locación × luz.** El vagón de pasajeros con luz ámbar y el mismo vagón en rojo son dos placas.
- **La primera toma aprobada de cada escena se convierte en referencia** de las siguientes (encadenado).
- Los hechos de continuidad marcados `fragil` se repiten en el texto del prompt, además de estar en la pila.

## 4. Consecuencias para el proceso
1. El Director sigue desglosando en **planos** (unidad de montaje).
2. El Asistente de dirección agrupa planos en **bloques de generación** (`bloques` en el YAML), decide la estrategia (A/B/C) y define la pila de referencias de cada bloque.
3. El Prompter compila **un prompt por bloque**, con los beats como planos.
4. El Montajista corta cada bloque en sus planos.
5. El Pipeline genera bloques, no planos. El estado se sigue por plano.

Para el capítulo 1 (cold open + escena 1) la agrupación probable es de 5 bloques en vez de 10 clips (ver el guion técnico cuando esté hecho).

## 5. Precios: aviso
Los precios de `image-to-video` de H3 Max tenían un descuento de lanzamiento del 50 % que **termina hoy, 30 de septiembre**. Desde mañana: 0,05 / 0,08 / 0,16 USD por segundo (480p / 768p / 1080p). Los cálculos del proyecto usan esas tarifas. `reference-to-video` ya figura a esas tarifas.

## 6. Plan de pruebas (antes de generar el guion técnico completo)

Todas a 480P (0,05 USD/s), unos 0,25 USD por prueba de 5 s. Total estimado: menos de 5 USD.

| # | Prueba | Qué responde |
|---|---|---|
| 1 | Bloque multi-beat de 8 s con 3 planos (Martina/Tomás, reacción, inserto de celular), solo con referencias de imagen | ¿Se sostienen la identidad y la luz entre cortes? ¿Respeta los tiempos de cada beat? |
| 2 | La misma escena como 3 clips sueltos desde keyframes | Comparar contra la prueba 1: ¿cuánto mejor es el control y cuánto peor la continuidad? |
| 3 | Beat de 1 s dentro de un bloque | ¿El modelo respeta un beat tan corto o lo estira? |
| 4 | Encadenado: `image_url` = último fotograma de la prueba 1 | ¿Continúa bien la luz y la posición? |
| 5 | Video de referencia = toma aprobada de la prueba 1 | ¿Mejora la continuidad? ¿Vale el costo de tokens? |
| 6 | `target_audio_url` con una línea de diálogo | ¿Sale con lip sync y acento correctos? |
| 7 | `prompt_expansion_mode: disabled` contra `balanced` | ¿Cuál obedece mejor un prompt estructurado? |
| 8 | Cold open: palma en el vidrio (plano B, keyframe exacto) | ¿Se logra el encuadre y el golpe en los primeros 1–2 s? |
| 9 | Misma escena en Kling 4.0 Flash por MCP | ¿Vale la pena para planos clave? |

Requisitos: `FAL_KEY` conectada, hojas de personaje mínimas (aunque sean provisorias) y una placa del vagón.
