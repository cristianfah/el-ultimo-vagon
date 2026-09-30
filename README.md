# EL ÚLTIMO VAGÓN

Microserie vertical de zombies donde el público decide. Equals AI Studio · fahren.tv.

**Para empezar:** lee `AGENTS.md`. Ahí están el contexto completo, el estado actual y el mapa del repo.

## Cómo usar este repo con Cursor

1. Abre la carpeta en Cursor. Las reglas de `.cursor/rules/` se cargan solas y `AGENTS.md` da el contexto general.
2. **Para discutir el guion:** abre `guion/cap01/cap01_v3.md` y pídele al agente que actúe como el rol de `agentes/guionista.md` o `agentes/showrunner.md`.
3. **Para producir:** a partir de un guion aprobado, el equipo técnico (`agentes/roles.md`) arma el guion técnico en `produccion/shotlists/capNN.yaml` y los prompts por plano en `produccion/prompts/`, con la plantilla de rodaje. El proceso completo está en `produccion/pipeline.md`.
4. **Cada decisión va a `biblia/decisiones.md`.** Así cualquier agente (o persona) que llegue después entiende por qué la historia es como es.

## Subir a GitHub

```bash
cd el-ultimo-vagon
git remote add origin git@github.com:<tu-usuario>/el-ultimo-vagon.git
git push -u origin main
```
