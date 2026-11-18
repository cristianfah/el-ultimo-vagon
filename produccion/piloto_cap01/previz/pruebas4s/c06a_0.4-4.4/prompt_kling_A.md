# c06a_0.4-4.4 · Kling 4.0 Omni-Ref (MCP) · brazo A (gris como video de referencia)

> **Borrador. No se envía sin el OK de Cristian.** Mismo prompt base que `prompt_kling_B.md`, `prompt_seedance_A.md`, `prompt_seedance_B.md`: cambian solo las referencias y las líneas fijas del brazo.

**Llamada:** MCP de Kling, `omni_ref_video` · `model` `kling-video-v4_0` · `resolution` 720p · `duration` 4 · `aspect_ratio` 9:16 · `imageCount` 1 · `prefer_multi_shots` true · `enable_audio` true · sin `audio_1`. Payload: `payload_kling.json` → `A`.

**Ventana:** c06a, de 0,4 a 4,4 s de la llamada · planos dentro de la prueba: b5_p8 0,0–1,4 · b5_p9 1,4–2,4 · b6_p1 (comienzo) 2,4–4,0.

**Entradas, en este orden:**

| En el prompt | Campo | Archivo | Se sube desde |
|---|---|---|---|
| 视频1 | `video_1` | `video_1.mp4` | `$PREVIZ_TRABAJO/pruebas4s/c06a_0.4-4.4/video_1.mp4` |
| 图片1 | `image_1` | `HOJA_hugo.png` | `$TRABAJO/refs/personajes__HOJA_hugo.png` |
| 图片2 | `image_2` | `HOJA_ivan.png` | `$TRABAJO/refs/personajes__HOJA_ivan.png` |
| 图片3 | `image_3` | `HOJA_carmen.png` | `$TRABAJO/refs/personajes__HOJA_carmen.png` |
| 图片4 | `image_4` | `HOJA_martina.png` | `$TRABAJO/refs/personajes__HOJA_martina.png` |
| 图片5 | `image_5` | `HOJA_tomas.png` | `$TRABAJO/refs/personajes__HOJA_tomas.png` |
| 图片6 | `image_6` | `PROP_llave_y_cerradura.png` | `$TRABAJO/refs/props__PROP_llave_y_cerradura.png` |
| 图片7 | `image_7` | `ref_infectados.jpg` | `REPO/direccion_arte/referencias/ref_infectados.jpg` |
| 图片8 | `image_8` | `F01_rojo_ultimo_vagon_hacia_puerta.png` | `$TRABAJO/refs/set__F01_rojo_ultimo_vagon_hacia_puerta.png` |
| 图片9 | `image_9` | `F03_rojo_puerta_desde_dentro_0-45.png` | `$TRABAJO/refs/set__F03_rojo_puerta_desde_dentro_0-45.png` |

**Prompt** (10192 caracteres, completo y listo para pegar):

```text
[EUV CAP01 - BLOQUE 5-6 - INT. LAST CARRIAGE - NOCHE - HANDHELD CLOSE, 35MM / LOCKED OFF, 35MM / LOCKED OFF HIGH, 24MM - 4s - 3 CUTS - REAL TIME 24 FPS, NO SLOW MOTION - 9:16 - prueba4s v1]

REFERENCES
图片1 is Hugo, 62, the train conductor: identity and wardrobe only, not framing - a long thin face, a thick grey moustache, tired watery eyes, a navy conductor's cap with a plain embroidered wheel badge and no letters, an old brushed navy conductor's uniform with dull bronze buttons, a whistle on a cord; slim and slightly stooped. Ignore the sheet layout and backdrop. In the grey previz he is the bronze cylinder.
图片2 is Iván, 45: identity and wardrobe only, not framing - a shaved head, a broken flattened nose, a wide weathered sunburnt face, two-day stubble with grey patches, a heavy dark brown canvas work jacket with worn reflective stripes on the arms over a grey hoodie, work trousers, safety boots with cement dust only on the boots and knees; broad shoulders, thick neck. Ignore the sheet layout and backdrop. In the grey previz he is the dark-brown cylinder.
图片3 is Carmen, 54, a night-shift nurse: identity and wardrobe only, not framing - a round face, short curly reddish-brown dyed hair with grey roots showing, reading glasses hanging on a beaded cord, faded light-blue scrubs under a long dark brown wool coat, a large cloth bag on her LEFT shoulder, worn white clogs; short and sturdy. Ignore the sheet layout and backdrop. In the grey previz she is the light-blue cylinder.
图片4 is Martina, 29: identity and wardrobe only, not framing - a narrow face, a small mole on her LEFT cheekbone, shoulder-length dark brown wavy hair tucked behind her right ear, an oversized oatmeal chunky wool sweater whose cuffs cover her knuckles, a long charcoal wool coat always worn open, faded dark jeans, worn brown leather boots. Ignore the sheet layout and backdrop. In the grey previz she is the oatmeal cylinder.
图片5 is Tomás, 31: identity and wardrobe only, not framing - thin full metal-frame glasses always on his face, short neat dark brown hair with a side part, clean-shaven, a fitted navy quilted jacket over a charcoal sweater, dark chinos, white sneakers, an average, slightly soft build. Ignore the sheet layout and backdrop. In the grey previz he is the navy-blue cylinder.
图片6 is the antique iron key and the lock of the last carriage's door: object identity only, not framing.
图片7 is the look of the infected only - grey skin, milky white eyes, dark veins, dark red-black stains at the mouth, ordinary passenger clothes; ignore its background, its lights and its framing. In the grey previz the infected are near-black cylinders (under the light they can read dark grey).
图片8 is a set plate of the last carriage looking toward its door, in red emergency light: look and light only, NEVER a shot.
图片9 is a set plate of the last carriage's door seen from inside, in red emergency light: look and light only, NEVER a shot.
视频1 is the grey previz of these exact 4 seconds, rendered from the real camera and lens: composition and blocking.
视频1 is the master reference for camera, blocking and timing. The character sheets define identity. 图片8 and 图片9 are style references only.
Cylinder legend of the grey previz: every person is a plain colored cylinder with a cone nose that shows where the face points. Hugo bronze, Iván dark brown, Carmen light blue, Martina oatmeal, Tomás navy blue, the infected near-black (under the cold light they can read grey).

LOCKS
CAST LOCK: ONLY 5 PEOPLE INSIDE - HUGO, IVÁN, CARMEN, MARTINA AND TOMÁS. THE INFECTED STAY OUTSIDE THE DOOR, NEVER INSIDE. CUT 1 SHOWS ONLY HUGO AND ONE INFECTED HAND; CUT 2 SHOWS NOBODY FROM THE GROUP.
HUGO: KEY IN HIS RIGHT HAND; IT GOES INTO THE LOCK, TURNS, COMES OUT AND LEAVES THE FRAME LOW, TOWARD HIS POCKET.
CARMEN: RIGHT PALM CUT, DARK RED-BLACK STAIN; SHE HOLDS THAT HAND CLOSED AGAINST HER CHEST.
DOOR: SHUT FROM 0.6s TO THE END; IT HAS ONLY A KEY LOCK AND A HANDLE.
SIDES LOCK: IN CUT 3, MARTINA LEFT OF TOMÁS; HUGO ON FRAME LEFT BY THE LOCK; IVÁN AT CENTER AGAINST THE DOOR.
LIGHT LOCK: ONE COLD WHITE TUBE, ABOVE THE DOOR ON THE INSIDE; EVERYTHING ELSE RED.
NOBODY LOOKS INTO THE LENS.

SCENE CONTEXT
A night train. The survivors have just made it into the last carriage, the only one they can lock; the infected fill the gangway outside its single door. Hugo, the old conductor, came in last. These 4 seconds: Hugo shuts the door on an infected hand and locks it from inside with the key, an infected face smashes into the door's small window, and the group backs away while the pounding goes on, until a distant scream draws the infected away. Held for the whole clip: wardrobe identical to the character sheets in every frame, never changing color; Hugo's cap stays on; Tomás's glasses stay on; Martina's coat stays open; Carmen's bag stays on her left shoulder. The side windows show night with rain on the outside of the glass.

ACTION
Hugo - GOAL: seal the door. TACTIC: crushes it shut with his right shoulder and all his weight, locks it from inside with the key and puts the key away out of sight; then stays by the lock, watching the door.
Iván - GOAL: hold the door. TACTIC: crosses to it, turns and leans his back against it, head down, bracing.
Martina - GOAL: get away from the door. TACTIC: backs off step by step, eyes on the small window.
Tomás - GOAL: stay next to Martina. TACTIC: backs off at her right side, watching the door.
Carmen - GOAL: put distance between herself and the door. TACTIC: backs off the furthest, into the aisle, her right hand closed against her chest.
The infected - force the gap, smash into the small window, pound the door; at the distant scream they leave.

PHYSICS
Real time at 24 fps: no slow motion, no speed ramp. The door is heavy steel: the hand in the gap stops it dead until Hugo's whole body weight crushes it; then it slams. The leaf trembles in its frame with every blow. The face hits the glass, bounces and slides down. Iván's back takes the blows. The whole train sways and the bodies sway with it.

LIGHTING
Only the set's own sources, no fill: red emergency light from above; one cold white tube above the door on the inside, which rims heads and shoulders and does not light the carriage. Faces half in shadow; blacks fall to black. Through the gap and the small window, the red gangway.

AUDIO
Continuous rail rhythm. 0.0s: snarls at the gap. 0.38s: a crunching thud as the door crushes the hand, and a howl outside. 0.58s: the slam. 1.0s: the clack of the key turning. 1.64s and 1.98s: the dull smack of a face on the glass. From 2.55s to 3.52s: violent pounding of many hands on the door and its window. 3.55s: a distant scream from carriage 5 and the pounding stops dead; footsteps running away; then only the train and their breathing. Nobody speaks; no dialogue audio in this test. AUDIO LOCK, no words, soft Santiago Chilean voices: Hugo, 62, low worn voice - one strained grunt on the push; Iván, 45, deep dry voice - heavy breathing; Carmen, 54, warm firm voice - a shaky exhale; Martina, 29, and Tomás, 31 - fast breathing that slows in the silence.

CUTS
CUT 1 (0 to 1.4s) - Inside the last carriage, close beside the door frame on the lock side, three-quarter on the gap and the lock, 35mm. Frame left: the door frame and the gap; center: the edge of the door with the lock and the handle; frame right: Hugo's body leaning into the door. Camera: handheld, close; it starts a little high (about 1.5 m) to read Hugo's body against the door and the gap, jolts 2 frames after the crush and 2 frames after the slam, then drops to lock height (about 1.1 m) and moves in 0.2 m for the key. At 0.0s Hugo, the last one in, is driving the door shut with his right shoulder and all his weight, and a grey infected hand with short, broken, dirty nails pushes into the gap between the door's edge and the frame at chest height; the door stops on it. At 0.38s Hugo throws his weight and crushes it; the hand pulls back; at 0.58s the door slams shut. With his right hand he puts the antique key into the lock from inside and turns it: at 1.0s the clack; he pulls the key out and lowers it out of frame, toward his pocket, by 1.35s. Through the gap, and then through the small window, the infected in the red gangway. - HARD CUT AT 1.4s
CUT 2 (1.4 to 2.4s) - The door's small window from inside, slightly low (about 1.35 m) and three-quarter from the left, 35mm. The window frame fills the center, the grey door leaf above and below it. Behind the glass: the red gangway and infected silhouettes. Camera: locked off, no push-in, vibrating only with the train; the impact shakes the frame 3 frames later and it settles back. At 1.4s an infected runs at the door; at 1.64s his face smashes into the upper half of the glass, bounces, hits again at 1.98s and slides down, leaving a dark red-black smear on the glass; other hands pound the glass. Nobody from the group is in frame. - HARD CUT AT 2.4s
CUT 3 (2.4 to 4.0s) - Wide shot of the last carriage from the aisle between rows 3 and 4, looking toward the door, slightly high (about 1.9 m), 24mm. Foreground center: Carmen, her back to us, in the aisle, seat backs on both sides; beyond her, Martina on the left of Tomás; at the far end, the door with its smeared small window and the cold tube above it; Iván at the door, center, above Carmen's head; Hugo on frame left, by the lock. Camera: locked off on purpose, no push-in, vibrating only with the train; it does not react to the pounding. At 2.4s the group is already backing toward the camera; from 2.55s to 3.52s many hands pound the door and its window and the leaf trembles against the lock. Iván crosses to the door, turns and leans his back against it at 2.92s, head down. At 3.55s a distant scream from carriage 5: the pounding stops dead; Iván lifts his head; the silhouettes leave the window, the glass stays smeared, and footsteps run away. Until 4.0s: stillness, the train and their breathing; everyone watches the door. - END OF CLIP AT 4.0s

Colored cylinders are blocking only: position, facing and path. Body, face and acting come from the character references.

No music. No subtitles, no captions, no on-screen text.
```
