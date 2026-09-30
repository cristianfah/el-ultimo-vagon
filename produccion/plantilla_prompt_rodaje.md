# Plantilla de prompt de rodaje (imagen)

Cada prompt de fotograma es una **orden de rodaje**, no una descripción de look. Se escribe en inglés y usa siempre los siete bloques:

```
FILM STILL: what kind of image this is + the role of each reference image
MOMENT: the exact beat of action, one frame before or after something happens
COMPOSITION: 9:16 vertical, camera height and position, where each character sits in the frame, foreground occluder, what falls into darkness
LENS: camera body, lens series, focal length, aperture, focus point, falloff, specific lens artifacts
LIGHT: each practical source with position, color temperature and intensity; contrast ratio; exposure
TEXTURE: exactly where there is water, blood and dirt, and where there is none
FINISH: film stock, grain, micro-contrast, color separation
```

## Ejemplo aprobado como método (prueba de interior de VAGÓN 7)

```
Film still from a feature film, not an illustration. Image 1 is the woman, image 2 is the man, image 3 is the carriage interior: match their faces, hair, wardrobe and the carriage exactly.

MOMENT: One second after a fight inside the dark train carriage. The woman has just turned toward a sound behind the camera, weight on her back foot, the red fire axe hanging low in her right hand, lips parted, catching her breath. The man stands six meters behind her in the far doorway, half in shadow, knife lowered, looking at her, not at the threat.

COMPOSITION: Camera at chest height, slightly low, placed in the aisle. The woman fills the left third from the waist up, three-quarter profile, her eyes on the upper third line. The man is small in the upper right, framed by the door frame. A dark out-of-focus seat back fills the lower-left corner as a foreground occluder. The ceiling and luggage rack fall into darkness at the top of the frame.

LENS: Shot on ARRI Alexa 35 with a Cooke S4 32mm spherical lens at T2. Focus on the woman's near eye; the man is softly out of focus. Gentle natural focus falloff, slight barrel curvature at the edges, soft halation around the fluorescent tube, faint veiling flare. No anamorphic streaks.

LIGHT: Only practical sources. One flickering fluorescent tube above the man, cold 5600K and hard, works as a backlight and rims his shoulders and her hair. Low red emergency lights along the walls, dim and deep red, spill across the floor and the side of her face; the other side of her face falls to near black. Light haze in the air catches the tube. Contrast ratio 8:1, one stop underexposed, deep blacks that keep detail, highlights that roll off softly.

TEXTURE: Real skin with pores and a light sheen of sweat, matte, not glossy. Rain only on the window glass behind her, streaks blurred by depth of field. Two dry dark smears on the lower window, nothing dripping. Damp matte clothing with natural folds. The axe head has a worn, used finish with a dark stain on the blade edge only.

FINISH: Kodak Vision3 500T film scan look, fine organic grain, soft natural micro-contrast, no digital sharpening, no HDR look. Color separation limited to deep red, cold cyan-white and near-black.
```

## Reglas
- **Correr en paralelo en GPT Image 2.5 y en Nano Banana Pro** y comparar. En la experiencia del estudio, GPT se deforma con prompts largos.
- **Generar a resolución nativa.** Escalar al final con Magnific o Topaz en creatividad baja.
- **Referencias de identidad en piel seca y luz neutra.** Si la referencia viene con la piel mojada, ese brillo se arrastra a todas las imágenes.
