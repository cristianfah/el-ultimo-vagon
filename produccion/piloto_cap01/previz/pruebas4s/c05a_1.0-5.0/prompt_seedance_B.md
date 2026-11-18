# c05a_1.0-5.0 · Seedance 2.5 draft (fal) · brazo B (hoja de storyboard como imagen, sin video)

> **Borrador. No se envía sin el OK de Cristian.** Mismo prompt base que `prompt_kling_A.md`, `prompt_kling_B.md`, `prompt_seedance_A.md`: cambian solo las referencias y las líneas fijas del brazo.

**Llamada:** fal, `bytedance/seedance-2.5/us/reference-to-video` · `draft` true (sale a 480p y devuelve `draft_id`) · `duration` "4" · `aspect_ratio` "9:16" · `seed` 1019 · `generate_audio` true · sin `audio_urls`. Payload: `payload_seedance.json` → `B`.

**Ventana:** c05a, de 1,0 a 5,0 s de la llamada · planos dentro de la prueba: b5_p1 (final) 0,0–0,8 · b5_p2 0,8–2,3 · b5_p3 2,3–4,0.

**Entradas, en este orden:**

| En el prompt | Campo | Archivo | Se sube desde |
|---|---|---|---|
| @Image1 | `image_urls[0]` | `HOJA_hugo.png` | `$TRABAJO/refs/personajes__HOJA_hugo.png` |
| @Image2 | `image_urls[1]` | `HOJA_ivan.png` | `$TRABAJO/refs/personajes__HOJA_ivan.png` |
| @Image3 | `image_urls[2]` | `HOJA_carmen.png` | `$TRABAJO/refs/personajes__HOJA_carmen.png` |
| @Image4 | `image_urls[3]` | `HOJA_martina.png` | `$TRABAJO/refs/personajes__HOJA_martina.png` |
| @Image5 | `image_urls[4]` | `HOJA_tomas.png` | `$TRABAJO/refs/personajes__HOJA_tomas.png` |
| @Image6 | `image_urls[5]` | `PROP_llave_y_cerradura.png` | `$TRABAJO/refs/props__PROP_llave_y_cerradura.png` |
| @Image7 | `image_urls[6]` | `ref_infectados.jpg` | `REPO/direccion_arte/referencias/ref_infectados.jpg` |
| @Image8 | `image_urls[7]` | `F07_rojo_fuelle_vestibulo.png` | `$TRABAJO/refs/set__F07_rojo_fuelle_vestibulo.png` |
| @Image9 | `image_urls[8]` | `F04_rojo_puerta_desde_fuelle.png` | `$TRABAJO/refs/set__F04_rojo_puerta_desde_fuelle.png` |
| @Image10 | `image_urls[9]` | `hoja_storyboard.jpg` | `$PREVIZ_TRABAJO/pruebas4s/c05a_1.0-5.0/hoja_storyboard.jpg` |

**Prompt** (9899 caracteres, completo y listo para pegar):

```text
[EUV CAP01 - BLOQUE 5 - INT. GANGWAY - NOCHE - HANDHELD CLOSE, 50MM / HANDHELD RETREATING, 28MM / HANDHELD LOW, 35MM - 4s - 3 CUTS - REAL TIME 24 FPS, NO SLOW MOTION - 9:16 - prueba4s v1]

REFERENCES
@Image1 is Hugo, 62, the train conductor: identity and wardrobe only, not framing - a long thin face, a thick grey moustache, tired watery eyes, a navy conductor's cap with a plain embroidered wheel badge and no letters, an old brushed navy conductor's uniform with dull bronze buttons, a whistle on a cord; slim and slightly stooped. Ignore the sheet layout and backdrop. In the grey previz he is the bronze cylinder.
@Image2 is Iván, 45: identity and wardrobe only, not framing - a shaved head, a broken flattened nose, a wide weathered sunburnt face, two-day stubble with grey patches, a heavy dark brown canvas work jacket with worn reflective stripes on the arms over a grey hoodie, work trousers, safety boots with cement dust only on the boots and knees; broad shoulders, thick neck. Ignore the sheet layout and backdrop. In the grey previz he is the dark-brown cylinder.
@Image3 is Carmen, 54, a night-shift nurse: identity and wardrobe only, not framing - a round face, short curly reddish-brown dyed hair with grey roots showing, reading glasses hanging on a beaded cord, faded light-blue scrubs under a long dark brown wool coat, a large cloth bag on her LEFT shoulder, worn white clogs; short and sturdy. Ignore the sheet layout and backdrop. In the grey previz she is the light-blue cylinder.
@Image4 is Martina, 29: identity and wardrobe only, not framing - a narrow face, a small mole on her LEFT cheekbone, shoulder-length dark brown wavy hair tucked behind her right ear, an oversized oatmeal chunky wool sweater whose cuffs cover her knuckles, a long charcoal wool coat always worn open, faded dark jeans, worn brown leather boots. Ignore the sheet layout and backdrop. In the grey previz she is the oatmeal cylinder.
@Image5 is Tomás, 31: identity and wardrobe only, not framing - thin full metal-frame glasses always on his face, short neat dark brown hair with a side part, clean-shaven, a fitted navy quilted jacket over a charcoal sweater, dark chinos, white sneakers, an average, slightly soft build. Ignore the sheet layout and backdrop. In the grey previz he is the navy-blue cylinder.
@Image6 is the antique iron key and the lock of the last carriage's door: object identity only, not framing.
@Image7 is the look of the infected only - grey skin, milky white eyes, dark veins, dark red-black stains at the mouth, ordinary passenger clothes; ignore its background, its lights and its framing. In the grey previz the infected are near-black cylinders (under the light they can read dark grey).
@Image8 is a set plate of the closed gangway between carriages, in red light: look and light only, NEVER a shot.
@Image9 is a set plate of the last carriage's door seen from the gangway, in red light: look and light only, NEVER a shot.
@Image10 is the storyboard sheet of these exact 4 seconds, one row per shot with its key stills from the real camera (A = start, B = key moment, C = end): composition and blocking.
@Image10 is a storyboard sheet; panels, gutters and labels are planning marks only. No storyboard grid, split screen or collage in the output. The character sheets define identity. @Image8 and @Image9 are style references only.
Cylinder legend of the grey previz: every person is a plain colored cylinder with a cone nose that shows where the face points. Hugo bronze, Iván dark brown, Carmen light blue, Martina oatmeal, Tomás navy blue, the infected near-black.

LOCKS
CAST LOCK: CUT 1 ONLY HUGO. CUT 2 ONLY MARTINA, TOMÁS, IVÁN, CARMEN AND 3 INFECTED BEHIND THE CARRIAGE 5 DOOR. CUT 3 ONLY CARMEN AND 3 INFECTED.
HUGO: BOTH HANDS ON THE KEY; THE KEY STAYS IN THE LOCK AND DOES NOT TURN.
CARMEN: GRABBED FROM BEHIND BY THE LEFT SHOULDER OF HER COAT; HER RIGHT ARM REACHES TOWARD THE GROUP.
SIDES LOCK: IN CUT 2, MARTINA ON FRAME LEFT AND TOMÁS ON FRAME RIGHT, IVÁN BEHIND MARTINA, CARMEN BEHIND TOMÁS. IN CUT 3, THE CARRIAGE 5 DOOR IS ON FRAME RIGHT.
LIGHT LOCK: THE GANGWAY IS LIT ONLY BY ITS RED CEILING STRIP; NO WHITE TUBE, NO FLUORESCENT LIGHT.
NOBODY LOOKS INTO THE LENS.

SCENE CONTEXT
A night train. The group has escaped carriage 5 into the short closed gangway that joins it to the last carriage; the infected are right behind them. Hugo, the old conductor, is fighting an antique key that jams in the lock of the last carriage's door. These 4 seconds: the key still jammed, Iván slamming the carriage 5 door shut, and an infected arm smashing through its glass to grab Carmen. Held for the whole clip: wardrobe identical to the character sheets in every frame, never changing color; Hugo's cap stays on; Tomás's glasses stay on; Martina's coat stays open, her sweater cuffs over her knuckles; Carmen's bag stays on her left shoulder. The gangway has no windows.

ACTION
Hugo - GOAL: open the door. TACTIC: forces the key with both hands, throwing his body weight on it again and again.
Iván - GOAL: stop the infected. TACTIC: slams the carriage 5 door shut behind the group, then turns and shoves everyone toward Hugo.
Tomás - GOAL: get Martina to the door. TACTIC: crouched, pulls her by the hand, looking back at her.
Martina - GOAL: keep up. TACTIC: crouched, lets herself be pulled, looking back over her left shoulder at the carriage 5 door.
Carmen - GOAL: follow the group. TACTIC: last in line; when she is grabbed she reaches for the group with her right arm and screams toward Iván.
The infected - reach the carriage 5 door; one smashes its glass and grabs Carmen.

PHYSICS
Real time at 24 fps: no slow motion, no speed ramp. The key resists and springs back. The carriage 5 door slams with weight and shudders in its frame. The glass bursts into the gangway in a spray of small shards. Each yank jerks Carmen's whole body back against the door and she fights it with her feet planted; coats swing and settle. The whole train sways and rattles and the bodies sway with it. Handheld moves start late and stop with weight.

LIGHTING
Only the set's own sources, no fill: the red emergency strip on the gangway ceiling, from above. No white light anywhere in the gangway. Faces half in shadow; blacks fall to black. Through the carriage 5 door's glass, the red-lit carriage beyond; through the small window of the last carriage's door, dim red.

AUDIO
Continuous heavy rail rhythm and the rattle of the gangway plates. From 0.0s to 0.8s the jammed key grinding, a metal scrape at 0.3s. 1.0s: Iván slams the carriage 5 door, a heavy bang. Running feet and snarls behind the glass, getting closer. 2.5s: the glass bursts. From 2.6s: Carmen's choked scream and the door banging with each yank. Nobody speaks; no dialogue audio in this test. AUDIO LOCK, no words, soft Santiago Chilean voices: Hugo, 62, low worn voice - effort grunts on each wrench; Iván, 45, deep dry voice - a grunt on the slam and heavy breathing; Carmen, 54, warm firm voice - a choked scream; Martina, 29, and Tomás, 31 - fast breathing.

CUTS
CUT 1 (0 to 0.8s) - Close shot of the lock of the last carriage's door, seen from the gangway on the lock side, at lock height (about 1.3 m), 50mm. Frame left, in the foreground: Hugo in profile, facing the door, eyes on the lock; frame right and low: the lock with the antique key in it; center: the door's small window with the red interior. Camera: handheld, close; it moves in 2 to 5 cm each time Hugo throws his weight, two frames late, and comes back. At 0.0s Hugo is already forcing the key with both hands; at 0.3s he wrenches it a third time: it gives a few degrees and springs back; at 0.56s he throws his weight on it again. The key does not turn. - HARD CUT AT 0.8s
CUT 2 (0.8 to 2.3s) - Medium shot from the last carriage's door, where Hugo is, looking down the gangway toward carriage 5, at eye height (about 1.5 m), 28mm. Camera: handheld, active, above Tomás and Martina, who come in crouched; it jolts 2 frames after the slam and backs off 0.35 m because the group is coming at it; it ends looking for Carmen, who is left behind. Foreground: Martina on frame left and Tomás on frame right, crouched; he pulls her by the hand and looks back at her; she looks back over her left shoulder. Behind Martina, on frame left, Iván slams the open carriage 5 door shut at 1.0s; through its glass the infected run closer. Iván turns by his left and shoves the group toward Hugo, off-screen left of the camera. Carmen ends up last, on frame right behind Tomás, her back to the carriage 5 door. Above, the red strip of the gangway ceiling. - HARD CUT AT 2.3s
CUT 3 (2.3 to 4.0s) - The carriage 5 door, seen low (about 1.2 m) and three-quarter from the right side of the gangway, 35mm; the door on frame right. Carmen left of center, her back to the door, facing frame left, toward the group. Camera: handheld, low; it shakes 3 frames after the glass bursts and follows each yank 2 to 3 frames late. At 2.5s an infected arm with grey skin and short, broken, dirty nails smashes through the door's glass; at 2.58s its hand grabs Carmen by the left shoulder of her coat, from behind; from 2.63s it yanks her back against the door, three times, until the end. Carmen stretches her right arm toward the group at frame left and screams toward Iván, never toward the lens. Through the smashed glass, the infected who holds her; deeper in carriage 5, two more coming. - END OF CLIP AT 4.0s
Follow the storyboard panels in order, each a key frame: match camera position, framing, screen direction and action; cut only where the shot number changes. The panels are grey previz stand-ins for blocking only; every look comes from the references and this text.

Colored cylinders are blocking only: position, facing and path. Body, face and acting come from the character references.

No music. No subtitles, no captions, no on-screen text.
```
