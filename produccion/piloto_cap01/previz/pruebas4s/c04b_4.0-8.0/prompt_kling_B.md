# c04b_4.0-8.0 · Kling 4.0 Omni-Ref (MCP) · brazo B (hoja de storyboard como imagen, sin video)

> **Borrador. No se envía sin el OK de Cristian.** Mismo prompt base que `prompt_kling_A.md`, `prompt_seedance_A.md`, `prompt_seedance_B.md`: cambian solo las referencias y las líneas fijas del brazo.

**Llamada:** MCP de Kling, `omni_ref_video` · `model` `kling-video-v4_0` · `resolution` 720p · `duration` 4 · `aspect_ratio` 9:16 · `imageCount` 1 · `prefer_multi_shots` true · `enable_audio` true · sin `audio_1`. Payload: `payload_kling.json` → `B`.

**Ventana:** c04b, de 4,0 a 8,0 s de la llamada · planos dentro de la prueba: b4_p5 (final) 0,0–1,0 · b4_p6 1,0–4,0.

**Entradas, en este orden:**

| En el prompt | Campo | Archivo | Se sube desde |
|---|---|---|---|
| 图片1 | `image_1` | `HOJA_hugo.png` | `$TRABAJO/refs/personajes__HOJA_hugo.png` |
| 图片2 | `image_2` | `HOJA_martina.png` | `$TRABAJO/refs/personajes__HOJA_martina.png` |
| 图片3 | `image_3` | `HOJA_tomas.png` | `$TRABAJO/refs/personajes__HOJA_tomas.png` |
| 图片4 | `image_4` | `HOJA_carmen.png` | `$TRABAJO/refs/personajes__HOJA_carmen.png` |
| 图片5 | `image_5` | `HOJA_ivan.png` | `$TRABAJO/refs/personajes__HOJA_ivan.png` |
| 图片6 | `image_6` | `PROP_llave_y_cerradura.png` | `$TRABAJO/refs/props__PROP_llave_y_cerradura.png` |
| 图片7 | `image_7` | `ref_infectados.jpg` | `REPO/direccion_arte/referencias/ref_infectados.jpg` |
| 图片8 | `image_8` | `F10_rojo_pasajeros_hacia_puerta.png` | `$TRABAJO/refs/set__F10_rojo_pasajeros_hacia_puerta.png` |
| 图片9 | `image_9` | `hoja_storyboard.jpg` | `$PREVIZ_TRABAJO/pruebas4s/c04b_4.0-8.0/hoja_storyboard.jpg` |

**Prompt** (10748 caracteres, completo y listo para pegar):

```text
[EUV CAP01 - BLOQUE 4 - INT. CARRIAGE 5 - NOCHE - HANDHELD, 40MM / HANDHELD RUNNING BACKWARD, 28MM - 4s - 2 CUTS - REAL TIME 24 FPS, NO SLOW MOTION - 9:16 - prueba4s v1]

REFERENCES
图片1 is Hugo, 62, the train conductor: identity and wardrobe only, not framing - a long thin face, a thick grey moustache, tired watery eyes, a navy conductor's cap with a plain embroidered wheel badge and no letters, an old brushed navy conductor's uniform with dull bronze buttons, a whistle on a cord; slim and slightly stooped. Ignore the sheet layout and backdrop. In the grey previz he is the bronze cylinder.
图片2 is Martina, 29: identity and wardrobe only, not framing - a narrow face, a small mole on her LEFT cheekbone, shoulder-length dark brown wavy hair tucked behind her right ear, an oversized oatmeal chunky wool sweater whose cuffs cover her knuckles, a long charcoal wool coat always worn open, faded dark jeans, worn brown leather boots. Ignore the sheet layout and backdrop. In the grey previz she is the oatmeal cylinder.
图片3 is Tomás, 31: identity and wardrobe only, not framing - thin full metal-frame glasses always on his face, short neat dark brown hair with a side part, clean-shaven, a fitted navy quilted jacket over a charcoal sweater, dark chinos, white sneakers, an average, slightly soft build. Ignore the sheet layout and backdrop. In the grey previz he is the navy-blue cylinder.
图片4 is Carmen, 54, a night-shift nurse: identity and wardrobe only, not framing - a round face, short curly reddish-brown dyed hair with grey roots showing, reading glasses hanging on a beaded cord, faded light-blue scrubs under a long dark brown wool coat, a large cloth bag on her LEFT shoulder, worn white clogs; short and sturdy. Ignore the sheet layout and backdrop. In the grey previz she is the light-blue cylinder.
图片5 is Iván, 45: identity and wardrobe only, not framing - a shaved head, a broken flattened nose, a wide weathered sunburnt face, two-day stubble with grey patches, a heavy dark brown canvas work jacket with worn reflective stripes on the arms over a grey hoodie, work trousers, safety boots with cement dust only on the boots and knees; broad shoulders, thick neck. Ignore the sheet layout and backdrop. In the grey previz he is the dark-brown cylinder.
图片6 is the antique iron key and the lock of the last carriage's door: object identity only, not framing.
图片7 is the look of the infected only - grey skin, milky white eyes, dark veins, dark red-black stains at the mouth, ordinary passenger clothes; ignore its background, its lights and its framing. In the grey previz the infected are near-black cylinders (under the light they can read dark grey).
图片8 is a set plate of the passenger carriage in red emergency light: look and light only, NEVER a shot.
图片9 is the storyboard sheet of these exact 4 seconds, one row per shot with its key stills from the real camera (A = start, B = key moment, C = end): composition and blocking.
图片9 is a storyboard sheet; panels, gutters and labels are planning marks only. No storyboard grid, split screen or collage in the output. The character sheets define identity. 图片8 is a style reference only.
Cylinder legend of the grey previz: every person is a plain colored cylinder with a cone nose that shows where the face points. Hugo bronze, Martina oatmeal, Tomás navy blue, Carmen light blue, Iván dark brown, the other passengers grey, the infected near-black.

LOCKS
CAST LOCK: CUT 1 ONLY HUGO AND 3 PASSENGERS. CUT 2 ONLY TOMÁS, MARTINA, CARMEN, IVÁN, ONE PASSENGER BEHIND THEM AND 3 INFECTED.
HUGO: KEY IN HIS RIGHT HAND, RAISED HIGH.
SIDES LOCK: IN CUT 2, MARTINA ON FRAME LEFT, TOMÁS ON FRAME RIGHT.
LIGHT LOCK: RED EMERGENCY LIGHT ONLY; NO AMBER LAMPS, NO WHITE LIGHT IN CARRIAGE 5.
NOBODY LOOKS INTO THE LENS.

SCENE CONTEXT
Carriage 5 of a night train in red emergency light. The infected are at the front door; Hugo, the old conductor, has burst in through the rear door and ordered everyone to the last carriage. These 4 seconds are the end of his order and the stampede toward him down the aisle, while the front door gives way behind them. Held for the whole clip: wardrobe identical to the character sheets in every frame, never changing color; Hugo's cap stays on; Tomás's glasses stay on; Martina's coat stays open, her sweater cuffs over her knuckles; Carmen's bag stays on her left shoulder. The side windows show night with rain on the outside of the glass, with red reflections.

ACTION
Hugo - GOAL: get every passenger out through his door. TACTIC: finishes the order with the key held high, then steps aside to his right to clear the doorway.
Tomás - GOAL: get Martina out. TACTIC: runs crouched, dragging her by the hand (his right hand holds her left), eyes on the floor ahead of his feet.
Martina - GOAL: keep up. TACTIC: runs bent behind him; one glance back at the front door, then forward again.
Carmen - GOAL: reach the door. TACTIC: runs behind them, bumping into seat backs.
Iván - GOAL: get Carmen out and watch their backs. TACTIC: last of the group, pushes her on and keeps checking over his shoulder.
Passengers - get up and head toward Hugo.
The infected - burst through the front door and run down the aisle after the group.

PHYSICS
Real time at 24 fps: no slow motion, no speed ramp. Runners lean forward, collide with seat backs and bounce off them; coats fly and settle; the front door slams open against its stop. The whole train sways and rattles and the bodies sway with it. The running camera has a step rhythm and weight; it never floats.

LIGHTING
Only the set's own sources, no fill: the red emergency strip along the ceiling, from above; the amber reading lamps are off. Faces half in shadow; blacks fall to black. Behind Hugo, the gangway is dark red.


DIRECTION RULES (27-nov)
LAYOUT: Carriage 5 never changes: two rows of paired blue seats with a central aisle; side windows on both walls; the front door (where the infected come in) at one end; the rear door (Hugo's door, to the gangway) at the other; Martina's seat on the window side.
LIGHT SOURCE: Red emergency strip on the ceiling, from above; amber lamps off; Hugo's doorway backed by the dark red gangway. Half of each face in shadow.
AXIS: every screen direction in SIDES LOCK holds for the whole clip; nobody crosses the axis.
BREATH: before any key line or key action, one directed breath or blink, never more.
TIMING: the action is already under way in the first frame; no dead air after it ends.
GAIT: Martina: quick, small steps, head down; Tomás: long, careful strides; Carmen: short, heavy, steady steps; Iván: heavy, square, pushing forward; Hugo: stiff, slightly stooped.
MARKS:
- CUT 1 (end of b4_p5): Hugo keeps the key high in his right hand; the whistle has already blown (it was his breath).
- CUT 2 (b4_p6): Tomás drags Martina by the hand; each passenger dodges a different seat back; Martina on frame left, Tomás on frame right.
END DIRECTION RULES

AUDIO
Continuous rail rhythm. From 0.0s to 0.56s Hugo's mouth finishes the shouted order, with no voice: no dialogue audio in this test. From 1.0s: running feet, bodies hitting seat backs at 1.7s and 2.85s, ragged breathing. 2.04s: the front door bursts open with a crash; from 2.2s snarls and running feet behind the group. AUDIO LOCK, breaths only, no words, soft Santiago Chilean voices: Tomás, 31, calm mid-low voice - fast breathing; Martina, 29, low husky voice - short breaths; Carmen, 54, warm firm voice - short gasps; Iván, 45, deep dry voice - heavy breathing. Hugo makes no sound in this test.
AUDIO LOCK (produccion/voces.md, never Mexican, neutral or Spain Spanish): Martina: Chilean woman, 29, soft Santiago accent; low, warm, tired, slightly husky voice, almost a whisper; answers too fast when she lies | Tomás: Chilean man, 31, soft Santiago accent; mid-low voice, calm and polite; when he doubts he lowers his voice and turns cold | Carmen: Chilean woman, 54, soft Santiago accent; warm but firm nurse's voice (no approved ElevenLabs voice yet) | Iván: Chilean man, 45, soft Santiago accent; deep, dry voice, short phrases (no approved ElevenLabs voice yet) | Hugo: Chilean man, 62, soft Santiago accent; deep, worn, unhurried voice with a conductor's quiet authority; when he shouts his voice cracks but commands

CUTS
CUT 1 (0 to 1.0s) - Looking down carriage 5 toward its rear door, from a standing passenger's eye height at row 16, left side (about 1.48 m), 40mm. Hugo at the far end, center, in the open rear door with the door leaf beside him; behind him only the dark red gangway. Frame left: a passenger standing up and heading toward him; low center: the head of a seated passenger turned toward him; at the end, the shoulder of another passenger enters from the right edge. Camera: handheld, just settled after a fast pan; at the end it takes half a step toward the aisle with the people. At 0.0s Hugo is finishing his shouted order: mouth wide on the last word, the antique key raised high in his right hand, his left hand on the edge of the door, his eyes on the passengers on the right side of the carriage, never on the lens; no dialogue audio in this test. From 0.7s he steps to his right to clear the doorway. - HARD CUT AT 1.0s
CUT 2 (1.0 to 4.0s) - The stampede down the aisle toward the rear door. Camera: handheld, running backward down the aisle ahead of the group at head height (about 1.74 m), 1.3 m in front of Tomás, 28mm, so the front door at the far end shows above their lowered heads; running-step shake and two bumps against seat backs, at 1.7s and 2.85s. Foreground frame right: Tomás, crouched, dragging Martina by the hand, eyes on the floor ahead of his feet; Martina right behind him on frame left; further back Carmen; then Iván, last of the group, pushing her on and looking back; behind them, one more passenger. Seat backs pass on both edges and they bump into them. At 2.04s the front door at the far end bursts open; from 2.2s the first infected run in down the aisle. From 2.1s to 2.5s Martina looks back over her right shoulder at the front door, then faces forward again. Until 4.0s the infected run down the aisle behind the group and the group keeps running at the camera. The runners look at the floor ahead of their feet or back over their shoulders, never into the lens. - END OF CLIP AT 4.0s
Follow the storyboard panels in order, each a key frame: match camera position, framing, screen direction and action; cut only where the shot number changes. The panels are grey previz stand-ins for blocking only; every look comes from the references and this text.

Colored cylinders are blocking only: position, facing and path. Body, face and acting come from the character references.

No music. No subtitles, no captions, no on-screen text.
```
