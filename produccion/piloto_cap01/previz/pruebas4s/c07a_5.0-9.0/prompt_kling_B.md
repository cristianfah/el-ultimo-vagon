# c07a_5.0-9.0 · Kling 4.0 Omni-Ref (MCP) · brazo B (hoja de storyboard como imagen, sin video)

> **Borrador. No se envía sin el OK de Cristian.** Mismo prompt base que `prompt_kling_A.md`, `prompt_seedance_A.md`, `prompt_seedance_B.md`: cambian solo las referencias y las líneas fijas del brazo.

**Llamada:** MCP de Kling, `omni_ref_video` · `model` `kling-video-v4_0` · `resolution` 720p · `duration` 4 · `aspect_ratio` 9:16 · `imageCount` 1 · `prefer_multi_shots` true · `enable_audio` true · sin `audio_1`. Payload: `payload_kling.json` → `B`.

**Ventana:** c07a, de 5,0 a 9,0 s de la llamada · planos dentro de la prueba: b7_p3 0,0–4,0.

**Entradas, en este orden:**

| En el prompt | Campo | Archivo | Se sube desde |
|---|---|---|---|
| 图片1 | `image_1` | `HOJA_martina.png` | `$TRABAJO/refs/personajes__HOJA_martina.png` |
| 图片2 | `image_2` | `HOJA_tomas.png` | `$TRABAJO/refs/personajes__HOJA_tomas.png` |
| 图片3 | `image_3` | `HOJA_carmen.png` | `$TRABAJO/refs/personajes__HOJA_carmen.png` |
| 图片4 | `image_4` | `F02_rojo_ultimo_vagon_hacia_fondo_cabina.png` | `$TRABAJO/refs/set__F02_rojo_ultimo_vagon_hacia_fondo_cabina.png` |
| 图片5 | `image_5` | `hoja_storyboard.jpg` | `$PREVIZ_TRABAJO/pruebas4s/c07a_5.0-9.0/hoja_storyboard.jpg` |

**Prompt** (7785 caracteres, completo y listo para pegar):

```text
[EUV CAP01 - BLOQUE 7 - INT. LAST CARRIAGE - NOCHE - HANDHELD, ALMOST STILL, 40MM - 4s - 1 CUT - REAL TIME 24 FPS, NO SLOW MOTION - 9:16 - prueba4s v1]

REFERENCES
图片1 is Martina, 29: identity and wardrobe only, not framing - a narrow face, a small mole on her LEFT cheekbone, shoulder-length dark brown wavy hair tucked behind her right ear, an oversized oatmeal chunky wool sweater whose cuffs cover her knuckles, a long charcoal wool coat always worn open, faded dark jeans, worn brown leather boots. Ignore the sheet layout and backdrop. In the grey previz she is the oatmeal cylinder.
图片2 is Tomás, 31: identity and wardrobe only, not framing - thin full metal-frame glasses always on his face, short neat dark brown hair with a side part, clean-shaven, a fitted navy quilted jacket over a charcoal sweater, dark chinos, white sneakers, an average, slightly soft build. Ignore the sheet layout and backdrop. In the grey previz he is the navy-blue cylinder.
图片3 is Carmen, 54, a night-shift nurse: identity and wardrobe only, not framing - a round face, short curly reddish-brown dyed hair with grey roots showing, reading glasses hanging on a beaded cord, faded light-blue scrubs under a long dark brown wool coat, a large cloth bag on her LEFT shoulder, worn white clogs; short and sturdy. Ignore the sheet layout and backdrop. In the grey previz she is the light-blue cylinder.
图片4 is a set plate of the last carriage looking toward its back wall, the black rear window and the conductor's cabin, in red emergency light: look and light only, NEVER a shot.
图片5 is the storyboard sheet of these exact 4 seconds, one row per shot with its key stills from the real camera (A = start, B = key moment, C = end): composition and blocking.
图片5 is a storyboard sheet; panels, gutters and labels are planning marks only. No storyboard grid, split screen or collage in the output. The character sheets define identity. 图片4 is a style reference only.
Cylinder legend of the grey previz: every person is a plain colored cylinder with a cone nose that shows where the face points. Martina oatmeal, Tomás navy blue, Carmen light blue.

LOCKS
CAST LOCK: ONLY 3 PEOPLE - MARTINA, TOMÁS AND CARMEN.
CARMEN: RIGHT HAND CLOSED INTO A FIST, HIDDEN INSIDE HER COAT.
SIDES LOCK: MARTINA ON FRAME RIGHT, IN THE FOREGROUND; TOMÁS ON THE LEFT EDGE; CARMEN BETWEEN THEM, FURTHER BACK. TOMÁS LOOKS TOWARD FRAME RIGHT TO SEE HER. THE CONDUCTOR'S CABIN IS ON FRAME LEFT IN THE BACKGROUND.
BACK WALL: THE BLACK REAR WINDOW AND THE CONDUCTOR'S CABIN, NOTHING ELSE.
LIPS CLOSED: NOBODY IN FRAME SPEAKS.
NOBODY LOOKS INTO THE LENS: MARTINA LOOKS JUST ABOVE IT.

SCENE CONTEXT
The last carriage of a night train, in red emergency light. The group has locked itself in. Through the small window of the door, behind the camera, a voice has just shouted that it saw Martina in carriage 2, the carriage where the outbreak began. These 4 seconds are the accusation landing: she does not move, and the people behind her turn to look at her one by one. Held for the whole clip: wardrobe identical to the character sheets in every frame, never changing color; Martina's coat stays open, her sweater cuffs over her knuckles; Tomás's glasses stay on; Carmen's reading glasses hang on their cord.

ACTION
Martina - GOAL: give nothing away. TACTIC: stays absolutely still, eyes fixed on the door's small window, lips closed; only her breath and one swallow give her away.
Tomás - GOAL: understand what he just heard. TACTIC: stops watching the door, turns his head to her and keeps looking.
Carmen - GOAL: read Martina. TACTIC: turns to her after Tomás and holds the look, her right hand hidden in her coat.

PHYSICS
Real time at 24 fps: no slow motion. The train sways and the three bodies sway with it; Martina's stillness holds against the sway. The heads turn with weight: the eyes first, then the head. The handheld camera breathes and never floats.

LIGHTING
Only the set's own sources, no fill: red emergency light from above; the single cold tube is above the door, above and behind the camera, and puts only a thin cold edge on the tops of their heads and shoulders; it does not light the carriage. Faces half in shadow; blacks fall to black; the rear window is black.


DIRECTION RULES (27-nov)
LAYOUT: The last carriage never changes: six rows of 2+2 seats facing the door; one single door with a small mesh window, the cold tube above it on the inside, the brass lock plate with keyhole above and handle below; the red emergency handle right of the door; at the far end the back wall with the black rear window and the conductor's cabin on its left. There is no second door.
LIGHT SOURCE: Red emergency light from above; the cold tube above the door, behind the camera, puts only a thin cold edge on heads and shoulders. Half of each face in shadow.
AXIS: every screen direction in SIDES LOCK holds for the whole clip; nobody crosses the axis.
BREATH: before any key line or key action, one directed breath or blink, never more.
TIMING: the action is already under way in the first frame; no dead air after it ends.
GAIT: Martina: quick, small steps, head down; Tomás: long, careful strides; Carmen: short, heavy, steady steps.
MARKS:
- b7_p3: Martina on frame right, facing us, eyes just above the lens. She inhales once through the nose before Diego's second line. Her only new gesture after «¡Te vi en el vagón 2!» is one single blink, nothing else. Behind her the heads turn one by one.
END DIRECTION RULES

AUDIO
Continuous low rail rhythm. Martina's short breaths through the nose; one swallow around 3.0s. No dialogue audio in this test: the shouted line exists in the story but not in this clip. AUDIO LOCK, no words: Martina, 29, low husky voice - breath only; Tomás and Carmen silent.
AUDIO LOCK (produccion/voces.md, never Mexican, neutral or Spain Spanish): Martina: Chilean woman, 29, soft Santiago accent; low, warm, tired, slightly husky voice, almost a whisper; answers too fast when she lies | Tomás: Chilean man, 31, soft Santiago accent; mid-low voice, calm and polite; when he doubts he lowers his voice and turns cold | Carmen: Chilean woman, 54, soft Santiago accent; warm but firm nurse's voice (no approved ElevenLabs voice yet)

CUTS
CUT 1 (0 to 4.0s) - Close-up of Martina from the door side, low (about 1.18 m, at lock height), looking slightly up at her, 40mm, shallow focus. Martina in the foreground on frame right, in focus, framed from mid-chest up with air above her head. Behind her, out of focus: Tomás at the left edge and, between him and Martina, further back and lower, Carmen. Background: the back wall with the black rear window behind her and the conductor's cabin on frame left. Camera: handheld, slight, almost still, set a little toward the lock side to open the gap between Martina and Tomás where Carmen stands; no push-in. From 0.0s Martina stares at the door's small window, just above the lens and slightly to frame left, and does not move; lips closed. From 0.0s to 2.06s she is hearing the accusation through the door (no dialogue audio in this test). From 0.55s to 0.95s Tomás turns his head toward frame right, to her; from 1.15s to 1.55s Carmen turns to her too. From 2.6s to 4.0s they hold: Tomás and Carmen keep looking at her, she keeps looking at the window; one swallow, her breathing. - END OF CLIP AT 4.0s
Follow the storyboard panels in order, each a key frame: match camera position, framing, screen direction and action; cut only where the shot number changes. The panels are grey previz stand-ins for blocking only; every look comes from the references and this text.

Colored cylinders are blocking only: position, facing and path. Body, face and acting come from the character references.

No music. No subtitles, no captions, no on-screen text.
```
