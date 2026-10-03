# Registro de decisiones

Formato: fecha · decisión · motivo.

## 2026-09-28
- **Reel de zombies con acción y gore melee**, con estructura de microdrama: gancho a los 3 s, un giro y cliffhanger.
- **Proyecto VAGÓN 7** (dos agentes, un traidor): se escribió el guion v1–v3. Hoy está archivado en `archivo/vagon7/`.
- **Dirección de arte:** una luz dominante por acto, toda motivada por fuentes reales; se mantiene como base visual.

## 2026-09-29
- **Midjourney solo para explorar arte.** Las imágenes finales se hacen en Weavy.
- **Flujo de Weavy «VAGÓN 7 — Assets base»:** 52 nodos, armado pegando un JSON en el canvas.
- **Los prompts de imagen se reescriben con la plantilla de rodaje.** Motivo: la prueba de look salió con estética genérica de IA (ruido, luz sin fuente, composición de afiche).

## 2026-09-30
- **Formato de serie interactiva:** el público vota cada capítulo. Motivo: el referente de Fruit Love Island y de Love Island.
- **9:16 directo.** Se descarta el flujo 4:5 → outpaint.
- **Sin teaser.** Cristian maneja las encuestas en las plataformas.
- **Se cambia la premisa, de agentes a pasajeros comunes** (EL ÚLTIMO VAGÓN). Motivo: la gente no se ve reflejada en un agente; el conflicto tiene que ser cotidiano.
- **Triángulo en el centro.** Motivo: con dos personajes no hay a quién elegir.
- **Don Hugo tiene un revólver con dos balas.**
- **Reglas del mundo: opción 1, primer día.** Nadie sabe las reglas. Se descartó un tren de evacuación con control sanitario porque resolvía todo demasiado bien.
- **El tren se detiene más adelante** por el freno de emergencia. Motivo: da razones para entrar y salir del vagón y lo aleja de Snowpiercer.
- **Guion cap01_v4:** se aplica la opción 1 en diálogo (Carmen duda). Conteo: cinco adentro al cerrar; Diego es el sexto desde el vagón 4. Martina le pasó el tren a Diego (pista del triángulo). La llave va a Martina porque Diego la nombra. Carmen carga culpa de no haber salvado a alguien en el pasillo. Rama NO: Diego no se confirma muerto. Motivo: cerrar agujeros del reporte de mejora sin matar el motor de temporada.

### Producción (herramientas y proceso)
- **Weavy queda solo para crear assets:** hojas de personaje, locaciones y props. Los keyframes y videos por plano salen de fal.ai, Kling y Comfy Cloud. Motivo: Weavy es cómodo para el trabajo creativo, pero no se puede automatizar por plano.
- **fal.ai es el motor base de tomas,** con MiniMax H3 Max para video (barato y rápido) y Nano Banana Pro para keyframes. Motivo: se paga por uso, tiene cola y MCP, y encaja con un orquestador.
- **Kling se usa por su MCP oficial** (`kling.ai/mcp`) con la suscripción de Cristian. Motivo: los nodos de Kling en ComfyUI no aceptan la suscripción propia; gastan créditos de Comfy.
- **Comfy Cloud es complemento:** upscale final, correcciones puntuales y modelos por nodos pagados con los créditos que ya hay. Motivo: quedan muchos créditos y sirve para lo que necesita un grafo.
- **El shot list pasa a ser un guion técnico en YAML** (`produccion/shotlists/capNN.yaml`): un solo archivo de datos del que leen todos los roles y los motores. Motivo: automatizar sin duplicar información.
- **Equipo técnico de agentes:** Director, Director de fotografía, Continuista, Asistente de dirección y Control de calidad, además de Prompter y Pipeline. Motivo: que cada plano esté dirigido como en un rodaje tradicional.
- **Ningún plano pasa a video sin keyframe aprobado por Cristian.** Motivo: el video es lo caro; el cuello de botella es elegir tomas, no generarlas.
- **Kling 4.0 Flash solo para explorar** hasta que salga la versión oficial (octubre 2026). Cada plano de Kling se prueba primero en H3 Max. Motivo: Flash está en acceso anticipado y no se puede comprometer un capítulo en él.
- **Los prompts se compilan, no se escriben** (`produccion/compilador_prompts.md`): salen de los campos de Director, Director de fotografía, Continuista y Asistente, con una receta por modelo. Un prompt de video = una acción, un movimiento de cámara y un sonido. Motivo: que todos los roles colaboren en cada prompt y que el prompt sea corto y fácil para el modelo.
- **Nuevo rol: Montajista.** Prepara el plan de montaje; Cristian también edita. Motivo: el guion técnico llega a tomas sueltas y alguien tiene que ensamblarlas en 75–90 s.
- **Sin sobreimpresión «20 MINUTOS ANTES».** El salto de tiempo se resuelve por corte en el montaje. Motivo: decisión de Cristian.
- **Plano ≠ bloque de generación.** Los modelos no hacen clips de 1 s (H3 Max 5–15 s; Kling 3 s o más), así que el Director desglosa en planos (montaje) y el Asistente agrupa en bloques (producción): multi-beat, plano suelto recortado o encadenado. Motivo: viabilidad y continuidad; ver `produccion/investigacion_referencias.md`.
- **Continuidad por «pila de referencias»:** cada bloque recibe hojas de personaje, placa de locación con su luz y, si conviene, una toma aprobada anterior y un audio. Motivo: la continuidad depende de lo que se le pasa al modelo, no de lo que se describe.
- **Antes de cerrar el guion técnico se hace una tanda de pruebas baratas (480P, menos de 5 USD)** listada en `investigacion_referencias.md`.
- **En la versión final, el video se genera con el audio ya hecho** (voces de ElevenLabs como `target_audio_url` o referencia de audio) para que el lipsync nazca en la generación. En las pruebas se usa el audio que genera el modelo. Motivo: decisión de Cristian.
- **La post es opcional, nunca obligatoria.** Todo plano se resuelve en la generación; retocar, animar un still o sobreimprimir es trabajo de Cristian y solo se sugiere como mejora. Las sobreimpresiones (tarjetas, textos) las pone Cristian en After Effects; los armados de prueba van sin ellas. Motivo: decisión de Cristian.
- **Las pruebas de montaje se generan a 480P,** y los keyframes que se generen para ellas, a 720×1280. La resolución alta (768P/1080P, keyframes de 1088×1920) queda para la versión final. Motivo: decisión de Cristian; en una prueba importa ver qué funciona, no la nitidez, y el video cuesta cerca de un 40 % menos.
- **Sin subtítulos en la generación de video,** ni en las pruebas ni en la versión final. Los subtítulos se ponen en edición. Todo prompt de video cierra con «No music. No subtitles, no captions, no on-screen text.». Motivo: decisión de Cristian, después de que H3 Max dibujara el «Diego…» como subtítulo en c01_b02.
- **Nuevo rol: Productor de impacto** (`agentes/impacto.md`, borrador). Propone gancho, ritmo, espectacularidad de cámara y final para votar; el Director decide. Entra después del Director y antes del Director de fotografía. Motivo: pedido de Cristian para mantener la atención y dar más espectacularidad; los planos de la prueba salieron correctos pero planos.

### 2026-09-30 · Revisión de la prueba de montaje v1 (proceso)
Detalle en `produccion/pruebas/cap01_montaje_v1/feedback_proceso.md`.
- **Los prompts dejan de ser cortos.** Reemplaza la regla «un prompt de video = una acción, un movimiento de cámara y un sonido». Ahora cada beat tiene una intención clara, pero el prompt lleva todo lo que definieron los agentes, en el formato oficial de cada motor (H3: I2VA, FL2VA y Ref2VA). Se escriben con la skill `.cursor/skills/director-de-prompts/`. Motivo: Cristian vio los prompts muy cortos. El trabajo de los agentes no llegaba al modelo, y la guía oficial de H3 pide 350–500 palabras en los bloques con referencias.
- **Cámara según la escena, sin catálogo.** El Director de fotografía escribe una gramática de cámara por escena. Ningún plano queda fijo sin un motivo escrito. Motivo: la cámara quieta delata la IA y hace perder atención; Cristian descartó el catálogo de movimientos.
- **Sistema de actuación** (`produccion/actuacion.md`): objetivo, obstáculo, tarea física, beats con tiempo y miradas con destino. Reemplaza la regla «quietud y mirada». Motivo: la actuación de la v1 no tenía intención.
- **Primer y último fotograma solo con control total:** el último fotograma tiene que ser una edición del primero y el cambio tiene que ser de estado. Por defecto se usan referencias. Motivo: en b06 el modelo inventó la chaqueta al interpolar dos fotogramas distintos. Aprobado por Cristian.
- **Se define antes de generar.** Control de calidad hace una revisión previa de cada bloque y hay un tope de dos tomas por bloque. Si fallan las dos, se vuelve a la definición. Motivo: Cristian no quiere generar hasta que salga, sino que salga en pocos intentos.
- **La biblia del set se detalla con los assets definitivos.** Motivo: decisión de Cristian.

### 2026-09-30 · Assets v1 (rama `plan-assets-v1`)
- **Método de assets:** en Midjourney 8.2 la cara y el vestuario se exploran por separado, y se unen en GPT Image 2.5 (en paralelo con Nano Banana Pro) en Weavy. Motivo: MJ 8.2 no sostiene una cara entre imágenes; separadas, la cara no cambia con cada variación de ropa. Plan en `produccion/assets/plan_assets_v1.md`.
- **Los sets salen de una plancha maestra:** los estados de luz y los ángulos se editan sobre la misma imagen, no se generan de cero. Motivo: en la prueba 1 el vagón cambiaba de un plano a otro.
- **La manija del freno de emergencia se planta desde el capítulo 1** en el set, junto a la puerta. Motivo: cuando alguien la tire en el capítulo 3, el público tiene que poder decir que estaba ahí.
- **Propuestas de casting visual aprobadas** (`direccion_arte/personajes/fichas_personajes_v1.md`): reloj de enfermera para Carmen y sin hacha en el último vagón.
- **fal.ai entra al pipeline** para las ediciones con GPT Image 2.5 (Flare y Sunburst) y Nano Banana Pro, con `tools/fal_gen.py`. Weavy se mantiene para los flujos de nodos. Motivo: es más rápido, se puede automatizar y cada corrección queda guardada como archivo de prompt.
- **El repositorio de imágenes vive en Drive**, en la carpeta privada del proyecto, y se sube con `tools/drive_sync.py`. Motivo: falta de espacio en disco local.
- **Ninguna imagen se propone para aprobación sin pasar por el equipo de agentes** (continuidad y DP/arte). Las correcciones son de una sola variable. Motivo: lo pidió Cristian, para cuidar la continuidad.
- **Set del último vagón, v2** (`direccion_arte/sets/set_ultimo_vagon_v2.md`), aprobado el 2026-10-01.
  - Son 6 filas de 2 + 2.
  - El compartimento del revisor es una cabina construida en la esquina trasera, del mismo lado que el freno.
  - No hay llave en las placas.
  - La cinta va en la fila 5 izquierda.
  - Motivo: la revisión de continuidad encontró la puerta del revisor dando al exterior, la llave en planos donde no corresponde y la cinta en filas distintas.
- **La luz roja sale de una tira de emergencia en el centro del cielo del vagón.** Motivo: Cristian la prefiere; tiene más sentido que las rejillas.
- **En el vagón de pasajeros, los asientos miran hacia su puerta delantera, igual que en el último vagón.** Motivo: es el mismo modelo de vagón, y en los contraplanos los asientos tienen que verse de frente.
- **La cámara de la utilería no puede parecerse a la de un modelo de marca** (por ejemplo, el celular de Martina). Motivo: es propiedad intelectual ajena; la revisión descartó dos versiones del celular.
- **Las vistas con luz neutra pasan a ser el plano técnico del set, no planchas finales.** La dirección de arte se fija antes de las planchas finales, con un cuadro de referencia por estado de luz. Cada plancha final se genera en una sola pasada (referencia de look más plano técnico) y admite como máximo una corrección, siempre sobre la pasada limpia. Motivo: con las ediciones en cadena aparece el ruido típico de la IA y se pierde el look cinematográfico de la referencia ámbar y azul.

## 2026-10-01
- **cap01_v5:** mezcla de la v4 de Cursor y la v4 de Claude. El hombre de camisa azul llega desde adelante y Carmen lo atiende (ve los dientes) e Iván la salva. En la puerta, primero la pregunta de Iván y después el «Vine por ti» de Diego. Tomás: «Quiero verle la cara». Motivo: que el grupo aprenda por acción y que la culpa de Carmen sea concreta.
- **cap01_v6:** Diego: «Si no estás segura, no abras» (ambigua: ¿honesto o manipulador?). Carmen comprimida. «Muy rápido» en vez de «en segundos». Manchas sin heridas. Se mantiene «O sea que no hay cómo saber» de Iván. Hugo se acorta a «Te llama a ti. Tú decides» (amenaza en gesto del arma). La semilla del corte en la palma de Carmen sale del guion y queda en preguntas abiertas. Motivo: no sesgar el voto, menos texto en vertical, coherencia con las reglas, no confundir a producción.
- **cap01_v7 (FINAL):** sale «Había gente viva» para ~90 s; Hugo solo «Te llama a ti. Tú decides», amenaza en gesto; Martina mira a Tomás, a Diego y aprieta la llave; el «Diego…» del cold open ocurre en la escena 4 (mismo plano); acuerdo Carmen–Iván filmable (ella baja la vista, él asiente); se mantiene «O sea que no hay cómo saber». Semilla del corte fuera del cap. 1.
- **Cristian aprueba los assets v1**, que pasan a `imagenes/04_aprobados` en Drive (registro con URLs en `produccion/assets/aprobados_v1.md`). Incluye las planchas F01 a F12, los cuadros de look y las vistas técnicas, los cuatro props, las referencias y hojas de los seis personajes y la pareja extra, el estado de Diego y los keyframes KF01 a KF03. Motivo: hacen falta para la prueba de video con otro agente. Los cambios posteriores se hacen como `v2`, sin reemplazar lo aprobado. Las notas de revisión abiertas (contextura de Tomás, cuello de Iván, Martina y la camisa azul bajo luz roja) quedan para esa v2.

## 2026-10-03

### Continuidad
- **Brazo herido de Diego: DERECHO.** Resuelve la contradicción entre el YAML (`hc19`, `hc20`, `hc21`) y las fichas v2. Motivo: decisión de Cristian; el YAML es la referencia de continuidad correcta. A corregir: `ESTADO_diego_mojado_herido.png` (muestra el izquierdo, hay que regenerarla), keyframe de c01_p01 y video b01.

### Dirección y calidad (feedback del montaje v2)
- **Sin push-in ni dolly in por defecto.** Cada plano necesita una intención en la actuación y una cámara elegida a propósito. La cámara fija o en mano leve es la base; cualquier movimiento es la excepción y tiene que estar justificado (una escena, un solo movimiento con motivo). El único movimiento de cámara del capítulo 1 se reserva para cuando aparece la cara de Diego (escena 4). Motivo: el dolly in en todos los planos delata la IA y no impacta.
- **Una intención por plano.** Cada escena tiene su propio lenguaje de cámara.
- **Keyframes en alta** (GPT Image en high o Nano Banana Pro en 2K). Motivo: calidad baja produce «IA slop».
- **Video en 1080p** para la versión final (pruebas siguen en 480p).
- **Cámara explícita en cada prompt** (fija o en mano, «no push-in»). Control de calidad rechaza las tomas con push-in o con movimiento de fondo sin motivo.
- **Grano agregado en edición,** no el que deja el modelo.

### Cold open v8
- **Cold open reescrito en 4 planos:** (1) la mano golpea de golpe con cámara fija a 65 mm; (2) Martina a ~3 m de la puerta salta y se congela; (3) la mano deja de golpear y se apoya plana; (4) primer plano de Martina, del miedo al reconocimiento, «Diego…» casi sin voz, los ojos se le van hacia Tomás por culpa, Tomás desenfocado gira la cabeza, corte a negro en la respiración. Motivo: que el primer cuadro sea el impacto, legible en el celular sin sonido; que Martina tenga expresión; que no haya push-in.
- **cap01_v8 es la versión vigente.** La v7 queda como histórica.

### Escena 1
- **Tomás ve que Martina está con el celular y gira la cabeza a propósito para no ver.** No lee el mensaje, pero elige no saber. Tensión callada entre los dos. Motivo: más tensión que simplemente «no lo vio»; el gesto tiene un porqué explícito.

### Producción del cold open (prueba de calidad + lipsync)
- **Solo MiniMax H3 Max a 1080p** para los 4 planos del cold open. Kling 4.0 Preview es 720p, así que **Kling queda fuera de este documento**. Motivo: decisión de Cristián (3-oct, 01:18); la promo de fal (0,096 USD/s hasta 15-oct) hace que H3 Max sea la opción más económica sin sacrificar resolución.
- **Keyframes en Nano Banana Pro 2K** (alternativa: GPT Image 2.5 high). Motivo: evitar el «AI slop» que dejó el montaje v2.
- **Segundo golpe fuera de campo en P2: SÍ.** (3-oct-2026, 10:33) Un segundo golpe **solo en audio**, fuera de campo, a los 0,3 s de P2. Martina salta en cámara con ese golpe. P1 sigue siendo «golpe seco, después silencio» durante 1,5 s. Motivo: sin el segundo golpe, el sobresalto de Martina llegaría tarde (P2 empieza 1,5 s después de P1).
- **Ventanita con malla de alambre (F03): SÍ.** (3-oct-2026, 10:52) Se mantiene F03 y se corrigió hc22. La ventanita es un rectángulo vertical de esquinas redondeadas con marco metálico remachado, vidrio de seguridad con malla de alambre fina en rombo (diamond wire mesh), a la altura de la cabeza de un adulto. Misma forma, tamaño y malla en todos los planos y desde ambos lados. Motivo: F03 ya estaba aprobada; hc22 decía "vidrio simple" por error.
- La lista técnica completa está en `produccion/pruebas/cap01_cold_open/lista_tecnica.md`.

### Pendientes para escenas siguientes (por confirmar con Cristián)
- Hugo tiene que verse con el boleto en la mano cuando se agacha.
- El revólver no se adelanta (el inserto no puede parecer preparación para un ataque que todavía no existe).
