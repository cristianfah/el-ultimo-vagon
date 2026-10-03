# El Último Vagón · Cap. 1 · Cold open: guion técnico (prueba de calidad + lipsync)
fahren.tv · 3-oct-2026 · base: `guiones/vagon_cold_open_v1.md` (guionista) · repo: `el-ultimo-vagon/repo` (rama `main` + YAML del PR #6) · lipsync: `produccion/lipsync_espanol.md`

> **Decisión de Cristián (3-oct, 01:18):** los 4 planos van **solo en MiniMax H3 Max, a 1080p** (`minimax/h3-max/image-to-video`). Su Kling 4.0 Preview es solo 720p, así que **Kling queda fuera de este documento**. Los costos usan la **promo de fal: 0,096 USD/s a 1080p hasta el 15-oct-2026** (después, 0,16 USD/s). Fuente: [llms.txt de H3 Max i2v](https://fal.ai/models/minimax/h3-max/image-to-video/llms.txt): *"these are promotional rates, 40% off for a limited time. The discount ends October 15"*.
> **Nada de esto se generó.** Son prompts y planes listos para una sesión.

## 0. Resumen

| | |
|---|---|
| Duración | **8,5 s** con 4 planos, más la tarjeta «20 MINUTOS ANTES» |
| Generaciones | **3 clips H3 Max** (P1 y P3 salen del mismo clip), **4 keyframes nuevos** en Nano Banana Pro 2K y 1 pista de voz |
| Costo | **~3,70 USD** en el plan base · **~5,65 USD** si se usan todos los respaldos (§4) |
| Tiempo | Una sesión de **~2 h**: ~1 h de generación y ~1 h de post (§3) |
| Cámara | P1 y P3 fijas, en trípode. P2 y P4 en mano muy leve. **Cero push-in, zoom o dolly en los 4.** El único movimiento del capítulo queda para la cara de Diego (escena 4) |

**Qué cambia respecto del montaje v2 y por qué:**

| Problema del v2 (feedback de Cristián) | Arreglo en este plan |
|---|---|
| "AI slop": GPT Image bajo y video a 480p | Keyframes nuevos en **Nano Banana Pro 2K** y video en **1080P**. Los prompts piden imagen limpia, sin grano ni nitidez artificial; el grano se agrega en post, igual para los 4 planos |
| Dolly-in en todos los planos | La cámara se escribe en cada prompt como frase propia: *static, locked off* o *handheld, operator standing still*, siempre con *no push-in, no zoom, no reframing*. No se usa el "slow push toward the secret" de `agentes/impacto.md` |
| La escena de la sangre no se entendía y los vagones se movían | El primer cuadro **es** el impacto. El fondo detrás del vidrio se pide **quieto y vacío** (hc24) y sin luces que se muevan. Se deja de usar FL entre dos keyframes separados (fue lo que dejó la mano limpia a mitad del clip en b01) |
| La mano tenía que aparecer de golpe | No hay acercamiento: el clip arranca con la palma ya contra el vidrio y el vidrio vibrando |
| Martina pegada al vidrio y sin expresión | Está a **3 m de la puerta** (hc35), con beats de actuación con tiempos: susto, congelamiento, reconocimiento, «Diego…», culpa y respiración |
| Brazo herido | **Mano y manga DERECHAS** (hc19–hc21). Vista desde adentro: pulgar hacia la derecha del cuadro y brazo entrando por abajo a la izquierda. Esa geometría es la correcta para una mano derecha vista por la palma; no es un error del v2 |

---

## 1. Geografía y ejes (todo el cold open)

Vista de arriba. La puerta está al norte y Martina, a 3 m, la mira de frente. Tomás está un paso detrás de ella, **a su derecha** (hc35).

```
            [ PUERTA + VENTANITA ]   ← tubo frío encima, tira roja al centro del cielo
                      |
         (cám. P1/P3) ·  ← 2,3 m de la puerta, ~8° a la derecha del eje, altura de ojos
                      |
       (cám. P2/P4) ◣ |      ← adelante y a la derecha de Martina, 25–30° fuera del eje
                      M      ← Martina, de frente a la puerta
                        T    ← Tomás, un paso atrás y a la derecha de ella
```

- **La cámara de P2 y P4 va adelante y a la derecha de Martina.** Desde ahí:
  - su mirada a la puerta va hacia la **derecha del cuadro**, rozando el lente;
  - Tomás queda en el **lado izquierdo del cuadro**, al fondo y fuera de foco;
  - y el desvío de ojos «hacia Tomás» (hacia la derecha de ella) se lee como un **movimiento a la izquierda del cuadro**, en sentido contrario a la mirada a la puerta. Así se entiende de un vistazo.
- **Las cámaras de los 4 planos están del mismo lado del eje Martina–puerta,** así que los cortes no cruzan el eje.
- **Esto calza con lo que ya existe:** el keyframe aprobado c01_p02 y la toma b02 del v2 ya la tienen mirando a la derecha del cuadro.
- **Ojo:** el YAML (c01_b02) todavía dice "door window off-screen left". Hay que corregirlo a *right* cuando se actualice el bloque.
- **La puerta y la ventanita siguen la plancha aprobada F03:** rectángulo de esquinas redondeadas con marco remachado, vidrio de seguridad con malla de alambre fina en rombo (diamond wire mesh), tubo frío encima, tira roja al centro del cielo, cerradura a la izquierda y freno a la derecha. (Decisión de Cristián, 3-oct-2026: SÍ a F03, hc22 corregido.)
- **Fondo del otro lado del vidrio (hc24):** el fuelle y el pasillo rojo, vacíos y **quietos**. Nada de vagones moviéndose ni de luces que pasen.

### Gramática de la escena (para el Director de fotografía)
- **Cold open, susto y reconocimiento:** la cámara no se acerca a nada. La mano se filma como evidencia, fija en trípode. Martina se filma con un operador que está quieto y contiene la respiración: hay vida, pero no avance.
- **El contraste viene de la escala:** inserto, plano medio corto, inserto, primer plano. No viene del movimiento.

### Luz (igual en los 4 planos)

| Fuente | Dónde está | Color | Para qué |
|---|---|---|---|
| **Key:** tira de emergencia | Centro del cielo de los dos vagones (`decisiones.md`) | Rojo #B3001B | En Martina: luz cenital, un poco por delante, que pega en la frente, los pómulos y el sudor. En la mano: contraluz rojo desde el pasillo |
| **Acento:** tubo fluorescente | Sobre la puerta | Blanco frío, ~6500 K | Brillo en el vidrio mojado y en los nudillos. Punto de luz en los ojos de Martina y un filo frío en el lado de su cara que da a la puerta |
| **Relleno:** rebote rojo | Piso y asientos | Rojo | ~3 pasos bajo el key |

- **Contraste de ~8:1.** El lado lejano de la cara queda casi negro, pero con detalle, sin negros aplastados.
- **No se usa ninguna fuente más.** La regla del Director de fotografía es que, si no se puede nombrar la fuente, la luz no existe.

---

## 2. Los 4 planos

**Parámetros comunes de video:**
- `minimax/h3-max/image-to-video`, con `resolution: "1080P"` y `prompt_expansion_mode: "disabled"`.
- `image_url` = el keyframe del plano. El cuadro de salida sigue al keyframe, así que el keyframe tiene que ser 9:16.
- Formato **I2VA** de `.cursor/skills/director-de-prompts/references/h3.md`.
- **No se usa `end_image_url`** salvo en la toma 2 opcional de B1 (abajo), que sí cumple la regla FL: el último fotograma es una edición del primero y el cambio es de estado.

**Parámetros comunes de keyframe:**
- `fal-ai/nano-banana-pro/edit`, con `aspect_ratio: "9:16"`, `resolution: "2K"` y las referencias en `image_urls` en el orden de cada prompt.
- **Alternativa:** GPT Image 2.5 en calidad *high* (por Weavy), si Nano Banana Pro no resuelve bien la anatomía de la mano.

**Bloque FINISH (va al final de cada keyframe):**
```
FINISH: Photorealistic film still from a live-action feature, shot on a large-sensor digital cinema camera, natural skin and material texture, realistic wet surfaces. Clean image: no film grain, no digital noise, no sharpening halos, no HDR look, no CGI, no illustration (grain is added later in post). No text, no logos, no watermark. Vertical 9:16.
```

---

### P1 · 0:00–0:01,5 (1,5 s) · El impacto · clip **B1**

| Campo | Valor |
|---|---|
| Encuadre | Inserto de la ventanita desde adentro. La ventana llena el centro, con un margen de puerta remachada alrededor. La mano está en la **mitad inferior izquierda** del vidrio (huella, hc23). Las manchas secas quedan arriba a la derecha y el puño gris empapado entra por abajo a la izquierda |
| Lente | **65 mm** (equivalente full frame), f/2.8. Foco en la palma contra el vidrio. El pasillo queda blando pero se lee |
| Soporte y movimiento | **Trípode, fijo.** La cámara **no reacciona al golpe**: el susto lo da la mano |
| Posición | 2,3 m de la puerta, altura de ojos de Martina (~1,60 m), ~8° a la derecha del eje |
| Luz | Contraluz rojo del pasillo, que recorta los dedos. El tubo frío roza el vidrio mojado y los nudillos. La puerta, adentro, queda oscura |
| Acción | **0,00 s:** la palma derecha **ya está** contra el vidrio; agua que salta y vidrio que vibra. **0,0–0,4 s:** tiembla el marco. **0,4–1,5 s:** la mano sigue apretada y tensa, sin volver a golpear |
| Continuidad | hc17, hc19–hc21 y hc23–hc24. Mano DERECHA, pulgar a la derecha del cuadro, sin anillos ni reloj. Las manchas, sobre todo en el talón de la palma y la base de los dedos, con las puntas casi limpias |

**Clip B1 = P1 + P3.** Es un solo clip de 5 s, cámara fija.
- P1 usa **0,00–1,50** del clip y P3 usa **3,00–5,00**.
- Lo que pase entre 1,5 y 3,0 s no se ve en el montaje, porque en ese tramo va P2.
- Así hay **una sola mano, un solo vidrio y una sola luz** para los dos insertos.
- Además, el estado final (palma plana, pulgar a la derecha y huella abajo a la izquierda) es el que se reutiliza a las 0:45. También es el primer fotograma del plano de la cara de Diego (encadenado C del YAML).

**Keyframe KF1 · impacto** (2 intentos). Las referencias:
- **Image 1:** F03 (`.../I6kNLxhGD5kjj6UWzbGV0_F03_rojo_puerta_desde_dentro_0-45.png`).
- **Image 2:** HOJA_diego.
- **Image 3:** ESTADO_diego_mojado_herido **espejada horizontalmente**. *Truco:* la imagen aprobada tiene la manga ensangrentada en el brazo izquierdo; espejada, queda en el derecho. En este plano solo se ve el puño, así que el espejo no rompe nada. Se hace con PIL y se sube a fal. La regeneración v2 de ESTADO sigue pendiente para la escena 4.

```
Image 1 is the approved door of the last carriage seen from inside: keep its small window exactly as it is (same rounded-rectangle shape, riveted metal frame, wire-mesh glass), the cold white fluorescent tube above the door and the red emergency strip in the ceiling. Image 2 is Diego: match his skin tone and hands. Image 3 shows his soaked light-grey canvas jacket; in this frame only his RIGHT cuff is visible, soaked almost black.
MOMENT: The exact instant of impact. From the outside, Diego's RIGHT hand has just slammed flat against the small window: palm toward the camera, fingers spread and pointing up, thumb toward frame right, the heel of the palm pressed hardest, the skin flattened white where it meets the glass. A fine spray of rainwater bursts off the glass around the palm, drops frozen in mid-air; the glass is still flexing.
COMPOSITION: Vertical 9:16, from inside the carriage at standing eye height, almost square-on to the door, slightly from the right. The window fills the middle of the frame with a margin of grey-green riveted door around it. The hand sits in the lower-left half of the window; the soaked grey cuff enters from the bottom-left edge of the window. Old dry dark stains in the upper-right corner of the glass. Through the glass behind the hand: the narrow connecting vestibule and an empty corridor lit deep red, no people, no faces.
LENS: 65mm, f/2.8, focus on the palm against the glass; the red corridor behind soft but readable.
LIGHT: Red emergency light (#B3001B) from a strip along the ceiling of both carriages; the corridor glows deep red behind the hand and rims the fingers. The cold white tube above the door (6500K) skims the wet glass and the knuckles with a thin cold highlight. Inside, the door is dark. Strong contrast, deep blacks that still hold detail.
HAND: Rainwater and dark red-black stains running down from the wrist, concentrated on the heel of the palm and the base of the fingers; fingertips almost clean. Five fingers, natural proportions, no rings, no watch, no bracelet.
[FINISH]
```

**Video B1** (`duration: 5`, 1080P):
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a vertical insert of the small window of a metal train door, seen from inside the carriage; the window and a margin of riveted door fill the frame. The video begins at the instant of impact shown in <Picture 1>: a wet RIGHT hand, palm toward the camera, fingers up, thumb toward frame right, has just slammed flat against the glass from outside, its soaked grey cuff entering from the bottom-left of the window. The camera holds a static shot, locked off on a tripod, for the whole video: no push-in, no zoom, no pan, no tilt, no shake; it does not react to the hit, so the hand alone carries the shock. From 0.00 to 0.40 seconds the glass and the door frame shudder from the impact and the spray of rainwater falls away from around the palm. From 0.40 to 3.20 seconds the hand stays pressed hard against the glass, fingers slightly curled, tense, trembling a little; it does not leave the glass and does not hit again. From 3.20 to 4.20 seconds the fingers slowly uncurl and spread, and the palm settles flat and still against the glass, almost gently. From 4.20 seconds to the end the hand rests flat and motionless; only rainwater trickles down the glass. The dark red-black stains stay on the heel of the palm and the base of the fingers, the fingertips stay almost clean, and the dry stains stay in the upper-right corner of the glass. Behind the glass, the vestibule and the empty red corridor stay completely still: no people, no faces, no moving lights, no passing carriages. The red emergency light and the cold white tube above the door stay steady. No music. No subtitles, no captions, no on-screen text.

overall_soundscape: A low, steady rumble of the train under the floor. One dry, heavy palm hit on the glass at 0.00 seconds, the window rattling in its frame, then near silence with only the rumble and rain on metal.

non_diegetic_music: N/A
```

> **Nota sobre la malla (decisión 3-oct-2026):** el vidrio de la ventanita tiene malla de alambre fina en rombo según F03. En los prompts de video se agrega: *"The small window has fine diamond wire mesh inside the glass; the mesh stays static, consistent, no flicker, no moiré."* Si el modelo genera parpadeo o moiré en la malla, se corrige con estabilización temporal en post o se regenera con otra seed.

**Tomas:** 2 como máximo (regla de `asistente_direccion.md`). La segunda depende de cómo salió la primera:
- **Si la mano o la luz saltan, o la mano se limpia:** el mismo prompt con otra `seed`.
- **Si en 3,2–4,2 s la mano no se abre:** FL válido. `image_url` = KF1 y `end_image_url` = **KF1b**, que es una *edición* de KF1 con Nano Banana Pro: "same image, the hand now rests flat and relaxed, fingers straight, no spray; change nothing else". El cambio es de estado, con la misma base, así que cumple las dos condiciones de FL.
- **Si el arranque se ve como una foto que recién empieza a moverse (ease-in):** se recortan 2–4 cuadros del inicio en el montaje y el golpe sonoro va en el primer cuadro que se mueve. No se gasta otra toma por esto.

**Audio:** se descarta el audio del modelo. Los efectos van en post (§6).

---

### P2 · 0:01,5–0:03 (1,5 s) · Susto y congelamiento · clip **B2**

| Campo | Valor |
|---|---|
| Encuadre | Plano medio corto, de medio pecho a sobre la cabeza. Martina, un poco a la derecha del centro, mira hacia la derecha del cuadro rozando el lente. **Tomás, fuera de foco, a la izquierda del cuadro y al fondo.** Detrás, el pasillo hacia la cola: respaldos y la tira roja, todo desenfocado |
| Lente | **50 mm**, f/2. Foco en el ojo cercano de Martina. Tomás, a ~1 m detrás, queda como una forma blanda |
| Soporte y movimiento | **En mano, muy leve:** un operador quieto, con el vaivén de su respiración (< 1°). Sin traslación, sin push-in, sin zoom. Al golpe, la cámara se sacude **muy poco y medio tiempo tarde**, y vuelve a asentarse |
| Posición | ~1,8 m de Martina, a la altura del hombro (~1,55 m), 25–30° a su derecha-adelante |
| Luz | La de §1: tira roja cenital como key y punto frío del tubo en los ojos (fuente fuera de cuadro, a la derecha) |
| Acción | **0,0–0,3 s:** congelada, sin respirar, con la mirada en la ventanita. **0,3 s:** segundo golpe fuera de campo y **sobresalto de todo el cuerpo** (hombros arriba, cabeza 2 cm atrás, ojos abiertos, inspiración brusca por la boca). **0,8 s hasta el final:** rígida, hombros todavía arriba, pecho que sube rápido, sin avanzar y sin hablar. **Tomás:** se sobresalta y mira a la puerta, con la boca cerrada |
| Continuidad | hc09–hc11 (mechones, sudor, suéter crema seco), hc12 (Tomás de oliva), hc35 (3 m, Tomás atrás a su derecha) |

> **Decisión de Cristián (3-oct-2026, 10:33):** SÍ al segundo golpe fuera de campo, solo en audio, a los 0,3 s de P2. Martina salta en cámara con ese golpe. P1 sigue siendo «golpe seco, después silencio» durante 1,5 s; en P3 «la mano deja de golpear» tiene sentido porque el segundo golpe fue el último.

**Keyframe KF2** (2 intentos). Image 1 = REF_martina, Image 2 = HOJA_martina, Image 3 = REF_tomas, Image 4 = **F02** (rojo, hacia el fondo; está en Drive `04_aprobados` y hay que subirla a fal, porque no está en `fal_urls_v1.json`).
```
Images 1 and 2 are Martina: keep her face, features, skin and build exactly. Image 3 is Tomás. Image 4 is the last carriage seen toward the tail under red emergency light: use it for the set behind them.
MOMENT: Night, the last carriage of a train under red emergency light. Martina stands frozen in the central aisle, about three metres from the door, her body facing the door, which is off-screen just past the camera on frame right. Her eyes are fixed on the small door window, wide and searching; lips closed; she is holding her breath. She does not move toward it.
COMPOSITION: Vertical 9:16 medium close-up, from mid-chest to just above her head, Martina slightly right of center, her look toward frame right grazing past the lens. One step behind her, deep in the frame on the left, Tomás stands soft and out of focus, half-turned toward the door, his face unreadable, mouth closed. Behind them the aisle recedes toward the tail: dark navy seat backs and the red emergency strip running along the center of the ceiling, deeply out of focus. Keep her head and eyes inside the middle of the frame (room for phone UI top and bottom).
WARDROBE AND STATE: Martina's low ponytail has come loose, strands around her face, a light sheen of sweat on her forehead and upper lip, a dry, clean cream wool crew-neck sweater, no rain, no stains, no jewellery. Tomás wears a closed olive-green cotton jacket over a dark grey T-shirt.
LENS: 50mm, f/2, focus on Martina's eye nearest the camera; Tomás and the background fall into soft shapes.
LIGHT: Key: the red emergency strip in the center of the ceiling, slightly in front of her, a hot red top light on her forehead, cheekbones and the bridge of her nose, catching the sweat. Accent: a cold white fluorescent tube above the door, off-screen frame right, leaves a small catchlight in her eyes and a thin cold edge on the side of her face toward the door and on the loose strands. The far side of her face falls almost to black. Contrast about 8:1; deep blacks that keep detail.
[FINISH]
```

**Video B2** (`duration: 3`; la salida puede durar hasta ~3,7 s):
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a vertical medium close-up of Martina, the woman in <Picture 1>, standing in the aisle of the last carriage of a night train about three metres from the closed door, which is off-screen just past the lens on frame right. Behind her, on frame left, Tomás stands one step back, soft and out of focus. The carriage behind them is the inside of the train and stays fixed relative to the camera. The camera is handheld by an operator standing still, with only a very slight sway from his breathing; it does not travel, push in, zoom or reframe. From 0.00 to 0.30 seconds she is frozen, eyes locked on the door window at frame right, holding her breath. At 0.30 seconds a heavy blow lands on the glass off-screen: her whole body jolts, shoulders snapping up, head jerking back a couple of centimetres, eyes going wide, a sharp intake of breath through the mouth; the camera jolts very slightly, half a beat late, and settles. From 0.80 seconds to the end she stays frozen where she is, rigid, shoulders still raised, chest rising high and fast, eyes on the window; she does not step toward the door and does not speak, her lips stay almost closed. Behind her, Tomás flinches and looks toward the door; his lips stay closed and he stays out of focus. She keeps the look of <Picture 1>: loose strands around her face, sweat sheen on her forehead, dry clean cream sweater. The red top light from the ceiling strip and the cold catchlight from the tube above the door stay steady. No music. No subtitles, no captions, no on-screen text.

overall_soundscape: A low, steady train rumble. A heavy palm blow on glass off-screen at 0.30 seconds, the door rattling. Her sharp gasp, then held breath.

non_diegetic_music: N/A
```
**Tomas:** 2 como máximo. **Audio:** efectos en post.

---

### P3 · 0:03–0:05 (2 s) · La palma se calma · clip **B1** (3,00–5,00 s)

| Campo | Valor |
|---|---|
| Encuadre | El mismo inserto de P1, desde su punto de vista. *Opcional:* un recorte fijo de ~8 % en post para diferenciarlo de P1, sin animar |
| Lente / soporte / luz | Los de P1: 65 mm, trípode, fijo |
| Acción (tiempo del clip) | **3,0–3,2 s:** la mano sigue tensa. **3,2–4,2 s:** los dedos se aflojan y la palma queda plana, casi suave. **4,2–5,0 s:** quieta. Se ve el puño gris claro empapado |
| Intención | El cambio de golpe a palma calmada es lo que le dice a ella "soy yo". La cámara quieta deja que ese cambio sea lo único que pasa |
| Generación | **No se genera aparte:** sale de B1 (ver P1) |

---

### P4 · 0:05–0:08,5 (3,5 s) · «Diego…» · clip **B3** (= bloque c01_b02, prueba de lipsync)

| Campo | Valor |
|---|---|
| Encuadre | Primer plano, de las clavículas hacia arriba y sin manos. La cara en el tercio medio, un poco a la derecha. La mirada va a la derecha del cuadro, rozando el lente. **Tomás:** una forma blanda arriba a la izquierda, cabeza y hombro, muy desenfocado |
| Lente | **85 mm**, f/1.8. Foco en el ojo cercano de Martina durante todo el plano. Tomás queda en bokeh, sin detalle legible |
| Soporte y movimiento | **En mano, casi imperceptible:** el operador contiene la respiración. Menos que en P2. Sin traslación, sin push-in, sin zoom y sin cambio de foco |
| Posición | ~1,1 m de Martina, en el mismo lado que P2. Tomás se *trampea* más cerca de su hombro para que entre en el borde del cuadro: a 85 mm, en su posición real quedaría fuera |
| Luz | La de P2, idéntica |
| Acción (tiempo del clip) | **0,0–1,0 s:** los ojos buscan en la ventanita con movimientos mínimos; miedo, sin respirar. **1,0 s:** la mirada se fija, las cejas se aflojan y la boca se abre: reconoce la mano. **1,5–2,1 s:** susurra, casi sin voz, **«Diego…»**. **2,2 s:** los ojos se van unos milímetros hacia la izquierda del cuadro (hacia Tomás, que está a la derecha de ella) sin girar la cabeza, y vuelven: culpa. **2,4–3,2 s:** Tomás gira la cabeza hacia ella, desenfocado y con la boca cerrada. **3,3 s:** una inspiración corta y temblorosa. **Corte a negro en ~3,5 s, en la respiración y no después.** Fuera de cuadro, ella aprieta el celular con la mano izquierda (hc26): se puede sugerir con tensión en el hombro, sin mostrar la mano |
| Continuidad | hc09–hc11, hc26, hc34 (nadie la oye) y hc35 |
| Nota del guionista | Lo que importa en la actuación es lo de antes y lo de después de la palabra. La palabra en sí no |

**Keyframe KF4** (2 intentos). Image 1 = **el KF2 elegido** (fija luz, set, vestuario y lado de cámara), Image 2 = REF_martina, Image 3 = REF_tomas.
```
Image 1 is the previous shot of the same scene: keep exactly the same light, set, wardrobe, sweat and loose strands, and the same side of the camera. Image 2 is Martina's face reference: keep her face exactly. Image 3 is Tomás.
MOMENT: The same instant, closer. Martina stares at the small door window off-screen on frame right, eyes fixed and searching, lips closed, breath held, fear.
COMPOSITION: Vertical 9:16 close-up framed from the collarbones up, hands out of frame, her face in the middle third slightly right of center, her eyeline toward frame right just past the lens. In the upper left of the frame, far behind her, Tomás's head and one shoulder are a soft, out-of-focus shape, facing the door, mouth closed.
LENS: 85mm, f/1.8, focus on her eye nearest the camera; Tomás is a soft blur with no readable detail.
LIGHT: Same as Image 1: the red ceiling strip as a hot top key on her forehead and cheekbones; a small cold catchlight from the tube above the door, frame right; the far side of her face near black.
[FINISH]
```
**Keyframe KF4b, sin Tomás** (1 intento; es el respaldo de §5). Se edita sobre el KF4 elegido:
```
Image 1: keep everything exactly the same (face, light, framing, focus, wardrobe). Remove the man in the background on the upper left; in his place, continue the soft out-of-focus red depth of the carriage (seat backs and the ceiling strip). Change nothing else.
```

**Audio primero (método voz-primero de `lipsync_espanol.md`):**
1. **Voz de Martina en ElevenLabs.**
   - Para esta prueba alcanza el **plan Free**, que incluye Voice Design ([pricing](https://elevenlabs.io/pricing), visto el 3-oct). Para publicar el reel hace falta **Starter**, por la licencia comercial: 6 USD al mes, o 1 USD el primer mes hasta el 18-oct.
   - Prompt de Voice Design: *"Chilean woman, 29, from Santiago. Low, warm, slightly husky voice, natural urban Chilean Spanish accent, intimate close-mic, no theatrical delivery."*
   - Hay que guardarla como voz propia (el plan Free tiene 3 espacios), porque es la voz fija del personaje.
2. **4–6 variantes** de `[whispering] Diego…`, con el modelo v4 si está en el plan (que las etiquetas funcionen en v4 está **sin verificar**; si no, usar v3).
   - Se elige la que tenga **aire y poca voz**, sin dicción de locutora.
   - Aparte, una respiración corta (`[inhales]` o una toma de efectos).
3. **Armar la pista** en Resolve o Audacity: WAV mono de 48 kHz y **5,0 s**.
   - **0–1,4 s:** room tone muy bajo y respiración contenida.
   - **1,50 s:** el susurro.
   - **3,30 s:** la inspiración.
   - Va sin música ni tren, para que el modelo solo "oiga" la voz.
   - Se sube a fal, que admite hasta 15 MB.
4. **Video B3** con `target_audio_url` = esa pista y `duration: 5`.
   - El audio **reemplaza** la banda sonora de salida; fal no documenta si además guía los labios (**sin verificar**).
   - Tampoco está confirmado que `target_audio_url` funcione a 1080P. Si da error, generar a 1080P sin audio y pasar directo a sync-3.
5. **Si la boca no calza** (más de ±2 cuadros, o labios quietos): **sync-3** (`fal-ai/sync-lipsync/v3`, 8 USD/min) sobre la mejor toma, con la misma pista.

**Video B3** (`duration: 5`, 1080P, `target_audio_url`):
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a vertical close-up of Martina, the woman in <Picture 1>, framed from the collarbones up, hands out of frame. She stands in the aisle of the last carriage of a night train, about three metres from the closed door, which is off-screen just past the lens on frame right; she looks toward frame right, almost grazing the camera. In the upper left of the frame, far behind her, Tomás is a soft out-of-focus shape; the carriage behind them stays fixed relative to the camera. The camera is handheld by an operator holding his breath: only a barely perceptible sway, no travel, no push-in, no zoom, no reframing, and the focus stays on her near eye for the whole shot. From 0.00 to 1.00 seconds her eyes search the small window in tiny movements, fear in her face, breath held. At 1.00 seconds her gaze locks on one point, her brows release a little and her lips part: she has recognised the hand. At 1.50 seconds Martina (S1), a woman around 29 with a low, breathy voice in Latin American Spanish, whispers almost without voice, so that nobody behind her can hear: <d>[Spanish] Diego…</d> At 2.20 seconds, right after the name, her eyes flick a few millimetres toward frame left, toward Tomás behind her, without turning her head, and come back to the window. From 2.40 to 3.20 seconds Tomás, still out of focus, slowly turns his head toward her; his lips stay closed and he does not speak. At 3.30 seconds she takes one short, shaky breath in through her parted lips, then holds still, lips slightly open, until the end. She keeps the look of <Picture 1>: loose strands, sweat sheen on her forehead, dry clean cream sweater. The red top light from the ceiling strip stays steady on her face, the cold catchlight from the tube above the door stays in her eyes, and the far side of her face stays almost black. No music. No subtitles, no captions, no on-screen text.

overall_soundscape: A low, steady train rumble under the floor. Her held breath, the whisper, a soft catch in her throat, and a short shaky inhale at 3.30 seconds. A faint rustle of fabric as Tomás turns.

non_diegetic_music: N/A
```
**Tomas:** 2 como máximo (2 seeds). Los respaldos están en §5.

---

## 3. Orden de generación (una sesión de ~2 h)

| # | Paso | Tiempo | Qué revisar antes de seguir |
|---|---|---|---|
| 0 | **Preparación.** Bajar F03, F02, REF y HOJA de Martina, Tomás y Diego, y ESTADO. Espejar ESTADO con PIL. Subir todo a fal. Revisar el saldo. Bajar efectos (Freesound o la librería) | 10 min | Que F02 esté en fal |
| 1 | **Voz de Martina** (ElevenLabs Free) y pista de 5,0 s | 15 min | Que suene a susurro real, con aire y acento chileno suave |
| 2 | **KF1 ×2 → KF2 ×2 → KF4 ×2** (con el KF2 elegido como Image 1) → **KF4b ×1** | 25 min | Hoja de contactos con el checklist de §6: mano derecha, pulgar a la derecha, malla, mirada a la derecha del cuadro, Tomás a la izquierda |
| 3 | **Primera toma de B1, B2 y B3**, lanzadas en paralelo. H3 Max tarda segundos por clip | 10 min | Revisar cuadro a cuadro en Resolve. Cámara fija de verdad: superponer el primer y el último cuadro con modo *difference* |
| 4 | **Segundas tomas** solo donde fallaron (ver la "toma 2" de cada plano) y **sync-3** si la boca de B3 no calza. Si Tomás molesta, B3 con KF4b | 15 min | Máximo 2 tomas por bloque. Si fallan las dos, el bloque vuelve a revisión, no a una tercera toma |
| 5 | **Post:** conformar, gradación, grano y sonido (§7) | 40–50 min | Verlo en el celular, con y sin sonido |
| | **Total** | **~2 h** | |

---

## 4. Costo (fal, promo de H3 Max a 1080p hasta el 15-oct-2026)

| Ítem | Cálculo | USD |
|---|---|---|
| Keyframes Nano Banana Pro 2K (KF1 ×2, KF2 ×2, KF4 ×2, KF4b, KF1b) | 8 × 0,15 | 1,20 |
| B1 (P1 + P3), 5 s, 2 tomas | 2 × 5 × 0,096 | 0,96 |
| B2 (P2), 3 s, 2 tomas | 2 × 3 × 0,096 | 0,58 |
| B3 (P4), 5 s con `target_audio_url`, 2 tomas | 2 × 5 × 0,096 | 0,96 |
| Voz (ElevenLabs Free) | — | 0 |
| **Total del plan base** | | **~3,70** |
| *Respaldo:* sync-3 sobre la mejor B3 | 5 s × 8 USD/min | +0,67 |
| *Respaldo:* B3 desde KF4b, sin Tomás | 5 × 0,096 | +0,48 |
| *Respaldo:* H3 Max Lip Sync desde KF4b (precio de lista; que tenga promo no está confirmado) | 5 × 0,16 | +0,80 |
| **Total con todos los respaldos** | | **~5,65** |

- **Después del 15-oct:** el video pasa a 0,16 USD/s. El plan base quedaría en ~5,40 USD y el máximo en ~7,60 USD.
- **Para publicar:** ElevenLabs Starter, 1 USD el primer mes hasta el 18-oct y después 6 USD al mes. Es una suscripción, no un costo de este plano.
- **No se cuentan** las 5 generaciones gratis diarias del sandbox de H3 Max: no está verificado que den 1080P ni que acepten `target_audio_url`.

---

## 5. ¿Es riesgoso el encuadre de P4, con Tomás desenfocado detrás girando la cabeza?

**Sí, es un riesgo moderado.** No es tanto por la sincronía, porque «Diego…» es una palabra susurrada y sin bilabiales, fácil de sincronizar. El riesgo está en **qué cara anima el modelo y en la consistencia del plano**:

1. **Dos caras en cuadro con audio fijado:** H3 puede repartir el movimiento de boca y hacer que Tomás "hable" o mueva los labios. El prompt lo frena («his lips stay closed and he does not speak»), pero eso no garantiza nada.
2. **El giro de cabeza dentro de la profundidad de campo** invita al modelo a enfocar a Tomás, a moverlo hacia adelante o a cambiarle la cara. Eso rompe la regla de que no hay cambio de foco y le resta protagonismo al ojo de Martina.
3. **sync-3 con dos caras:** no está verificado a qué cara aplica la corrección. Si toma la de Tomás, el respaldo de post falla.
4. **Atención en la pantalla del celular:** a 85 mm, cualquier movimiento en el fondo compite con el desvío de ojos de Martina, que es el verdadero beat de culpa.

**Respaldos, en orden:**
- **A · Tomás quieto.** Misma toma, pero se saca la frase del giro: queda inmóvil, desenfocado y mirando a la puerta. Su reacción al nombre pasa al sonido, con un roce de chaqueta en 2,4 s. Es lo más barato: solo se cambia el prompt.
- **B · Sin Tomás: KF4b** (+0,48 USD). La culpa la carga solo el desvío de ojos hacia la izquierda del cuadro. Que Tomás está detrás ya se estableció en P2. Es el respaldo **recomendado** si la toma 1 muestra cualquiera de los problemas 1 o 2.
- **C · sync-3 con recorte.** Si hay que corregir la boca y Tomás está en cuadro:
  1. exportar desde Resolve un recorte de 1080×1080 solo con la cara de Martina;
  2. pasar sync-3 sobre ese recorte;
  3. componerlo de vuelta con una máscara suave.
  
  Así sync-3 ve una sola cara.
- **D · H3 Max Lip Sync desde KF4b** (+0,80 USD). Es el último recurso: no hay control de la actuación antes y después de la palabra, que es justo lo que importa en este plano.

---

## 6. Checklist de "alta producción" (para aprobar cada keyframe y cada clip)

**Imagen**
- [ ] Keyframe a 2K y clip a 1080P (1080×1920 después del conform). Nada escalado desde 480p o 768p.
- [ ] Piel con poros y textura real; sin piel de plástico, sin brillo de "IA", sin nitidez artificial ni look HDR.
- [ ] El rojo no satura ni pierde detalle: en el scope, el canal rojo no clipea en la cara ni en la mano.
- [ ] Cada luz tiene su fuente (tira roja, tubo frío) y es la misma en P2 y P4. No aparecen luces nuevas.
- [ ] Sin texto, subtítulos ni logos en cuadro (la falla de b02 del v2).

**Cámara**
- [ ] P1 y P3, fijos de verdad: superponiendo el primer y el último cuadro en modo *difference*, el marco de la puerta no se mueve.
- [ ] P2 y P4: mano leve, sin deriva hacia adelante, sin zoom y sin reencuadre. El foco no cambia.
- [ ] El fondo detrás del vidrio y detrás de Martina está quieto: ni vagones ni luces que se muevan.

**Continuidad**
- [ ] Mano **derecha**: pulgar a la derecha del cuadro, puño gris claro empapado entrando por abajo a la izquierda, cinco dedos, sin anillos ni reloj, puntas casi limpias.
- [ ] La mano no se limpia ni cambia a mitad del clip, y las manchas del vidrio no saltan (la falla FL de b01).
- [ ] Ventanita igual a F03; manchas secas arriba a la derecha y huella abajo a la izquierda.
- [ ] Martina igual a REF: mechones, sudor, suéter crema seco, sin manchas. Mira a la derecha del cuadro y desvía los ojos a la izquierda.
- [ ] Tomás de oliva, desenfocado y con la boca cerrada.

**Actuación**
- [ ] P1: el primer cuadro ya es el golpe; nada se mueve antes.
- [ ] P2: el sobresalto se lee sin sonido y ella no avanza.
- [ ] P3: el cambio de golpe a palma calmada se lee en menos de 1 s.
- [ ] P4: miedo, reconocimiento, palabra, culpa y respiración, en ese orden. La boca calza dentro de ±2 cuadros, sin sobrearticular.

**Prueba final**
- [ ] Verlo en un celular, a pantalla completa y **sin sonido**: ¿se entiende que alguien herido golpea, que ella lo reconoce y que lo esconde de Tomás?
- [ ] Ponerlo al lado de un fotograma de referencia de una serie real: ¿se aguanta la comparación?

---

## 7. Post (DaVinci Resolve)

1. **Conform:** 1080×1920 a 24 fps. Cortes secos con estos tiempos:
   - **P1:** clip B1, 0,00–1,50 (menos los cuadros de *ease-in*, si los hay).
   - **P2:** clip B2, ~0,10–1,60.
   - **P3:** clip B1, 3,00–5,00.
   - **P4:** clip B3, 0,00–~3,50, con corte en la inspiración.
2. **Limpieza antes del grano:**
   - reducción de ruido temporal suave, solo si el modelo deja parpadeo o textura de IA;
   - en P1 y P3, *Stabilizer → Camera Lock* si la cámara "fija" deriva;
   - sin nitidez extra.
3. **Gradación**, con un mismo nodo de look para los 4 planos:
   - empatar primero P2 con P4 (piel y rojo);
   - contraste de ~8:1 y negros con un poco de detalle;
   - compresión suave de altas luces en el rojo para que no clipee;
   - el tubo frío como único blanco del cuadro;
   - viñeta leve;
   - halation sutil en la tira roja y el tubo (Film Look Creator o el OFX de halation).
4. **Grano**, al final y a resolución final: Film Grain OFX, 35 mm, tamaño medio, intensidad baja. Es **el mismo en los 4 planos y en la tarjeta**, para que la textura sea una sola y no la que deja cada clip.
5. **Sonido** (Fairlight; el audio de los modelos se descarta):
   - **Fondo:** retumbo de tren continuo bajo los 4 planos, **una sola pista sin cortes**.
   - **Golpe 1** (P1, cuadro 0): palmada húmeda + golpe sordo en vidrio + vibración de la puerta + sub grave corto. Después, el fondo baja ~10 dB durante 1 s («y después silencio»).
   - **Golpe 2** (P2, +0,3 s, fuera de campo; ver la propuesta en P2): más sordo.
   - **P3:** un chirrido muy suave de piel mojada en el vidrio cuando la palma se apoya.
   - **P4:** la pista de ElevenLabs, alineada al mismo cuadro que se usó como `target_audio_url`; un roce de la chaqueta de Tomás en 2,4 s; y la inspiración. **Corte a negro con la imagen**, con un fundido de 2 cuadros.
   - **Tarjeta:** ~0,5 s de silencio y después «20 MINUTOS ANTES», si Cristián la deja en esta pieza, en la zona segura.
6. **Exportar:** H.264 de bitrate alto, 1080×1920. Mezcla en **−14 LUFS integrados** y −1 dBTP (objetivo habitual de Reels y TikTok, sin verificar para cada plataforma).
7. **Registro:** anotar en la hoja de la prueba las URLs de fal de cada toma, las seeds y qué respaldo se usó. Las URLs de fal pueden vencer, así que hay que **bajar los archivos el mismo día**.

---

## 8. Convenciones del repo que conviene mantener (de `agentes/asistente_direccion.md` y `agentes/prompter.md`)

- **FL solo si el último fotograma es una edición del primero y el cambio es de estado.** Por eso B1 parte desde el impacto con I2VA, y el único FL posible (toma 2 de B1) usa KF1b, una edición de KF1. Lo que rompió b01 en v1 y v2 fueron dos keyframes generados por separado.
- **En imagen, nada de *blood* ni *gore*:** se escribe *dark red-black stains*. Así se evitan bloqueos del safety checker y la estética de terror barato.
- **También aplican:** **2 tomas por bloque como máximo**, y **una sola generación para el plano que se repite** (el cold open y su momento en la escena 4, a las 0:45).

## 9. Pendientes y contradicciones que encontré (no se resolvieron aquí)

- **Ventanita:** ✅ Decidido (3-oct-2026): se mantiene F03 (rectángulo de esquinas redondeadas con malla de alambre fina en rombo) y se corrigió hc22.
- **Tablas de set y fichas v1 corregidas en este PR.** `set_ultimo_vagon_v1.md`, `set_ultimo_vagon_v2.md`, `fichas_personajes_v1.md` y `plan_assets_v1.md` ya dicen "antebrazo derecho". Pendiente: regeneración de `ESTADO_diego_mojado_herido.png` (ver `biblia/decisiones.md` y `fichas_personajes_v2.md` línea 29).
- **El YAML c01_b02 tiene la puerta a la izquierda del cuadro** ("off-screen left"). Con este eje va a la derecha.
- **El keyframe c01_p05 tiene el texto de la v3,** «Estoy en el tren.», y la v7 dice «Ya subí. Vagón 4.». No es parte del cold open, pero hay que regenerarlo antes de la escena 1.
- **Sin verificar:** si `target_audio_url` mueve los labios en H3 Max; si funciona a 1080P; si la promo del 40 % aplica también al modo Lip Sync; y si sync-3 elige bien la cara cuando hay dos en cuadro.
