# Pipeline de producción

El proceso es automático desde que el guion y los assets están aprobados. La creatividad está antes (guion, casting visual, hojas de personaje) y en las aprobaciones. Qué motor se usa para cada paso está en `produccion/motores.md`.

```
Guion aprobado (guion/capNN)          + Assets bloqueados (Weavy: personajes, locaciones, props)
  │
  ├─ Director ................ desglose dramático: planos, intención, qué sabe el público
  ├─ Director de fotografía .. cámara, lente y luz de cada plano
  ├─ Continuista ............. estado de entrada y salida de cada plano
  ├─ Asistente de dirección .. assets por plano, orden de generación, costo
  │     → produccion/shotlists/capNN.yaml  (guion técnico)
  │
  ◆ APROBACIÓN 1 · Cristian aprueba el guion técnico
  │
  ├─ Prompter ................ compila el prompt de keyframe y de video de cada plano (compilador_prompts.md)
  ├─ Pipeline ................ keyframes (fal · Nano Banana Pro), 2–4 variantes por plano
  ├─ Control de calidad ...... descarta las que no cumplen y propone una corrección por vez
  │
  ◆ APROBACIÓN 2 · Cristian elige un keyframe por plano
  │
  ├─ Control de calidad ...... revisión previa de cada bloque: prompt, keyframes y referencias sin huecos
  ├─ Pipeline ................ tomas de video (H3 Max para explorar, Kling para planos clave)
  ├─ Control de calidad ...... revisa identidad, continuidad y reglas
  │
  ◆ APROBACIÓN 3 · Cristian elige la toma de cada plano
  │
  ├─ Montajista .............. plan de montaje (produccion/montaje/capNN.md)
  ├─ Upscale (Comfy Cloud) → Audio (ElevenLabs + SFX + Suno) → Edición (Cristian, Resolve) + After Effects
  │
  ◆ APROBACIÓN 4 · corte final → se publica y se abre la votación
```

## Reglas del proceso
- **Se define antes de generar.** El objetivo es que cada bloque salga bien en una o dos tomas. Si dos tomas fallan, no se genera una tercera: el bloque vuelve a la revisión previa con lo que faltaba definir.
- **Nada pasa a video sin keyframe aprobado ni revisión previa `lista`.** El video es lo caro.
- **Una corrección por vez.** Si una toma falla, se cambia una variable (luz, encuadre, referencia, seed) y se vuelve a generar.
- **Todo queda en el guion técnico:** qué motor, qué seed, qué toma se eligió y por qué. Si no está escrito, no se puede repetir.
- **Los archivos generados no van a git.** Se guardan en `renders/capNN/<id_plano>/` (ignorado) y el YAML guarda la URL y el nombre.

## Guion técnico
Formato en `produccion/formato_guion_tecnico.md`. Un archivo por capítulo: `produccion/shotlists/capNN.yaml`.

**Estados de un plano:** `pendiente` → `prompt ok` → `keyframe ok` → `video ok` → `montado`.

## Assets reutilizables
- Weavy: flujo «VAGÓN 7 — Assets base» (`app.weavy.ai/flow/WI36yqNHek7HlgrUH3IFBP`). Tiene locaciones del tren, infectados y props.
- Se reutilizan la librea del tren, el bosque, el interior del vagón y el grupo de infectados.

## Cadencia objetivo
- Votación abierta 48 h.
- Producción del capítulo ganador en 3–4 días.
- Un capítulo por semana.

## Por construir
- **Orquestador (`tools/orquestador`):** script que lea el YAML y mande cada plano al motor que indica, guarde los resultados en `renders/` y actualice el estado. Mientras no exista, el agente Pipeline trabaja con los MCP de fal y Kling.
- **Adaptador de Weavy:** el `weavy_builder` pendiente pasa a ser un adaptador más que lee el mismo YAML.
