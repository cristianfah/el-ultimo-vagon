# Set: el último vagón — v1 (propuesta)

Base: `guion/cap01/cap01_v3.md`, `biblia/premisa.md`, `biblia/arco_temporada.md` y la librea de VAGÓN 7 (`archivo/vagon7/VAGON7_Guion_Biblia_v1.md`, sección 4.5).
Método: `produccion/assets/plan_assets_v1.md`, fase 4.
**Estado:** propuesta, pendiente de las imágenes de referencia de Cristian.

## 1. La idea del set

**Un vagón viejo que alguien cuidó por treinta años.** Es el vagón de Don Hugo: gastado pero limpio, con arreglos caseros (una cinta en un asiento roto, una cortina que no hace juego). Es la «villa» del reality: tiene que sentirse como un lugar donde se puede vivir varios capítulos.

**Tres cosas que tienen que estar siempre en el mismo lugar**, porque el público las va a buscar:
1. **La puerta con la ventanita y la cerradura:** es por donde entra y sale la gente.
2. **La manija del freno de emergencia:** se planta desde el capítulo 1, junto a la puerta. En el capítulo 3 alguien la tira y el público tiene que poder decir «estaba ahí desde el principio».
3. **El compartimento del revisor, al fondo:** la radio, el botiquín, el agua y las linternas. En el capítulo 1 está cerrado.

**Sin hacha de emergencia** en este vagón (propuesta del abogado del diablo: si hay un arma a mano, cambia la lógica del capítulo).

## 2. Plano del vagón

```
          HACIA EL RESTO DEL TREN (vagones con infectados)
     ┌───────────────────────────────────────────────┐
     │  vestíbulo del vagón anterior (la «esquina»   │  ← desde aquí llegan los infectados (1:08)
     │  por donde doblan los infectados)             │
     │  fuelle de goma entre vagones                 │  ← Diego está aquí (0:45)
     ├──────────────[ PUERTA + VENTANITA ]───────────┤  ← tubo fluorescente encima · cerradura de llave
     │ [FRENO]                                       │  ← manija roja del freno, pared derecha
     │  ▭▭  ▭▭   fila 1                    ▭▭  ▭▭    │
     │  ▭▭  ▭▭   ...        pasillo        ▭▭  ▭▭    │  ← 8 filas, 2 + 2, tapiz azul gastado
     │  ▭▭  ▭▭   fila 8     central        ▭▭  ▭▭    │     lámpara de lectura sobre cada par
     │                                               │     tira de luces de emergencia en el techo
     │ [COMPARTIMENTO   ]                            │
     │ [DEL REVISOR     ]   [ VENTANA TRASERA ]      │  ← los rieles que se alejan en la noche
     └───────────────────────────────────────────────┘
                     COLA DEL TREN
```

**Por qué sirve en 9:16:** el pasillo central es una línea vertical natural. Mirando hacia la puerta, la ventanita queda en el tercio medio del cuadro; mirando hacia el fondo, la ventana trasera con los rieles es la salida que no existe.

**El vagón de pasajeros de la escena 1** es **el mismo modelo** de vagón, pero con una puerta en cada extremo, sin compartimento ni ventana trasera, y con más pasajeros. Se saca editando la plancha del último vagón: así los dos vagones son coherentes y no generamos dos diseños.

## 3. Estados de luz

| Estado | Capítulo | Fuentes encendidas | Todo lo demás |
|---|---|---|---|
| **Ámbar** (antes del brote) | 1, 0:03–0:16 | Lámparas de lectura, 2700K, charcos de luz sobre cada par de asientos | Ventanas azul noche. Techo apagado |
| **Rojo** (brote) | 1, desde 0:16 | Tira de emergencia del techo, rojo `#B3001B` tenue · tubo fluorescente sobre la puerta, 5600K, parpadea | Lámparas apagadas. Bajo los asientos y el portaequipaje, casi negro |
| **Batería** (tren detenido) | 3 | Solo la tira roja a media intensidad, linternas y celulares | Afuera, oscuridad total del bosque. Se genera cuando llegue el capítulo 3 |

Los estados **no se generan de cero:** se editan sobre la plancha maestra.

---

## 4. Prompts

### 4.1 Exploración de look (Midjourney 8.2)

Solo para decidir materiales, época y desgaste. La distribución del vagón se decide en la plancha maestra, no aquí. Si 8.2 mantiene los image prompts o `--sref`, aquí entran tus imágenes de referencia.

**Último vagón, look general**
```
documentary photograph of the interior of the last carriage of an old long-distance night passenger train in South America, decades old but cared for, worn blue fabric seats with lighter patches where heads rest, one seat repaired with black tape, chrome grab handles, metal luggage racks with nets, small individual reading lamps under the racks, faded beige curtains that do not all match, grey linoleum floor with a rubber strip down the aisle, at the far end a heavy grey-green metal door with a small wired-glass window, empty, eye level from the rear end looking down the central aisle, lit only by the warm reading lamps, deep night blue outside the windows, 24mm lens, Kodak Vision3 500T film scan --ar 9:16 --raw --s 50 --preview --no people, text, logos, futuristic, luxury
```

**La puerta y la ventanita (detalle)**
```
documentary close photograph of a heavy grey-green metal door at the end of an old train carriage, a small rectangular window at face height with wired safety glass, the glass dirty with dry fingerprints and old scratches, below it an antique keyhole lock with a worn brass escutcheon and a large iron key in it, chipped paint around the handle, a single fluorescent tube above the door, on the wall to the right a red emergency brake handle with a small lead seal, eye level, 35mm lens, neutral light, Kodak Portra 400 film scan --ar 9:16 --raw --s 50 --preview --no people, text, logos, futuristic
```

**El vestíbulo del otro lado (lo que se ve por la ventanita)**
```
documentary photograph looking through the rubber bellows gangway between two old train carriages at night, the connecting metal floor plates, beyond it the vestibule of the next carriage with a side exit door and a corner where the aisle turns out of sight, everything lit only by dim deep red emergency lights, one light flickering, rain water on the floor plates, empty, eye level, 35mm lens, Kodak Vision3 500T film scan --ar 9:16 --raw --s 50 --preview --no people, text, logos
```

### 4.2 Plancha maestra (Weavy · Nano Banana Pro y GPT Image 2.5 en paralelo)

Entradas: `image_1` = el look elegido en MJ; `image_2` = tu referencia principal de materiales (si la hay). 9:16, resolución nativa.

**`set_ultimo_vagon_base`**
```
Photographic film set reference, not an illustration. Image 1 is the look reference and image 2 is the materials reference: match their materials, era and wear only, and ignore their layout, light and camera angle. Build this exact layout: the interior of the last carriage of an old long-distance night passenger train, seen from the rear end of the carriage looking forward down the narrow central aisle, camera at standing eye height, 24mm lens, deep focus with everything sharp from the foreground to the far door. Eight rows of paired seats on each side of the aisle, worn blue fabric upholstery with lighter patches where heads rest, one seat repaired with black tape, chrome grab handles on the aisle corners. Metal luggage racks with nets above the seats on both sides, and under each rack a small individual reading lamp. Faded beige curtains tied at each window, not all matching; the windows are black glass. Along the ceiling above the aisle, a continuous strip of small emergency light fixtures, switched off. At the far end, the front door of the carriage: a heavy grey-green metal door with a small rectangular window of wired safety glass at face height, the glass dirty; below the window, an antique keyhole lock with a worn brass escutcheon. Above the door, a single fluorescent tube. On the wall to the right of the door, a red emergency brake handle with a small lead seal and a plain metal plate with no readable text. Worn grey linoleum floor with a black rubber strip down the aisle. Lighting: neutral even work light from the ceiling, 4500K, no drama and no color cast, so every surface and material is readable. No people, no text, no logos.
```

### 4.3 Estados de luz (Weavy · editar sobre la plancha)

Entrada: `image_1` = `set_ultimo_vagon_base` aprobado.

**`set_ultimo_vagon_ambar`**
```
Photographic film set, not an illustration. Image 1 is the set: keep every object, surface, seat, curtain, window, door and the camera position exactly the same. Change only the lighting and the view through the windows. It is night, before anything has happened. The ceiling work light is off. Every small reading lamp under the luggage racks is on, warm 2700K, each one casting a soft pool of light onto its pair of seats that falls off quickly into shadow in the aisle. The emergency strip on the ceiling is off. The fluorescent tube above the far door is off; the door is lit only by the last pair of reading lamps. Through the windows, deep night blue, with rain streaks on the outside of the glass only. Contrast ratio 6:1, slightly underexposed, deep shadows that keep detail, highlights that roll off softly. No people, no text, no logos. Kodak Vision3 500T film scan look, fine organic grain, no digital sharpening, no HDR look.
```

**`set_ultimo_vagon_rojo`**
```
Photographic film set, not an illustration. Image 1 is the set: keep every object, surface, seat, curtain, window, door and the camera position exactly the same. Change only the lighting and the view through the windows. The reading lamps and the ceiling work light are off. The strip of emergency lights along the ceiling is on, dim deep red, washing the tops of the seats and the aisle floor in red and leaving the spaces under the seats and the luggage racks in near black. The single fluorescent tube above the far door is on, cold 5600K and hard, lighting the door and its small window from above; one end of the tube is darker, as if it is about to flicker. Light haze in the air catches the tube. Through the side windows, black night with rain streaks on the outside of the glass only. Contrast ratio 8:1, one stop underexposed, deep blacks that keep detail, highlights that roll off softly. No people, no text, no logos. Kodak Vision3 500T film scan look, fine organic grain, no digital sharpening, no HDR look. Color separation limited to deep red, cold cyan-white and near-black.
```

### 4.4 Vistas por eje (Weavy · Nano Banana Pro)

Entrada: `image_1` = `set_ultimo_vagon_base`. Primero con luz de trabajo; después se reilumina con los prompts de 4.3.

**`set_ultimo_vagon_eje_fondo`** (contraplano: mirando hacia la cola)
```
Photographic film set reference, not an illustration. Image 1 shows the carriage seen from the rear end looking toward the front door. Show the same carriage from the opposite direction: camera at standing eye height in the aisle, two meters from the front door, looking back toward the rear end of the carriage, 24mm lens, deep focus. Keep the same seats, blue upholstery, taped seat, luggage racks, reading lamps, curtains, linoleum floor, rubber aisle strip and ceiling emergency strip as image 1. At the rear end of the carriage: on the left, the conductor's compartment, a narrow varnished wooden door with a small window and its own keyhole lock, closed; in the center of the end wall, a large rear window showing the dark rails receding into a night forest, the tracks only faintly visible. Lighting: neutral even work light from the ceiling, 4500K, no color cast. No people, no text, no logos.
```

**`set_puerta_ventanita_interior`** (la puerta de cerca, desde adentro)
```
Photographic film set reference, not an illustration. Image 1 is the carriage: keep the door, its small wired-glass window, the antique keyhole lock, the fluorescent tube above it and the red emergency brake handle on the wall to its right exactly as they are. Move the camera into the aisle, one and a half meters from the door, at face height, 35mm lens, so the door fills the middle of the vertical frame, with the last pair of seats entering the frame at the lower left and lower right edges. Through the small window, the dark rubber bellows gangway and a dim vestibule beyond. Lighting: neutral even work light, 4500K, no color cast. No people, no text, no logos.
```

### 4.5 Props (Weavy · Nano Banana Pro · luz neutra · 16:9)

**`prop_llave`**
```
Photographic prop reference sheet, not an illustration. An antique iron train door key, about twelve centimeters long, with an oval bow worn smooth by years of use, a simple bit with two teeth, and a small brass tag with no readable text on an old split ring. Next to it, the matching lock: an antique keyhole lock with a worn brass escutcheon mounted on a small piece of grey-green painted metal door with chipped paint. Two views of the key, front and side, and one view of the lock. Plain mid-grey backdrop, soft even studio light, natural metal wear, no text, no labels, no logos.
```

**`prop_revolver`**
```
Photographic prop reference sheet, not an illustration. An old short-barrel six-shot revolver, decades old, with a worn dark blued steel finish rubbed silver at the edges and a cracked wooden grip, no brand markings. Three views: left side closed, right side closed, and the cylinder swung open showing two brass cartridges and four empty chambers. Plain mid-grey backdrop, soft even studio light, no text, no labels, no logos, no engravings.
```

**`prop_celular_martina`**
```
Photographic prop reference sheet, not an illustration. An ordinary mid-range black smartphone in a plain worn grey silicone case with slightly frayed corners, no brand markings. Three views: front with the screen lit plain dark grey and empty, back of the case, and the phone lying face down on dark blue denim. The screen shows no text, no icons and no interface; notifications are added in post. Plain mid-grey backdrop, soft even studio light, no text, no labels, no logos.
```

**`prop_freno_emergencia`**
```
Photographic prop reference sheet, not an illustration. An old train emergency brake handle mounted on a grey-green painted metal wall panel: a red painted steel lever in a recessed box, a thin wire with a small lead seal holding it in place, and a plain riveted metal plate above it with no readable text. Two views: front and three-quarter left. Paint worn at the grip, a few scratches, clean and cared for. Plain mid-grey backdrop around the panel, soft even studio light, no text, no labels, no logos.
```

---

## 5. Continuidad (lo que no puede cambiar entre planos)

| Elemento | Se fija como |
|---|---|
| Lado del freno de emergencia | Pared derecha de la puerta, mirando hacia adelante |
| Compartimento del revisor | Izquierda del fondo |
| Tapiz de los asientos | Azul gastado, con un asiento reparado con cinta negra (fila 3, izquierda) |
| Ventanita | Rectangular, vidrio con malla de alambre, a la altura de la cara |
| Llave | Hierro, con placa de bronce sin texto. Hugo la lleva en el cinturón hasta que se la da a Martina |
| Herida de Diego (propuesta) | Antebrazo izquierdo |

---

## 6. Pruebas en situación (fase 5 del plan)

Plantilla de rodaje (`produccion/plantilla_prompt_rodaje.md`). Correr en paralelo en GPT Image 2.5 y Nano Banana Pro. 9:16, resolución nativa.

**PS-01 · Martina y Tomás, luz ámbar (0:03)** · `image_1` = `ref_martina`, `image_2` = `ref_tomas`, `image_3` = `set_vagon_pasajeros_ambar`
```
Film still from a feature film, not an illustration. Image 1 is the woman, image 2 is the man, image 3 is the carriage interior: match their faces, hair, wardrobe and the carriage exactly.

MOMENT: One second after he has asked her a question. They sit side by side in a pair of seats, not touching, a hand's width of empty seat between their shoulders. He has turned his head toward her and waits. She keeps looking at the dark window, her phone face down on her thigh under her hand, her sleeves pulled over her fingers.

COMPOSITION: 9:16 vertical. Camera at seated eye height in the aisle, one row ahead of them, looking back at a slight angle. She sits by the window on the left, her face on the upper third line; he sits on the aisle side, on the right, in three-quarter profile, slightly closer to the camera. Both sit in the middle third of the frame. The out-of-focus top of a seat back fills the bottom of the frame as a foreground occluder. The luggage rack above them falls into darkness at the top of the frame.

LENS: Shot on ARRI Alexa 35 with a Cooke S4 50mm spherical lens at T2. Focus on her near eye; he is slightly soft. Gentle natural focus falloff, soft halation around the reading lamp. No anamorphic streaks.

LIGHT: Only practical sources. One reading lamp under the luggage rack above them, warm 2700K, soft, lights her face from above and in front and makes a small pool on her hand and the phone; his face is half in that light and half in shadow. Behind them, the other reading lamps of the carriage recede as dim warm pools. The window beside her is deep night blue and reflects a faint copy of the lamp. Contrast ratio 6:1, slightly underexposed, deep shadows that keep detail.

TEXTURE: Rain only on the outside of the window glass, the streaks blurred by depth of field. Their skin is dry and matte with real pores. Their clothes are dry, with natural creases. Nothing is dirty.

FINISH: Kodak Vision3 500T film scan look, fine organic grain, soft natural micro-contrast, no digital sharpening, no HDR look. Color separation limited to warm amber, deep night blue and near-black.
```

**PS-02 · Diego en la ventanita, luz roja (0:45)** · `image_1` = `estado_diego_mojado`, `image_2` = `set_puerta_ventanita_interior` reiluminado en rojo
```
Film still from a feature film, not an illustration. Image 1 is the man, image 2 is the carriage door seen from inside: match his face, hair, wardrobe and state, and the door, window, lock and brake handle exactly.

MOMENT: One second after he has slammed his open right palm against the small window from the outside. His palm is still flat on the glass, his face close behind it, mouth open on a name. His soaked left forearm is lifted into view at the bottom edge of the window.

COMPOSITION: 9:16 vertical. Camera inside the carriage at face height, one and a half meters from the door. The door fills the frame; the small window sits in the middle third, with his face in its upper half. The dark out-of-focus back and shoulder of a passenger fills the lower-left corner as a foreground occluder. The red emergency brake handle is visible on the wall to the right of the door, in shadow. The ceiling falls into darkness at the top of the frame.

LENS: Shot on ARRI Alexa 35 with a Cooke S4 35mm spherical lens at T2.8. Focus on his eyes through the glass; the glass surface and his palm are slightly soft. Gentle natural focus falloff, soft halation around the fluorescent tube. No anamorphic streaks.

LIGHT: Only practical sources. Inside, the fluorescent tube above the door, cold 5600K and hard, throws a bright reflection across the top of the window glass and spills onto the grey-green door. Outside, the gangway behind him is lit by dim deep red emergency lights from the next carriage, rimming his wet hair and shoulders in red; his face is lit mostly by the cold spill of the tube through the glass. Inside, the dim red ceiling strip touches the edges of the door frame. Contrast ratio 8:1, one stop underexposed, deep blacks that keep detail.

TEXTURE: The window glass has dry fingerprints and old scratches, and the wired mesh inside the glass crosses his face. His hair is soaked and stuck to his forehead; drops of water on his face, matte skin between the drops. The left sleeve of his light stone canvas jacket is soaked dark red-black from the elbow to the cuff. No dark stains inside the carriage.

FINISH: Kodak Vision3 500T film scan look, fine organic grain, soft natural micro-contrast, no digital sharpening, no HDR look. Color separation limited to deep red, cold cyan-white and near-black.
```

**Qué revisar en las pruebas:**
- ¿Se reconoce a cada uno en miniatura?
- **PS-01:** ¿se siente la distancia entre los dos sin que nadie sobreactúe?
- **PS-02:** ¿se lee la manga a través del vidrio? ¿Se sigue reconociendo a Diego con la malla del vidrio y la luz roja?
