# Método de producción

Vigente desde el 18-oct-2026; actualizado el mismo día después de la revisión del animatic v1 (sección 8 y `produccion/pruebas/cap01_animatic/revision_v1.md`). **Este documento manda sobre `produccion/pipeline.md`** donde se contradigan.

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
- **Duración del bloque:** la de su escena en el guion. **La llamada al motor es más corta:** en H3 Max, de 4 a 8 s y con un máximo de tres planos; en Kling 4.0, hasta 15 s. En las pruebas, las llamadas largas con pocos planos hicieron que el modelo terminara cada acción antes de tiempo y rellenara con espera (`revision_v1.md`).
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
| 5 | Pista de diálogo de la llamada | Voz, tiempos y lipsync | Las tomas aprobadas de ElevenLabs, montadas en los tiempos del guion en una sola pista (de 2 a 15 s en H3; de 5 a 30 s en Kling). **En el animatic y en la versión final** |
| 6 | Video del bloque anterior | Continuidad de espacio y movimiento | Los últimos 3 a 5 s, solo si corresponde (sección 2) |
| 7 | Fotograma de la previsualización | Composición, luz y continuidad del plano | El del primer plano de la llamada va como primer fotograma; los de los demás planos, como referencia de su plano (sección 8) |

El orden importa: personajes primero, luego props, después el set y al final el estilo. Cada referencia se nombra con su rol en el prompt (por ejemplo: «@Image1 is Martina: identity and wardrobe only; ignore the sheet layout and background»). En H3 Max, hasta 4 imágenes de 1024 × 1024 no tienen costo extra.

## 4. Qué motor para qué (decidido el 18-oct-2026)

| Motor | Rol | Lo que aporta | Costo aproximado |
| --- | --- | --- | --- |
| **MiniMax H3 Max** | Animatic del capítulo completo **a 768p** (desde el animatic v2), insertos y exploración. Lo corren los bots de Cursor por fal (`minimax/h3-max/reference-to-video`) | Hasta 15 s, hasta 9 imágenes y 3 audios de referencia. A 768p respeta la pista de diálogo como audio de referencia; a 480p, no | 0,05 USD/s (precio de lista; confirmar el cobro real a 768p en la primera llamada) |
| **Kling 4.0** | Versión final de todos los bloques. Se corre por el MCP oficial de Kling con la suscripción | Hasta 30 s, 15 referencias, 10 keyframes, videos de referencia para guiar movimiento y cámara. Salió el 16-oct-2026 | Créditos de la suscripción |
| **Seedance 2.5** | Respaldo: solo el bloque que en Kling falle dos veces | Hasta 30 s, hasta 30 imágenes y 10 audios de referencia, audio nativo con lipsync | ~0,57 USD/s a 720p · ~1,40 USD/s a 1080p |
| **GPT Image 2.5** (`openai/gpt-image-2.5/flare/edit`; `sunburst/edit` para fotogramas clave) | Previsualización, fotogramas guía, estados nuevos y todo lo que necesite composición precisa | Sigue instrucciones de encuadre y continuidad con varias referencias | ~0,15 USD por imagen |
| **Nano Banana Pro** (`fal-ai/nano-banana-pro/edit`) | Ediciones de una sola variable sobre un asset aprobado | Rápido y barato para cambios chicos | ~0,15 USD por imagen |
| **ElevenLabs** | Voces de la versión final (plan Creator) | Una voz fija por personaje para toda la temporada | Plan Creator |

- **El animatic sigue siendo barato:** el capítulo 1 completo en H3 Max a 768p, con dos tomas por llamada, son unos 160 s de generación, cerca de 8 USD por pasada a precio de lista.
- **La versión final no se itera:** máximo dos tomas por bloque en Kling. Si las dos fallan, ese bloque pasa a Seedance; un bloque de 14 s a 720p cuesta cerca de 8 USD.
- **Pendiente de verificar:** si el MCP de Kling que usan los bots de Cursor expone la versión 4.0 completa. Mientras no se confirme, la versión final la genera Cristian (o Claude) desde su sesión.

## 5. El flujo

1. **Guion por bloques** (`guion/capNN/capNN_vX.md`): fichas con intención, energía, cámara, referencias, planos con tiempo, sonido, tabla «Estado del mundo», assets que faltan y voces.
2. **Voces primero:** se eligen las tomas y se arma la pista de diálogo de cada llamada con los tiempos del guion.
3. **Assets:** los que faltan (GPT Image 2.5 o Nano Banana Pro, sección 4).
4. **Previsualización:** un fotograma por plano (GPT Image 2.5), montado con las pistas de diálogo en un video de imágenes fijas. **Cristian la aprueba antes de generar video.** Corregir aquí cuesta centavos; corregir en video cuesta una versión.
5. **Fichas de dirección y prompts** (`produccion/prompting/guia_direccion_video.md`): una ficha por bloque, compilada en el formato de H3 (animatic) y de Kling (final), con los fotogramas aprobados como referencia.
6. **Animatic** en H3 Max a 768p, dos tomas por llamada, revisado contra la lista de `revision_v1.md` antes de mostrarlo.
7. **Cristian aprueba el animatic.** Si no funciona, se corrige la ficha del bloque y se vuelve a generar el animatic, nunca la versión final.
8. **Bloque final** en Kling 4.0 (máximo dos tomas; si fallan, Seedance 2.5).
9. **Montaje y post:** recorte, subtítulos, tarjetas, música y grano (Cristian).
10. **Reel listo** con su encuesta.

## 6. Reglas fijas para los bots

1. **El guion manda.** Cada bloque se genera desde su ficha (planos, tiempos, cámara, referencias). Lo que no está en la ficha no se inventa: se pregunta.
2. **Nunca primer y último fotograma,** salvo un inserto en el que se controlan las dos imágenes.
3. **Prompts completos,** en el formato oficial de cada motor, con el rol de cada referencia declarado al principio.
4. **Cámara explícita en cada plano:** tipo, amplitud y velocidad. Sin push-in por defecto; cada movimiento tiene un motivo escrito en el guion.
5. **Mano y lado del cuadro** en todo gesto, y dónde corta el encuadre en los planos cerrados.
6. **Cierre fijo de todo prompt de video:** «No music. No subtitles, no captions, no on-screen text.»
7. **Violencia:** se corta en el impacto y las manchas son oscuras. En los prompts nunca van las palabras *blood* ni *gore*.
8. **Diálogo:** la voz se genera antes, **también en el animatic**, y entra como pista de referencia de la llamada. La línea del prompt es idéntica a la del guion y su entrega física coincide con la toma elegida.
9. **Dos tomas por llamada (dos semillas) desde el principio,** para elegir. Si fallan las dos, se revisa la ficha del bloque antes de seguir generando.
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
- [ ] ¿Pasa la lista de fallas de `produccion/pruebas/cap01_animatic/revision_v1.md` (sección 5)?

## 8. Reglas nuevas después del animatic v1 (18-oct-2026)

Salen de las notas de Cristian (`produccion/pruebas/cap01_animatic/revision_v1.md`). Mandan sobre cualquier regla anterior de este documento.

1. **Ritmo:** un plano dura lo que dura su acción más 0,5 s como máximo. En la acción, planos de 1 a 1,5 s; en el diálogo, la línea más 0,3 s. Cada plano empieza con la acción en marcha.
2. **Sin tiempo muerto antes de hablar:** la línea entra a 0,3 s del corte como máximo, salvo una pausa escrita en el guion.
3. **Cámara con intención en cada plano:** tamaño, altura, tipo, amplitud, velocidad y motivo. La cámara fija es una elección para un plano, no un valor por defecto. La energía del bloque (de 1 a 5, en el guion) decide la gramática.
4. **Continuidad escrita:** cada guion trae la tabla «Estado del mundo». Cada prompt copia las filas de su bloque y cada toma se revisa contra ella.
5. **Todos los personajes en cuadro llevan su hoja de referencia.** Nada de personajes «solo descritos» para ahorrar imágenes (H3 acepta 9).
6. **Previsualización antes del video:** un fotograma por plano, aprobado por Cristian. Esos fotogramas son la referencia de composición, luz y continuidad de cada plano.
7. **Voces primero, también en el animatic,** como pista de diálogo de la llamada (H3 a 768p).
8. **El montaje corta en la acción y en los cortes reales de la toma** (se detectan en el video, no se suponen). Nunca se congelan cuadros para estirar.
9. **Revisión antes de entregar:** cada bot pasa su entrega por la lista de `revision_v1.md` (sección 5). Lo que llega a Cristian ya pasó por ella.
10. **Presupuesto:** el ahorro no justifica una versión más. Se gasta lo necesario para que la entrega salga bien a la primera, dentro del tope de la tanda.

