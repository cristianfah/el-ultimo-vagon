# Compilador de prompts: del guion técnico al prompt de cada modelo

Los prompts **no se escriben desde cero**. Se compilan a partir de los campos que ya llenaron los demás roles, con una receta por modelo. Así todos los agentes colaboran en cada prompt, y el prompt final es corto y claro para el modelo.

```
Director ── acción, actuación, audio, texto ─┐
D. de fotografía ── cámara, lente, luz ──────┤
Continuista ── hechos, estado de entrada ────┼──► Prompter (receta del modelo) ──► prompt del plano
Asistente ── referencias, motor, método ─────┘                                        │
                                                                                      ▼
                                                                          Control de calidad revisa
```

**Regla de oro:** un prompt de video describe **una acción, un movimiento de cámara y un sonido**. Todo lo demás (luz, cara, vestuario, encuadre) ya está en el keyframe y se protege con una frase de «se mantiene».

## De qué campo sale cada parte

| Parte del prompt | Sale de | Qué se hace con el campo |
|---|---|---|
| Acción física | `accion` + `actuacion` | Verbos concretos, la acción primero. Sin palabras de emoción |
| Cámara | `camara.movimiento` | Un solo movimiento, con anclaje temporal |
| Sonido y diálogo | `audio` | Ambiente + efectos; el diálogo entre comillas con dirección de tono |
| Lo que no cambia | `continuidad.hechos` marcados `fragil` + `luz` | Se convierten en la frase «se mantiene» |
| Referencias | `referencias` | Se declara el rol de cada una al inicio |
| Parámetros | `motor_video`, `duracion_s`, `metodo_video` | Van en `params`, no en el texto |

Los hechos de continuidad que **no** son frágiles no entran al prompt de video: ya están en el keyframe. Meterlos todos alarga el prompt y baja la adherencia.

## Recetas por modelo

### Keyframe · Nano Banana Pro (plantilla de rodaje)
Los siete bloques de `plantilla_prompt_rodaje.md`, en inglés y en este orden de fuentes:

| Bloque | Campos |
|---|---|
| FILM STILL | `referencias` (rol de cada imagen: «Image 1 is …») |
| MOMENT | `accion` (un fotograma, un segundo antes o después de algo) + hechos de `entrada` |
| COMPOSITION | `tipo_plano`, `camara.altura`, `camara.posicion`, `zona_segura_9x16` |
| LENS | `lente` |
| LIGHT | `luz.fuentes` (cada una con posición, temperatura e intensidad) + `luz.contraste` |
| TEXTURE | hechos de vestuario, sangre, agua y suciedad: dónde sí y dónde no |
| FINISH | fijo del proyecto (ver plantilla) |

Máximo 5 personas en cuadro. Sin texto en la imagen: tarjetas y mensajes de celular se rehacen en post si no salen legibles.

### Video · MiniMax H3 Max (image-to-video)
Estructura, en inglés y en este orden. Entre 60 y 110 palabras:

```
[Action, physical verbs first, one beat]. [Camera: one movement, or "locked-off"].
Keep the framing, lighting, faces and wardrobe exactly as in the still. [Fragile facts if any].
Sound: [ambience], [2-3 specific effects], [dialogue in quotes with delivery direction if any]. No music. No on-screen text.
```

Reglas propias de este modelo:
- Sonido concreto («knuckles on glass, rain, train rumble»), nunca «tense atmosphere».
- El diálogo va en comillas con la dirección de tono («quiet, barely audible»).
- Cerrar con «No music. No on-screen text.» (la música y los textos se ponen en post).
- Si el plano es muy corto, pedir la acción en los primeros 2 s del clip de 5 s, para que el montaje corte ahí.
- `prompt_expansion_mode`: **`disabled`**. En la prueba del 2026-09-30, `balanced` reescribió el prompt e invirtió la acción (ver `investigacion_referencias.md`).
- Secuencia multi-beat (solo si el grupo lo pide): `0.0 to 2.0s: … CUT. 2.0 to 4.0s: …`, describiendo a cada personaje idéntico en cada beat.

### Video · Kling 4.0 / 4.0 Flash (image-to-video)
Reglas completas en `kling/kling_4_0_resumen.md`. Estructura:

```
@Image1 is the first frame. [@Element1 is <character>.]
[Camera movement over time]. [Physical action first]. [Scene change, if any]. [Ambient sound].
[Character: Name, tone, Chilean Spanish accent]: "line".
From the first frame to the last frame, [what must stay constant].
```
`negative_prompt`: negaciones por eje (*no tilt, no yaw, no pan, no orbit, no arc, no zoom*, según lo que el plano no debe hacer). Torso: «slim build, consistent proportions». No describir el tono de una voz ya vinculada.

### Video · H3 Max, bloque multi-beat (`reference-to-video`)
Un prompt por **bloque**, con un beat por plano. Entre 90 y 160 palabras:

```
Image 1 is <character A>. Image 2 is <character B>. Image 3 is <location and light>. Keep every person and the location consistent with their references in every beat.
0.0 to 3.0s: [shot type, camera, one physical action, dialogue in quotes with delivery]. CUT.
3.0 to 5.0s: [shot type, camera, one physical action]. CUT.
5.0 to 8.0s: ...
Sound: [continuous ambience], [effects per beat]. No music. No on-screen text.
```
- Los beats suman la `duracion_s` del bloque; el último beat puede sobrar 1 s para recortar.
- Cada personaje se describe **igual en cada beat** (misma frase de vestuario).
- Un beat de menos de 2 s se pide como acción única; si el modelo lo estira, se recorta en el montaje.
- Con `end_image_url` o `target_audio_url` (ruta `image-to-video`) se controla el final o la voz.
- **Versión final:** todo plano con diálogo se genera con su audio de ElevenLabs (`target_audio_url` o `Audio 1`) para el lipsync. En pruebas se omite.

## Reglas de actuación (todas las recetas)
- Se describe lo que **hace el cuerpo**: dónde mira, qué mano se mueve, cuánto dura la quietud.
- Prohibido: «aterrada», «furioso», «nervioso». Permitido: «no parpadea», «traga saliva», «la mirada no sale de la puerta».
- Un plano de reacción es **quietud**; el modelo sobreactúa si se le da margen.
- Los extras no actúan: están.

## Reglas de luz en los prompts de video
La luz no se reescribe: se protege. El keyframe ya la trae; el prompt solo dice qué se mantiene y qué cambia (por ejemplo, «the red emergency light flickers once»). Si el plano necesita un cambio de luz, es un evento con fuente visible.

## Formato de salida en el guion técnico
El Prompter escribe `prompts` en cada **plano** (keyframe) y, en cada **bloque** de `bloques`, el prompt de video del bloque:

```yaml
prompts:
  keyframe:
    motor: nano_banana_pro
    params: { aspect_ratio: "9:16", resolution: "2K", num_images: 3 }
    referencias: ["Image 1 = martina (sheet)", "Image 2 = loc_ultimo_vagon"]
    texto: |
      (los siete bloques)
  video:                        # solo en planos de estrategia B; en A y C el prompt de video vive en el bloque
    motor: h3_max
    params: { duration: 5, resolution: "480P", prompt_expansion_mode: balanced }
    texto: |
      (la receta del modelo)
    negativo: null              # solo Kling
```
En `bloques[].prompt_video` va el mismo esquema (`motor`, `params`, `texto`, `negativo`) para los bloques multi-beat y encadenados.
Cada prompt tiene que poder pegarse tal cual en fal o Kling. Los prompts nunca se entregan como fragmentos.

## Prueba de sencillez
Antes de entregar, el Prompter comprueba: ¿tiene una sola acción?, ¿un solo movimiento de cámara?, ¿el sonido es concreto?, ¿cabe en el largo de la receta? Si no, lo simplifica o propone dividir el plano al Director.
