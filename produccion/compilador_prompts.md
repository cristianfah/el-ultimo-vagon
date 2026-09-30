# Compilador de prompts: del guion técnico al prompt de cada modelo

Los prompts **no se escriben desde cero**. Se compilan a partir de los campos que ya llenaron los demás roles, con la skill `.cursor/skills/director-de-prompts/` y el formato oficial de cada modelo. Así todos los agentes colaboran en cada prompt, y **todo lo que definieron llega al modelo**.

```
Director ── acción, actuación, audio, texto ─┐
D. de fotografía ── cámara, lente, luz ──────┤
Continuista ── hechos, estado de entrada ────┼──► Prompter (receta del modelo) ──► prompt del plano
Asistente ── referencias, motor, método ─────┘                                        │
                                                                                      ▼
                                                                          Control de calidad revisa
```

**Regla de oro (desde la prueba v1):** simple no es corto. Cada beat tiene una intención clara, pero el prompt lleva todo lo que el modelo necesita para no inventar: fondo, bloqueo, actuación en beats, cámara, continuidad, luz y sonido. La regla anterior («una acción, un movimiento, un sonido», 60–160 palabras) dejaba fuera el trabajo de los agentes: el keyframe de c01_p02 tenía unas 600 palabras y su video, unas 110. Ver `produccion/prompting/investigacion.md`.

## De qué campo sale cada parte

| Parte del prompt | Sale de | Qué se hace con el campo |
|---|---|---|
| Primer fotograma y bloqueo | `continuidad.entrada`, `eje`, `camara.posicion` | Quién está dónde, a qué distancia, de frente a qué y mirando a qué |
| Mapa de la locación y fondo | `locacion`, `lente.foco`, `continuidad.entrada` | Qué hay detrás y si se mueve; qué se ve por cada vidrio |
| Actuación | `actuacion` (objetivo, tarea, beats, miradas, ojos) | Estados por beat con segundos. Sin palabras de emoción |
| Cámara | `camara.gramatica_escena` + `movimiento` + `motivo` | Tipo + amplitud + velocidad, en su propia frase |
| Continuidad | **todos** los `continuidad.hechos` del plano | Vestuario, pelo, props y su mano, estado del entorno |
| Luz | `luz` | Se protege con sus fuentes; los cambios, con su fuente |
| Sonido y diálogo | `audio` | En los campos del motor; diálogo exacto con quién habla y cómo |
| Referencias | `referencias` | Etiqueta y rol de cada una |
| Parámetros | `motor_video`, `duracion_s`, `metodo_video` | Van en `params`, no en el texto |

Entran **todos** los hechos que aplican al plano, no solo los frágiles. El keyframe fija el primer fotograma, pero el video los pierde a mitad del clip.

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

### Video · MiniMax H3 Max
Formato oficial de H3, según el modo: I2VA para `image-to-video`, FL2VA con `end_image_url` y Ref2VA para `reference-to-video`. Las plantillas y reglas están en `.cursor/skills/director-de-prompts/references/h3.md`, y hay un ejemplo antes y después en `references/ejemplo_c01_b02.md`.

Reglas del proyecto que se mantienen:
- `prompt_expansion_mode`: **`disabled`**. En la prueba del 2026-09-30, `balanced` reescribió el prompt e invirtió la acción. Por eso escribimos directamente en el formato del modelo.
- Sonido concreto («knuckles on glass, rain, train rumble»), nunca «tense atmosphere».
- Sin texto en cuadro: el candado en positivo («The frame contains no text of any kind; the line exists only as sound») y, al final de la descripción, el cierre fijo «No music. No subtitles, no captions, no on-screen text.» (decisión de Cristian). En la v1, «No on-screen text» solo no alcanzó y el modelo dibujó el diálogo como subtítulo.
- Si el plano es muy corto, la acción va en los primeros segundos del clip de 5 s, seguida de un estado quieto pero vivo, para que el montaje corte ahí.
- **Versión final:** todo plano con diálogo se genera con su audio de ElevenLabs (`target_audio_url` o `<Audio 1>`) para el lipsync. En las pruebas se omite.

### Video · Kling 4.0 / 4.0 Flash
Plantilla en `.cursor/skills/director-de-prompts/references/kling.md`; reglas del motor en `kling/kling_4_0_resumen.md`. `negative_prompt`: negaciones por eje, solo para lo que el plano no debe hacer (*no tilt, no orbit*…). Torso: «slim build, consistent proportions». No se describe el tono de una voz ya vinculada.

## Actuación (todas las recetas)
Sale de `actuacion` y sigue `produccion/actuacion.md`: estados por beat con segundos, miradas con destino, manos y lado del cuadro, ojos vivos. Nunca palabras de emoción. En planos cerrados, menos movimiento de cara: solo los ojos y el pensamiento. Los extras no actúan: están.

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
    params: { duration: 5, resolution: "480P", prompt_expansion_mode: disabled }
    texto: |
      (la receta del modelo)
    negativo: null              # solo Kling
```
En `bloques[].prompt_video` va el mismo esquema (`motor`, `params`, `texto`, `negativo`) para los bloques multi-beat y encadenados.
Cada prompt tiene que poder pegarse tal cual en fal o Kling. Los prompts nunca se entregan como fragmentos.

## Revisión antes de entregar
El Prompter pasa la revisión de la skill `director-de-prompts`. La pregunta que manda es: **¿hay algo que el modelo tenga que inventar?** Si lo hay y es un dato de otro rol, no se inventa: va a `alertas` y el bloque no pasa la revisión previa de Control de calidad. Si un beat tiene dos intenciones o dos movimientos superpuestos, se propone dividir el plano al Director.
