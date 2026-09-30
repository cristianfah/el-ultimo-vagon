# Kling 4.0: resumen operativo

La versión completa está en el proyecto Fahren.tv (`Kling_VIDEO_4_0_Guia_Prompting_Avanzado.md`). Conviene copiarla aquí.

**Disponibilidad:**
- Kling 4.0 sale oficialmente en octubre de 2026. La versión Flash está en acceso anticipado desde el 28 de septiembre.
- **Todavía no está en Weavy**, que hoy tiene Kling 3, con referencias de personaje, y O1.

## Especificaciones

| Parámetro | Kling 4.0 |
|---|---|
| Duración | 3–30 s |
| Resolución | 720p / 1080p / 4K |
| Aspect ratio | 21:9 / 16:9 / 1:1 / **9:16** / Auto |
| Modos | Texto a video, imagen a video, primer y último fotograma, varios keyframes (hasta 10), Omni Reference, edición de video |
| Referencias | Hasta 10 imágenes, 5 videos y 7 personajes guardados (elements); 15 en total |
| Audio | Estéreo, solo la voz como referencia, español incluido |
| Prompt | Hasta 8.000 tokens. Más corto suele ser mejor |

## Reglas del estudio
- **Imagen a video:** describir solo la cámara y el comportamiento del sujeto. Nunca redescribir la imagen.
- **Anclaje temporal:** «from the first frame to the last frame», «held constant the whole time».
- **Negaciones por eje** en el negative prompt: *no tilt, no yaw, no pan, no orbit, no arc, no zoom*.
- **Kling infla el volumen del torso:** indicar «slim build, consistent proportions».
- **Omitir antes que negar** en el prompt positivo.
- **Declarar el rol de cada referencia** al inicio: `@Image1 is…`, `@Element1 is…`.
- **Diálogo:** `[Character: Nombre, tono, acento]: "línea"`. La acción física va antes del diálogo. El acento se indica explícito, por ejemplo *Chilean Spanish accent*.
- **Actuación:** quietud y mirada. Nada de palabras de emoción, porque el modelo sobreactúa.
- **Voz vinculada al personaje:** no describir el tono.
- Con `prefer_multi_shots` en la API, confirmar si hay que ponerlo en false.

## Plantillas

**Imagen a video**
```
[Camera movement over time]. [Subject behavior, physical action first]. [Scene evolution / environmental change]. [Ambient sound]. From the first frame to the last frame, [what must stay constant].
```

**Diálogo**
```
[Setting + ambient sound]. [Character A: Name, tone, Chilean Spanish accent] does [physical action]. [Character A]: "line". Immediately, [Character B] [reaction]. [Character B: Name, tone]: "line". Silence. The camera slowly pushes in on [face].
```

## Validar en las primeras pruebas
- [ ] Si acepta primer fotograma y personajes guardados (elements) en la misma generación.
- [ ] Si existe el campo de negative prompt.
- [ ] Si distingue acento chileno de español neutro.
- [ ] Una toma de 30 s contra 2–3 clips cortos empalmados.
- [ ] Si llega a Weavy o al MCP de Kling.
