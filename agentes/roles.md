# Roles de agentes

Un sistema de varios agentes, todos con el mismo contexto (`AGENTS.md` y `biblia/`). Cada uno tiene una responsabilidad y un lugar donde deja lo que produce.

| Rol | Responsabilidad | Lee | Escribe |
|---|---|---|---|
| **Showrunner** | Coherencia de la temporada, arco, qué se decide en cada capítulo, que haya debate | `biblia/` y todos los guiones | `biblia/arco_temporada.md`, `biblia/decisiones.md` |
| **Guionista** | Escribe y reescribe capítulos y ramas. Diálogo con la voz de cada personaje | `biblia/`, el capítulo anterior | `guion/capNN/capNN_vX.md` |
| **Abogado del diablo** | Busca agujeros de lógica («¿por qué no hacen lo obvio?»), reglas violadas y opciones de votación desbalanceadas | Guion y `biblia/reglas_del_mundo.md` | Comentarios al final del guion, sección «Revisión» |
| **Director de arte** | Casting visual, vestuario, sets y props. Que cada asset sea consistente, original y se lea en un teléfono | `biblia/personajes.md`, guion vigente y `direccion_arte/` | `direccion_arte/personajes/`, `direccion_arte/sets/`, `produccion/assets/` |
| **Director y DP** | Convierte el guion en shot list, con encuadre, lente, luz y método de Kling | Guion y `direccion_arte/` | `produccion/shotlists/capNN.md` |
| **Prompter** | Escribe los prompts de fotograma (plantilla de rodaje) y los de Kling por plano | Shot list, `produccion/plantilla_prompt_rodaje.md`, `produccion/kling/` | `produccion/prompts/capNN/` |
| **Pipeline** | Arma el JSON de Weavy desde los prompts y lleva el estado de cada plano | Prompts y `produccion/weavy/` | JSON de Weavy y columna de estado del shot list |

## Ciclo de un capítulo
1. **Showrunner:** define la decisión del capítulo según la votación anterior.
2. **Guionista:** escribe la v1.
3. **Abogado del diablo:** revisa. El guionista corrige hasta que Cristian aprueba.
4. **Director y DP:** arma el shot list. **Prompter:** escribe los prompts. **Pipeline:** arma el JSON de Weavy.
5. Se generan las imágenes y los videos, y después el montaje.
6. **Se publica** y se abre la votación.
