# AGENTS.md — Contexto maestro del proyecto

Todo agente que trabaje en este repo (Cursor, Claude, cualquier otro) lee este archivo primero.

## Qué es este proyecto

**EL ÚLTIMO VAGÓN** es una microserie vertical (9:16) de terror y acción con zombies, hecha con IA, para Instagram Reels y TikTok. La produce Equals AI Studio / fahren.tv, con Cristian Fahrenkrog como director creativo.

**El formato:** capítulos de 75–90 s donde **el público decide**. Cada capítulo termina en una decisión moral y el público responde una encuesta «Si fueras ___, ¿qué harías?» (Cristian la maneja en las plataformas). En la temporada 1 las encuestas no cambian la historia; la decisión mayor va al final de temporada (`biblia/votaciones.md`).

**Referentes de formato:** Love Island (entradas y salidas de personajes votadas por el público, triángulos amorosos, traiciones) y Fruit Love Island (serie hecha con IA en TikTok en 2026, más de 300 millones de vistas, episodios cortos y drama de reality). También los juegos *60 Seconds!* y *No, I'm Not a Human*: decidir a quién dejar entrar y cómo sobrevivir. Se toma la mecánica, nunca sus elementos puntuales.

**El motor de la serie:** el escenario es extremo (zombies en un tren), pero el conflicto es cotidiano (celos, culpa, lealtad, qué harías tú). Si una escena no genera debate entre personas reales, no sirve.

## Estado actual (actualizar con cada decisión)

- **Biblia v2 (18-oct-2026):** un tren nocturno lleva un virus hacia la capital; la hija del Presidente (Martina) lo liberó sin saberlo, obligada por una secta; el gobierno puede bombardear el tren; el grupo se atrinchera en el último vagón. Detrás de la secta hay una IA (solo para guionistas, `biblia/conspiracion.md`). La biblia anterior está en `archivo/biblia_v1/`.
- **Temporada 1:** 8 capítulos escritos en línea recta, con encuestas de «Si fueras ___, ¿qué harías?» que no cambian la historia. Escaleta en `biblia/escaleta_t1.md`; votaciones en `biblia/votaciones.md`.
- **Guion vigente:** `guion/cap01/cap01_v9.md` (**VIGENTE**), escrito en 8 bloques de generación. La v8 y anteriores quedan como históricas y pertenecen a la biblia v1.
- **Producción (método nuevo):** bloques de generación con paquete de referencias, animatic en H3 Max a 480p (bots de Cursor por fal), aprobación de Cristian sobre el animatic, versión final en **Kling 4.0** y **Seedance 2.5** como respaldo. Ver `produccion/metodo.md`. Los prompts se escriben con `produccion/prompting/guia_direccion_video.md` y la skill `.cursor/skills/director-de-prompts/`.
- **Tarea en curso:** animatic del capítulo 1. Plan y reparto de tareas en `produccion/pruebas/cap01_animatic/plan.md`.
- **Obsoleto:** `produccion/shotlists/cap01.yaml` y las pruebas `cap01_montaje_v1`, `cap01_montaje_v2` y `cap01_cold_open` corresponden al guion anterior (v3–v8). Se consultan por lo aprendido, no se producen.
- **Assets v1 aprobados (2026-10-01):** planchas F01–F12, cuadros de look, vistas técnicas, 4 props, referencias y hojas de los 6 personajes y la pareja extra, estado de Diego y keyframes KF01–KF03. URLs en `produccion/assets/aprobados_v1.md`, archivos en `imagenes/04_aprobados` (Drive). Los cambios posteriores se hacen como v2.
- **Imágenes:** viven en la carpeta privada de Drive y se suben con `tools/drive_sync.py`. Las ediciones se corren con `tools/fal_gen.py`. Ninguna imagen se propone para aprobación sin pasar antes por la revisión de continuidad de los agentes.
- **Proyecto anterior archivado:** VAGÓN 7, de agentes y traición, en `archivo/vagon7/`. Su dirección de arte y sus assets se reutilizan.

## Mapa del repo

| Carpeta | Contenido |
|---|---|
| `biblia/` | Premisa, reglas del mundo, conspiración (solo guionistas), personajes, arco, escaleta de la temporada 1, votaciones, decisiones y preguntas abiertas. **Es la fuente de verdad.** |
| `guion/capNN/` | Guiones por capítulo, versionados (`capNN_vX.md`). Desde la v9, escritos en bloques de generación con fichas de producción |
| `direccion_arte/` | Look, guion de color, reglas contra la estética genérica de IA, referencias visuales |
| `produccion/` | Método vigente (`metodo.md`), motores, guía de dirección para prompts (`prompting/`), sistema de actuación, assets aprobados, guías de Kling 4.0 y H3, y las pruebas de cada tanda (`pruebas/`) |
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
- **fal.ai (API y MCP):** MiniMax H3 Max para el animatic (480p) y Nano Banana Pro / GPT Image 2.5 para assets, estados y fotogramas guía.
- **Kling 4.0:** motor final de todos los bloques, por el MCP oficial con la suscripción propia (salió el 16-oct-2026); ver `produccion/kling/` y `.cursor/skills/director-de-prompts/references/kling.md`.
- **Seedance 2.5:** respaldo para el bloque que falle dos veces en Kling. Es bastante más caro: siempre con OK de Cristian.
- **Comfy Cloud (API):** upscale final, correcciones puntuales y nodos pagados con créditos de Comfy.
- **ElevenLabs:** voces.
- **Suno:** música.
- **DaVinci Resolve y After Effects:** post.
