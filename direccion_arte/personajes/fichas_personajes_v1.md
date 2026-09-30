# Fichas de personajes — v1 (propuesta de casting visual)

Base: `biblia/personajes.md` y `guion/cap01/cap01_v3.md`. Método y fases: `produccion/assets/plan_assets_v1.md`.
**Estado:** propuesta. Nada de esto está aprobado hasta la aprobación 1 del plan.

## Cómo leer cada ficha
- **Idea:** el personaje en una frase visual.
- **Ancla de identidad:** el rasgo que tiene que sobrevivir en todos los planos, incluso bajo luz roja y en miniatura.
- **En rojo se lee:** claro u oscuro. Bajo la luz de emergencia desaparece el color y los personajes se distinguen por valor y silueta.
- **Variables:** qué cambiar en MJ, **de a una por ronda**.

## El elenco junto

| Personaje | Silueta | En rojo se lee | Ancla |
|---|---|---|---|
| Martina | Suéter grande, mangas sobre las manos, pelo al hombro | Claro | Lunar en el pómulo izquierdo |
| Tomás | Chaqueta acolchada entallada, anteojos | Oscuro, líneas limpias | Anteojos de marco metálico fino |
| Diego | Chaqueta de lona clara, pelo lacio que le cae en la frente | Claro (la mancha se lee) | Pelo lacio largo y barba de tres días |
| Carmen | Abrigo largo y ancho, figura baja y firme | Oscuro con el uniforme claro asomando | Anteojos colgando de un cordón de cuentas |
| Iván | Hombros anchos, cuello grueso, cabeza rapada | Oscuro, con franjas reflectantes | Nariz quebrada y cabeza rapada |
| Don Hugo | Delgado, gorra de revisor, uniforme que le queda grande | Oscuro, botones que brillan | Bigote gris tupido y gorra |

**Regla del triángulo:** Tomás y Diego son dos formas distintas de ser querible. Tomás es el que ordena y cuida; Diego, el que se siente cercano y desordenado. Ninguno es más guapo que el otro de forma obvia.

**Parámetros de MJ 8.2:** los mismos de la exploración de VAGÓN 7 (`--raw --s 50 --preview`). Caras en `--ar 4:5`, vestuario en `--ar 2:3`. MJ 8.2 no tiene `--oref`: la identidad se fija después, en Weavy.

---

## Prompt común de corrección (GPT Image 2.5, en Weavy)

Se usa sobre la cara elegida en MJ, antes de unirla con el vestuario. Entrada: `image_1` = la cara elegida.

```
Photographic identity reference, not an illustration. Image 1 is the person: keep their face, bone structure, skin tone, age, hair, and every mark exactly as they are, including asymmetries, moles and scars. Do not beautify, do not smooth the skin, do not make the face more symmetrical. Fix only these problems: make the skin dry and matte with visible pores and no sheen or sweat; make the light soft, even and frontal with a gentle falloff to the right; replace the background with a plain mid-grey seamless backdrop; correct any anatomical errors in the ears, teeth, eyes and hairline. Head and shoulders, looking straight into the lens, neutral closed mouth. Natural color, no retouching look, no HDR, no digital sharpening. No text, no logos.
```

---

## MARTINA, 29 · La culpa
**Tarjeta:** «Vine a salvar mi relación.»

- **Idea:** la que se esconde dentro de su ropa. Mangas sobre las manos y el celular siempre boca abajo.
- **Ancla:** lunar pequeño en el pómulo izquierdo.
- **Cara:** cara angosta, nariz fuerte con un pequeño quiebre en el tabique, cejas gruesas y un poco desparejas, ojos hundidos con ojeras suaves, labios secos. Nada de maquillaje o solo un resto de delineador del día.
- **Pelo:** castaño oscuro, ondulado, al hombro, algo encrespado, metido detrás de la oreja derecha.
- **Vestuario:** suéter de lana gruesa color avena, con el cuello estirado; abrigo largo de lana gris carbón, abierto; jeans oscuros desteñidos; botines de cuero café gastados; cartera pequeña cruzada. El celular, con una funda simple gastada.
- **Evitar:** cara de Instagram, cejas perfectas, labios con relleno, ojos enormes.
- **Variables:** (1) la estructura de la cara: angosta / pómulos altos / cara más redonda; (2) el pelo: ondulado al hombro / tomado en un moño flojo / corto a la mandíbula; (3) el color de la piel: morena clara / oliva / trigueña.

**MJ · cara**
```
documentary portrait photograph of a 29-year-old South American woman, street casting, a real person, not a model, head and shoulders, looking straight into the lens with a guarded, tired stillness, narrow face, strong nose with a small bump on the bridge, thick dark eyebrows slightly uneven, deep-set dark brown eyes with faint shadows under them, a small mole on her left cheekbone, dry lips, visible pores and fine facial hair, no makeup, shoulder-length dark brown wavy hair a little frizzy, tucked behind her right ear, the collar of an oatmeal knit sweater, plain mid-grey backdrop, soft overcast window light from the left, dry matte skin, 85mm lens, Kodak Portra 400 film scan --ar 4:5 --raw --s 50 --preview --no beauty, glamour, retouching, makeup, symmetry
```

**MJ · vestuario (sin cara)**
```
full-length documentary photograph of a woman's night train travel outfit, framed from the chin down, her head out of frame, standing still with her arms relaxed, sleeves pulled over her hands: oversized oatmeal chunky wool sweater with a stretched collar, long charcoal grey wool coat worn open, faded dark blue jeans, worn brown leather ankle boots, a small crossbody bag, a phone with a plain worn case held face down in her right hand, lived-in clothes with natural creases and slight pilling, slim average build, plain mid-grey backdrop, soft even light, 50mm lens, film scan --ar 2:3 --raw --s 50 --preview --no face, logos, text, fashion pose
```

**Unión (GPT Image 2.5 y Nano Banana Pro en paralelo)** · `image_1` = `cara_martina`, `image_2` = `vest_martina` · 9:16
```
Photographic character reference, not an illustration. Image 1 is the identity: use this woman's face, hair, skin tone and the small mole on her left cheekbone exactly, without beautifying. Image 2 is wardrobe only: dress her in exactly these clothes and ignore any body or pose details from image 2. Full-body, standing in a neutral relaxed pose, facing the camera, sleeves pulled over her hands, a phone held face down in her right hand. Slim average build, about 1.63 m, natural adult proportions. Plain mid-grey seamless backdrop, soft even light from the front-left, dry matte skin with no sheen. Lived-in clothes with natural creases. The whole figure from head to shoes with space above and below. No text, no logos, no labels.
```

**Hoja de personaje (Nano Banana Pro y GPT Image 2.5)** · `image_1` = `ref_martina` · 16:9
```
Photographic character reference sheet of the woman in image 1, not an illustration. Top row: three full-body views side by side — front, left profile, back — with an identical face, hair, outfit and slim average proportions in all three. Bottom row: three head-and-shoulders close-ups — front, three-quarter left, right profile — with the same face, the same small mole on her left cheekbone and the same wavy hair tucked behind her right ear. Neutral still expression in every view. Plain mid-grey backdrop, soft even light, dry matte skin. No text, no labels, no numbers.
```

---

## TOMÁS, 31 · Los celos
**Tarjeta:** «Todavía creo en nosotros.»

- **Idea:** el que organizó el viaje. Todo ordenado, todo limpio, hasta que duda.
- **Ancla:** anteojos de marco metálico fino. **Uso dramático:** cuando se vuelve frío (1:16), la luz roja se refleja en los vidrios y le tapa los ojos.
- **Cara:** cara amable y bien afeitada, mandíbula apretada, mentón suave, orejas un poco salidas, una irritación leve de afeitada en el cuello. Pelo corto y ordenado, con partidura al costado.
- **Vestuario:** chaqueta acolchada azul marino entallada; suéter de merino gris carbón sobre una camiseta blanca; chinos oscuros; zapatillas blancas demasiado limpias para un tren; reloj de correa de cuero. **No usar camisa azul:** es la del hombre que se convierte.
- **Contextura:** media, un poco blanda. No es de gimnasio.
- **Evitar:** mandíbula de modelo, cara de villano, barba de diseño.
- **Variables:** (1) el marco de los anteojos: metálico fino / acetato negro delgado / sin anteojos; (2) el pelo: partidura al costado / corto parejo / algo ondulado; (3) la contextura: media / delgada.

**MJ · cara**
```
documentary portrait photograph of a 31-year-old South American man, street casting, a real person, not a model, head and shoulders, looking straight into the lens with a polite, controlled stillness, a kind clean-shaven face with a tight jaw and a soft chin, ears that stick out slightly, faint razor irritation on his neck, thin wire-rimmed glasses, short neat dark brown hair with a side part, visible pores, the collar of a charcoal merino sweater over a white t-shirt, plain mid-grey backdrop, soft overcast window light from the left, dry matte skin, 85mm lens, Kodak Portra 400 film scan --ar 4:5 --raw --s 50 --preview --no beauty, glamour, retouching, model jaw, stubble
```

**MJ · vestuario (sin cara)**
```
full-length documentary photograph of a man's neat travel outfit, framed from the chin down, his head out of frame, standing still with his arms relaxed: fitted navy blue quilted jacket zipped halfway, charcoal grey merino crewneck sweater over a white t-shirt, dark chinos, very clean white leather sneakers, a watch with a brown leather strap on his left wrist, tidy clothes with light natural creases, medium build slightly soft, plain mid-grey backdrop, soft even light, 50mm lens, film scan --ar 2:3 --raw --s 50 --preview --no face, logos, text, fashion pose, blue shirt
```

**Unión (GPT Image 2.5 y Nano Banana Pro en paralelo)** · `image_1` = `cara_tomas`, `image_2` = `vest_tomas` · 9:16
```
Photographic character reference, not an illustration. Image 1 is the identity: use this man's face, clean-shaven skin, side-parted hair and thin wire-rimmed glasses exactly, without beautifying. Image 2 is wardrobe only: dress him in exactly these clothes and ignore any body or pose details from image 2. Full-body, standing in a neutral relaxed pose, facing the camera, arms at his sides. Medium build, slightly soft, about 1.76 m, natural adult proportions. Plain mid-grey seamless backdrop, soft even light from the front-left, dry matte skin with no sheen, no reflections hiding his eyes. Tidy clothes with light natural creases. The whole figure from head to shoes with space above and below. No text, no logos, no labels.
```

**Hoja de personaje (Nano Banana Pro y GPT Image 2.5)** · `image_1` = `ref_tomas` · 16:9
```
Photographic character reference sheet of the man in image 1, not an illustration. Top row: three full-body views side by side — front, left profile, back — with an identical face, glasses, hair, outfit and medium build in all three. Bottom row: three head-and-shoulders close-ups — front, three-quarter left, right profile — with the same clean-shaven face, the same thin wire-rimmed glasses and the same side-parted hair. Neutral still expression in every view. Plain mid-grey backdrop, soft even light, dry matte skin. No text, no labels, no numbers.
```

---

## DIEGO, 30 · El que ruega por entrar
**Tarjeta:** ninguna hasta que aparece.

- **Idea:** el que viene de afuera. Tiene que dar pena dejarlo afuera: cara abierta, casi de niño, nada de «chico malo».
- **Ancla:** pelo negro lacio, largo hasta las cejas, y barba de tres días.
- **Cara:** cara abierta, cejas expresivas que se levantan en el centro, dientes un poco torcidos, ojos cafés cálidos, piel trigueña con marcas de acné antiguas en las mejillas.
- **Vestuario:** chaqueta de trabajo de lona **color piedra clara** (para que la mancha oscura de la manga se lea a través del vidrio bajo la luz roja); sudadera con capucha gris oscuro debajo; jeans negros; zapatillas gastadas; una mochila con una sola correa al hombro.
- **Herida (propuesta, confirmar):** antebrazo izquierdo. La manga clara está oscura desde el codo hasta el puño.
- **Evitar:** chaqueta de cuero, tatuajes, mandíbula de modelo, mirada intensa de galán.
- **Variables:** (1) el largo del pelo: hasta las cejas / hasta la mandíbula / corto desordenado; (2) la cara: abierta de niño / más angulosa; (3) la barba: tres días / una semana.

**MJ · cara**
```
documentary portrait photograph of a 30-year-old South American man, street casting, a real person, not a model, head and shoulders, looking straight into the lens with an open, unguarded stillness, a warm boyish face, expressive eyebrows that lift slightly in the middle, slightly crooked teeth visible between parted lips, warm brown eyes, light brown skin with faint old acne marks on the cheeks, three-day stubble, straight black hair long enough to fall onto his eyebrows, the hood of a dark grey hoodie, plain mid-grey backdrop, soft overcast window light from the left, dry matte skin, dry hair, 85mm lens, Kodak Portra 400 film scan --ar 4:5 --raw --s 50 --preview --no beauty, glamour, retouching, tattoos, leather jacket, intense stare
```

**MJ · vestuario (sin cara)**
```
full-length documentary photograph of a young man's everyday outfit, framed from the chin down, his head out of frame, standing still with his arms relaxed: light stone-colored canvas chore jacket with a worn collar and patch pockets, dark grey hoodie underneath with the hood out over the collar, black jeans faded at the knees, worn grey sneakers, a dark backpack hanging from one strap on his right shoulder, lived-in clothes with natural creases, slim wiry build, plain mid-grey backdrop, soft even light, 50mm lens, film scan --ar 2:3 --raw --s 50 --preview --no face, logos, text, fashion pose, leather
```

**Unión (GPT Image 2.5 y Nano Banana Pro en paralelo)** · `image_1` = `cara_diego`, `image_2` = `vest_diego` · 9:16
```
Photographic character reference, not an illustration. Image 1 is the identity: use this man's face, stubble, acne marks and straight black hair falling onto his eyebrows exactly, without beautifying. Image 2 is wardrobe only: dress him in exactly these clothes and ignore any body or pose details from image 2. Full-body, standing in a neutral relaxed pose, facing the camera, arms at his sides, the backpack on his right shoulder. Slim wiry build, about 1.74 m, natural adult proportions. Clean dry clothes, no stains. Plain mid-grey seamless backdrop, soft even light from the front-left, dry matte skin and dry hair with no sheen. The whole figure from head to shoes with space above and below. No text, no logos, no labels.
```

**Hoja de personaje (Nano Banana Pro y GPT Image 2.5)** · `image_1` = `ref_diego` · 16:9
```
Photographic character reference sheet of the man in image 1, not an illustration. Top row: three full-body views side by side — front, left profile, back — with an identical face, hair, outfit, backpack and slim wiry build in all three. Bottom row: three head-and-shoulders close-ups — front, three-quarter left, right profile — with the same face, the same three-day stubble and the same straight black hair falling onto his eyebrows. Neutral still expression in every view. Plain mid-grey backdrop, soft even light, dry matte skin. No text, no labels, no numbers.
```

**Estado: Diego mojado y herido (Nano Banana Pro)** · `image_1` = `ref_diego` · 9:16
```
Photographic continuity reference, not an illustration. Image 1 is the identity and the wardrobe: keep his face, hair, build and clothes exactly. Change only his state: he has been running through rain between train carriages. His hair is soaked and stuck to his forehead in dark strands. The light stone canvas jacket is darkened by rain on the shoulders and the upper back only. His left forearm is held against his chest: the left sleeve is soaked dark red-black from the elbow to the cuff, the fabric heavy and clinging, the hand below it streaked with dark red-black stains; no visible wound. Drops of water on his face, matte skin between the drops, not glossy. Full-body, standing, facing the camera. Plain mid-grey seamless backdrop, soft even light. No text, no logos.
```

---

## CARMEN, 54 · Proteger a la persona
**Tarjeta:** «Enfermera. Treinta años de turnos de noche.»

- **Idea:** viene saliendo de un turno. Cansada pero firme; es la que se acerca cuando todos retroceden.
- **Ancla:** anteojos de lectura colgando de un cordón de cuentas.
- **Prop propuesto (confirmar):** un reloj de enfermera prendido al uniforme. Es con lo que puede medir el tiempo de transformación: une su oficio con las reglas del mundo.
- **Cara:** cara redonda, arrugas de risa, bolsas bajo los ojos, papada suave, aros pequeños de oro. Pelo corto y rizado, teñido castaño rojizo, con **las raíces canosas a la vista**.
- **Vestuario:** uniforme clínico celeste desteñido (blusa y pantalón), arrugado, debajo de un abrigo largo de lana café oscuro; zuecos blancos gastados; una credencial en blanco dada vuelta en el bolsillo; un bolso grande de tela.
- **Contextura:** baja, robusta, centro de gravedad bajo.
- **Evitar:** «abuelita tierna» de comercial, pelo blanco perfecto, uniforme nuevo.
- **Variables:** (1) el pelo: rizado corto teñido / tomado con una pinza / canoso natural; (2) la cara: redonda / más alargada con rasgos marcados; (3) la piel: morena / clara con manchas de sol.

**MJ · cara**
```
documentary portrait photograph of a 54-year-old South American woman, street casting, a real person, not a model, head and shoulders, looking straight into the lens with a warm, steady stillness, a round face with deep laugh lines, heavy bags under her eyes, a soft double chin, small gold stud earrings, short curly hair dyed reddish brown with two centimeters of grey roots showing, reading glasses hanging on a beaded cord around her neck, visible pores and age spots, no makeup, the collar of faded light blue nurse scrubs under a dark brown wool coat, plain mid-grey backdrop, soft overcast window light from the left, dry matte skin, 85mm lens, Kodak Portra 400 film scan --ar 4:5 --raw --s 50 --preview --no beauty, glamour, retouching, perfect white hair, smile
```

**MJ · vestuario (sin cara)**
```
full-length documentary photograph of a nurse leaving a night shift, framed from the chin down, her head out of frame, standing still with her arms relaxed: faded light blue scrub top and trousers, creased and worn, under a long dark brown wool coat worn open, a nurse's fob watch pinned to the scrub top, a blank ID badge turned backwards in the breast pocket, worn white nursing clogs, a large canvas tote bag on her left shoulder, reading glasses hanging on a beaded cord, short and sturdy build, plain mid-grey backdrop, soft even light, 50mm lens, film scan --ar 2:3 --raw --s 50 --preview --no face, logos, text, hospital logo, fashion pose
```

**Unión (GPT Image 2.5 y Nano Banana Pro en paralelo)** · `image_1` = `cara_carmen`, `image_2` = `vest_carmen` · 9:16
```
Photographic character reference, not an illustration. Image 1 is the identity: use this woman's face, laugh lines, dyed curly hair with grey roots and the reading glasses on a beaded cord exactly, without beautifying or making her look younger. Image 2 is wardrobe only: dress her in exactly these clothes and ignore any body or pose details from image 2. Full-body, standing in a neutral relaxed pose, facing the camera, the tote bag on her left shoulder, the fob watch pinned to her scrub top. Short and sturdy build, about 1.55 m, natural adult proportions. Plain mid-grey seamless backdrop, soft even light from the front-left, dry matte skin with no sheen. Creased, worn clothes. The whole figure from head to shoes with space above and below. No text, no logos, no labels.
```

**Hoja de personaje (Nano Banana Pro y GPT Image 2.5)** · `image_1` = `ref_carmen` · 16:9
```
Photographic character reference sheet of the woman in image 1, not an illustration. Top row: three full-body views side by side — front, left profile, back — with an identical face, hair, outfit, tote bag and short sturdy build in all three. Bottom row: three head-and-shoulders close-ups — front, three-quarter left, right profile — with the same face, the same dyed curly hair with grey roots and the same reading glasses hanging on a beaded cord. Neutral still expression in every view. Plain mid-grey backdrop, soft even light, dry matte skin. No text, no labels, no numbers.
```

---

## IVÁN, 45 · Proteger al grupo
**Tarjeta:** «No confío en nadie. Por eso sigo vivo.»

- **Idea:** puro músculo que en realidad es miedo. Mira a todos desde su asiento.
- **Ancla:** nariz quebrada y aplastada, cabeza rapada.
- **Cara:** cara ancha y curtida, piel quemada por el sol de obra, arruga profunda entre las cejas, barba de dos días con manchas canosas, una cicatriz vieja en el labio superior. Ojos chicos y atentos.
- **Vestuario:** chaqueta de trabajo de lona gruesa café oscuro con **franjas reflectantes gastadas** en los brazos (se encienden con las linternas en el capítulo 3); sudadera gris debajo; pantalón de trabajo; botas de seguridad con polvo de cemento **solo en las botas y en las rodillas**.
- **Prop para más adelante:** una foto de su hijo en la billetera.
- **Contextura:** robusto, hombros anchos, cuello grueso.
- **Evitar:** soldado de videojuego, músculos de gimnasio, mirada de villano.
- **Variables:** (1) el pelo: rapado / muy corto canoso; (2) la contextura: robusto / grueso con barriga; (3) la barba: dos días / bigote.

**MJ · cara**
```
documentary portrait photograph of a 45-year-old South American construction worker, street casting, a real person, not a model, head and shoulders, looking straight into the lens with a wary, watchful stillness, a broad weathered face, sunburnt skin on his forehead and neck, a broken flattened nose, a deep vertical crease between his eyebrows, small attentive eyes, two-day stubble with grey patches, a faint old scar on his upper lip, shaved head, thick neck, the collar of a heavy dark brown canvas work jacket over a grey hoodie, plain mid-grey backdrop, soft overcast window light from the left, dry matte skin, 85mm lens, Kodak Portra 400 film scan --ar 4:5 --raw --s 50 --preview --no beauty, glamour, retouching, soldier, tactical gear, tattoos
```

**MJ · vestuario (sin cara)**
```
full-length documentary photograph of a construction worker's outfit after a shift, framed from the chin down, his head out of frame, standing still with his arms relaxed: heavy dark brown canvas work jacket with worn silver reflective strips around both upper arms, grey hoodie underneath, dark grey work trousers with pale cement dust on the knees only, scuffed brown steel-toe boots with cement dust on the toes only, thick calloused hands, stocky build with broad shoulders, plain mid-grey backdrop, soft even light, 50mm lens, film scan --ar 2:3 --raw --s 50 --preview --no face, logos, text, company logo, helmet, fashion pose
```

**Unión (GPT Image 2.5 y Nano Banana Pro en paralelo)** · `image_1` = `cara_ivan`, `image_2` = `vest_ivan` · 9:16
```
Photographic character reference, not an illustration. Image 1 is the identity: use this man's face, broken nose, shaved head, sunburnt skin and grey-patched stubble exactly, without beautifying. Image 2 is wardrobe only: dress him in exactly these clothes and ignore any body or pose details from image 2. Full-body, standing in a neutral relaxed pose, facing the camera, arms at his sides. Stocky build with broad shoulders and a thick neck, about 1.78 m, natural adult proportions, not a bodybuilder. Plain mid-grey seamless backdrop, soft even light from the front-left, dry matte skin with no sheen. Cement dust only on the knees and boot toes. The whole figure from head to shoes with space above and below. No text, no logos, no labels.
```

**Hoja de personaje (Nano Banana Pro y GPT Image 2.5)** · `image_1` = `ref_ivan` · 16:9
```
Photographic character reference sheet of the man in image 1, not an illustration. Top row: three full-body views side by side — front, left profile, back — with an identical face, shaved head, outfit, reflective strips and stocky build in all three. Bottom row: three head-and-shoulders close-ups — front, three-quarter left, right profile — with the same face, the same broken flattened nose and the same grey-patched stubble. Neutral still expression in every view. Plain mid-grey backdrop, soft even light, dry matte skin. No text, no labels, no numbers.
```

---

## DON HUGO, 62 · La ley
**Tarjeta:** «Revisor. Este es mi tren.»

- **Idea:** treinta y dos años en el mismo tren. El uniforme le queda grande: se lo dieron cuando era más joven y más ancho.
- **Ancla:** bigote gris tupido y gorra de revisor.
- **Cara:** cara larga y delgada, surcos profundos junto a la boca, manchas de edad, ojos húmedos y cansados, orejas grandes, pelo gris peinado con cuidado bajo la gorra.
- **Vestuario:** uniforme de revisor azul marino, viejo y cepillado, con botones de bronce opacos; gorra con un emblema bordado **de una línea ferroviaria inventada** (el logo está pendiente de diseño propio); perforadora de boletos colgando de una cadena; una llave de hierro antigua en un aro, en el cinturón; zapatos negros lustrados pero gastados.
- **El revólver** no va en el vestuario: es un prop aparte (`prop_revolver`) y se agrega en el keyframe.
- **Contextura:** delgado, un poco encorvado.
- **Evitar:** militar, policía, «abuelo sabio» de película.
- **Variables:** (1) el bigote: tupido / fino y recortado; (2) la cara: larga y delgada / más ancha y caída; (3) el pelo: gris peinado / casi calvo.

**MJ · cara**
```
documentary portrait photograph of a 62-year-old South American train conductor, street casting, a real person, not a model, head and shoulders, looking straight into the lens with a slow, tired stillness, a long thin face, deep lines beside his mouth, age spots on his temples, watery tired eyes, large ears, a thick grey mustache, carefully combed grey hair under an old navy conductor's cap with a small plain embroidered train emblem, visible pores, the collar of a worn navy uniform jacket with dull brass buttons, plain mid-grey backdrop, soft overcast window light from the left, dry matte skin, 85mm lens, Kodak Portra 400 film scan --ar 4:5 --raw --s 50 --preview --no beauty, glamour, retouching, military, police, logo, text
```

**MJ · vestuario (sin cara)**
```
full-length documentary photograph of an old train conductor's uniform, framed from the chin down, his head out of frame, standing still with his arms relaxed: worn navy blue conductor's jacket one size too big, brushed and cared for, with dull brass buttons, matching navy trousers with a sharp crease, a ticket punch hanging from a short chain at his belt, a single large antique iron key on a ring clipped to his belt, polished but worn black leather shoes, thin slightly stooped build, plain mid-grey backdrop, soft even light, 50mm lens, film scan --ar 2:3 --raw --s 50 --preview --no face, logos, text, badges, military, police, gun, fashion pose
```

**Unión (GPT Image 2.5 y Nano Banana Pro en paralelo)** · `image_1` = `cara_hugo`, `image_2` = `vest_hugo` · 9:16
```
Photographic character reference, not an illustration. Image 1 is the identity: use this man's face, thick grey mustache, age spots, large ears and navy conductor's cap exactly, without beautifying or making him look younger. Image 2 is wardrobe only: dress him in exactly this uniform, one size too big for him, and ignore any body or pose details from image 2. Full-body, standing in a neutral relaxed pose, facing the camera, arms at his sides, the ticket punch and the antique iron key hanging at his belt. Thin, slightly stooped build, about 1.70 m, natural adult proportions. No weapon visible. Plain mid-grey seamless backdrop, soft even light from the front-left, dry matte skin with no sheen. The whole figure from head to shoes with space above and below. No text, no logos, no labels.
```

**Hoja de personaje (Nano Banana Pro y GPT Image 2.5)** · `image_1` = `ref_hugo` · 16:9
```
Photographic character reference sheet of the man in image 1, not an illustration. Top row: three full-body views side by side — front, left profile, back — with an identical face, cap, uniform, key and thin stooped build in all three. Bottom row: three head-and-shoulders close-ups — front, three-quarter left, right profile — with the same face, the same thick grey mustache and the same navy conductor's cap. Neutral still expression in every view. Plain mid-grey backdrop, soft even light, dry matte skin. No text, no labels, no numbers.
```

---

## Extras del capítulo 1 (prioridad 2)

**El hombre de camisa azul y su esposa (0:19).** La camisa tiene que ser de un **azul fuerte y claro**, para que el público la recuerde cuando Iván dice «el de la camisa azul». Es el único azul fuerte del elenco.

**MJ · pareja**
```
documentary photograph of a South American couple in their late 40s standing side by side on a night train, street casting, real people, not models, waist-up, looking straight into the lens with a plain stillness: the man is heavyset with a receding hairline and a short grey beard, wearing a bright light blue button-up shirt tucked into grey trousers; the woman is short with shoulder-length straight black hair and a beige cardigan, holding his arm, plain mid-grey backdrop, soft even light, dry matte skin, 50mm lens, Kodak Portra 400 film scan --ar 4:5 --raw --s 50 --preview --no beauty, glamour, retouching, logos, text
```
