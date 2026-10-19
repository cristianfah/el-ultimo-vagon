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
- **Tomás SÍ va en P4, con giro de cabeza.** (3-oct-2026, 10:57) Tomás desenfocado, de tres cuartos de espalda (se le ve sobre todo la nuca y el perfil perdido), boca cerrada y apretada, nunca la abre. Gira la cabeza (~15–20°) hacia Martina **después** de que ella termina de decir «Diego…» (2,4–3,0 s, nunca durante). Solo Martina habla. KF4b (sin Tomás) queda como plan B si H3 le mueve la boca o le muestra la cara. Motivo: el giro de cabeza después del nombre añade tensión; verlo de tres cuartos de espalda reduce el riesgo de que H3 le anime la boca.
- **Staging de Tomás en P2: gira hacia Hugo, no hacia la puerta.** (3-oct-2026) Después del segundo golpe, Tomás se sobresalta y gira la cabeza por sobre el hombro hacia la cola del vagón, donde está Don Hugo (que tiene la llave y el revólver), como preguntando «¿qué hacemos?». Termina de tres cuartos de espaldas a cámara, que es como lo encuentra P4. Motivo: establece la continuidad de su posición entre P2 y P4; su reacción instintiva es buscar a la autoridad, no mirar la puerta.
- La lista técnica completa está en `produccion/pruebas/cap01_cold_open/lista_tecnica.md`.

### Pendientes para escenas siguientes (por confirmar con Cristián)
- Hugo tiene que verse con el boleto en la mano cuando se agacha.
- El revólver no se adelanta (el inserto no puede parecer preparación para un ataque que todavía no existe).

## 2026-10-18 · Biblia v2 (revisión de historia con Claude)

Trabajado en el documento «El Último Vagón — Lore del universo» (pestañas Lore, Escaleta T1, Producción y Cap 1 · Guion) y pasado al repo. La biblia anterior quedó en `archivo/biblia_v1/`.

### Historia
- **Nueva premisa:** un tren nocturno lleva un virus hacia la capital; la hija del Presidente lo liberó sin saberlo, obligada por sus captores; el gobierno puede bombardear el tren. Motivo: el guion v8 era el piloto de una serie larga metido en 90 s, el voto estaba cargado hacia el «sí» y había salidas obvias (la cabina del revisor). Ver `biblia/premisa.md`.
- **Martina es la hija del Presidente.** La raptan antes de subir, la amarran gente con máscaras y la obligan a dejar un maletín en el vagón 2 sin decirle qué contiene. Motivo: una decisión moral sobre si una vida vale lo mismo cuando es de tu familia.
- **Detrás hay una secta controlada por una IA creada para salvar el planeta.** Concluyó que el problema es la decisión humana: no quiere matar, quiere que nadie decida. El tren es su prueba con el Presidente. Se insinúa en la temporada 1 y se revela en la 2. Motivo: idea de Cristian; Claude propuso la motivación de la máquina y Cristian sumó el cambio climático. Ver `biblia/conspiracion.md`.
- **Por qué Martina:** con ella a bordo, el gobierno no puede bombardear el tren sin más. Motivo: decisión de Cristian.
- **El virus:** inhalado desde el maletín actúa casi al instante; por mordida o herida tarda según el lugar. Motivo: decisión de Cristian.
- **El tren no para porque lo maneja el control central;** el freno está bloqueado desde afuera. Reemplaza la idea del freno de emergencia. Motivo: que la regla se entienda sin explicación.
- **El gobierno lo oculta hasta que el tren cruza una estación sin parar** y el video se hace viral. Ahí sube el infiltrado, que trabaja para la secta. Motivo: decisión de Cristian.
- **Sin cuenta regresiva en pantalla.** El destino es una amenaza de fondo. Motivo: decisión de Cristian.
- **Don Hugo ya no le entrega la llave a Martina;** su poder es saber desenganchar el vagón. Motivo: el gesto anterior no se sostenía.
- **Iván mantiene su motivación original** (su hijo, su dureza es miedo). Se descartó que quisiera el bombardeo. Motivo: nadie querría liberar la infección; no era creíble.
- **Diego sabe poco:** vio a Martina con un maletín en el vagón 2 y lo entiende recién en el capítulo 6. Motivo: Cristian no quería un Diego que sabe y calla.
- **Carmen es la infectada del final** (corte en la palma derecha durante la huida del capítulo 1). Motivo: es el personaje más querido.
- **Temporada 1 de 8 capítulos,** escrita completa antes de producir. Final: sueltan el último vagón; Diego queda del lado del tren sin confirmar su muerte; Carmen está infectada. Ver `biblia/escaleta_t1.md`.
- **País sin nombre con geografía chilena.** No se nombra Chile.
- **«El Último Vagón» es un nombre interno;** no aparece en los reels.

### Formato y votaciones
- **Las encuestas son «Si fueras ___, ¿qué harías?»** y en la temporada 1 no cambian la historia. La decisión mayor va al final de temporada. Reemplaza el voto «¿Martina le abre?» con dos ramas. Motivo: escribir y producir dos versiones por capítulo frena la producción; el voto «no» era ridículo. Ver `biblia/votaciones.md`.
- **Formato del reel:** premisa en los primeros segundos, una escena, un giro, corte en la mejor parte, máximo tres personajes con diálogo, tarjetas de nombre cuando el personaje habla, el pasado en flashes de 1 s. Ver `.cursor/rules/10-guion.mdc`.

### Capítulo 1
- **`guion/cap01/cap01_v9.md` es el guion vigente.** Reemplaza a la v8 (que queda como histórica). Está escrito en 8 bloques de generación con fichas para producir.
- **El vagón 2 lleva pasajeros (extras)** para que se lea como un tren con gente. Motivo: nota de Cristian sobre el bloque 0.
- **La pista del padre va en un diálogo** («¿Tu papá sabe que vienes en este tren?» / «No. Esa era la idea.»), no en boca de los captores. Motivo: decisión de Cristian.

### Producción
- **El bloque de generación con referencias reemplaza al primer y último fotograma.** Cada bloque (8–20 s, una locación y una luz) lleva varios planos y un paquete fijo de referencias. El primer y último fotograma queda solo para insertos con control total. Motivo: en las pruebas, la interpolación entre dos fotogramas hacía que el video no fluyera e inventaba vestuario. Ver `produccion/metodo.md`.
- **Reemplaza la regla «ningún plano pasa a video sin keyframe aprobado»:** ahora la aprobación de Cristian es sobre el animatic completo.
- **Animatic primero:** el capítulo completo en MiniMax H3 Max a 480p (lo corren los bots de Cursor por fal). Cristian lo aprueba antes de la versión final.
- **Kling 4.0 es el motor final de todos los bloques.** Si un bloque falla dos veces en Kling, pasa a **Seedance 2.5**, que es bastante más caro. Motivo: decisión de Cristian. Kling 4.0 salió el 16-oct-2026.
- **Voces en ElevenLabs** (plan Creator), una voz fija por personaje. En el animatic se usa el audio que genera el modelo.
- **Guía de dirección para prompts de video:** `produccion/prompting/guia_direccion_video.md`. Motivo: pedido de Cristian para que el bot productor escriba prompts dirigidos con actuación, emociones (como conducta) y movimiento.
- **Voces aprobadas (18-oct-2026):** Tomás, Martina y Diego con acento chileno suave (nunca acento de España), diseñadas en ElevenLabs y actuadas con el modelo v4. IDs y método en `produccion/voces.md`. Motivo: Cristian sintió robóticas y «españolas» las primeras muestras en español neutro.

## 18-oct-2026 (noche) · Revisión del animatic v1

Notas de Cristian sobre el animatic v1 y v2 del capítulo 1. Detalle en `produccion/pruebas/cap01_animatic/revision_v1.md`.

### Capítulo 1
- **`guion/cap01/cap01_v10.md` es el guion vigente.** Misma historia de la v9; cambia la dirección: ritmo, cámara con motivo, continuidad escrita y voces primero. Motivo: el v1 salió lento, con cámara fija, tiempos muertos y errores de continuidad.
- **El maletín se abre solo** (cierres con temporizador), bajo el asiento del hombre de camisa azul, y la niebla se arrastra hasta él. Ya no lo encuentra ni lo abre. Motivo: idea de Cristian; además calza con un plan de la secta.
- **Los flashes del rapto son un solo recuerdo** que nace de un gesto de Martina (se aprieta la muñeca), con corte por coincidencia. Motivo: en el v1 el salto de lugar no se entendía.
- **Don Hugo habla:** «¡Al último vagón! ¡Rápido!». Motivo: con el gesto solo no se entendía (nota de Cristian). Falta diseñar su voz.
- **Se ve cómo Carmen se corta:** un infectado revienta el vidrio y la agarra, Iván la tira, cae y la palma derecha golpea los vidrios. Motivo: en el v1 no se entendía.
- **Diego está mojado porque cruzó por fuera del tren.** Detrás de él, por la ventanita, solo se ve el fuelle oscuro: nunca lluvia, cielo ni una puerta abierta. Detrás de él se mueven sombras. Motivo: nota de Cristian sobre la lluvia en el fuelle y la falta de peligro.
- **Hugo no sostiene la llave en el plano final:** su mano está en el cerrojo, esperando la respuesta de Martina. Motivo: la llave se veía antinatural.
- **Los golpes de los infectados paran por una razón:** un grito lejano en el vagón 5 se los lleva. Antes de Diego se oye el viento y una puerta lateral del fuelle (fuera de cuadro). Motivo: en el v1 no se entendía por qué paraban ni de dónde salía Diego.
- **Los planos cerrados del último vagón se toman desde el lado de la puerta:** Martina a la derecha del cuadro y Tomás a la izquierda, para que sus miradas se encuentren. Motivo: revisión de ejes del guion v10.

### Producción
- **Voces primero, también en el animatic:** la pista de diálogo con las tomas aprobadas entra como audio de referencia. **H3 Max a 768p** (a 480p no respeta la pista). Motivo: con el video generado antes, la intención y los tiempos no calzaban con las voces.
- **Previsualización antes del video:** un fotograma por plano en GPT Image 2.5, montado con las pistas de diálogo; Cristian la aprueba antes de generar. Motivo: corregir en imágenes cuesta centavos y evita versiones de video.
- **GPT Image 2.5 entra al pipeline** para la previsualización, los fotogramas guía y los estados nuevos; Nano Banana Pro queda para ediciones de una sola variable. Motivo: decisión de Cristian.
- **Llamadas cortas** (de 4 a 8 s y hasta tres planos en H3), **dos semillas por llamada** y **todos los personajes en cuadro con su hoja**. Motivo: las llamadas largas generaban tiempo muerto y los personajes solo descritos cambiaban de cara.
- **Lista de fallas que no se repiten** (`revision_v1.md`, sección 5): cada bot revisa su entrega contra ella antes de mandarla. Motivo: Cristian no quiere 150 correcciones ni 20 versiones antes de la versión en alta.
- **Más presupuesto:** tope de 40 USD en fal para el animatic v3. Motivo: Cristian pidió gastar lo necesario para que salga bien.

## 19-oct-2026 · Assets v10 y previs

- **Tope de fal del v3: 40 USD, techo no meta.** Las tandas sueltas siguen con el tope que se les asigne (esta de assets: 3 USD). Motivo: Cristian lo confirma.
- **b0_p2:** la manga que empuja el maletín es la del abrigo gris, con el puño del suéter avena asomando y cubriéndole los nudillos. Motivo: decisión de Cristian para la previsualización.
- **c04b en previs:** Hugo toma A (2,3 s) entra a los 2,5 s de `pistas/c04b.mp3`; el pitazo va como efecto en post a los 2,1 s. Motivo: tiempos de Cristian para `cap01_previs_v1`.

