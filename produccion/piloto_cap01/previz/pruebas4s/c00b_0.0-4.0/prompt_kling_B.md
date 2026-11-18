# c00b_0.0-4.0 · Kling 4.0 Omni-Ref (MCP) · brazo B (hoja de storyboard como imagen, sin video)

> **Borrador. No se envía sin el OK de Cristian.** Mismo prompt base que `prompt_kling_A.md`, `prompt_seedance_A.md`, `prompt_seedance_B.md`: cambian solo las referencias y las líneas fijas del brazo.

**Llamada:** MCP de Kling, `omni_ref_video` · `model` `kling-video-v4_0` · `resolution` 720p · `duration` 4 · `aspect_ratio` 9:16 · `imageCount` 1 · `prefer_multi_shots` true · `enable_audio` true · sin `audio_1`. Payload: `payload_kling.json` → `B`.

**Ventana:** c00b, de 0,0 a 4,0 s de la llamada · planos dentro de la prueba: b0_p3 0,0–2,0 · b0_p4 2,0–4,0.

**Entradas, en este orden:**

| En el prompt | Campo | Archivo | Se sube desde |
|---|---|---|---|
| 图片1 | `image_1` | `HOJA_martina.png` | `$TRABAJO/refs/personajes__HOJA_martina.png` |
| 图片2 | `image_2` | `HOJA_extra_pareja_camisa_azul.png` | `$TRABAJO/refs/personajes__HOJA_extra_pareja_camisa_azul.png` |
| 图片3 | `image_3` | `PROP_maletin_v2.png` | `$TRABAJO/refs/props__PROP_maletin_v2.png` |
| 图片4 | `image_4` | `F08_v2_ambar_bajo.png` | `REPO/produccion/pruebas/cap01_animatic_v3/assets/F08_v2_ambar_bajo.png` |
| 图片5 | `image_5` | `hoja_storyboard.jpg` | `$PREVIZ_TRABAJO/pruebas4s/c00b_0.0-4.0/hoja_storyboard.jpg` |

**Prompt** (7060 caracteres, completo y listo para pegar):

```text
[EUV CAP01 - BLOQUE 0 - INT. CARRIAGE 2 - NOCHE - HANDHELD WITH SHORT PAN, 35MM / LOCKED OFF, 24MM - 4s - 2 CUTS - REAL TIME 24 FPS, NO SLOW MOTION - 9:16 - prueba4s v1]

REFERENCES
图片1 is Martina, 29: identity and wardrobe only, not framing - a narrow face, a small mole on her LEFT cheekbone, shoulder-length dark brown wavy hair tucked behind her right ear, an oversized oatmeal chunky wool sweater whose cuffs cover her knuckles, a long charcoal wool coat always worn open, faded dark jeans, worn brown leather boots. Ignore the sheet layout and backdrop. In the grey previz she is the oatmeal cylinder.
图片2 is the couple in their late 40s: identity and wardrobe only, not framing - the man is heavyset, with a receding hairline and a short grey beard, in a bright cobalt-blue button-up shirt and grey trousers; the woman is short, with shoulder-length straight black hair and a beige cardigan. Ignore the sheet layout and backdrop. In the grey previz the man is the strong-blue cylinder and his wife the pinkish-beige one.
图片3 is the briefcase: a dark body with gold-toned metal corners and two metal clasps; object identity only, not framing.
图片4 is a set plate of carriage 2 at night with only two or three reading lamps lit: look and light only, NEVER a shot.
图片5 is the storyboard sheet of these exact 4 seconds, one row per shot with its key stills from the real camera (A = start, B = key moment, C = end): composition and blocking.
图片5 is a storyboard sheet; panels, gutters and labels are planning marks only. No storyboard grid, split screen or collage in the output. The character sheets define identity. 图片4 is a style reference only.
Cylinder legend of the grey previz: every person is a plain colored cylinder with a cone nose that shows where the face points. Martina oatmeal; the man in the blue shirt strong blue; his wife pinkish beige; the other passengers, the woman reading among them, grey.

LOCKS
CAST LOCK: ONLY 5 PEOPLE - THE MAN IN THE BLUE SHIRT, HIS WIFE, MARTINA, THE WOMAN READING AND ONE SLEEPING PASSENGER FAR BACK. CUT 1 SHOWS ONLY THE COUPLE AND MARTINA.
BRIEFCASE: UNDER THE MAN'S SEAT, ON THE AISLE SIDE; ONLY ITS METAL CORNER SHOWS; IT DOES NOT MOVE.
SIDES LOCK: CUT 1 OPENS WITH THE MAN ON FRAME LEFT AGAINST THE WINDOW AND HIS WIFE ON FRAME RIGHT; AFTER THE PAN, THE WIFE IS ON FRAME LEFT AND MARTINA ON FRAME RIGHT. IN CUT 2 THE WOMAN READING IS FAR BACK ON FRAME RIGHT.
LIGHT LOCK: ONLY TWO OR THREE READING LAMPS LIT; EVERYTHING ELSE DARK.
NOBODY LOOKS INTO THE LENS.

SCENE CONTEXT
Carriage 2 of a night train, near midnight; almost everyone sleeps in the dark. Martina has just pushed a briefcase under the seat of a sleeping couple and has to get away without anyone seeing her. These 4 seconds are the man stirring while she freezes, then her walking away down the aisle. Held for the whole clip: wardrobe identical to the character sheets in every frame, never changing color; Martina's charcoal coat stays open and her oatmeal sweater cuffs cover her knuckles and wrists; the man's bright blue shirt; the wife's beige cardigan. The side windows show night with rain on the outside of the glass.

ACTION
Martina - GOAL: leave without anyone noticing her. TACTIC: freezes mid-turn with her right hand on the back of the couple's seat and holds her breath; then walks away fast, without running and without looking back.
The man in the blue shirt - asleep. GOAL: stay asleep. TACTIC: shifts, gives one short snore and settles, unaware of her.
His wife - asleep on his shoulder; she does not wake.
The woman reading - GOAL: keep reading. TACTIC: never lifts her eyes from her book.

PHYSICS
Real time at 24 fps: no slow motion. The whole carriage sways gently with the rails and the sleeping bodies sway with it; the man's head slides down the glass under its own weight and stops. Martina's open coat swings as she turns and walks; her steps are quick and light. The briefcase does not move. The train's sway is in the bodies, not in the camera.

LIGHTING
Only practical sources, no fill: only two or three warm amber reading lamps are lit - one over the couple's row, one over the woman reading across the aisle, one far back near the rear door - with darkness between them. Faces half in shadow; blacks fall to black. The side windows are deep night with rain streaks on the outside of the glass and faint reflections.

AUDIO
Continuous rail rhythm and a soft carriage rattle; rain ticking on the windows. 0.55s: one short snore. From 0.75s to 1.05s: the faint squeak of his head sliding on the glass. Martina's held breath. From 2.0s: her quick, soft footsteps on the carriage floor. Nobody speaks. AUDIO LOCK, no words: the man in the blue shirt, a heavyset man in his late 40s - one short, low snore; Martina, 29, low husky voice - only a held breath through the nose.

CUTS
CUT 1 (0 to 2.0s) - Medium shot from seated eye height (about 1.25 m), from the aisle just in front of the couple's row, looking toward the rear of the carriage, 35mm; the edge of the seat back in front sits low on frame left. Frame left: the man asleep with his head against the window; frame right: his wife asleep on his shoulder in the aisle seat. Camera: handheld, small and slow; between 0.98s and 1.28s a quick short pan (about 22 degrees) from him to Martina, because she is the one watching him; it overshoots a little and settles back at 1.44s. At 0.0s the man is already stirring; at 0.55s one short snore; from 0.75s to 1.05s his head slides down the window glass. Martina stands in the aisle just behind the wife's seat, already turning toward the rear; at 0.62s she freezes with her eyes on him, her right hand on the back of the couple's seat, holding her breath. After the pan: the wife on frame left, Martina standing on frame right, frozen. - HARD CUT AT 2.0s
CUT 2 (2.0 to 4.0s) - Wide shot down the aisle toward the rear of the carriage, from seated eye height (about 1.25 m), tilted slightly down, 24mm. Low on frame left, in the foreground and out of focus: the metal corner of the briefcase showing under the man's seat. At center: Martina, her back to us, walking away down the aisle. Far back on frame right, across the aisle: the woman reading under her lamp; further back on frame left, a sleeping passenger. Camera: locked off, no push-in, only the train's vibration, because the secret stays still while she leaves. At 2.0s Martina is already stepping out of the foreground; she walks away fast, without running and without looking back; at about 3.45s she passes the woman reading, who does not look up; at 4.0s she is still walking. - END OF CLIP AT 4.0s
Follow the storyboard panels in order, each a key frame: match camera position, framing, screen direction and action; cut only where the shot number changes. The panels are grey previz stand-ins for blocking only; every look comes from the references and this text.

Colored cylinders are blocking only: position, facing and path. Body, face and acting come from the character references.

No music. No subtitles, no captions, no on-screen text.
```
