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
