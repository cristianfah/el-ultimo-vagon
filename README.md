# EL ÚLTIMO VAGÓN

Microserie vertical de zombies donde el público decide. Equals AI Studio · fahren.tv.

**Para empezar:** lee `AGENTS.md`. Ahí están el contexto completo, el estado actual y el mapa del repo.

## Cómo usar este repo con Cursor

1. Abre la carpeta en Cursor. Las reglas de `.cursor/rules/` se cargan solas y `AGENTS.md` da el contexto general.
2. **Para discutir el guion:** abre `guion/cap01/cap01_v9.md` y pídele al agente que actúe como el rol de `agentes/guionista.md` o `agentes/showrunner.md`. La historia está en `biblia/` (biblia v2, 18-oct-2026).
3. **Para producir:** el método está en `produccion/metodo.md` (bloques de generación con referencias, animatic en H3 Max, versión final en Kling 4.0) y la guía de prompts en `produccion/prompting/guia_direccion_video.md`. El plan de trabajo vigente está en `produccion/pruebas/cap01_animatic/plan.md`.
4. **Cada decisión va a `biblia/decisiones.md`.** Así cualquier agente (o persona) que llegue después entiende por qué la historia es como es.

## Subir a GitHub

```bash
cd el-ultimo-vagon
git remote add origin git@github.com:<tu-usuario>/el-ultimo-vagon.git
git push -u origin main
```
