# Decisiones de la previs v1c

19-oct-2026. Hechos de esta corrida. Cada llamada, con prompt y veredicto, está en `log_generaciones_v1c.json`. Los montos son estimados: fal no devolvió un costo en la respuesta ni en el status.

## Cifras

- Llamadas registradas: 73 (48 de NBP o flare, 25 de sunburst).
- Sin PNG usable: 2 (carga de `HOJA_hugo.png`, y un rechazo del checker en `b7_p2`).
- En el montaje: 33 fotogramas salidos de fal. Los otros 10 planos del corte usan el PNG original de la previs (no había paso, o el paso quedó marcado).
- Corredor `gastado_usd`: 6.85. La suma de las tarifas del lote por las llamadas V es 6.40. La diferencia, 0.45, coincide con las tres tomas del FIX de `b2_p4`, anotadas también en `correcciones`. No se suman dos veces.
- Sunburst, estimado: 1.44 USD (25 llamadas).
- Total estimado de esta corrida: 8.29 USD. Tope del lote: 12. Tope v3: 40, con 5.56 ya gastados antes.

La estimación de sunburst sale de la tabla de fal del 9-sep-2026 (calidad high, una referencia: 1920×1080 = 0.03960 USD, 2560×1440 = 0.05529). 1152×2048 son 2.359 megapíxeles, interpolados a 0.0424. Cada referencia extra suma 0.008, cifra del 8-sep-2026 en `prompts_previs_v1.md`, no remedida. El texto suma 0.004. Si la factura real es más alta, este número queda corto.

## Editar o regenerar

El plan del lote era una variable por paso, en Nano Banana Pro, encadenando la salida aceptada. Después de la corrección de Cristián eso se cortó.

Se regeneró en sunburst, desde el PNG original de `previs/frames/`, cuando el plano ya tenía dos cambios o la salida editada era la base de otra edición:

- `b0_p2` (luz + puño), `b0_p3` (luz + mirada), `b3_p6` (luz + forcejeo + lectora), `b4_p6` (fuelle + pelo), `b5_p6` (llave + luz), `b5_p8` (ventanita + reencuadre).
- `b2_p4`: V18 y luego tres ediciones de banca. La última se apoyaba en una salida ya editada.
- `b3_p1`: el paso V03 editaba el `b0_p2` ya corregido, no el original.
- `b6_p2`: dos tomas flare sobre el original. La segunda se aceptó y después se regeneró por la regla de no apilar y por la acción de la mano.
- `b6_p3`: la edición NBP (V35) dejó vías y cielo en la ventanita trasera. No se editó esa salida.
- `b6_p1`: dos NBP no giraron a Iván. Sunburst fue el tercer intento, desde el original.
- Bloque 7 entero (`b7_p1` a `b7_p6`): cada plano tenía dos o tres pasos. Se hizo un solo sunburst por plano, con todos los cambios en el prompt. V36–V47 no se corrieron.

Se dejó la edición NBP o flare, de una sola variable y desde el original, en los planos de una sola corrección que no se rehicieron: `b0_p1`, `b0_p4`, `b1_f2`, `b2_p1`, `b2_p2`, `b2_p3`, `b3_p3`, `b3_p4`, `b3_p5`, `b4_p1`, `b5_p1`, `b5_p2`, `b5_p4`, `b5_p5`, `b5_p7`, `b5_p9`.

`b0_p1` (V14 t1) se volvió a mirar con la regla de ruido: primer plano de ojos, piel nítida, sin el grano crujiente del ejemplo. Se mantuvo.

`b2_p1` (V19) se mantuvo. La banca se lee con apoyabrazos central. No se regeneró: el pedido de banca compartida se aplicó a `b2_p4`, que era el plano señalado.

## Reescrituras de prompt

Solo cambió el párrafo del momento. El resto del prompt quedó igual.

`b0_p2`, toma 0 → toma 1. Motivo: el maletín seguía en el pasillo.

- Antes: «sits fully UNDER the blue seat, on the AISLE side, tucked into the shadow beneath the cushion».
- Después: «The cushion hides the top of the briefcase. Only its front face and brass corner peek out below the seat rail.»

Toma 1 → toma 2. Misma falla.

- Después: «Slide the briefcase backward, toward the window, until the blue cushion covers two thirds of it.»

Las tres tomas lo dejaron contra el riel, no debajo. El original de la previs ya lo tiene así. Se aceptó la toma 2 con esa falla.

`b3_p6`, toma 0 → toma 1. Motivo: la pareja del primer término estaba sentada, no forcejeaba.

- Antes: «a dark struggling tangle in shadow».
- Después: «the blue-shirt man is on his feet and lunging onto his wife. They are not asleep and not sitting calmly.»

La toma 1 sí lo muestra de pie y abalanzado.

`b6_p2`. La toma 0 pedía la palma hacia su cara y el puño entrando al abrigo. La mancha no se leía y el puño no entraba. Se reescribió a «closed fist already inside the brown coat» y no se llegó a generar esa versión: el cupo se usó en planos sin toma.

`b7_p2`. El primer texto pedía manga rasgada y «stained dark reddish black», con `ESTADO_diego_mojado_herido_v3`. El checker lo rechazó (`content_policy_violation`) y no hubo PNG. Se sacó la hoja de estado y las palabras de herida. La toma siguiente salió con marcas rojo vivo en la espalda. La tercera pidió «clean pale canvas» y «charcoal grey» en el vidrio. Esa es la del montaje: la chaqueta queda clara con manchas oscuras, ya no rojo vivo, pero las manchas no están solo en la manga derecha.

`b7_p5`. La toma 0, con la hoja de estado, llenó el pecho y la manga de rojo vivo y puso las dos manos en el vidrio. Se reescribió: palma izquierda sola, chaqueta clara, sin la hoja de estado. La toma 1 tiene la palma izquierda en el vidrio. Queda una marca rojo vivo en la manga.

`b7_p6`. La toma 0 dejó una puerta detrás de Martina. Se agregó: «There is no door in that wall, no door handle on it». La toma 1 es pared ciega y ventanita negra.

## Chequeos que fallaron

- Maletín bajo el asiento, lado pasillo: falló en `b0_p2` (tres sunburst) y en `b3_p1` (uno). También en V04 (`b3_p2`, dos flare): una toma lo dejó al lado de las piernas y la otra bajo el asiento pero del lado de la ventana. Ese plano sigue con el PNG original.
- Mirada: `b0_p3` quedó bien (hacia el hombre). V14 t0 no se aceptó; t1 sí, ojos a la izquierda.
- Pelo de Tomás: `b4_p6` y `b7_p4` quedaron con partidura. `b6_p3` no es una partidura estricta.
- Ventana del lado de Martina: `b2_p3` y `b2_p4` la tienen a la izquierda de ella. No se reabrió el resto.
- Luz: los sunburst de vagón 2 bajaron a pocas lámparas. `b2_p4` quedó con más de dos o tres. En el último vagón la tira del techo sigue siendo larga en varios planos; la media cara en sombra sí se lee en `b5_p6`, `b6_p2`, `b7_p3`.
- Geografía del último vagón: V35 (`b6_p3`) mostró vías y cielo. El sunburst no. `b7_p6` toma 0 tenía una segunda puerta; la toma 1 no. `b7_p3` y `b7_p4` salieron con la pared trasera a la primera.
- Iván de espaldas a la puerta: dos NBP no lo giraron. El sunburst sí.
- Palma de Carmen: el puño está en el pecho y no se muestra a cámara. No se ve la mancha y el puño no entra en el abrigo.
- Manga derecha de Diego: ni `b7_p2` ni `b7_p5` la dejan como única zona oscura.
- Ruido y piel: no se aceptó una salida con la piel crujiente del ejemplo. `b0_p1` y los sunburst de cara se leyeron nítidos. No hay una medida automática de eso; fue juicio al mirar el PNG.
- Banca compartida: `b2_p4` muestra el lugar vacío al lado, sin divisor. El encuadre quedó más abierto que un primer plano.

## Orden y paralelismo

Hasta V35 el corredor iba de a una llamada, en orden, porque cada paso dependía de haber aceptado el anterior. A partir de la corrección, los planos independientes salieron de a seis:

1. `b0_p2`, `b0_p3`, `b3_p6`, `b4_p6`, `b5_p6`, `b5_p8`. `b5_p6` falló por la hoja de Hugo; los otros cinco sí.
2. Reintentos de `b0_p2` y `b3_p6`, más `b5_p6`, `b2_p4`, `b6_p2`, `b6_p3`.
3. `b7_p1` a `b7_p6`. `b7_p2` lo rechazó el checker.
4. `b7_p2`, `b7_p5`, `b7_p6`, `b3_p1`, `b6_p1`, `b0_p2`.
5. Un solo reintento de `b7_p2`.

No se corrió V36–V47. `num_images` quedó en 1 en todas.

## Parches al script

`run_lote_v1c.py` no se tocó. `run_sunburst.py` se escribió para este lote.

- `next_toma`: si ya existe `SB_<plano>_tN`, la siguiente escribe `tN+1`. Sirve para reintentar sin pisar la toma anterior. La primera versión del script usaba siempre `t0`.
- El pool ahora atrapa la excepción de una llamada y sigue con las otras. En el primer grupo, el 422 de Hugo cortó el proceso con código 1, pero los otros cinco PNG ya se habían guardado.
- Carrera: en un arranque, el proceso de Python y la escritura de `run_sunburst.py` cayeron en el mismo segundo. El grupo siguiente imprimió `t1` para los planos que ya tenían `t0`, así que cargó el script nuevo y no pisó esas tomas. En `b7_p2` pasó lo mismo con el prompt: el meta de la toma 1 guarda el texto nuevo («clean pale canvas»), o sea que esa vez el proceso leyó el archivo ya escrito. No hubo una toma cobrada con el prompt viejo por esa carrera.
- `HOJA_hugo.png` pesaba 2752×1536 y fal respondió `image_load_error`. Se bajó a 1536×858 con ffmpeg y la toma siguiente cargó.
- Los meta de las primeras tomas solo guardan `request_id`. A partir del bloque 7 guardan también latencia de pared, prompt y rutas. La latencia de las primeras se completó con `inference_time` del status de fal (sin la subida).

## Aceptados con falla conocida

- `b0_p2` toma 2 y `b3_p1`: maletín al lado del asiento, no debajo.
- `b5_p8`: la mano atorada tiene uñas largas.
- `b2_p4`: banca compartida, encuadre abierto, más lámparas de las pedidas.
- `b6_p2`: puño en el pecho, sin mancha visible y sin entrar del todo al abrigo.
- `b6_p3`: pelo de Tomás no es la partidura estricta de la hoja.
- `b7_p1`: las manos del vidrio se leen rojas, no casi negras.
- `b7_p2` toma 1: manchas oscuras en la espalda, no solo en la manga derecha.
- `b7_p5` toma 1: marca rojo vivo en la manga derecha.
- `b7_p3`: Iván queda grande en el primer término, no solo en el borde.
- `b3_p2`: las dos tomas flare se marcaron. El montaje usa el original.
- `b2_p1`: sigue con apoyabrazos entre los dos asientos.

## Llamadas que costaron sin plano usable

Sin PNG:

- `SB_b5_p6` request `01a15216-809f-7271-95e9-dfef6c0d122a`. 422 al cargar la hoja de Hugo. El status dice COMPLETED y 6.6 s de inferencia. No está confirmado el cobro. Estimado: igual que una toma de 4 referencias.
- `SB_b7_p2` primer intento. `content_policy_violation`. No quedó request_id en el log. No está confirmado el cobro.

Con PNG, y no entraron al montaje: todas las tomas marcadas `retry` o `flag` en el JSON (V04 las dos, V33 las dos, los reintentos de sol y el FIX t1 y t2, entre otras). Son pruebas que se pagaron para llegar a la toma que sí quedó.

## Qué se podría volver determinístico

Patrones que se repitieron:

- Pedir «under the seat» no mueve el maletín si el fotograma de referencia lo tiene en el pasillo. Tres formulaciones no alcanzaron. Un script puede medir la caja del maletín contra la caja del asiento y rechazar la toma si el maletín no queda cubierto por el cojín.
- La ventanita de la puerta, o la trasera, se llena de cielo, vías o lluvia si el prompt no dice que es un fuelle oscuro. Pasó en V35 y en la primera `b7_p6`.
- Encadenar dos ediciones NBP sobre el mismo plano cambia cosas que el segundo prompt pedía conservar (lámparas de más, maletín que se corre). La regla que funcionó: si hay dos cambios, un solo sunburst desde el original, con el plano entero escrito.
- La hoja de estado de Diego y las palabras de herida disparan el checker o llenan la chaqueta de rojo vivo. El texto que pasó fue «clean pale canvas» y «charcoal grey», sin esa hoja.
- Una hoja de personaje de más de 2048 px de ancho puede fallar al cargarse. Conviene bajarla antes de subirla.
- `num_images=1` y grupos de seis planos independientes no cambiaron el costo por imagen. El corredor secuencial solo hace falta cuando la base es la salida de otro paso.

Plantilla que sirvió, en sunburst, calidad high, 1152×2048:

1. «FILM STILL, vertical 9:16. Rebuild this shot clean, in one pass, from Image 1.»
2. Una línea por referencia, con su rol.
3. MOMENT con quién, de qué lado del cuadro, y la mano concreta.
4. BEHIND con la pared o el fuelle, y la lista de lo que sí hay (ventanita negra, sin vías).
5. LIGHT en una frase: de dónde viene y qué mitad de la cara queda en sombra.
6. TEXTURE: piel nítida, grano fino, sin texto.

Chequeos que un script puede hacer sin mirar:

- Contar lámparas encendidas por umbral de brillo en la franja del techo.
- Rechazar un plano si el borde superior tiene píxeles de cielo (azul) en la ventanita de la puerta.
- Comparar el histograma de la manga derecha contra el del pecho en Diego.
- Medir si el maletín intersecta el rectángulo del asiento.
- Rechazar la respuesta de fal si el status no trae imagen, y no contar esa toma como aceptable.
- Guardar en cada meta el prompt, las rutas, el `request_id` y la latencia. Las primeras tomas de este lote no lo hicieron y hubo que reconstruir el texto.

Regla práctica: una sola corrección, desde el PNG original, puede ser una edición. Dos correcciones, o una edición que ya salió ruidosa, se regeneran una vez con el plano entero escrito. No se edita la salida de una edición.
