# Roles de agentes

Un sistema de varios agentes, todos con el mismo contexto (`AGENTS.md` y `biblia/`). Cada uno tiene una responsabilidad y un lugar donde deja lo que produce. Los roles con archivo propio tienen su prompt de sistema en esta carpeta.

## Equipo de historia

| Rol | Responsabilidad | Lee | Escribe |
|---|---|---|---|
| **Showrunner** (`showrunner.md`) | Coherencia de la temporada, arco, qué se decide en cada capítulo, que haya debate | `biblia/` y todos los guiones | `biblia/arco_temporada.md`, `biblia/decisiones.md` |
| **Guionista** (`guionista.md`) | Escribe y reescribe capítulos y ramas. Diálogo con la voz de cada personaje | `biblia/`, el capítulo anterior | `guion/capNN/capNN_vX.md` |
| **Abogado del diablo** | Busca agujeros de lógica («¿por qué no hacen lo obvio?»), reglas violadas y opciones de votación desbalanceadas | Guion y `biblia/reglas_del_mundo.md` | Comentarios al final del guion, sección «Revisión» |

## Equipo técnico

Todos escriben en el guion técnico (`produccion/shotlists/capNN.yaml`), cada uno solo en sus campos. Formato en `produccion/formato_guion_tecnico.md`.

| Rol | Pregunta que responde | Campos que escribe |
|---|---|---|
| **Director** (`director.md`) | ¿Qué ve el público, en qué orden y para qué? | Planos, acción, intención, información, actuación, audio, corte |
| **Productor de impacto** (`impacto.md`, borrador) | ¿Por qué el público no desliza el dedo? | Propuestas de gancho, ritmo, espectacularidad de cámara y final, como alertas «Impacto:». El Director decide |
| **Director de fotografía** (`director_fotografia.md`) | ¿Cómo se ve? | Cámara, lente, luz, zona segura 9:16 |
| **Continuista** (`continuista.md`) | ¿Qué debe seguir igual de un plano al siguiente? | Hechos de continuidad; entrada, salida y eje de cada plano |
| **Asistente de dirección** (`asistente_direccion.md`) | ¿Qué necesitamos, con qué motor, en qué orden y cuánto cuesta? | Assets, referencias, motor, método, costo, grupos de generación |
| **Prompter** (`prompter.md`) | ¿Cómo se le pide al modelo? | Bloque `prompts` de cada plano, **compilado** desde los campos de los demás roles con las recetas de `produccion/compilador_prompts.md` |
| **Pipeline** | ¿Qué se generó y en qué estado está? | Tomas, toma elegida y estado. Ejecuta con los MCP de fal y Kling (o el orquestador) y guarda en `renders/` |
| **Control de calidad** (`control_calidad.md`) | ¿La toma cumple lo que se pidió? | Revisión de cada toma, con una sola corrección |
| **Montajista** (`montajista.md`) | ¿Cómo se ensamblan las tomas en 75–90 s? | `produccion/montaje/capNN.md`: línea de tiempo, cortes, sonido, textos y tareas de post. Cristian también edita; el plan es su punto de partida |

## Ciclo de un capítulo
1. **Showrunner:** define la decisión del capítulo según la votación anterior.
2. **Guionista:** escribe la v1. **Abogado del diablo:** revisa. El guionista corrige hasta que Cristian aprueba.
3. **Director → Productor de impacto → Director de fotografía → Continuista → Asistente de dirección:** arman el guion técnico, en ese orden. El Director acepta o descarta las propuestas de impacto antes de que pasen a fotografía.
4. **Cristian aprueba el guion técnico.**
5. **Prompter:** escribe los prompts. **Pipeline:** genera los keyframes. **Control de calidad:** filtra. **Cristian elige** un keyframe por plano.
6. **Pipeline:** genera las tomas de video. **Control de calidad:** filtra. **Cristian elige** la toma de cada plano.
7. **Montajista:** plan de montaje. Upscale, audio y edición (Cristian y el plan). **Se publica** y se abre la votación.

El detalle de cada paso está en `produccion/pipeline.md`.
