# 02 · Plan de producción con presupuesto por tanda

9-nov-2026. **Nada se ejecuta antes del OK de Cristián.** La primera llamada de cada setting nuevo mide el costo real y se reporta antes de seguir (regla 4).

**La idea en una línea:** el capítulo entero se dirige en Blender y lo apruebas en gris; dos pruebas chicas confirman el motor; después se produce el diálogo y luego la acción. Kling por créditos; fal para lo que Kling no hace y para las retomas que no quepan.

## Las dos bolsas

| Bolsa | Disponible | Ya gastado | Este plan |
|---|---:|---:|---:|
| Créditos de Kling (plan Pro) | **3.176** (leído hoy) | — | ~2.870 a 3.050 estimados. **Cabe justo, casi sin margen** |
| fal, tope del piloto | **60 USD** (lo ratificas tú) | ~13,85 USD **estimados, sin factura** | topes por 15 USD + reserva de 15 + 5 opcionales → quedan ~11 sin asignar |

**Supuesto de créditos (sin verificar):** 10 créditos por segundo a 720p, y el video de referencia suma sus segundos. El 10 viene de un tercero; Kling no lo publica y el MCP no lo entrega. Se mide en T0 y T1.

## Requisitos previos (sin costo, pero necesitan tu OK)

1. **Instalar `ffmpeg` y Blender en este Mac.** No están. Sin ellos no hay previz ni montaje. Los bajo de sus sitios oficiales si me das el OK, o los instalas tú.
2. **Bajar al repo las 38 referencias que hoy solo viven en fal** (hojas, planchas de set, props). Están vivas hoy y pueden vencer.
3. **El monto real de fal del 18 y 19 de octubre** (panel de fal → Usage). El historial que puedo leer no trae montos.
4. **Una carpeta fija para el trabajo.** Hoy está en una carpeta temporal de la sesión.

## Tandas, en orden

Duraciones de Kling redondeadas a entero. «s fact.» = segundos facturables (salida + video de entrada).

| # | Tanda y objetivo | Qué incluye | Motor y setting | Tomas | Costo estimado | **Tope** | Revisión contra §5 | Cuándo ve Cristián |
|---|---|---|---|---:|---|---|---|---|
| **P** | **La película en gris** | Fichas de plano (lente, altura, motivo de cámara) · set y elenco en bloques · previz de las 17 llamadas · montaje gris de ~70 s con las voces · recorte de fotogramas | Local (Blender, ffmpeg, Python) | — | 0 | 0 | 1–8 y 18–20 ya se pueden revisar en gris: ritmo, ejes, 180°, entrada de cada línea | **Página 1** |
| **T0** | **Lipsync en español** (decide el motor del diálogo) | c02a con la misma pista limpia | H3 768P + audio ref · Kling Omni 720p + `audio_1` · Seedance 480p + `audio_urls` | 2 · 2 · 1 | 2,2 USD · 120 créditos | **4 USD · 150 créditos** | 3, 14, 15 + boca cerrada del que no habla + pista sin cambios | Página 1 |
| **T1** | **Cámara** (¿Kling sigue a Blender?) | c05a y c00a con su previz · el previz de c05a en Seedance · controles: c05a sin previz y c00a con primer fotograma | Kling Omni 720p con `video_1` · Seedance 480p + video · Kling Omni sin video · Kling i2v | 1 c/u | 270 créditos · 1,3 USD | **300 créditos · 2 USD** | 6, 7, 8, 9, 15 + bordes de Blender superpuestos sobre la toma | Página 1 |
| **T2** | **Fotogramas** rehechos desde cero | 17 cuadros (lista abajo) | GPT Image 2.5 sunburst `quality: high`, 1152×2048, el cuadro actual como referencia | 2 candidatos c/u | ~2,5–3,5 USD | **5 USD** | 9, 10, 11, 15, 17 + luz de la locación | Página 1 |
| | **→ PARAR. Página 1.** Apruebas el gris y eliges el motor del diálogo. | | | | | | | |
| **T3** | **Diálogo** | c02a, c02b, c04b, c07a, c07b, todas con previz y pista | El ganador de T0. Si es Kling: Omni 720p + `video_1` + `audio_1` | 2 | 152 s fact. → 1.520 créditos (o ~7 USD si gana H3) | **1.550 créditos** (o 8 USD) | 3, 7, 8, 14, 15, 16 + pasada de vestuario | — |
| **T4** | **Acción e insertos** | c00a, c00b, c01, c01f, c03a, c03b, c04a, c05a, c05b, c05i, c06a, c06b, todas con previz | Kling Omni 720p + `video_1` | 1 | 114 s fact. → 1.140 créditos (960 si sirven las dos tomas de T1) | **1.150 créditos** | 1, 2, 5, 6, 9–13, 17 + pasada de vestuario | — |
| **T5** | **Retomas** | Solo llamadas que fallaron la revisión, con la ficha o el previz corregidos | Créditos que queden; lo demás en fal | 1 | según fallas | **lo que quede de créditos · 15 USD de reserva · 2 USD (fotogramas)** | La falla que motivó la retoma | — |
| **T6** | **Montaje y sonido** | EDL cortada en la acción real · pista limpia en sus tiempos · ambiente, golpes, pitazo · grano y color · 1080×1920 | ffmpeg local · efectos de sonido (ElevenLabs o audio de las tomas) | — | 0–2 USD | **2 USD** | 1–5, 18, 19, 20 (prueba sin sonido) + entrada de cada línea ≤ 0,3 s | **Página 2 (Corte 1)** |
| **T7** | Ajustes del Corte 1 y entrega | Lo que pidas · Drive + rama + PR en borrador | — | — | sale de lo no asignado | se fija en la página 2 | Lista §5 completa, marcada | **Página 3 (final)** |

**Opcional: 5 USD** para un escalado con modelo, que se decide en la página 2.

### Qué va en paralelo

- P, T0, T1 y T2 van juntas. T0 no necesita previz. T1 necesita solo el previz de c05a y c00a, que se hacen primero.
- Dentro de T3 y T4, todas las llamadas van juntas, salvo las que usan la cola de la toma anterior (c06a → c06b → c07a → c07b), que esperan a que se elija esa toma.
- La revisión de cada toma parte apenas se baja.

### Primeras llamadas que miden costo real (se reportan antes de escalar)

| Setting nuevo | Tanda | Cómo se mide |
|---|---|---|
| Kling Omni 720p, sin video, con `audio_1` | T0 | saldo antes y después |
| Kling Omni 720p, con `video_1` | T1 | saldo antes y después |
| Kling Omni 720p, sin video ni audio | T1 | saldo antes y después |
| Kling `image_to_video` 720p | T1 | saldo antes y después |
| Kling Omni 720p, con `video_1` y `audio_1` | T3 (primera: c02a) | saldo antes y después |
| H3 Max 768P con audio de referencia | T0 | panel de fal |
| Seedance 2.5 480p con audio / con video | T0 / T1 | panel de fal |
| GPT Image 2.5 sunburst high, 1152×2048 | T2 | panel de fal |

### Regla de ajuste después de medir

Con el costo real de T0 y T1 se recalculan T3 y T4. Si los créditos no alcanzan, te aviso antes de seguir y se recorta en este orden:

1. **Las llamadas sin voz con previz pasan a Kling en fal** (`kling/v4/reference-to-video`, 0,188 USD por segundo de salida a 720p: ~10,7 USD una toma de las 12). Sale de la reserva.
2. Los cuatro planos fijos puros (c01, c01f, c05i, c06b) van con primer fotograma, sin video de entrada, si la prueba T1 muestra que queda igual.
3. El diálogo baja a una toma más retoma.

Los créditos se guardan primero para el diálogo: nuestra pista solo entra por el MCP. La otra salida, que decides tú, es recargar créditos de Kling.

## Fotogramas para rehacer (T2): 17 cuadros

Todos desde cero en sunburst high, con el cuadro actual como referencia y todos los cambios en un solo prompt (regla 2). Cada prompt lleva la frase de luz de su locación, el vestuario inmutable y lo que no se mueve.

Frases de luz: **ámbar** = «only 2–3 warm amber ceiling lamps, darkness between them, no added fill» · **rojo** = «single red emergency light from above, half the face in shadow, no white fill» · **tubo** = «one cold tube above the glass is the only light» · **rapto** = «single hard cold downlight from straight above, darkness around it, no added fill».

| Cuadro | Llamada | Qué se corrige | Luz |
|---|---|---|---|
| b1_f1 ★ | c01f | Cenital duro, oscuridad alrededor. Sube a 1152×2048 | rapto |
| b2_p1 ★ | c02a | Hoy tiene ~8 lámparas y relleno en las caras. Pelo de Tomás corto con partidura | ámbar |
| b2_p4 ★ | c02b | 6 lámparas, y **falta Tomás** en el asiento de al lado | ámbar |
| b3_p1 ★ | c03a | Maletín **bajo** el asiento, lado pasillo, tapa cerrada | ámbar |
| b4_p4 ★ | c04b | Rehacer a 1152×2048 | rojo |
| b5_p8 ★ | c06a | Uñas cortas, rotas y sucias. Llave por dentro y ventanita seca se mantienen | rojo |
| b6_p2 ★ | c06b | Desde cero: palma derecha abierta cerca del pecho, la mirada sobre el corte | rojo |
| b3_p2 | c03a | El hombre **sentado**, el maletín bajo su asiento. Hoy está de pie en el pasillo | ámbar |
| b4_p5 | c04b | Hugo no mira al lente: mira al fondo del vagón. Sube a 1152×2048 | rojo |
| b5_p4 | c05b | **Carmen mira a cámara.** Debe mirar su mano en el vidrio | rojo |
| b5_p7 | c05b | **Tomás mira a cámara.** Debe mirar hacia adentro del vagón. Sin luz blanca en las caras | rojo |
| b6_p3 | c06b | Luz blanca plana, otra cara de Tomás, y al fondo parece una puerta | rojo |
| b7_p2 | c07a | Diego: solo la manga derecha con manchas rojo-negro; la izquierda limpia | tubo |
| b7_p5 | c07b | Diego: sin la mano roja en el hombro. Detrás, solo el fuelle oscuro | tubo |
| b2_p3 | c02b | Primer cuadro de la llamada: lámparas de más y relleno en la cara | ámbar |
| b4_p1 | c04a | Primer cuadro de la llamada: 7 lámparas encendidas | ámbar |
| b1_p1 | c01 | Primer cuadro de la llamada: está a 608×1088 | ámbar |

★ = los siete de la lista del kit. Los otros diez salen de la revisión visual de hoy.

Antes de rehacerlos hay que fijar en el «Estado del mundo» lo que hoy cambia entre planos: la bandolera de Martina, el lado de la placa de la cerradura, el tubo frío encendido, el pelo y la chaqueta de Tomás, y el color de las esquineras del maletín.

## Comparación de rutas

| Ruta | Previz en | Tomas | Créditos (est.) | fal (USD) | ¿Cabe? |
|---|---|---|---:|---:|---|
| Completa, como la estimó el productor | las 17 | 2 en todas | ~3.800 + pruebas | fotogramas y pruebas | **No cabe** en 3.176 créditos. Por fal serían 35,7 USD |
| **Completa con tomas ajustadas (la que propongo)** | las 17 | 2 con voz, 1 + retoma sin voz | ~2.870–3.050 con pruebas | ~9 + reserva de 15 para retomas | **Sí, justo.** Las retomas sin voz van a fal |
| Selectiva (respaldo del productor) | c04b, c05a, c05b, c06a, c07a, c07b | 2 | ~1.640 | ~6,9 (el resto en H3) | Sí. Pero 11 llamadas quedan con la cámara en texto |

Las cifras en USD de las rutas del productor son **estimación del productor**. Las de créditos son mías, con el supuesto de 10 por segundo.

## Total previsto

- **Créditos de Kling:** topes 150 + 300 + 1.550 + 1.150 = **3.150 de 3.176**. Estimado: 2.870 a 3.050.
- **fal:** 13,85 gastados (estimado) + topes 4 + 2 + 5 + 2 + 2 = **28,85 USD**. Con la reserva de 15 y el escalado opcional de 5: **48,85 de 60**. Quedan ~11 sin asignar.

Si una tanda va a pasar su tope, paro y aviso.

## Actualización después de T0 y T1 (10-nov-2026)

Costos **medidos** en Kling a 720p: 10 créditos por segundo de salida sin video y **12 con un previz de la misma duración** (no 20, como suponía este plan).

| | Supuesto del plan | Medido |
|---|---:|---:|
| Una toma de las 17 llamadas con previz | ~1.900 créditos | **~1.140** |
| Dos tomas de las 17 con previz | ~3.800 (no cabía) | **~2.280** |
| Saldo | 3.176 | **2.858** después de las pruebas |

Consecuencia: **caben dos tomas de todo el capítulo con previz**, con ~580 créditos de margen para retomas. La propuesta de una sola toma en las llamadas sin voz ya no hace falta.

Motor del diálogo: **Kling 4.0 Omni-Ref con `audio_1`** (correlación 0,99 con la pista, desfase 0). Seedance queda fuera del diálogo. Detalle en `pagina_1.md`.
