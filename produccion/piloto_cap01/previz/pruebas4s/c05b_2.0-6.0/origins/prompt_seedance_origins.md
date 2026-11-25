# c05b_2.0-6.0 · prueba «formato ORIGINS» · Seedance 2.5 US (fal)

> **Borrador del 25-nov-2026. Nada de esto se ha corrido.** No se sube un archivo ni se llama a fal sin el OK escrito de Cristian. Higgsfield no se usa.

## Qué es

Es el mismo tramo de 4 s que el brazo A de `../prompt_seedance_A.md` (gris como video de referencia), con el prompt reescrito en el formato que Cristian describió de ORIGINS EP. 01: ZARA (Higgsfield Selected, 23-nov-2026). El formato es un prompt largo por secciones (estilo, cámara, textura, sonido, guion cronometrado y assets), un bloque CRITICAL y un resumen al final. **No pude leer los prompts originales de ORIGINS** (ver «No verificado»), así que el formato sale de la descripción de Cristian y no de un prompt real.

El único cambio contra el brazo A es la forma del prompt. El tramo, las referencias, la semilla y el gris son los mismos, así que la comparación mide solo el formato.

## Plano

- **Llamada c05b, de 2,0 a 6,0 s.** El plano que importa es **b5_p7, «Entran en tropel»**: de 1,5 a 4,0 s en la prueba. Es blocking y geografía puros: cinco personas entran por los dos lados de la cámara, con la puerta, el tubo frío, Hugo afuera y tres infectados al fondo.
- b5_p7 dura 2,5 s, y Seedance y Kling piden 4 s como mínimo. Por eso la ventana arranca con la cola de **b5_p6** (la llave gira, 1,5 s), y hay un corte duro en 1,5 s. Ese corte pone a prueba la idea (1) de ORIGINS: una generación con planos cronometrados y cortes duros.
- Ningún plano de blocking de las llamadas con gris en el Drive (c00b, c03b, c04a, c04b, c05a y c05b) dura 4 s solo. El más largo es b4_p6, con 3,0 s. La alternativa sería `c04b_4.0-8.0` (1 s de b4_p5 y 3 s de b4_p6), que ya tiene borrador.

## Entradas, en este orden

| En el prompt | Campo | Archivo | Se sube desde |
|---|---|---|---|
| @Video1 | `video_urls[0]` | `video_1.mp4` (gris recortado, 4,000 s, 720×1280, 24 fps, sin audio) | `prueba4s_c05b_2.0-6.0.zip` en el Drive (`pruebas4s_borrador/`) |
| @Image1 | `image_urls[0]` | `HOJA_hugo.png` (reducida a 2.048 px de lado largo) | `imagenes/04_aprobados` |
| @Image2 | `image_urls[1]` | `HOJA_ivan.png` | ídem |
| @Image3 | `image_urls[2]` | `HOJA_carmen.png` | ídem |
| @Image4 | `image_urls[3]` | `HOJA_martina.png` | ídem |
| @Image5 | `image_urls[4]` | `HOJA_tomas.png` | ídem |
| @Image6 | `image_urls[5]` | `PROP_llave_y_cerradura.png` | ídem |
| @Image7 | `image_urls[6]` | `ref_infectados.jpg` | `direccion_arte/referencias/` |
| @Image8 | `image_urls[7]` | `F04_rojo_puerta_desde_fuelle.png` | `imagenes/04_aprobados` |
| @Image9 | `image_urls[8]` | `F03_rojo_puerta_desde_dentro_0-45.png` | ídem |

Son las mismas entradas y en el mismo orden que el brazo A. Las planchas F04 y F03 hacen de los «plates still» de locación de la idea (4): ya existen y están aprobadas, así que no hay que generar nada.

## Prompt (completo y listo para pegar)

```text
[EUV CAP01 - BLOCK 5 - c05b 2.0-6.0 - INT. GANGWAY / LAST CARRIAGE - NIGHT - 9:16 VERTICAL - 4s - 2 SHOTS, 1 HARD CUT - REAL TIME 24 FPS - origins-format test v1]

CRITICAL
1. @Video1 is the master for camera position, lens, camera path, blocking, timing and the cut. Match it shot by shot; do not add pans, zooms, push-ins or cuts that are not in it. Exactly one hard cut, at 1.5s.
2. Colored cylinders are blocking only: position, facing and path. Body, face and acting come from the character references.
3. Nobody in the output is a cylinder, a mannequin or a grey figure: every person has the body, face, hands and wardrobe of their character sheet.
4. ONLY 8 PEOPLE: HUGO, IVAN, CARMEN, MARTINA, TOMAS AND 3 INFECTED. SHOT 1 SHOWS ONLY HUGO.
5. SIDES: seen from inside the last carriage, Martina comes in on frame left, Tomas and Carmen on frame right; Hugo stays outside, left of the doorway.
6. Hugo holds the key in his RIGHT hand from the moment it leaves the lock to the end. Carmen keeps her cut RIGHT palm pressed to her chest.
7. The cold white tube exists only inside the last carriage, above its door. The gangway has no white light, only its red ceiling strip.
8. Nobody looks into the lens. No slow motion. No music, no subtitles, no on-screen text.

STYLE
Grounded night-train horror shot on a real set, like a handheld cinema camera in a cramped space. Low-key practical light only, deep blacks, red emergency light, one cold edge light. Faces half in shadow. No glossy CGI look, no beauty lighting, no lens flares, no color grade beyond what the lights give.

CAMERA
Shot 1: handheld close, 50mm, at key height (about 1.2 m), on the lock side of the door, seen from the gangway. Small, slow handheld; it eases in 3 cm with the clack and jolts 3 frames after each impact.
Shot 2: handheld at standing eye height (about 1.55 m), 24mm, inside the last carriage facing its only door. It backs away about 0.7 m because the group is coming straight at it: starts 2 frames late, stops with weight, one jolt 3 frames after Martina stumbles. The camera never floats and never pans to follow anyone.

TEXTURE
Fine natural film grain. Worn steel, scuffed paint, dirty glass, old rubber gangway folds. Wool coats, canvas, quilted nylon and cotton scrubs read as real fabric with weight. Skin with pores, sweat and tiredness. Dark red-black stains only on the infected and on Carmen's palm.

SOUND
Continuous heavy rail rhythm and the rattle of the gangway plates. 0.15s and 0.3s: the key grinding in the lock. 0.45s: a hard metallic clack as it turns. 0.72s: off-screen, behind the camera, the crash of the carriage 5 door bursting into the gangway, then running feet and snarls getting closer. 1.08s: a shoulder thud and groaning hinges. From 1.5s: scrambling feet, a toe knocking the threshold at 2.2s and 2.3s, ragged breathing. No words: breaths and effort only, soft Santiago Chilean voices - Hugo, 62, one strained grunt on the shoulder blow; Ivan, 45, heavy breathing through his teeth; Carmen, 54, one short choked gasp when she stumbles; Martina, 29, a sharp intake of breath when she stumbles; Tomas, 31, fast breathing.

SCRIPT
SHOT 1 (0.0 to 1.5s) - Close on the lock of the last carriage's door. Frame left, in the foreground: Hugo in profile, facing the door, eyes on the lock. Frame right: the lock with the antique key in it. Above center: the door's small window, dim red behind it. 0.0s: Hugo already throws his weight on the key with both hands. 0.15s: he wrenches it again and it slips back. 0.45s: it turns a quarter turn in one snap. 0.6s to 0.9s: his right hand pulls the key out and closes around it. 0.72s: his shoulders flinch at the crash behind him; he does not turn. 1.08s: he rams the door with his shoulder; the heavy steel door swings inward, away from camera, on the right of frame. 1.5s: he steps back to the lock side, turning his head over his left shoulder toward the gangway, away from the lens. HARD CUT AT 1.5s.
SHOT 2 (1.5 to 4.0s) - Inside the last carriage, looking at its only door. Doorway at center; the door is wide open inward and its leaf rests against the right side; the cold tube glows above the frame, inside. Through the doorway: the short red gangway and, at its far end, the carriage 5 door burst open and hanging on the left, glass smashed, three infected running down the gangway behind the group. 1.5s: Tomas is already at the doorway on frame right, his right hand dragging Martina by her left hand, looking back at her; Martina half a step behind him on frame left, eyes on the floor. 2.2s: just past the threshold her toe catches and she stumbles forward two steps; his grip keeps her up. Behind them Ivan shoves Carmen through by the back. 2.3s: Carmen stumbles, head down, right hand pressed to her chest, her bag on her left shoulder. They pass on both sides of the camera: Martina on the left, Tomas and Carmen on the right; Ivan comes in behind Carmen and turns to face the door. Outside, left of the doorway, Hugo stands by the lock, key in his right fist, waving them in with his free hand and watching the infected. 3.0s: the first infected is less than a meter from him; Hugo backs toward the threshold to come in last. 4.0s: he is stepping backward over it. END OF CLIP AT 4.0s.
Gazes: Tomas on Martina, Martina on the floor, Carmen on the floor ahead of her, Ivan on Carmen's back and then on the door, Hugo on the infected.
Physics: bodies have weight and inertia; a stumble carries two steps before it recovers; coats swing and settle; the whole train sways and the bodies sway with it.

ASSETS
@Video1 - grey previz of these exact 4 seconds, rendered from the real camera and lens. Master for camera, blocking, timing and the cut. Cylinder legend: every person is a plain colored cylinder with a cone nose that shows where the face points - Hugo bronze, Ivan dark brown, Carmen light blue, Martina oatmeal, Tomas navy blue, the infected near-black. Never copy its grey surfaces, its flat shading or the cylinder shapes.
@Image1 - Hugo, 62, the train conductor: long thin face, thick grey moustache, tired watery eyes, navy conductor's cap with a plain embroidered wheel badge and no letters, old brushed navy uniform with dull bronze buttons, whistle on a cord; slim, slightly stooped. Cap stays on. Identity and wardrobe only, not framing.
@Image2 - Ivan, 45: shaved head, broken flattened nose, wide weathered sunburnt face, two-day stubble with grey patches, heavy dark brown canvas work jacket with worn reflective stripes over a grey hoodie, work trousers, safety boots with cement dust on boots and knees; broad shoulders, thick neck. Identity and wardrobe only.
@Image3 - Carmen, 54, night-shift nurse: round face, short curly reddish-brown dyed hair with grey roots, reading glasses on a beaded cord, faded light-blue scrubs under a long dark brown wool coat, large cloth bag on her LEFT shoulder, worn white clogs; short and sturdy. Identity and wardrobe only.
@Image4 - Martina, 29: narrow face, small mole on her LEFT cheekbone, shoulder-length dark brown wavy hair tucked behind her right ear, oversized oatmeal chunky wool sweater with cuffs over her knuckles, long charcoal wool coat always open, faded dark jeans, worn brown leather boots. Identity and wardrobe only.
@Image5 - Tomas, 31: thin full metal-frame glasses always on, short neat dark brown hair with a side part, clean-shaven, fitted navy quilted jacket over a charcoal sweater, dark chinos, white sneakers; average, slightly soft build. Identity and wardrobe only.
@Image6 - the antique iron key and the lock of the last carriage's door: object identity only.
@Image7 - the look of the infected only: grey skin, milky white eyes, dark veins, dark red-black stains at the mouth, ordinary passenger clothes. Ignore its background, light and framing.
@Image8 - location plate: the last carriage's door seen from the gangway, red light. Look and light for shot 1 only, never a shot.
@Image9 - location plate: the last carriage's door seen from inside, red emergency light. Look and light for shot 2 only, never a shot.
Ignore the layout, labels and backdrop of every character sheet. Wardrobe identical to the sheets in every frame, never changing color.

RECAP
Two shots, one hard cut at 1.5s, camera and paths exactly as @Video1. Real people from @Image1 to @Image5, never cylinders. Martina left, Tomas and Carmen right, Hugo outside left of the doorway with the key in his right hand. Cold tube only inside, above the door. Nobody looks into the lens. Real time, no music, no text.
```
