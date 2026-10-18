# Método de producción

Vigente desde el 18-oct-2026. **Este documento manda sobre `produccion/pipeline.md`** donde se contradigan.

Cada escena se genera en bloques continuos de 8 a 20 s, con varios planos adentro, a partir de un paquete fijo de referencias. El primer y último fotograma queda solo para insertos con encuadre exacto. El capítulo se arma dos veces: primero barato (animatic, para decidir) y después caro (versión final, para entregar).

## 1. Por qué cambia

El primer y último fotograma obliga al modelo a interpolar entre dos imágenes fijas. Por eso el movimiento se ve forzado y los planos no fluyen: la acción se inventa para llegar a una pose, no nace de la escena.

Las pruebas del repo ya mostraron el camino (`produccion/investigacion_referencias.md`):
- **Un bloque de 12 s con 7 referencias y 5 planos funcionó:** el modelo cortó cerca de los tiempos pedidos y mantuvo identidad, vestuario y luz.
- **El primer y último fotograma solo funcionó con control total de las dos imágenes,** y aun así inventó vestuario al interpolar.
- **Los prompts cortos salieron poco dirigidos.** Un bloque con referencias necesita una descripción completa de cada plano (ver `produccion/prompting/guia_direccion_video.md`).

## 2. El bloque de generación

Un bloque es un tramo continuo de una escena, generado en una sola llamada, con varios planos adentro. Es la unidad de producción; el plano es la unidad de montaje.

- **Una locación y una luz por bloque.** Si la luz cambia (de ámbar a rojo), es otro bloque, salvo que el cambio sea la acción del bloque.
- **Duración de 8 a 20 s.** Más corto no aprovecha el modelo; más largo pierde control de los tiempos. Si el motor tiene un tope menor (H3 Max: 15 s), el bloque se parte en dos llamadas que cortan en un cambio de plano.
- **Varios planos con tiempos.** El guion indica cada plano con su segundo de inicio, tamaño de plano y cámara. El modelo hace los cortes dentro de la generación.
- **El montaje recorta, no inventa.** Del bloque se quitan los colchones del inicio y del final. Si falta un plano, se regenera el bloque, no se parcha.
- **El primer fotograma solo cuando importa.** Si el primer cuadro del bloque tiene que ser exacto (el gancho de un capítulo), se pasa un fotograma guía como primer fotograma. Nunca primer y último a la vez.
- **Insertos aparte.** Un detalle con encuadre exacto (una mano, una herida, una pantalla) se genera como plano suelto de 3 a 5 s desde su fotograma guía, y el montaje usa uno o dos segundos.
- **Continuidad entre bloques.** Los últimos segundos del bloque aprobado anterior pueden pasarse como video de referencia del siguiente, cuando el motor lo acepte y la escena sigue sin salto de lugar ni de tiempo (por ejemplo, del bloque 6 al 7 del capítulo 1). No siempre: solo cuando corresponde.

## 3. El paquete de referencias

La continuidad depende de lo que se le pasa al modelo, no de lo bien que se describa. Cada bloque lleva un paquete fijo, y el prompt declara el rol de cada referencia al principio.

| Orden | Referencia | Qué define | Regla |
| --- | --- | --- | --- |
| 1 | Hoja de cada personaje en cuadro | Cara, cuerpo, vestuario | Solo los que aparecen en el bloque. Una imagen por personaje, sin fondo |
| 2 | Estado del personaje | Herida, ropa mojada, manchas | Solo si cambia algo respecto de la hoja |
| 3 | Plancha del set con la luz de la escena | Geografía y luz | Una por combinación de set y luz (ámbar o rojo) |
| 4 | Prop protagonista | Forma exacta del objeto | Solo si el bloque gira en torno a él |
| 5 | Voz de cada línea | Voz, ritmo y lipsync | Audio de ElevenLabs, una pista por personaje. Solo en la versión final |
| 6 | Video del bloque anterior | Continuidad de espacio y movimiento | Los últimos 3 a 5 s, solo si corresponde (sección 2) |
| 7 | Fotograma guía | Composición del primer plano | Solo para ganchos o planos que deben ser exactos |

El orden importa: personajes primero, luego props, después el set y al final el estilo. Cada referencia se nombra con su rol en el prompt (por ejemplo: «@Image1 is Martina: identity and wardrobe only; ignore the sheet layout and background»). En H3 Max, hasta 4 imágenes de 1024 × 1024 no tienen costo extra.

## 4. Qué motor para qué (decidido el 18-oct-2026)

| Motor | Rol | Lo que aporta | Costo aproximado |
| --- | --- | --- | --- |
| **MiniMax H3 Max** | Animatic del capítulo completo a 480p, insertos y exploración. Lo corren los bots de Cursor por fal (`minimax/h3-max/reference-to-video`) | 5 a 15 s, hasta 12 referencias, bloques de varios planos ya probados en el repo | 0,05 USD/s a 480p |
| **Kling 4.0** | Versión final de todos los bloques. Se corre por el MCP oficial de Kling con la suscripción | Hasta 30 s, 15 referencias, 10 keyframes, videos de referencia para guiar movimiento y cámara. Salió el 16-oct-2026 | Créditos de la suscripción |
| **Seedance 2.5** | Respaldo: solo el bloque que en Kling falle dos veces | Hasta 30 s, hasta 30 imágenes y 10 audios de referencia, audio nativo con lipsync | ~0,57 USD/s a 720p · ~1,40 USD/s a 1080p |
| **Nano Banana Pro / GPT Image 2.5** | Assets nuevos, estados y fotogramas guía (fal, `tools/fal_gen.py`) | Ediciones de una sola variable sobre assets aprobados | ~0,15 USD por imagen |
| **ElevenLabs** | Voces de la versión final (plan Creator) | Una voz fija por personaje para toda la temporada | Plan Creator |

- **El animatic sale barato:** el capítulo 1 completo en H3 Max a 480p son unos 97 s de generación (10 llamadas), cerca de 5 USD por pasada.
- **La versión final no se itera:** máximo dos tomas por bloque en Kling. Si las dos fallan, ese bloque pasa a Seedance; un bloque de 14 s a 720p cuesta cerca de 8 USD.
- **Pendiente de verificar:** si el MCP de Kling que usan los bots de Cursor expone la versión 4.0 completa. Mientras no se confirme, la versión final la genera Cristian (o Claude) desde su sesión.

## 5. El flujo

1. **Guion por bloques** (`guion/capNN/capNN_vX.md`): fichas con intención, cámara, referencias, planos con tiempo, sonido, assets que faltan y voces.
2. **Assets y voces:** se generan los assets que faltan (una variable por edición sobre lo aprobado) y, para la versión final, las voces.
3. **Fichas de dirección y prompts** (`produccion/prompting/guia_direccion_video.md`): una ficha por bloque, compilada en el formato de H3 (animatic) y de Kling (final).
4. **Animatic** en H3 Max a 480p, armado con los tiempos del guion.
5. **Cristian aprueba el animatic.** Si no funciona, se corrige la ficha del bloque y se vuelve a generar el animatic, nunca la versión final.
6. **Bloque final** en Kling 4.0 (máximo dos tomas; si fallan, Seedance 2.5).
7. **Montaje y post:** recorte, subtítulos, tarjetas, música y grano (Cristian).
8. **Reel listo** con su encuesta.

## 6. Reglas fijas para los bots

1. **El guion manda.** Cada bloque se genera desde su ficha (planos, tiempos, cámara, referencias). Lo que no está en la ficha no se inventa: se pregunta.
2. **Nunca primer y último fotograma,** salvo un inserto en el que se controlan las dos imágenes.
3. **Prompts completos,** en el formato oficial de cada motor, con el rol de cada referencia declarado al principio.
4. **Cámara explícita en cada plano:** tipo, amplitud y velocidad. Sin push-in por defecto; cada movimiento tiene un motivo escrito en el guion.
5. **Mano y lado del cuadro** en todo gesto, y dónde corta el encuadre en los planos cerrados.
6. **Cierre fijo de todo prompt de video:** «No music. No subtitles, no captions, no on-screen text.»
7. **Violencia:** se corta en el impacto y las manchas son oscuras. En los prompts nunca van las palabras *blood* ni *gore*.
8. **Diálogo:** en la versión final, la voz se genera antes y entra como referencia de audio. La línea del prompt es idéntica a la del guion.
9. **Dos tomas por bloque como máximo.** Si fallan las dos, se revisa la ficha del bloque antes de seguir generando.
10. **Nada pasa a la versión final** sin que Cristian apruebe el animatic.
11. **Todo queda registrado:** prompt, referencias, motor, semilla, costo y URL de cada toma, en la carpeta de la prueba (`produccion/pruebas/...`).
12. **No se gastan créditos sin el OK de Cristian** para la tanda (el plan del día lo indica).

## 7. Qué se revisa en cada toma

Vale para el animatic y para cada toma final. Si una respuesta es «no», se corrige la ficha del bloque antes de volver a generar.

- [ ] ¿Los planos cortan cerca de los tiempos del guion?
- [ ] ¿Se mantienen caras, vestuario y luz entre cortes?
- [ ] ¿El movimiento fluye o se ve interpolado?
- [ ] ¿La cámara hace lo que pide el guion y nada más?
- [ ] ¿La actuación tiene intención (miradas con destino, manos ocupadas, reacciones antes de que el otro termine)?
- [ ] ¿El lipsync y el acento funcionan? (en el animatic, solo como referencia)
- [ ] ¿Aparecen subtítulos, música o detalles que no se pidieron?
