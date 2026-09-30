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
