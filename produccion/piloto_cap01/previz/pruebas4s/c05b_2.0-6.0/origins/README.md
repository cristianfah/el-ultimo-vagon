# Prueba «formato ORIGINS» · c05b_2.0-6.0 · plan de gasto

**25-nov-2026. Fase 1 hecha (costo 0). Fase 2 escrita, sin correr. Se espera el OK de Cristian.**

## 1. Qué sirve de ORIGINS EP. 01: ZARA

**Fuente.** El post de @higgsfield_ai del 23-nov-2026 dice: «The entire project is open source. All prompts and assets are public. Here's the full workflow:». No pude leer el hilo, porque x.com devuelve 402, xcancel 451 y nitter está cerrado. fxtwitter entrega solo el post principal: el enlace del «workflow» es el video adjunto (7 min 29 s, 4K) y el texto del flujo no está. La ficha de Higgsfield, sin login, entrega solo el título y la descripción («Zara fights her way through a flooded penthouse…»): los prompts no se ven. **No leí ningún prompt de ORIGINS.** Lo que sigue sale de las cinco ideas que anotó Cristian y no de un prompt real.

| Idea | ¿Sirve en el Vagón? | Cómo entra en esta prueba |
|---|---|---|
| (1) Una generación es una secuencia de planos cronometrados con cortes duros | **Sí.** Es lo que ya hacen nuestros bloques CUTS, y además resuelve que el plano de blocking (2,5 s) sea más corto que el mínimo de 4 s | SCRIPT con SHOT 1 y SHOT 2 a tiempo de segundo, «HARD CUT AT 1.5s» y «Exactly one hard cut» en CRITICAL |
| (2) Un bloque CRITICAL para lo que no puede romperse | **Sí**, como cambio de forma: junta en un solo bloque numerado, **al principio**, nuestros LOCKs y la línea fija de los cilindros | CRITICAL con 8 puntos: el gris manda en la cámara, la línea de los cilindros, ningún cilindro en la salida, el elenco, los lados, las manos, la luz y la mirada al lente |
| (3) Prompt largo por secciones (estilo, cámara, textura, sonido, script, assets) y recap al final | **Sí.** Lo nuevo contra nuestro formato son STYLE y TEXTURE por separado, los assets al final y el RECAP que repite lo esencial | Orden: CRITICAL · STYLE · CAMERA · TEXTURE · SOUND · SCRIPT · ASSETS · RECAP (8.544 caracteres, contra 10.708 del brazo A) |
| (4) Las locaciones como plates still antes del video | **Sí, ya lo tenemos:** las planchas F01–F12 aprobadas | F04 (desde el fuelle) para el SHOT 1 y F03 (desde adentro) para el SHOT 2, cada una atada a su plano en ASSETS. No se genera nada nuevo |
| (5) Las hojas de personaje en video de 15 s | **Se anota y no se adopta.** Cuesta una generación por personaje y aquí no se prueba | — |

Lo que **no** se toma: el look de ORIGINS, Higgsfield (ni su app, ni su CLI, ni su MCP) y Seedream.

## 2. El prompt

Está en `prompt_seedance_origins.md`, completo y listo para pegar. El payload es `payload_seedance_origins.json`, con las URL como marcadores `<subir: …>`. La sintaxis es solo la de Seedance 2.5 US: `@Video1` y `@Image1`–`@Image9`.

## 3. Plano y archivos

- **Plano: b5_p7, «Entran en tropel»** (c05b, de 3,5 a 6,0 s de la llamada). Es el plano de blocking y geografía que quedó pendiente en la PARADA 1. Va dentro de la ventana c05b de 2,0 a 6,0 s, porque solo dura 2,5 s y el modelo pide 4. Así entran 1,5 s de b5_p6 (la llave) y un corte duro.
- **Gris recortado:** `video_1.mp4` (c05b, de 2,0 a 6,0 s), que sale de `prueba4s.py` y ya está en el Drive dentro de `pruebas4s_borrador/prueba4s_c05b_2.0-6.0.zip`. El gris completo de la llamada es `refs_luz_real/c05b_ref.mp4`. No se hace un recorte nuevo.
- **Hojas y referencias:** las cinco hojas (Hugo, Iván, Carmen, Martina y Tomás), `PROP_llave_y_cerradura`, `ref_infectados`, `F04` y `F03`, las mismas del brazo A.
- **Comparación:** la toma se compara con el brazo A (`../prompt_seedance_A.md`), que tiene el mismo tramo, las mismas entradas y la misma semilla con el formato anterior. El brazo A no se corre en esta prueba. Esta toma sola ya responde si el formato ORIGINS respeta el gris y las hojas.

## 4. La generación propuesta (una sola)

| | |
|---|---|
| Endpoint | fal · `bytedance/seedance-2.5/us/reference-to-video` (`task: reference`) |
| Resolución | **480p** (`resolution: "480p"`, sin `draft`: ver la nota de abajo) |
| Formato y duración | 9:16 · `duration: "4"` |
| Video de referencia | `video_1.mp4`, 4,000 s, en `video_urls[0]` (fal pide de 1,8 a 30,2 s) |
| Imágenes | 9, en `image_urls` (el límite es 30) |
| Audio | `generate_audio: true`, sin `audio_urls` ni diálogo |
| Semilla | 1019 (la misma del brazo A) |
| Tomas | **1** |

**Costo, con el precio publicado en fal.ai hoy (25-nov-2026, página pública, sin llamar a la API):**
- Si hay video de referencia, fal cobra toda la llamada a **0,0128 USD por 1.000 tokens** (480p y 720p), y cuenta los segundos de entrada y de salida. Los tokens se calculan así: alto × ancho × (s de entrada + s de salida) × 24 / 1024.
- 480p en 9:16 (fal no publica los píxeles; se supone de ~480×854 a ~496×864) × 8 s da de 76.900 a 80.400 tokens: **de ~0,98 a 1,03 USD**.
- 720p (720×1280) da 172.800 tokens: **~2,21 USD**. No se propone.
- **Tope pedido: 1,10 USD, una toma.** Con tu cotización del 24-nov (~1,03 USD) el precio no cambió.

**Alternativa más barata, por si prefieres el motor final:** Kling 4.0 en fal (`kling/v4/reference-to-video`) a 720p fijado, 4 s de salida y 4 s de gris. Con video de referencia cobra 0,094 USD por segundo facturable (entrada más salida, con un mínimo del doble de la salida), así que 8 s dan **~0,75 USD**. Con Kling el prompt va con la misma sintaxis `@Video1`/`@Image1`, pero hay que sacar `resolution: 480p` (Kling no tiene 480p) y poner `aspect_ratio: "9:16"` (su valor por defecto es 16:9).

**Nota sobre `draft`:** la página dice que `draft: true` fuerza 480p y devuelve un `draft_id` que se puede completar a 1080p o 4K durante 14 días (el README de 4 s dice 7). No publica el precio del borrador. Por eso propongo `resolution: 480p` sin `draft`, con un precio que se puede calcular. Si prefieres el `draft_id`, el costo del borrador queda sin verificar.

## 5. Qué vamos a mirar

1. **Cámara y recorrido:** ¿sigue el gris o inventa algo? En el SHOT 1, la cámara se acerca 3 cm con el clac y no hace paneo. En el SHOT 2, retrocede ~0,7 m sin paneo y sin seguir a nadie. ¿Hay **un solo corte, en 1,5 s**, o inventa otro corte, un zoom o un paneo?
2. **Cuerpos:** ¿salen con la contextura, la cara, las manos y la ropa de cada hoja, o copia los cilindros (figuras tiesas, cuerpos tubulares, cosas grises o color pastel)? **Si un cuerpo sale mal, se para, no se repite y se avisa a Cristian (07).**
3. **Lados:** Martina a la izquierda, Tomás y Carmen a la derecha y Hugo afuera, a la izquierda del vano.
4. **CRITICAL:** la llave en la mano derecha de Hugo, la palma derecha de Carmen contra el pecho, el tubo frío solo adentro, nadie mirando al lente, 8 personas y sin texto.
5. **Formato:** contra el brazo A, en cuanto se corra, ¿CRITICAL al principio y RECAP al final cumplen mejor los LOCKs?

## 6. Pasos cuando haya OK (en orden; nada antes)

1. Escribir en el log el OK con el tope.
2. Bajar el zip del Drive y confirmar con ffprobe que `video_1.mp4` dura 4,000 s, tiene 96 cuadros a 24 fps y 720×1280 y no tiene audio.
3. Bajar las 9 referencias y reducir `HOJA_hugo` a 2.048 px (dio `image_load_error`).
4. Subir cada archivo una vez, reemplazar los `<subir: …>` y enviar **una** llamada.
5. Bajar la toma a `$TRABAJO/pruebas4s/c05b_2.0-6.0/seedance_origins.mp4` y anotar el costo real (el panel Usage de fal antes y después) en el log y en `tomas.json` (`P4S_c05b_seedance_ORIGINS`).
6. Mirar los cinco puntos de arriba. Si el cuerpo sale mal, se para ahí.

## No verificado

- Los prompts de ORIGINS y el contenido del hilo, porque no los pude leer sin login. Tampoco cómo usan ellos CRITICAL ni el recap.
- `video_1.mp4`: no lo bajé en esta sesión para pasarle ffprobe (el Drive lo entrega en base64 dentro de la conversación). Lo doy por bueno según el log del 18-nov, y se revisa en el paso 2.
- Los píxeles exactos de 480p en 9:16 en Seedance 2.5, y por lo tanto los centavos del costo.
- Si `generate_audio` o las 9 imágenes cambian el precio (la fórmula publicada solo cuenta los segundos de video).
- Si las tarifas por segundo (0,2205 USD/s a 480p) se suman a las de tokens cuando hay video. Leí la página como «la llamada entera a 0,0128 por 1.000 tokens». Si las dos se sumaran, serían ~0,88 USD más.
