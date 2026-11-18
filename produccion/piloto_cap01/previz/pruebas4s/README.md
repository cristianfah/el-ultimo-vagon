# Pruebas de 4 s de los planos difíciles · piloto cap. 1

**Borrador del 18-nov-2026. Nada de esto se ha corrido.** No se llama a Kling ni a fal (ni se sube un archivo) sin el OK de Cristian.

## Qué son

Son siete tramos de 4 s, tomados de las llamadas más difíciles del gris. Sirven para saber, antes de gastar en el capítulo, si el modelo de video respeta la cámara, el blocking y los lados del gris, y si los cuerpos salen bien cuando el gris solo tiene cilindros. Cada prueba se corre en dos motores y con dos brazos, así que lleva cuatro prompts:

| | Brazo A: el gris como video | Brazo B: la hoja de storyboard como imagen |
|---|---|---|
| **Kling 4.0 Omni-Ref** (MCP, `omni_ref_video`, `kling-video-v4_0`, 720p) | `video_1.mp4` (视频1) + hojas + plancha | `hoja_storyboard.jpg` (último 图片N) + hojas + plancha |
| **Seedance 2.5 draft** (fal, `bytedance/seedance-2.5/us/reference-to-video`, `draft: true`, sale a 480p) | `video_1.mp4` (@Video1) + hojas + plancha | `hoja_storyboard.jpg` (última @ImageN) + hojas + plancha |

Los cuatro usan el mismo prompt base. Solo cambian las referencias y las líneas fijas de cada brazo: en el A, «Video 1 is the master reference…»; en el B, «Image N is a storyboard sheet…» y, después de los cortes, «Follow the storyboard panels in order…». Las pruebas no llevan pista de voz, porque Kling exige un `audio_1` de 5 s o más y Seedance rehace las pistas. Si alguien habla dentro de la ventana, el prompt lo describe como acción con la boca y dice «no dialogue audio in this test».

Cada carpeta trae `prompt_kling_A.md`, `prompt_kling_B.md`, `prompt_seedance_A.md` y `prompt_seedance_B.md`. Cada uno lleva arriba la lista de entradas en orden, con su archivo, y abajo el prompt completo. También trae `payload_kling.json` y `payload_seedance.json`, con los dos brazos y las URL como marcadores `<subir: ruta local>`.

Rutas de los marcadores:
- `$PREVIZ_TRABAJO`: la carpeta de trabajo del gris.
- `$TRABAJO`: su carpeta madre, la carpeta de trabajo de la sesión.
- `$TRABAJO/refs/<carpeta>__<archivo>`: las referencias aprobadas bajadas del Drive o de `produccion/assets/fal_urls_v1.json`, con el mismo nombre que en T2.
- `REPO/`: la raíz del repo.

## Las siete pruebas

Los tiempos de «Planos en la prueba» ya tienen restado el inicio de la ventana; son los mismos que van en los cortes del prompt.

| # | Prueba (carpeta) | Ventana en la llamada | Planos en la prueba | Por qué es difícil | Qué se mira, además de lo común |
|---|---|---|---|---|---|
| 1 | `c00b_0.0-4.0` | c00b 0,0–4,0 | b0_p3 0,0–2,0 · b0_p4 2,0–4,0 | Paneo corto y rápido (22°) motivado por una mirada, con dos personas que tienen que seguir dormidas. El maletín tiene que quedar en su marca, y esa marca ya falló en tres cuadros. Martina se aleja de espaldas por un pasillo largo a 24 mm con cámara fija y solo 2 o 3 lámparas | Hombre a la izquierda y esposa a la derecha antes del paneo; Martina a la derecha después. ¿El paneo se pasa y vuelve, o flota? ¿La esquina del maletín sigue bajo el asiento, del lado del pasillo, y quieta? ¿La lectora queda al fondo a la derecha sin levantar la vista? ¿Prende lámparas de más? ¿Martina camina con peso o patina? |
| 2 | `c03b_0.7-4.7` | c03b 0,7–4,7 | b3_p4 0,0–1,3 · b3_p5 1,3–2,3 · b3_p6 2,3–4,0 | Tres cortes en 4 s. La transformación (ojos blancos, venas) sin sobreactuar. Una embestida con contacto entre dos cuerpos (en el gris los cilindros se tocan a propósito) que corta en el impacto. Un paneo que llega tarde al grito | ¿El hombre está a la izquierda, la esposa a la derecha y la embestida va hacia la derecha? ¿El contacto se lee como dos cuerpos o se funden? ¿Muestra violencia o manchas que el prompt no pide? ¿El paneo encuentra a la lectora ya de pie? ¿La niebla se queda en el piso? |
| 3 | `c04b_4.0-8.0` | c04b 4,0–8,0 | b4_p5 (final) 0,0–1,0 · b4_p6 1,0–4,0 | Una estampida con cámara que corre de espaldas, cuatro personajes, un pasajero y tres infectados, y la puerta delantera que revienta al fondo. Hugo termina su grito sin pista: solo boca | ¿Martina a la izquierda y Tomás a la derecha? ¿Alguien corre mirando al lente? Es lo que el chequeo marcó en la c05a del 10-nov. ¿La cámara corre con peso? ¿Chocan con los respaldos? ¿Hugo tiene la llave en la mano derecha? ¿Hay gente duplicada o de más? |
| 4 | `c05a_1.0-5.0` | c05a 1,0–5,0 | b5_p1 (final) 0,0–0,8 · b5_p2 0,8–2,3 · b5_p3 2,3–4,0 | Es el mismo tramo que T1 (10-nov), ahora con cilindros en vez de figuras de bloques. En T1, Kling metió un tubo blanco en el P2 y Carmen gritó al lente al final del P3. Además, el brazo que revienta el vidrio y agarra a Carmen no está en el gris: solo existe en el texto | ¿Hay un tubo blanco o una luz fría en el fuelle? ¿Carmen grita hacia el grupo, a la izquierda del cuadro, y no al lente? ¿La mano la agarra del hombro izquierdo y desde atrás? ¿Respeta los lados del P2? ¿El fuelle se alarga o se ilumina? (Fue la falla de T1 sin previz.) Comparar con la toma de T1: ¿los cilindros funcionan mejor o peor que las figuras? |
| 5 | `c05b_2.0-6.0` | c05b 2,0–6,0 | b5_p6 0,0–1,5 · b5_p7 1,5–4,0 | **La prueba A/B recomendada.** Hay dos espacios separados por una puerta que se abre. La llave es un prop chico que tiene que terminar en la mano derecha. b5_p7 es un solo plano de blocking: cinco actores entran en tropel por los dos lados de la cámara, con tres infectados al fondo y Hugo afuera. La luz cambia del rojo del fuelle al rojo con tubo frío | ¿La llave gira, sale y se queda en la mano derecha? ¿La puerta se abre hacia adentro y la hoja queda a la derecha? ¿Martina entra por la izquierda y Tomás y Carmen por la derecha? ¿Los tropiezos tienen peso? ¿Hugo se queda afuera, a la izquierda del vano? ¿El tubo frío aparece solo adentro? ¿Se ve al fondo la puerta del vagón 5 reventada? |
| 6 | `c06a_0.4-4.4` | c06a 0,4–4,4 | b5_p8 0,0–1,4 · b5_p9 1,4–2,4 · b6_p1 (comienzo) 2,4–4,0 | La mano en la ranura, aplastada por la puerta. La llave por dentro en una puerta sin cerrojo. La cara que se estrella y deja la mancha en el vidrio. Un general fijo con cinco personas que retroceden a sus marcas y el silencio de golpe | ¿La mano se lee como mano (uñas cortas y rotas) y no se funde con la puerta? ¿La puerta queda cerrada desde 0,6 s? ¿Inventa un cerrojo o un pestillo? ¿La llave sale de cuadro sin guardarse en cuadro? ¿La mancha se queda en el vidrio? ¿La cámara fija no acusa los golpes? ¿Los golpes paran de verdad? ¿Hugo a la izquierda junto a la cerradura, Iván contra la puerta y Martina a la izquierda de Tomás? |
| 7 | `c07a_5.0-9.0` | c07a 5,0–9,0 | b7_p3 0,0–4,0 (un solo plano; Diego en off) | Plano casi quieto con desenfoque y miradas que giran en ola. Martina mira 20° por encima del lente, así que es fácil que el modelo la ponga mirando a cámara. Sin la voz de Diego, la reacción tiene que leerse sola. Al fondo va la pared trasera con la cabina a la izquierda (una sola puerta). Kling fuerza `prefer_multi_shots` y puede inventar un corte en un plano único | ¿Martina mira la ventanita y no al lente? ¿Tomás gira hacia la derecha del cuadro? ¿Los giros van en orden, Tomás y después Carmen? ¿Aparece una segunda puerta, Diego u otra persona? ¿Carmen tiene la mano escondida? ¿La cámara respira o queda tiesa? ¿Kling corta donde no hay corte? |

### Qué se mira en todas

1. **Eje y lados:** que cada personaje quede del lado del cuadro que dice el SIDES LOCK, corte por corte, y que las miradas vayan hacia donde está el otro.
2. **Movimiento:** que sea natural y no tieso. La gente tiene que tener peso e inercia, la cámara tiene que arrancar tarde y frenar con peso, y el balanceo del tren tiene que estar en los cuerpos, no en la cámara. Que no haya cámara lenta.
3. **Cosas inventadas en el espacio:** gente de más, una segunda puerta, un tubo blanco donde no va, lámparas de más, cielo o lluvia en la ventanita, texto.
4. **El cuerpo sin cuerpos en el gris:** contextura, manos, piernas y ropa contra la hoja de cada personaje. Si los cuerpos salen mal (con forma de cilindro, contextura inventada o miembros raros), **se para la tanda y se avisa a Cristian.** Es el riesgo anotado en el log el 18-nov a las 00:10.
5. **LOCKs:** que nadie mire al lente y que se cumplan las manos y los lados (la llave en la derecha de Hugo, la palma derecha de Carmen), el vestuario y la luz.
6. **A contra B:** ¿el video da mejor tiempo y cámara que la hoja? ¿La hoja da un movimiento más natural? **Kling contra Seedance:** las mismas preguntas, comparando al mismo alto (Seedance draft sale a 480p).

## Costo estimado (se mide al correr)

| Corrida | Costo estimado | De dónde sale |
|---|---|---|
| Kling A (gris de 4 s como `video_1`, salida de 4 s) | **48 créditos** | 12 créditos por segundo de salida, medido en T1 (c00a con previz, 10-nov) |
| Kling B (sin video) | **40 créditos** | 10 créditos por segundo, medido en T1 |
| Seedance A (draft 480p, con video de entrada) | **~0,8 USD**, hasta **~1,6 USD** si fal cobra también los tokens del video de entrada | 0,0214 USD por 1.000 tokens (precio publicado); fal no devuelve el cobro por llamada |
| Seedance B (draft 480p, sin video) | **~0,8 USD** | ídem |

- **Por prueba:** 88 créditos de Kling y ~1,6–2,4 USD de fal.
- **Las siete:** 616 créditos de Kling y ~11,2–16,8 USD de fal. El saldo de Kling medido el 10-nov era de 2.858 créditos.
- **Solo c05b (lo que se correría primero):** 88 créditos y ~1,6–2,4 USD.
- No incluye completar un borrador de Seedance a 1080p o 4K (`…/draft/complete`), que se cobra aparte y se decide después de mirar.
- En Kling, `enable_audio` va en `true` para que el bloque AUDIO sirva de algo. En T1 no quedó anotado si los 12 y 10 créditos por segundo eran con audio o sin audio: si el MCP cobra distinto, se ve en `creditsConsumed`.

## Cómo se corre, cuando haya OK

0. **El OK de Cristian, escrito en el log:** qué pruebas y con qué tope.
1. **Entradas de 4 s** (sin costo, en esta máquina):
   - Hoy no existe ningún `$PREVIZ_TRABAJO/out/<llamada>_ref.mp4`. Se renderiza el gris de la llamada: `python3 storyboard.py video --json ../shots/<llamada>.json --samples 6`.
   - **c05a no tiene `stills/c05a/indice.json`**: antes hay que correr `python3 storyboard.py stills --json ../shots/c05a.json --samples 12`.
   - Después: `python3 prueba4s.py --llamada <llamada> --desde <s>`, que deja `video_1.mp4`, `hoja_storyboard.jpg` y `planos.json` en `$PREVIZ_TRABAJO/pruebas4s/<llamada>_<desde>-<hasta>/`.
   - Se revisa con ffprobe que `video_1.mp4` dure 4,000 s, tenga 96 cuadros a 24 fps y 720×1280 y no tenga audio. La hoja se mira.
2. **Referencias:** se bajan las hojas, planchas y props del Drive (`imagenes/04_aprobados`) o de `fal_urls_v1.json` a `$TRABAJO/refs/`. `HOJA_hugo` mide 2.752 px y dio `image_load_error` en fal: se reduce a 2.048 px de lado largo sin cambiarle el nombre.
3. **Subida:** cada archivo se sube una sola vez y se usa la misma URL pública en los cuatro brazos, para que «mismo archivo» sea literal. Puede ser la subida de fal o `file_upload` del MCP de Kling, si Kling rechaza la URL de fal. Se reemplaza cada `<subir: …>` del payload y no se toca el prompt.
4. **Orden:**
   - **c05b primero**, en este orden: Kling A, Kling B, Seedance A y Seedance B, una toma cada uno (`imageCount` 1, `seed` 1019).
   - Cada toma se baja apenas termina (la URL de Kling vence en 24 h). De Seedance se guarda el `draft_id`, que se puede completar dentro de 7 días sin volver a tirar.
   - Se comparan las cuatro, y **Cristian decide** si se corren las otras seis. El orden propuesto para el resto es c05a (se compara con T1), c04b, c06a, c03b, c00b y c07a.
   - Nada se reenvía sin OK. Si un motor falla dos veces o el cuerpo sale mal, se para.
5. **Registro del costo:**
   - Kling: el saldo antes y después con `query_membership_and_credits` y el `creditsConsumed` de cada envío.
   - fal: el panel Usage antes y después de la tanda (no hay cobro por API).
   - Se anota en `produccion/piloto_cap01/LOG_PRODUCCION.md`, con una entrada por tanda («pruebas 4s · <llamada>»).
   - Se anota en `produccion/piloto_cap01/tomas.json`, con una fila por toma. El id es `P4S_<llamada>_<motor>_<brazo>` y la fila lleva setting, refs, costo, archivo y veredicto.
   - Se llena la tabla de abajo.
   - Las tomas van a `$TRABAJO/pruebas4s/<prueba>/` como `kling_A.mp4`, `kling_B.mp4`, `seedance_A_draft.mp4` y `seedance_B_draft.mp4`.

### Registro (se llena al correr: costo real · veredicto)

| Prueba | Kling A | Kling B | Seedance A | Seedance B |
|---|---|---|---|---|
| c05b_2.0-6.0 | — | — | — | — |
| c05a_1.0-5.0 | — | — | — | — |
| c04b_4.0-8.0 | — | — | — | — |
| c06a_0.4-4.4 | — | — | — | — |
| c03b_0.7-4.7 | — | — | — | — |
| c00b_0.0-4.0 | — | — | — | — |
| c07a_5.0-9.0 | — | — | — | — |

## Decisiones de este borrador (para revisar)

**Referencias por prueba.** Todas tienen la hoja de cada personaje en cuadro y una o dos planchas, que se usan solo para look y luz.

| Prueba | Imágenes, en orden (en B se suma la hoja de storyboard al final) |
|---|---|
| c00b | `HOJA_martina` · `HOJA_extra_pareja_camisa_azul` · `PROP_maletin_v2` · `F08_v2_ambar_bajo` |
| c03b | `HOJA_extra_pareja_camisa_azul` · `ESTADO_hombre_azul_infectado` · `F08_v2_ambar_bajo` |
| c04b | `HOJA_hugo` · `HOJA_martina` · `HOJA_tomas` · `HOJA_carmen` · `HOJA_ivan` · `PROP_llave_y_cerradura` · `ref_infectados` · `F10_rojo_pasajeros_hacia_puerta` |
| c05a | `HOJA_hugo` · `HOJA_ivan` · `HOJA_carmen` · `HOJA_martina` · `HOJA_tomas` · `PROP_llave_y_cerradura` · `ref_infectados` · `F07_rojo_fuelle_vestibulo` · `F04_rojo_puerta_desde_fuelle` |
| c05b | las mismas cinco hojas · `PROP_llave_y_cerradura` · `ref_infectados` · `F04_rojo_puerta_desde_fuelle` · `F03_rojo_puerta_desde_dentro_0-45` |
| c06a | las mismas cinco hojas · `PROP_llave_y_cerradura` · `ref_infectados` · `F01_rojo_ultimo_vagon_hacia_puerta` · `F03_rojo_puerta_desde_dentro_0-45` |
| c07a | `HOJA_martina` · `HOJA_tomas` · `HOJA_carmen` · `F02_rojo_ultimo_vagon_hacia_fondo_cabina` |

- **c05b:** usa F04 (para el P6, la puerta vista desde el fuelle) y F03 (para el P7, la puerta vista desde adentro). El guion pone F07 y F04 para c05b, pero el P7 transcurre dentro del último vagón.
- **c07a:** usa F02 (el fondo y la cabina) en vez de F03 y F05, que son las del guion, porque la ventana es solo b7_p3, que mira hacia el fondo. No lleva las hojas de Diego, Iván ni Hugo, porque en estos 4 s no están en cuadro (CAST LOCK de 3). Por la misma razón, el giro de Iván fuera de cuadro que pide la ficha queda fuera del prompt: la regla es no nombrar lo que no tiene que aparecer.
- **c03b:** no lleva `PROP_maletin_v2` ni `ref_infectados`. El estado del hombre ya trae su look y el maletín apenas asoma.
- **La lectora, el joven de audífonos y los pasajeros** no tienen hoja: van solo en el texto. `lectora_b0_p4.png` existe en `previs/v1c/refs/`, pero no está aprobada.
- **Diego** no aparece en ninguna ventana. No se usa ninguna imagen suya, ni la `HOJA_diego` ni el estado marcado «a regenerar».
- **Orden de las imágenes:** primero las hojas, después los props o el estado, después `ref_infectados` y al final las planchas. En el brazo B, la hoja de storyboard va al final, para que cada hoja tenga el mismo número en los cuatro prompts.
- **LOCKs que se suman a los del 07:**
  - SIDES LOCK: los lados, corte por corte.
  - LIGHT LOCK: el tubo frío existe solo dentro del último vagón (T1 metió un tubo blanco en el fuelle).
  - BRIEFCASE, en c00b.
  - DOOR, en c06a.
  - BACK WALL y LIPS CLOSED, en c07a.
  - Se pueden quitar si Cristian prefiere solo los del 07.
  - `MARTINA: WINDOW SIDE IN CARRIAGE 5` no se usa, porque en ninguna ventana está sentada en el vagón 5.
  - El LOCK de la palma de Carmen se adapta al estado de cada bloque. En c05b y c06a dice «palma cortada, contra el pecho». En c07a dice «mano en puño dentro del abrigo». En c05a no va, porque la palma todavía no está cortada.
- **Tiempos:** son los del gris menos el inicio de la ventana. `prueba4s.py` redondea el inicio al cuadro: c03b parte en el cuadro 17 (0,708 s) y c06a en el 10 (0,417 s). Los cortes del prompt quedan a menos de un cuadro de los reales.
- **Largo:** los prompts tienen de 5.700 a 11.100 caracteres. Kling acepta hasta ~8.000 tokens (dato sin verificar). Si fal rechaza el largo en Seedance, se acortan PHYSICS y AUDIO, nunca CUTS ni LOCKS.
