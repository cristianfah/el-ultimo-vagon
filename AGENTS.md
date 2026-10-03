# AGENTS.md — Contexto maestro del proyecto

Todo agente que trabaje en este repo (Cursor, Claude, cualquier otro) lee este archivo primero.

## Qué es este proyecto

**EL ÚLTIMO VAGÓN** es una microserie vertical (9:16) de terror y acción con zombies, hecha con IA, para Instagram Reels y TikTok. La produce Equals AI Studio / fahren.tv, con Cristian Fahrenkrog como director creativo.

**El formato:** capítulos de 75–90 s donde **el público decide**. Cada capítulo termina en una decisión moral y el público vota con una encuesta (Cristian la maneja en las plataformas). El capítulo siguiente se produce según el resultado.

**Referentes de formato:** Love Island (entradas y salidas de personajes votadas por el público, triángulos amorosos, traiciones) y Fruit Love Island (serie hecha con IA en TikTok en 2026, más de 300 millones de vistas, episodios cortos y drama de reality). También los juegos *60 Seconds!* y *No, I'm Not a Human*: decidir a quién dejar entrar y cómo sobrevivir. Se toma la mecánica, nunca sus elementos puntuales.

**El motor de la serie:** el escenario es extremo (zombies en un tren), pero el conflicto es cotidiano (celos, culpa, lealtad, qué harías tú). Si una escena no genera debate entre personas reales, no sirve.

## Estado actual (actualizar con cada decisión)

- **Premisa en desarrollo:** cinco se encierran en el último vagón el primer día del brote; el sexto (Diego) pide entrar. Triángulo en el centro (Martina, Tomás y Diego).
- **Guion vigente:** `guion/cap01/cap01_v7.md` (**FINAL**).
- **Aplicado hasta v7 FINAL:** opción 1; conteo 5+Diego; Carmen atiende; Diego ambiguo; Hugo corto; Iván «no hay cómo saber»; gesto final de Martina; continuidad del «Diego…» cold open = escena 4; semilla del corte fuera del guion.
- **Pendiente de temporada:** el tren se detiene más adelante (cap. 2 o 3) por el freno de emergencia. Ver `biblia/decisiones.md`.
- **Producción:** equipo técnico de agentes definido en `agentes/roles.md`. El guion técnico del capítulo 1 está en prueba en `produccion/shotlists/cap01.yaml` (cold open y escena 1), todavía desglosado desde la v3 (pendiente de actualizar a v7; ver deuda en `produccion/pruebas/cap01_montaje_v2/plan.md`).
- **Producción:** la prueba de montaje v2 del capítulo 1 tiene keyframes y video tanda 1 generados (en Drive); falta el armado. Plan en `produccion/pruebas/cap01_montaje_v2/plan.md`. Los prompts se escriben con la skill `.cursor/skills/director-de-prompts/`.
- **Assets v1 aprobados (2026-10-01):** planchas F01–F12, cuadros de look, vistas técnicas, 4 props, referencias y hojas de los 6 personajes y la pareja extra, estado de Diego y keyframes KF01–KF03. URLs en `produccion/assets/aprobados_v1.md`, archivos en `imagenes/04_aprobados` (Drive). Los cambios posteriores se hacen como v2.
- **Imágenes:** viven en la carpeta privada de Drive y se suben con `tools/drive_sync.py`. Las ediciones se corren con `tools/fal_gen.py`. Ninguna imagen se propone para aprobación sin pasar antes por la revisión de continuidad de los agentes.
- **Proyecto anterior archivado:** VAGÓN 7, de agentes y traición, en `archivo/vagon7/`. Su dirección de arte y sus assets se reutilizan.

## Mapa del repo

| Carpeta | Contenido |
|---|---|
| `biblia/` | Premisa, personajes, reglas del mundo, arco de temporada, decisiones y preguntas abiertas. **Es la fuente de verdad.** |
| `guion/capNN/` | Guiones por capítulo, versionados (`capNN_vX.md`). Las ramas del capítulo siguiente van al final de cada guion |
| `direccion_arte/` | Look, guion de color, reglas contra la estética genérica de IA, referencias visuales |
| `produccion/` | Pipeline, motores de generación, formato del guion técnico, plantilla de prompt de rodaje, guías de Weavy y Kling 4.0, guiones técnicos (`shotlists/`) y prompts por plano |
| `agentes/` | Roles y responsabilidades de cada agente |
| `archivo/` | Versiones y proyectos descartados. Solo se consultan, nunca se editan |

## Reglas para todos los agentes

1. **Idioma:** documentos y notas en español neutro (no rioplatense). Los prompts para modelos van en inglés, dentro de bloques de código.
2. **Los prompts siempre completos** y listos para pegar, nunca solo el fragmento modificado.
3. **La biblia manda.** Si un guion contradice `biblia/`, se corrige el guion o se propone un cambio en `biblia/decisiones.md`. Nunca se contradice en silencio.
4. **Cada cambio de historia queda registrado** en `biblia/decisiones.md`, con fecha y motivo.
5. **Nada de propiedad intelectual ajena:** ni personajes, logos, insignias o nombres de franquicias. Todo es original.
6. **Gore:** se corta en el impacto y la sangre es oscura. La violencia fuerte va en el sonido y fuera de campo. En prompts de imagen se evitan las palabras *blood* y *gore* (se usa *dark red-black stains*, *dark splatter*).
7. **Versionado:** no se sobreescribe una versión aprobada. Se crea `vN+1`.
8. **Antes de escribir diálogo,** leer `biblia/personajes.md`: cada personaje tiene su voz y su postura.

## Herramientas del pipeline

Qué motor se usa para qué está en `produccion/motores.md`.

- **Midjourney 8.2:** solo exploración de arte.
- **Weavy (Figma Weave):** solo creación de assets (hojas de personaje, locaciones, props). Los flujos se arman como JSON para pegarlos; ver `produccion/weavy/`.
- **fal.ai (API y MCP):** motor base de tomas. MiniMax H3 Max para video y Nano Banana Pro para keyframes.
- **Kling 4.0:** video de planos clave, por el MCP oficial con la suscripción propia; ver `produccion/kling/`.
- **Comfy Cloud (API):** upscale final, correcciones puntuales y nodos pagados con créditos de Comfy.
- **ElevenLabs:** voces.
- **Suno:** música.
- **DaVinci Resolve y After Effects:** post.
