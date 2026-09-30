# Ejemplo: c01_b02 antes y después

Es el plano de Martina bajo luz roja diciendo «Diego…». Se genera con I2VA (`image-to-video` desde el keyframe aprobado de c01_p02), dura 5 s y en el montaje se usa algo más de un segundo.

La **cámara** y la **actuación** de la versión nueva son ilustrativas: las decisiones reales son del Director de fotografía (`gramatica_escena`) y del Director (`actuacion`). Aquí se completaron para mostrar cómo llegan al prompt.

## Antes (v1, unas 110 palabras)

```text
Martina stands completely still, eyes fixed on the door window off-screen left. Within the first 1.5 seconds her lips part just enough to say, almost voiceless, barely audible, in neutral Latin American Spanish: "Diego…" Her breath catches. She does not blink and does not step forward. Handheld, subtle breathing, no reframing. Keep the framing, lighting, face and wardrobe exactly as in the still: loose strands around her face, sweat sheen on her forehead, dry clean cream sweater, nobody else in frame. Sound: one knock on glass off-screen, her whisper, then dry silence. No music. No subtitles, no captions, no on-screen text.
```

Qué faltaba: qué hay detrás de ella y que no se mueve (el modelo lo animó como una ventana lateral), qué quiere Martina, adónde va su mirada además de la puerta, dónde está Tomás, un movimiento de cámara con motivo y el formato de H3.

## Después (skill v1, unas 330 palabras)

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a vertical close-up framed from the collarbones up, hands out of frame. Martina, the woman in <Picture 1>, around 29, stands alone in the aisle of the last carriage of a night train, about three metres from the closed connecting door, her body facing the door. The door is off-screen to frame left, just past the lens; she looks toward frame left, almost grazing the camera. Behind her, the interior of the carriage recedes toward the tail: empty seat backs and low red emergency lights at floor level, deeply out of focus as soft red shapes. This background is the inside of the train and stays fixed relative to the camera; only a faint vibration of the moving train passes through the frame. She keeps the look of <Picture 1>: low ponytail come loose, strands around her face, a light sheen of sweat on her forehead, a dry, clean cream crew-neck wool sweater. The camera pushes in with small amplitude at slow speed toward her eyes for the whole shot, as if drawn to what she has just recognised. From 0.0 to 1.2 seconds she holds her breath, eyes locked on the small door window, making tiny movements between the palm print on the glass and its edges, searching for a face. At 1.2 seconds a heavy knock lands on the glass off-screen; only her eyelids flinch, her head stays still. At 1.6 seconds her lips part and Martina, with a low, breathy voice in neutral Latin American Spanish (S1), says almost without voice, so that no one behind her can hear: <d>[Spanish] Diego…</d> Right after the name, her eyes flick for a fraction of a second toward frame right, where Tomás stands one step behind her right shoulder, out of frame, then return to the window. She does not step forward. Her mouth stays slightly open, her breath caught high in her chest, one slow blink at 3.5 seconds. The red light rising from the floor stays steady on the right side of her face; a steady cold-white tube above the door leaves a catchlight in her eyes and a cold edge on the loose strands; the far side of her face falls almost to black. The frame contains no text of any kind; the whispered name exists only as sound. No music. No subtitles, no captions, no on-screen text.

overall_soundscape: A low, steady rumble of the train runs under the floor. One heavy palm knock hits the glass off-screen at 1.2 seconds. Her held breath and a soft catch in her throat follow the name, then near-silence with only the train.

non_diegetic_music: N/A
```

Qué se fijó, y de qué campo sale cada cosa:

| Qué | Sale de |
|---|---|
| Formato I2VA y línea de alineación | Guía oficial de H3 |
| Fondo interior quieto respecto de la cámara | `continuidad.entrada` y `lente.foco`. En la v1 se perdió |
| Tomás detrás de su hombro derecho, fuera de cuadro | hc35 |
| Nadie la oye, y la mirada rápida hacia Tomás | hc34 convertido en conducta, con un objetivo: que nadie la oiga |
| Empuje lento hacia los ojos, con motivo | Director de fotografía (ilustrativo) |
| Luz protegida con sus fuentes | `luz`, igual que en el keyframe |
| Sin texto en cuadro, dicho en positivo, más el cierre fijo | Falla de subtítulos de la v1 y decisión de Cristian en `biblia/decisiones.md` |
