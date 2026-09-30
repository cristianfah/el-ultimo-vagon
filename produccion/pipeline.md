# Pipeline de producción

```
Guion aprobado (guion/capNN)
  → Shot list (produccion/shotlists/capNN.md): un plano por fila
  → Prompts por plano (produccion/prompts/capNN/NN.md): plantilla de rodaje y prompt de Kling
  → Weavy: keyframes 9:16 (GPT Image 2.5 o Nano Banana Pro con referencias de personajes y locaciones)
  → Kling 4.0: image-to-video con elements de personajes (identidad y voz)
  → Audio: ElevenLabs (voces fijas por personaje) + SFX + Suno
  → Post: Resolve (montaje y color) + After Effects (sangre, subtítulos, tarjetas)
```

## Formato de shot list (una fila por plano)

| Campo | Ejemplo |
|---|---|
| id | `c01_p07` |
| tiempo | `0:19–0:23` |
| plano | PP / PM / general / inserto / POV |
| acción | qué pasa, en una línea |
| audio y diálogo | quién dice qué |
| personajes | martina, tomas… |
| locación | `loc_vagon_rojo` |
| método Kling | FF (first frame) · FF+E (con elements) · FL (first y last frame) |
| estado | pendiente / keyframe ok / video ok / montado |

## Assets reutilizables
- Weavy: flujo «VAGÓN 7 — Assets base» (`app.weavy.ai/flow/WI36yqNHek7HlgrUH3IFBP`). Tiene locaciones del tren, infectados y props.
- Se reutilizan la librea del tren, el bosque, el interior del vagón y el grupo de infectados.

## Cadencia objetivo
- Votación abierta 48 h.
- Producción del capítulo ganador en 3–4 días.
- Un capítulo por semana.

Para lograrlo, los flujos de Weavy tienen que estar **plantillados por plano**.
