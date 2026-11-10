# Manual de producción · El Último Vagón (se escribe durante el piloto)

Receta para producir un capítulo, escrita a partir de lo que de verdad se hizo en el piloto. Tiene que servir para el capítulo 2 sin leer el log.

**Estado al 9-nov-2026:** escritas las secciones que salen de las fases (a) a (d). Las de settings, fallas y costos se llenan al producir.

## 1. Entradas

Antes de empezar un capítulo tiene que existir:

| Entrada | Dónde | Chequeo |
|---|---|---|
| Guion vigente, **una sola versión** | `guion/capNN/` | Sin copias fuera del repo; el diff contra la anterior está a la vista |
| Decisiones vigentes de Cristián | `biblia/decisiones.md` | Cada decisión con fecha. Si no está escrita, no existe |
| Tiempos por plano y por llamada | `tiempos_montaje.json` | Suma = duración del capítulo; cada llamada con duración entera para Kling (3–30 s) |
| Un fotograma aprobado por plano | `previs/frames/` | 1152×2048 como mínimo si va a ser primer fotograma |
| Hojas de personaje y planchas de set | archivo local en el repo o en el Drive, **no solo URL de fal** | Las URLs de fal vencen |
| Pistas de voz por llamada | `pistas/` | Cada pista ≥ 5 s y ≤ 30 s (límite de `audio_1` en Kling); las líneas en sus tiempos desde el segundo 0 |
| Lista de fallas | `revision_v1.md` §5 (20 puntos) | — |
| Saldo de Kling y gasto de fal | MCP de Kling; panel de fal | Anotados en el log el día que se parte |

## 2. Pasos, en orden

| # | Paso | Entra | Sale | Herramienta | Revisión | Aprueba |
|---|---|---|---|---|---|---|
| 1 | Chequeo de arranque | repo, kit | estado de herramientas, saldo, rama | `git`, MCP de Kling, conector de fal (solo lectura) | — | — |
| 2 | Lectura por áreas con subagentes | repo y kit | un informe por área | 6 subagentes en paralelo | El director lee las reglas y decisiones él mismo | — |
| 3 | Consolidar el guion | versiones del guion + decisiones | una versión + diff | edición + `git diff` | La historia no cambia | Cristián |
| 4 | Propuesta y plan con topes | informes | `01_propuesta.md`, `02_plan.md` | — | Cada precio con su fuente; lo no verificado, marcado | **Cristián (parar aquí)** |
| 5 | Pruebas críticas (lipsync, cámara) | un plano, la misma pista | tomas + medición + costo real | *(se llena al producir)* | | Cristián |
| 6 | Fotogramas | | | | | |
| 7 | Video por tanda | | | | | |
| 8 | Revisión de tomas | | | | | |
| 9 | Montaje y sonido | | | | | |
| 10 | Entrega | | | | | Cristián |

## 3. Settings que funcionaron

Medido en el piloto (9 y 10-nov-2026):

| Setting | Para qué sirvió | Costo real | Resultado |
|---|---|---|---|
| Kling 4.0 `omni_ref_video`, 720p, `audio_1` + hojas + cuadro de composición, sin video | Diálogo | **10 créditos por segundo de salida** | Conserva la pista (correlación 0,99, desfase 0) y calza las bocas en español. Sin previz abre el encuadre respecto de la referencia |
| Kling 4.0 `omni_ref_video`, 720p, `video_1` (previz de la misma duración) + hojas + cuadros de look | Acción con cámara dirigida | **12 créditos por segundo de salida** | Sigue encuadres, lente y cortes del previz al cuadro |
| Kling 4.0 `image_to_video`, 720p, `first_image` | Control | 10 créditos por segundo | *(resultado en el log)* |
| H3 Max 768P, primer fotograma + audio de referencia | Respaldo del diálogo | sin dato (fal no devuelve el cobro); ~0,45 USD por toma de 5 s | Conserva la pista (0,98); boca exagerada, luz más pareja |
| Seedance 2.5 480p, `audio_urls` | — | sin dato; ~1,3 USD por toma de 6 s | **No sirve para diálogo:** rehace y atrasa la pista (0,63; +0,6 s) |
| GPT Image 2.6 sunburst edit, 1152×2048, high, hasta 5 referencias | Fotogramas | sin dato; ~0,07 USD (estimado) | Reconstruye luz, lados y miradas aunque reciba el cuadro viejo como referencia |
| Nano Banana 2.1 edit, 9:16, 2K | Fotogramas | sin dato; ~0,15 USD (estimado) | Se queda pegado al cuadro de referencia: útil para un edit puntual, no para rehacer |

**Cómo se mide el costo:** en Kling, `query_membership_and_credits` antes y después (y el envío devuelve `creditsConsumed`). En fal no hay forma por API ni por el conector: hay que leer el panel (Usage) a mano.

Límites ya confirmados en los schemas (9-nov-2026), sin generar:

| Motor | Límite que condiciona el plan |
|---|---|
| Kling 4.0 `omni_ref_video` (MCP) | Duración entera 3–30 s · `audio_1` de 5–30 s · `video_1` de 3–30 s, y sus segundos se cobran · sin rol de primer fotograma · sin semilla (dos tomas = `imageCount: 2`) · sin campo de negativos · `prefer_multi_shots` siempre `true` · referencias en el prompt como 图片1, 视频1, 音频1 |
| Kling 4.0 `image_to_video` (MCP) | `first_image` · sin audio, sin hojas, sin Elements |
| Kling 4.0 en fal | Sin audio de entrada: para usar nuestra pista hay que ir por el MCP |
| Seedance 2.5 en fal | Mínimo 4 s · sin primer fotograma · `audio_urls` de 1,8–30,2 s |
| H3 Max en fal | `reference_audio_urls` de 2–15 s · `image_url` como primer fotograma · no combinar primer fotograma con video de referencia |

## 4. Prompts tipo

Bloques fijos que van en todo prompt de video (en inglés):

- **Vestuario inmutable:** `Wardrobe identical to Picture N in every frame; it does not change color and does not change during the shot.`
- **Lo que no se mueve:** una línea `What stays still in this shot: …` por plano, que parte con la frase de luz.
- **Frases de luz** (describen lo que ya se ve, no piden un cambio):
  - Vagón 2 y 5: `only 2–3 warm amber ceiling lamps, darkness between them, no added fill`
  - Rojo: `single red emergency light from above, half the face in shadow, no white fill`
  - Ventanita de Diego: `one cold tube above the glass is the only light`
  - Cuarto del rapto: `single hard cold downlight from straight above, darkness around it, no added fill`
- **Miradas:** `Nobody looks into the lens; every gaze has a target in the carriage.`
- **Boca cerrada del que no habla:** `X's lips stay closed and still while Y speaks.`
- **Pista:** `Audio 1 is the exact dialogue of this scene: use it as the soundtrack and sync every line to the lips of the speaker. Voices only from Audio 1.`
- **Cierre:** `No music. No subtitles, no captions, no on-screen text.`
- **Nunca:** `blood`, `gore`, grano de película, ni posición de un prop sin decir desde dónde se mira.

*(Las plantillas completas por motor se agregan cuando estén probadas.)*

## 5. Fallas vistas y cómo se resolvieron

| Falla | Causa | Qué se hizo |
|---|---|---|
| Tres versiones del guion, ninguna completa | Una copia de trabajo editada fuera del repo y nunca subida | Consolidar en la rama y mostrar el diff. Regla: el guion se edita solo en el repo |
| El gasto de fal no se puede confirmar | El corredor no guardó el cobro y la cuenta se comparte con otros proyectos | Medir saldo o panel antes y después de cada tanda, y anotarlo en el log en el momento |
| El maletín mal puesto en tres cuadros después de varias vueltas | El prompt decía «lado del pasillo» sin decir cuál asiento ni desde dónde se ve | *(se confirma al rehacer los cuadros)* |
| Hojas disponibles solo como URL de fal | No se guardó el archivo | Bajar cada referencia al repo o al Drive el mismo día que se aprueba |

## 6. Costos y tiempos reales

*(Por tanda y total; horas de agente y de Cristián. Se llena al producir.)*

Fases (a) a (d): 0 USD, 0 créditos. ~1 hora de agente con seis subagentes de lectura.

## 7. Qué se podría volver determinístico

Tareas repetitivas que un equipo de bots (o un script) puede hacer sin criterio creativo.

| Tarea | Entrada | Salida | Regla o chequeo automático | Hoy lo hace | Riesgo si se automatiza |
|---|---|---|---|---|---|
| Chequeo de arranque | repo, entorno | tabla: rama, herramientas instaladas, variables definidas (sin mostrarlas), saldo de Kling | todo presente o lista de lo que falta | agente, a mano | ninguno |
| Detectar versiones distintas de un mismo archivo | repo + copias | tabla de diferencias por línea | `diff` de a pares | subagente | bajo. Elegir cuál gana sí requiere criterio |
| Recortar primeros fotogramas a 9:16 | `previs/frames/*.png` | `primeros_fotogramas/*_9x16.png` | tamaño exacto, sin barras, ≥ 1152×2048 | `prep_frames.py` (ruta fija, hay que parametrizarla) | ninguno |
| Validar duraciones contra los límites de cada motor | tiempos + pistas | tabla «cumple / no cumple» por llamada | Kling 3–30 s enteros, audio 5–30 s; Seedance ≥ 4 s | subagente | ninguno |
| Medir la duración de cada pista | `pistas/*` | tabla de duraciones | `afinfo` o `ffprobe` | subagente | ninguno |
| Revisar qué URLs de referencia siguen vivas | `fal_urls_v1.json` | vivas y muertas | petición HEAD, código 200 | subagente | ninguno |
| Armar payloads desde la ficha de plano | ficha + plantilla | payload por llamada | campos obligatorios presentes; frases fijas presentes; diálogo idéntico al guion | *(pendiente)* | medio: el texto de actuación sí es creativo |
| Registrar cada llamada paga | respuesta del motor + saldo | fila en `tomas.json` y en el log | saldo antes y después; para si pasa el tope | *(pendiente)* | ninguno; es obligatorio |
| Bajar cada toma apenas termina | URL de resultado | archivo local + hash | el archivo existe y dura lo pedido | *(pendiente)* | ninguno |
| Hoja de contacto por toma | mp4 | jpg con cuadros a tiempos fijos | un cuadro al inicio y al final de cada plano | *(pendiente)* | ninguno |
| Medir entrada de línea contra el corte | mp4 + pista | tabla de desfases | tope de 0,3 s | Métricas, a mano | bajo |
| Medir si la pista salió sin cambios | audio de la toma + pista | correlación y desfase | correlación ≥ 0,8, desfase ≤ 2 cuadros | script del 18-oct | bajo |
| Armar el corte desde la EDL | EDL + tomas + pistas | mp4 | duración total = suma de la EDL | *(pendiente)* | ninguno |
| Chequeo de vestuario y continuidad por toma | toma + hoja + lista | OK o problema | visión con lista de chequeo, dos revisores que no se ven | subagentes | **alto: falsos OK.** Siempre con hoja de contacto para una persona |
