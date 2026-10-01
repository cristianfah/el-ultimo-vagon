# AGENTS.md — Contexto maestro del proyecto

Todo agente que trabaje en este repo (Cursor, Claude, cualquier otro) lee este archivo primero.

## Qué es este proyecto

**EL ÚLTIMO VAGÓN** es una microserie vertical (9:16) de terror y acción con zombies, hecha con IA, para Instagram Reels y TikTok. La produce Equals AI Studio / fahren.tv, con Cristian Fahrenkrog como director creativo.

**El formato:** capítulos de 75–90 s donde **el público decide**. Cada capítulo termina en una decisión moral y el público vota con una encuesta (Cristian la maneja en las plataformas). El capítulo siguiente se produce según el resultado.

**Referentes de formato:** Love Island (entradas y salidas de personajes votadas por el público, triángulos amorosos, traiciones) y Fruit Love Island (serie hecha con IA en TikTok en 2026, más de 300 millones de vistas, episodios cortos y drama de reality). También los juegos *60 Seconds!* y *No, I'm Not a Human*: decidir a quién dejar entrar y cómo sobrevivir. Se toma la mecánica, nunca sus elementos puntuales.

**El motor de la serie:** el escenario es extremo (zombies en un tren), pero el conflicto es cotidiano (celos, culpa, lealtad, qué harías tú). Si una escena no genera debate entre personas reales, no sirve.

## Estado actual (actualizar con cada decisión)

- **Premisa en desarrollo:** seis pasajeros encerrados en el último vagón de un tren nocturno el primer día de un brote. Hay un triángulo amoroso en el centro (Martina, Tomás y Diego).
- **Guion vigente:** `guion/cap01/cap01_v3.md`.
- **Decisión pendiente de aplicar (v4):**
  - Opción 1 de reglas: es el primer día, nadie conoce las reglas, los personajes solo saben lo que vieron y las deducciones pueden estar mal.
  - El tren se detiene más adelante (capítulo 2 o 3) porque alguien tira el freno de emergencia.
  - Ver `biblia/decisiones.md`.
- **Assets en preparación:** plan en `produccion/assets/plan_assets_v1.md`, fichas de personajes en `direccion_arte/personajes/` y set vigente en `direccion_arte/sets/set_ultimo_vagon_v2.md`. **Assets v1 aprobados por Cristian (2026-10-01):** las doce planchas finales del set (F01 a F12), los cuadros de look, las vistas técnicas, los cuatro props, las referencias y hojas de los seis personajes y la pareja extra, el estado de Diego y los keyframes KF01 a KF03. Las URLs están en `produccion/assets/aprobados_v1.md` y los archivos en `imagenes/04_aprobados` (Drive). Cualquier cambio se hace como v2.
- **Imágenes:** viven en la carpeta privada de Drive y se suben con `tools/drive_sync.py`. Las ediciones se corren con `tools/fal_gen.py`. Ninguna imagen se propone para aprobación sin pasar antes por la revisión de continuidad de los agentes.
- **Proyecto anterior archivado:** VAGÓN 7, de agentes y traición, en `archivo/vagon7/`. Su dirección de arte y sus assets se reutilizan.

## Mapa del repo

| Carpeta | Contenido |
|---|---|
| `biblia/` | Premisa, personajes, reglas del mundo, arco de temporada, decisiones y preguntas abiertas. **Es la fuente de verdad.** |
| `guion/capNN/` | Guiones por capítulo, versionados (`capNN_vX.md`). Las ramas del capítulo siguiente van al final de cada guion |
| `direccion_arte/` | Look, guion de color, reglas contra la estética genérica de IA, referencias visuales |
| `produccion/` | Pipeline, plantilla de prompt de rodaje, guía de Weavy, guía de Kling 4.0, shot lists y prompts por plano |
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

- **Midjourney 8.2:** solo exploración de arte.
- **Weavy (Figma Weave):** imágenes finales. Hay que capturar la estructura de los nodos del canvas y armar los flujos como JSON para pegarlos; ver `produccion/weavy/`.
- **GPT Image 2.5 y Nano Banana Pro:** los dos están disponibles en Weavy.
- **Kling 4.0:** video. Todavía no está en Weavy; ver `produccion/kling/`.
- **ElevenLabs:** voces.
- **Suno:** música.
- **DaVinci Resolve y After Effects:** post.
