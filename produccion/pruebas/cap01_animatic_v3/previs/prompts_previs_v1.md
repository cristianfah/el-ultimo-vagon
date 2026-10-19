# Previsualización cap. 1 · prompts v1 (director)

18-oct-2026 · guion `guion/cap01/cap01_v10.md` en `main` @ `f830bb7` (PR #11 y #12 ya fusionados) · plan `produccion/pruebas/cap01_animatic_v3/plan.md` (fase 4).
**Solo prompts: no se ha generado nada ni gastado nada.** Corre último vagón, después de los assets de la fase 3.

## Resumen

- **43 planos** del guion v10 (bloque 0: 4 · bloque 1: 5 · bloque 2: 4 · bloque 3: 6 · bloque 4: 6 · bloque 5: 9 · bloque 6: 3 · bloque 7: 6).
- **41 fotogramas los escribe el director.** F1 lo escribe el productor (`assets_v10/prompts_assets_v10.md`, §2, «Fotograma F1»). F3 no se genera: es el asset `PANTALLA_tomas_anden`, con «VAGÓN 2» en post.
- Endpoint: `openai/gpt-image-2.5/flare/edit` (b0_p1 en `sunburst/edit`) · `image_size: portrait_16_9` (9:16) · `quality: high` · 1 imagen por llamada.
- **Orden:** generar en el orden de la lista. Hay referencias de composición que dependen de fotogramas anteriores: b1_p2 ← b1_p1 · b1_f1 ← b1_p1 · b3_p1 ← b0_p2 · b5_p6 ← b5_p1 · b7_p5 ← b7_p2.
- **Esperan assets de la fase 3:** todo lo del vagón 2 usa `F08_v2_ambar_bajo` (respaldo: F08 original más la frase de luz baja). b1_f2 espera `cuarto_rapto_martina` v2 · b3_p4 y b3_p5 esperan `ESTADO_hombre_azul_infectado` · b5_p4, b5_p5 y b6_p2 esperan `ESTADO_carmen_palma`. Los demás se pueden correr ya.
- Todas las URL de fal de `produccion/assets/fal_urls_v1.json` (main) respondieron 200 el 18-oct-2026 a las 21:25 (UTC-3).

## Costo estimado (GPT Image 2.5 en fal)

- Precio publicado por fal (página del modelo, medido el 8-sep-2026): edición en calidad **high**, 1024×1536 vertical, **0,0495 USD** con una referencia; cada referencia extra suma **unos 0,008 USD**, y un prompt largo suma un poco más. Flare y sunburst cuestan lo mismo. **No verifiqué el precio exacto de `portrait_16_9`**: lo estimo como el vertical de 1024×1536.
- Con 156 referencias en total (de 2 a 8 por fotograma): **~3,0 USD** para los 41 según la tabla publicada.
- Cobro real que ya registró el repo: 0,15 USD por imagen (Diego v3, `tomas.json`), que coincide con el ~0,15 de `metodo.md` → **~6,2 USD** si se cobra así.
- **Estimación: entre 3 y 6,2 USD por los 41**, más ~0,15 por el F1 del productor. Una pasada de correcciones de ~10 fotogramas sumaría 0,5 a 1,5 USD. Queda bajo los ~10 USD de la partida del plan.

## Contradicciones y decisiones abiertas

1. **Cuarto del rapto (silla):** el §2 de `prompts_assets_v10.md` ya está bien: conserva la silla sin brazos y amarra las muñecas sobre los muslos. **Pero la sección «Retomas propuestas» de `produccion/pruebas/cap01_animatic/notas.md` y `/workspace/fahren-tv/midjourney/a01_retoma_looks.md` todavía traen el prompt antiguo**, con las muñecas sobre las piernas pegadas al borde del asiento. El texto de la pauta de Midjourney (`pauta_look_cap01_v3.md`) dice «silla con brazos». Que nadie corra esas versiones.
2. **Escala del corte por coincidencia:** el P1 del tren es un plano medio de cintura arriba, y el F1 del productor encuadra del pecho bajo a la mitad de los muslos, sin la cara. El corte calza por posición (muñecas en el tercio inferior, la derecha a la izquierda del cuadro), no por tamaño. Si Cristián quiere un corte exacto, el F1 tendría que ser también de cintura arriba con la cara.
3. **Manga del bloque 0 P2 (decisión de Cristián):** la v10 dice «la manga avena sobre los nudillos», pero Martina lleva el abrigo carbón encima. Escribí la manga del abrigo carbón, con el puño del suéter avena asomando sobre los nudillos. Así se cumplen las dos cosas. Falta que Cristián lo confirme.
4. **«Cerrojo» (5 P8, Estado del mundo bloque 7):** el set aprobado (`set_ultimo_vagon_v2.md`) solo tiene una placa de bronce con la bocallave arriba y la manija abajo; no tiene cerrojo. En los prompts, la mano de Hugo va «en la manija de la cerradura». Si se quiere un pestillo, hay que agregarlo al set.
5. **Plancha que falta en fal:** `F11_rojo_pasajeros_hacia_atras` (el contraplano del vagón hacia atrás, para la entrada de Hugo en 4 P5) está aprobada en Drive, pero no está en `fal_urls_v1.json`. Usé F10 más el texto. Tampoco hay una plancha de la puerta del vagón 5 vista desde el fuelle (5 P2 a P4); usé F07.
6. **Vagón 5 en ámbar:** no hay una plancha ámbar del vagón 5 hacia la puerta. Para 4 P1 usé `F08_ambar_pasajeros_hacia_puerta`, el original con todas las lámparas encendidas, porque el vagón 5 no lleva el ámbar bajo. Su ventanita trae una lámpara encendida detrás, y el prompt la pide oscura.
7. **Iván en el bloque 7:** el guion lo deja «junto a la puerta», y en 7 P3 se aplicó la nota del guionista: va en primer término, en el borde izquierdo, desenfocado. En 7 P1 (desde atrás) queda junto a la puerta.
8. **La mujer que lee (0 P4 y 3 P6)** no tiene hoja de personaje: va solo descrita. Es un extra, pero puede cambiar de cara entre los dos planos.
9. **Tope de gasto:** el plan dice 40 USD (propuesto) y el mensaje de hoy dice 25 USD (pendiente). Cristián tiene que confirmar cuál vale.

## Revisión global contra la lista (sección 5 de `revision_v1.md`) y la pauta de look

- Cámara: todos los planos llevan tamaño, altura, lente y tipo de cámara, con el motivo del movimiento cuando lo hay. El ritmo y el montaje no se aplican a fotogramas fijos; las duraciones del guion van en cada encabezado.
- Regla de 180° y ejes de mirada: en el vagón 5, Martina a la izquierda y Tomás a la derecha. En el último vagón, desde atrás, Martina a la izquierda de Tomás; desde el lado de la puerta, Martina a la derecha y Tomás a la izquierda, y él mira hacia la derecha.
- Estado del mundo: el maletín queda bajo el asiento del hombre, por el lado del pasillo, en 0 P2 a P4 y 3 P1 a P2, y no se ve en los demás. La palma derecha de Carmen se ve desde 5 P4, y en el bloque 7 su mano queda dentro del abrigo. La llave queda en el bolsillo de Hugo desde 5 P6, y su mano siempre va vacía. Diego va mojado, con la manga derecha manchada y sin herida a la vista. Por la ventanita nunca se ve cielo ni lluvia, la puerta lateral del fuelle está cerrada y en el vagón 2 la ventanita queda negra. Los infectados solo vienen por delante o desde el vagón 5, nunca por la puerta de Hugo.
- Causa antes que efecto: el vidrio revienta en 5 P3, antes de que Carmen se corte en 5 P4 y 5 P5; la niebla sale en 3 P2, antes de la infección en 3 P4.
- Las reacciones en grupo van en ola (3 P6, 4 P1, 4 P5, 7 P3).
- Luz: el vagón 2 en ámbar bajo con 3 de 8 lámparas; el rojo con su tubo frío sobre la puerta y zonas negras; el cuarto del rapto frío, sin ámbar ni rojo. Todos los prompts cierran con el bloque contra el look «IA» (grano 500T, piel con poros, sin HDR, sin halos) y con «No text, no captions, no watermark.».
- Ningún prompt lleva las palabras prohibidas; lo comprueba el script.

## Planos

### b0_p1 · bloque 0 P1 · llamada c00a · 0:00 (1.2 s)

- **Modelo:** `openai/gpt-image-2.5/sunburst/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. MOMENT: extreme close-up of Martina's eyes, the first frame of the chapter, already in motion. She stands in the aisle in profile facing frame LEFT (her left cheek and the small mole on her left cheekbone toward camera), framed from the brow to the upper lip. Her eyes have just darted to the far end of the aisle at frame left, whites showing, breath held, lips pressed, a loose strand of dark hair on her cheek. A single reading-lamp beam cuts diagonally across her eyes; the rest of her face falls into shadow. CAMERA: handheld, centimetres from her face at her standing eye height, 85mm, f/2, focus on the near eye, background a dark amber blur. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. Martina wears her oat knit sweater under the open charcoal coat; the red mark on her right wrist stays hidden under the sleeve. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Tamaño PPP ✓ · altura ojos de pie ✓ · en mano ✓ · mirada con destino (fondo del pasillo, izq.) ✓ · luz ámbar bajo, 1 lámpara ✓ · sin texto ✓ · pauta: sin brillo en ojos, sombra real ✓

### b0_p2 · bloque 0 P2 · llamada c00a · 0:01.2 (1.8 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `HOJA_extra_pareja_camisa_azul` — https://v3b.fal.media/files/b/0aaeee79/Y-JPlHDGfrxyuD28x8lFG_HOJA_extra_pareja_camisa_azul.png
  3. `PROP_maletin_v2` — https://v3b.fal.media/files/b/0aaeeeb3/XmGD-bbhILh7w0-tYMXaS_prop_maletin_v2_nbp_0.png
  4. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is the blue-shirt man (bright cobalt-blue shirt) and his wife. Identity and wardrobe only. Image 3 is the briefcase: exact shape, dark body, metal corners. Image 4 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. MOMENT: floor-level insert. Under the window seat of the sleeping blue-shirt man (only his dark shoes and trouser hems visible, upper frame), the briefcase is half under the seat on its AISLE side, its back edge jammed on the seat's metal rail. Martina's RIGHT hand enters from frame right on top of the briefcase: the charcoal coat sleeve with the oat sweater cuff pulled down over her knuckles, fingers trembling. At the same instant the toe of her brown boot, also from frame right, pushes the briefcase's metal corner the last few centimetres under the seat. CAMERA: locked off on the aisle floor at floor level, 35mm, f/2.8, focus on the metal corner and her fingers; the double rubber strip of the floor runs into the dark. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. One amber cone grazes the floor and catches the metal corner; the rest is shadow. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Mano DERECHA ✓ · maletín bajo el asiento del hombre, lado pasillo ✓ (no se mueve después) · bota la empuja ✓ · manga: abrigo gris con puño avena sobre los nudillos (DECISIÓN abierta, ver informe) · dedos separados ✓ · sin texto ✓

### b0_p3 · bloque 0 P3 · llamada c00a · 0:03 (1.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_extra_pareja_camisa_azul` — https://v3b.fal.media/files/b/0aaeee79/Y-JPlHDGfrxyuD28x8lFG_HOJA_extra_pareja_camisa_azul.png
  2. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  3. `PROP_maletin_v2` — https://v3b.fal.media/files/b/0aaeeeb3/XmGD-bbhILh7w0-tYMXaS_prop_maletin_v2_nbp_0.png
  4. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)

```text
FILM STILL, vertical 9:16. Image 1 is the blue-shirt man (bright cobalt-blue shirt) and his wife. Identity and wardrobe only. Image 2 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 3 is the briefcase: exact shape, dark body, metal corners. Image 4 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. MOMENT: medium shot from across the aisle at seated height. The blue-shirt man sits at frame LEFT in the window seat, asleep, his head sliding down the window glass, mouth open mid-snore; his wife sleeps on his shoulder in the aisle seat, centre-right. At the RIGHT edge of frame Martina stands in the aisle, cut at mid-torso, frozen, her RIGHT hand gripping the top of the aisle-side seatback, her eyes locked on him (looking toward frame left). Only the briefcase's metal corner shows under his seat at the bottom edge, aisle side. CAMERA: handheld at seated eye height, 32mm, f/2.8, slight horizontal motion blur from a short fast pan from him to her; focus on the man. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. The nearest lit lamp sits just ahead of their row and spills warm light on the couple; Martina is half in shadow. The window behind him: black night, rain on the outside only. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Plano medio altura asiento ✓ · él izq./esposa pasillo der./Martina borde der. ✓ · mirada de Martina hacia la izq. (a él) ✓ · mano en respaldo, natural ✓ · maletín misma posición ✓ · lluvia solo en ventana lateral ✓

### b0_p4 · bloque 0 P4 · llamada c00b · 0:04.5 (1.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `PROP_maletin_v2` — https://v3b.fal.media/files/b/0aaeeeb3/XmGD-bbhILh7w0-tYMXaS_prop_maletin_v2_nbp_0.png
  3. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is the briefcase: exact shape, dark body, metal corners. Image 3 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. MOMENT: wide shot down the aisle toward the tail of carriage 2. Foreground bottom-left, out of focus, the briefcase's metal corner peeking from under the blue-shirt man's seat on the aisle side. Mid-ground, Martina walks away fast down the aisle toward the rear door, back to camera, coat open and swinging, not running and not looking back. Background right, across the aisle, a woman reading a book under her lit lamp, unaware; a young man with earphones lit by his phone. At the end, the rear door. CAMERA: locked off at seated eye height, 32mm, f/4, focus on Martina. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. The small wired-glass window of the inter-carriage door shows only the dark, unlit gangway, black glass, still relative to camera: no sky, no rain, no lamp. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** General fijo altura asiento ✓ · maletín en primer término, mismo lugar ✓ · lectora a la der. (la misma de b3_p6) ✓ · ventanita negra ✓ · nadie aparece de la nada ✓

### b1_p1 · bloque 1 P1 · llamada c01 · 0:06 (0.8 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. MOMENT: MEDIUM shot, waist up, of Martina leaning with her back against the rear end door of carriage 2, facing camera. Her eyes are closing, lids almost shut, jaw tight. In front of her body at waist height her LEFT hand squeezes her RIGHT wrist over the sweater sleeve, knuckles pale. COMPOSITION LOCK for the match cut to the kidnap flash: both wrists sit in the LOWER third of the frame, in the lower-centre, with her right wrist on the LEFT of frame and her left hand gripping it from the right; her head in the upper third. Behind her head the door's small wired-glass window. CAMERA: locked off at her chest height, 40mm, f/2.8, focus on her face, wrists still sharp. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. One lit reading lamp from frame right sculpts her face and hands; the rest is shadow. The small wired-glass window of the inter-carriage door shows only the dark, unlit gangway, black glass, still relative to camera: no sky, no rain, no lamp. Martina wears her oat knit sweater under the open charcoal coat; the red mark on her right wrist stays hidden under the sleeve. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Plano medio (cintura arriba) ✓ · ojos cerrándose ✓ · izq. aprieta der. a la cintura, muñeca der. a la IZQ. del cuadro, tercio inferior ✓ (calza con el F1 del productor) · ventanita negra ✓ · marca tapada ✓

### b1_f1 · bloque 1 F1 · llamada c01f · 0:06.8 (0.7 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** prompt del productor
- **Referencias (en este orden):**
  1. `cuarto_rapto_martina_v2` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §2)
  2. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  3. `previs/b1_p1.png` — (fotograma aprobado de b1_p1; generar antes)

```text
NO LO ESCRIBE EL DIRECTOR: usar el prompt «Fotograma F1 de la previsualización» del productor en /workspace/fahren-tv/el-ultimo-vagon/assets_v10/prompts_assets_v10.md (§2). Depende de cuarto_rapto_martina v2 y de b1_p1.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Lo revisa el productor. Director: confirmar que las muñecas caen en el mismo tercio inferior que en b1_p1, con la muñeca derecha a la izquierda del cuadro.

### b1_f2 · bloque 1 F2 · llamada c01f · 0:07.5 (0.7 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** espera cuarto_rapto_martina v2
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `cuarto_rapto_martina_v2` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §2)
  3. `PROP_maletin_v2` — https://v3b.fal.media/files/b/0aaeeeb3/XmGD-bbhILh7w0-tYMXaS_prop_maletin_v2_nbp_0.png

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is the kidnap room (approved armless metal folding chair, concrete, hard cold downlight, masked figures, monitor) with Martina's wrists taped together on her thighs. Image 3 is the briefcase: exact shape, dark body, metal corners. MOMENT: medium shot in the kidnap room. Martina sits on the approved armless metal folding chair, her wrists taped together with matte grey duct tape resting on the middle of her thighs, right wrist on top at frame left. She looks up toward frame right at a figure in a smooth featureless grey mask and a dark jacket who stands at frame right, bent forward, both gloved hands setting the briefcase down across her KNEES — the instant it touches. The briefcase sits forward on her knees, below and in front of her wrists, so the grey tape and both wrists stay fully visible above it and are never covered. The other two masked figures stand behind her, dark and still. CAMERA: locked off, slightly above her seated eye height, 35mm, f/2.8, focus on her wrists and the briefcase. LIGHT: Kidnap room: bare concrete, one hanging lamp with a hard cold white downlight, deep shadows in the eye sockets and under the nose, short black shadow under the chair, almost black outside the cone, a faint cyan edge from the monitor at frame right. No amber, no red. The monitor shows only a blank cyan-white glow. Martina wears her oat knit sweater under the open charcoal coat; her wrists are covered by the tape. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Silla aprobada sin brazos ✓ · muñecas juntas con cinta sobre los muslos, VISIBLES, el maletín no las tapa ✓ · maletín sobre las rodillas (Estado del mundo bloque 1) ✓ · máscara lisa sin rasgos ✓ · luz fría, sin ámbar ni rojo ✓ · monitor sin texto ✓

### b1_f3 · bloque 1 F3 · llamada F3 (imagen fija) · 0:08.2 (0.8 s)

- **Modelo:** `(sin generación)` · `image_size: portrait_16_9` (9:16) · `quality: -` · **Estado:** usa asset
- **Referencias (en este orden):**
  1. `PANTALLA_tomas_anden` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §3)

```text
NO SE GENERA: se usa el asset PANTALLA_tomas_anden (prompt del productor, assets_v10 §3) con un empuje leve en post. Franja inferior oscura vacía para «VAGÓN 2», que va en post.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Sin texto generado; tercio inferior vacío para «VAGÓN 2» en post.

### b1_p2 · bloque 1 P2 · llamada c01 · 0:09 (1.0 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)
  3. `previs/b1_p1.png` — (fotograma aprobado de b1_p1; generar antes)

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. Image 3 is composition, framing and light of shot b1_p1: keep the same camera position and framing. MOMENT: the same MEDIUM waist-up framing and position as the composition reference (her back against the rear end door, facing camera). Her eyes have just snapped open, gaze fixed forward down the carriage just past the left side of the lens. Her left hand has let go of the wrist and is pulling the sweater sleeve down over her right wrist, in the lower third, right wrist on the LEFT of frame; her right shoulder is already turning toward the door behind her to push it open. CAMERA: locked off at her chest height, 40mm, f/2.8. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. Same single lamp from frame right. The small wired-glass window of the inter-carriage door shows only the dark, unlit gangway, black glass, still relative to camera: no sky, no rain, no lamp. Martina wears her oat knit sweater under the open charcoal coat; the red mark on her right wrist stays hidden under the sleeve. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Mismo encuadre que b1_p1 ✓ · ojos abiertos con destino (fondo del vagón) ✓ · estira la manga, marca tapada ✓ · lado de las muñecas igual ✓ · ventanita negra ✓

### b2_p1 · bloque 2 P1 · llamada c02 · 0:10 (3.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  3. `F09_ambar_asiento_pareja` — https://v3b.fal.media/files/b/0aaca77b/PzOwbqmC0cGCK6rcDZl44_F09_ambar_asiento_pareja.png

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 3 is carriage 5, the couple's seats and the amber light. MOMENT: frontal two-shot from the facing seat, framed from the knees up. Martina at frame LEFT in the window seat, Tomás at frame RIGHT in the aisle seat. She has just dropped into the seat and is adjusting her open coat with both hands, eyes down on the coat, not looking at him: too casual, a forced ease. Tomás is turned toward her (looking toward frame left), eyebrows slightly raised, curious with a hint of suspicion, lips just closing after a question. CAMERA: handheld, barely breathing, at seated eye height, 35mm, f/2.8, focus on both. LIGHT: Carriage 5 at night in warm amber from the reading lamps (~3000K), practical light only, deeper shade between lamps; rear passengers dozing, soft and dark. Side window: black night, rain only on the outside of the glass. The window at frame left behind Martina. Martina wears her oat knit sweater under the open charcoal coat; the red mark on her right wrist stays hidden under the sleeve. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Martina izq./Tomás der. (180°) ✓ · Tomás mira a la izq. (a ella) ✓ · ella no lo mira, manos ocupadas con el abrigo (toma 2B casual) ✓ · lluvia solo afuera ✓ · marca tapada ✓

### b2_p2 · bloque 2 P2 · llamada c02 · 0:13.5 (1.0 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `F09_ambar_asiento_pareja` — https://v3b.fal.media/files/b/0aaca77b/PzOwbqmC0cGCK6rcDZl44_F09_ambar_asiento_pareja.png

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is carriage 5, the couple's seats and the amber light. MOMENT: close insert of Martina's RIGHT wrist on her lap: the sweater and coat sleeve have ridden up and reveal a narrow raw red band around the wrist, an abrasion mark like a tight binding left (not a bracelet, not a thread, no jewellery). Her LEFT fingers already pinch the cuff, mid-yank, pulling the sleeve down over it. CAMERA: locked off, close, at her lap height, 85mm, f/2.8, focus on the mark. LIGHT: Carriage 5 at night in warm amber from the reading lamps (~3000K), practical light only, deeper shade between lamps; rear passengers dozing, soft and dark. Side window: black night, rain only on the outside of the glass. Warm lamp light from above on her hands, the jeans in shade. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Muñeca DERECHA ✓ · marca se lee como marca, no pulsera ✓ · dedos izquierdos la tapan ✓ · un solo gesto ✓

### b2_p3 · bloque 2 P3 · llamada c02 · 0:14.5 (3.0 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  2. `F09_ambar_asiento_pareja` — https://v3b.fal.media/files/b/0aaca77b/PzOwbqmC0cGCK6rcDZl44_F09_ambar_asiento_pareja.png

```text
FILM STILL, vertical 9:16. Image 1 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 2 is carriage 5, the couple's seats and the amber light. MOMENT: close-up of Tomás from mid-chest up, positioned at frame RIGHT, looking toward frame LEFT at Martina (out of frame). A soft half smile: he has decided not to insist; lips parting on the first word of a gentle, sincere question. CAMERA: handheld, easing in slightly toward him, at seated eye height, 50mm, f/2, focus on his eyes behind the glasses. LIGHT: Carriage 5 at night in warm amber from the reading lamps (~3000K), practical light only, deeper shade between lamps; rear passengers dozing, soft and dark. Side window: black night, rain only on the outside of the glass. A warm lamp catches the rim of his metal frames; dozing passengers soft behind him. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** PP de pecho arriba, Tomás a la der. ✓ · mira a la izq. (a Martina fuera de cuadro) ✓ · entrega 3C suave ✓ · anteojos y chaqueta azul ✓

### b2_p4 · bloque 2 P4 · llamada c02 · 0:17.5 (4.0 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  3. `F09_ambar_asiento_pareja` — https://v3b.fal.media/files/b/0aaca77b/PzOwbqmC0cGCK6rcDZl44_F09_ambar_asiento_pareja.png

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 3 is carriage 5, the couple's seats and the amber light. MOMENT: close-up of Martina from just below the chest up, positioned at frame LEFT. She stares straight ahead toward the front of the train, just past the left side of the lens, never at Tomás; jaw clenched, flat expression, the line just finished. At the bottom right of frame, Tomás's hand (navy quilted cuff) has entered from frame right and rests over her LEFT hand on the armrest; she does not look and does not pull away. CAMERA: handheld, still, at seated eye height, 50mm, f/2, focus on her eyes. LIGHT: Carriage 5 at night in warm amber from the reading lamps (~3000K), practical light only, deeper shade between lamps; rear passengers dozing, soft and dark. Side window: black night, rain only on the outside of the glass. Martina wears her oat knit sweater under the open charcoal coat; the red mark on her right wrist stays hidden under the sleeve. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** PP, Martina a la izq. ✓ · mira al frente, nunca a él ✓ · mano de Tomás entra por la der. sobre su mano izquierda ✓ · manos naturales ✓ · marca tapada ✓

### b3_p1 · bloque 3 P1 · llamada c03a · 0:21.5 (1.3 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_extra_pareja_camisa_azul` — https://v3b.fal.media/files/b/0aaeee79/Y-JPlHDGfrxyuD28x8lFG_HOJA_extra_pareja_camisa_azul.png
  2. `PROP_maletin_v2` — https://v3b.fal.media/files/b/0aaeeeb3/XmGD-bbhILh7w0-tYMXaS_prop_maletin_v2_nbp_0.png
  3. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)
  4. `previs/b0_p2.png` — (fotograma aprobado de b0_p2; generar antes)

```text
FILM STILL, vertical 9:16. Image 1 is the blue-shirt man (bright cobalt-blue shirt) and his wife. Identity and wardrobe only. Image 2 is the briefcase: exact shape, dark body, metal corners. Image 3 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. Image 4 is composition, framing and light of shot b0_p2: keep the same camera position and framing. MOMENT: the SAME floor-level framing as the composition reference (b0_p2), without any hand or boot: the briefcase in exactly the same place under the blue-shirt man's seat, aisle side. Both latches have sprung open on their own and the lid has lifted just a finger's width; a thin thread of white mist begins to seep out of the gap. His dark shoes behind, still. CAMERA: locked off at floor level, 35mm, f/2.8, focus on the latches. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. One amber cone on the metal corner and the open latches. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Mismo encuadre que b0_p2 ✓ · maletín mismo lugar ✓ · se abre solo, tapa solo un dedo ✓ · nadie lo toca ✓ · niebla fina ✓

### b3_p2 · bloque 3 P2 · llamada c03a · 0:22.8 (1.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_extra_pareja_camisa_azul` — https://v3b.fal.media/files/b/0aaeee79/Y-JPlHDGfrxyuD28x8lFG_HOJA_extra_pareja_camisa_azul.png
  2. `PROP_maletin_v2` — https://v3b.fal.media/files/b/0aaeeeb3/XmGD-bbhILh7w0-tYMXaS_prop_maletin_v2_nbp_0.png
  3. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)

```text
FILM STILL, vertical 9:16. Image 1 is the blue-shirt man (bright cobalt-blue shirt) and his wife. Identity and wardrobe only. Image 2 is the briefcase: exact shape, dark body, metal corners. Image 3 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. MOMENT: low shot near the floor. Thin white mist creeps across the floor out of the briefcase's gap (bottom edge of frame) between the blue-shirt man's shoes and climbs around his shins up to his knees; his trousers from Image 1, his hands resting slack on his thighs at the top edge. CAMERA: tilting up slowly with the mist from the shoes to the knees, at shin height, 35mm, f/2.8. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. The mist catches the amber cone and is otherwise grey in shadow, thin and low, not dense. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Niebla fina desde el maletín hacia él (causa antes del efecto) ✓ · maletín en su lugar ✓ · sin niebla densa ✓

### b3_p3 · bloque 3 P3 · llamada c03a · 0:24.3 (2.2 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_extra_pareja_camisa_azul` — https://v3b.fal.media/files/b/0aaeee79/Y-JPlHDGfrxyuD28x8lFG_HOJA_extra_pareja_camisa_azul.png
  2. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)

```text
FILM STILL, vertical 9:16. Image 1 is the blue-shirt man (bright cobalt-blue shirt) and his wife. Identity and wardrobe only. Image 2 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. MOMENT: medium shot of the couple from across the aisle. The blue-shirt man at frame LEFT, in the window seat, awake and doubled over coughing hard, eyes looking down at the thin mist that reaches his chest, his RIGHT hand at his throat. His wife still asleep on his shoulder in the aisle seat at frame RIGHT. CAMERA: handheld, slight, at seated eye height, 35mm, f/2.8. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. The lit lamp just ahead of their row lights them; the window behind him: black night, rain on the outside only. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Él izq./esposa der. (igual que b0_p3) ✓ · mano DERECHA al cuello ✓ · mira hacia abajo, a la niebla ✓ · ella dormida ✓

### b3_p4 · bloque 3 P4 · llamada c03b · 0:26.5 (1.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** espera ESTADO_hombre_azul_infectado
- **Referencias (en este orden):**
  1. `ESTADO_hombre_azul_infectado` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §4)
  2. `HOJA_extra_pareja_camisa_azul` — https://v3b.fal.media/files/b/0aaeee79/Y-JPlHDGfrxyuD28x8lFG_HOJA_extra_pareja_camisa_azul.png
  3. `ref_infectados` — https://v3b.fal.media/files/b/0aaeee57/acsDjue9s2V4HF70fQcO-_ref_infectados.jpg
  4. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)

```text
FILM STILL, vertical 9:16. Image 1 is the blue-shirt man infected: milky white eyes, dark veins from the neck up to the jaw. Image 2 is the blue-shirt man (bright cobalt-blue shirt) and his wife. Identity and wardrobe only. Image 3 is infection look only (eyes, skin, veins); ignore faces, wardrobe and setting. Image 4 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. MOMENT: very close close-up of the blue-shirt man. His eyes have turned fully milky white, no iris, no glow; dark grey-violet veins climb from his collar up his neck to the jaw and stop there. He has stopped coughing; mouth slack. His head is turning slowly toward frame RIGHT, toward his sleeping wife (a strand of her hair at the right edge). CAMERA: handheld, still, very close, 50mm, f/2, focus on the near eye. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. Warm side light from the lamp, deep shadow on the far side of his face. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Ojos blancos + venas hasta la mandíbula ✓ · cabeza gira a la der. (a la esposa) ✓ · sin heridas ✓ · pauta: no maquillaje de Halloween, ojos sin brillo ✓

### b3_p5 · bloque 3 P5 · llamada c03b · 0:28 (1.0 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** espera ESTADO_hombre_azul_infectado
- **Referencias (en este orden):**
  1. `ESTADO_hombre_azul_infectado` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §4)
  2. `HOJA_extra_pareja_camisa_azul` — https://v3b.fal.media/files/b/0aaeee79/Y-JPlHDGfrxyuD28x8lFG_HOJA_extra_pareja_camisa_azul.png
  3. `ref_infectados` — https://v3b.fal.media/files/b/0aaeee57/acsDjue9s2V4HF70fQcO-_ref_infectados.jpg
  4. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)

```text
FILM STILL, vertical 9:16. Image 1 is the blue-shirt man infected: milky white eyes, dark veins from the neck up to the jaw. Image 2 is the blue-shirt man (bright cobalt-blue shirt) and his wife. Identity and wardrobe only. Image 3 is infection look only (eyes, skin, veins); ignore faces, wardrobe and setting. Image 4 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. MOMENT: medium shot at the instant of impact: the infected man lunges toward frame RIGHT onto his wife, both hands on her shoulders, his weight crashing into her against the aisle seat; her eyes snapping open. The shot cuts on the impact: no wound, nothing graphic. CAMERA: handheld, shaken by the hit, motion blur on the bodies, at seated eye height, 32mm. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Se lanza a la der., sobre la esposa (corrige a03 v1) ✓ · corte en el impacto, sin nada gráfico ✓ · cámara sacudida ✓

### b3_p6 · bloque 3 P6 · llamada c03b · 0:29 (1.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `F08_v2_ambar_bajo` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §1). Respaldo si no está: F08_ambar_pasajeros_hacia_puerta + la frase de luz baja del prompt (respaldo: `F08_ambar_pasajeros_hacia_puerta` https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png)
  2. `HOJA_extra_pareja_camisa_azul` — https://v3b.fal.media/files/b/0aaeee79/Y-JPlHDGfrxyuD28x8lFG_HOJA_extra_pareja_camisa_azul.png

```text
FILM STILL, vertical 9:16. Image 1 is carriage 2 set and its LOW amber light: only three of the eight reading lamps lit, the far door window black. Image 2 is the blue-shirt man (bright cobalt-blue shirt) and his wife. Identity and wardrobe only. MOMENT: wide shot of the aisle. Across the aisle at frame RIGHT the woman who was reading (the same one from the opening) springs up screaming, her book falling from her hands in mid-air. Foreground left, the couple's seat as a dark struggling tangle, shapes only. Behind, passengers waking in a wave: the nearest already turning, the next lifting a head, the farthest still asleep. Thin white mist covers the aisle floor. CAMERA: handheld, arriving late to the scream, framing slightly off-centre and catching up, 28mm, at seated eye height. LIGHT: Carriage 2 near midnight in LOW amber, matching the F08_v2_ambar_bajo plate: of the eight reading lamps under the luggage racks only three are lit; every other fixture is dark. Short warm cones (~2800K) with real darkness between them, ceiling lights off, passengers in deep shade, almost silhouettes. Side windows: black night with rain only on the outside of the glass and faint interior reflections, no landscape. The small wired-glass window of the inter-carriage door shows only the dark, unlit gangway, black glass, still relative to camera: no sky, no rain, no lamp. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Lectora a la der. (misma de b0_p4) ✓ · reacción en ola ✓ · niebla en el piso ✓ · cámara llega tarde ✓ · ventanita negra ✓

### b4_p1 · bloque 4 P1 · llamada c04a · 0:30.5 (1.8 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_ivan` — https://v3b.fal.media/files/b/0aaca77b/jKxRb5IV8dbedLGy4_Kdq_HOJA_ivan.png
  2. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  3. `F08_ambar_pasajeros_hacia_puerta` — https://v3b.fal.media/files/b/0aaca77b/vgqFytQvyrQx4kWSLF2fi_F08_ambar_pasajeros_hacia_puerta.png
  4. `F09_ambar_asiento_pareja` — https://v3b.fal.media/files/b/0aaca77b/PzOwbqmC0cGCK6rcDZl44_F09_ambar_asiento_pareja.png

```text
FILM STILL, vertical 9:16. Image 1 is Iván: shaved head, broken nose, canvas worker jacket. Identity and wardrobe only. Image 2 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 3 is passenger carriage geometry and amber light, looking toward the front door. Image 4 is carriage 5, the couple's seats and the amber light. MOMENT: wide shot toward the front door of carriage 5 at the eye height of a seated passenger. A muffled scream has just come from ahead: heads rise in a wave. A passenger near the front door already stands staring at it; Iván, mid-carriage, is halfway up, pushing off the seat with both hands; Carmen, nearer camera, is just waking, head lifting, glasses on the cord against her chest, bag on her left shoulder. CAMERA: handheld, slight, 32mm, f/2.8. LIGHT: Carriage 5 at night in warm amber from the reading lamps (~3000K), practical light only, deeper shade between lamps; rear passengers dozing, soft and dark. Side window: black night, rain only on the outside of the glass. The front door's small window: only the dark gangway, nothing in it yet. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Ola: pasajero → Iván → Carmen ✓ · Iván se apoya en el asiento (peso) ✓ · bolso hombro izq. ✓ · ventanita oscura, aún sin siluetas ✓ · ámbar antes del apagón ✓

### b4_p2 · bloque 4 P2 · llamada c04a · 0:32.3 (1.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  3. `F09_ambar_asiento_pareja` — https://v3b.fal.media/files/b/0aaca77b/PzOwbqmC0cGCK6rcDZl44_F09_ambar_asiento_pareja.png

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 3 is carriage 5, the couple's seats and the amber light. MOMENT: close-up of Martina, chest up, at frame left-centre, from the facing seat. She knows: face drained, eyes fixed past the lens toward the front door. Her LEFT hand clamps onto Tomás's arm; Tomás, out of focus at the RIGHT edge of frame, is turning his head toward her. CAMERA: handheld, 50mm, f/2, focus on her eyes. LIGHT: Carriage 5 at night in warm amber from the reading lamps (~3000K), practical light only, deeper shade between lamps; rear passengers dozing, soft and dark. Side window: black night, rain only on the outside of the glass. Martina wears her oat knit sweater under the open charcoal coat; the red mark on her right wrist stays hidden under the sleeve. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Mano IZQUIERDA sobre Tomás, que está a la der. del cuadro ✓ · mirada a la puerta delantera ✓ · Tomás gira hacia ella ✓

### b4_p3 · bloque 4 P3 · llamada c04a · 0:33.8 (1.2 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `F10_rojo_pasajeros_hacia_puerta` — https://v3b.fal.media/files/b/0aaeee79/CcgvlprGujBKr1bN0wAuC_F10_rojo_pasajeros_hacia_puerta.png
  2. `HOJA_ivan` — https://v3b.fal.media/files/b/0aaca77b/jKxRb5IV8dbedLGy4_Kdq_HOJA_ivan.png
  3. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png

```text
FILM STILL, vertical 9:16. Image 1 is carriage 5 geometry in red emergency light, looking toward the front door. Image 2 is Iván: shaved head, broken nose, canvas worker jacket. Identity and wardrobe only. Image 3 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. MOMENT: wide shot of carriage 5 toward the front door at the instant the red emergency strip snaps on after the blackout: reading lamps dead, the cabin mostly black, the narrow red strip along the ceiling just lit, passengers frozen mid-movement as dark silhouettes (Iván standing mid-aisle, Carmen half risen). CAMERA: locked off, seated eye height, 32mm, f/4. LIGHT: Carriage 5 in red emergency light: the narrow continuous red strip along the centre of the ceiling is the dominant source (#B3001B), deep and dark, not pink or magenta; faces half in shadow, real black zones, no white fill. Side windows black with rain on the outside of the glass. The front door's small window: dark gangway with a faint red cast. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Fija ✓ · apagón → rojo ✓ · sin luz blanca de relleno ✓ · pauta: contraste con negros ✓

### b4_p4 · bloque 4 P4 · llamada c04a · 0:35 (1.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `F10_rojo_pasajeros_hacia_puerta` — https://v3b.fal.media/files/b/0aaeee79/CcgvlprGujBKr1bN0wAuC_F10_rojo_pasajeros_hacia_puerta.png
  2. `ref_infectados` — https://v3b.fal.media/files/b/0aaeee57/acsDjue9s2V4HF70fQcO-_ref_infectados.jpg

```text
FILM STILL, vertical 9:16. Image 1 is carriage 5 geometry in red emergency light, looking toward the front door. Image 2 is infection look only (eyes, skin, veins); ignore faces, wardrobe and setting. MOMENT: the small wired-glass window of carriage 5's front door, close. Two infected silhouettes have just slammed into the glass from the gangway side: palms flat and a face pressed against the rhombic wire mesh, dark smears on the glass; the door visibly jolting in its frame. CAMERA: short fast push toward the glass, jolted by the impact, 35mm. LIGHT: Carriage 5 in red emergency light: the narrow continuous red strip along the centre of the ceiling is the dominant source (#B3001B), deep and dark, not pink or magenta; faces half in shadow, real black zones, no white fill. Side windows black with rain on the outside of the glass. Behind the silhouettes only the dark red-lit gangway: no sky, no rain. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Siluetas en rojo contra la ventanita (Estado bloque 4) ✓ · sin cielo ni lluvia ✓ · manchas oscuras, sin palabras prohibidas ✓

### b4_p5 · bloque 4 P5 · llamada c04b · 0:36.5 (2.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_hugo` — https://v3b.fal.media/files/b/0aaca77b/Y0NtlR1O9i2eW4avjrp79_HOJA_hugo.png
  2. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  3. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  4. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  5. `HOJA_ivan` — https://v3b.fal.media/files/b/0aaca77b/jKxRb5IV8dbedLGy4_Kdq_HOJA_ivan.png
  6. `F10_rojo_pasajeros_hacia_puerta` — https://v3b.fal.media/files/b/0aaeee79/CcgvlprGujBKr1bN0wAuC_F10_rojo_pasajeros_hacia_puerta.png
  7. `PROP_llave_y_cerradura` — https://v3b.fal.media/files/b/0aaeee79/7TfwxCV9IVD0Q6DbwH8wL_PROP_llave_y_cerradura.png
  8. `ref_infectados` — https://v3b.fal.media/files/b/0aaeee57/acsDjue9s2V4HF70fQcO-_ref_infectados.jpg

```text
FILM STILL, vertical 9:16. Image 1 is Don Hugo: grey moustache, conductor cap with a plain wheel badge (no letters), conductor jacket below the hip, whistle on a cord. Identity and wardrobe only. Image 2 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 3 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 4 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 5 is Iván: shaved head, broken nose, canvas worker jacket. Identity and wardrobe only. Image 6 is carriage 5 geometry in red emergency light, looking toward the front door. Image 7 is the antique key and the worn bronze lock plate (keyhole above, handle below). Image 8 is infection look only (eyes, skin, veins); ignore faces, wardrobe and setting. MOMENT: reverse shot toward the REAR of carriage 5, in red. The rear door has just burst open and Don Hugo steps in: his RIGHT hand raises the antique key high, the whistle just dropped from his lips onto its cord, mouth wide shouting an order, his left arm beckoning toward himself. In the foreground, out of focus, passengers turn toward him in a wave: Iván first (already facing Hugo), Carmen turning, Martina and Tomás lower left still turning. Behind Hugo, through the open rear door, only the dark red gangway, empty: no infected on this side. CAMERA: the end of a fast whip pan from the front door to Hugo, a streak of motion blur at the frame's left edge, handheld, 28mm. LIGHT: Carriage 5 in red emergency light: the narrow continuous red strip along the centre of the ceiling is the dominant source (#B3001B), deep and dark, not pink or magenta; faces half in shadow, real black zones, no white fill. Side windows black with rain on the outside of the glass. Hugo is rimmed red from the ceiling strip. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Contraplano al fondo ✓ · llave en alto en mano DERECHA ✓ · silbato antes de la voz ✓ · ola de cabezas ✓ · infectados solo por delante, nunca por la puerta de Hugo ✓ · FALTA plancha F11 (contraplano hacia atrás) en fal ⚠

### b4_p6 · bloque 4 P6 · llamada c04b · 0:39 (2.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  3. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  4. `HOJA_ivan` — https://v3b.fal.media/files/b/0aaca77b/jKxRb5IV8dbedLGy4_Kdq_HOJA_ivan.png
  5. `F10_rojo_pasajeros_hacia_puerta` — https://v3b.fal.media/files/b/0aaeee79/CcgvlprGujBKr1bN0wAuC_F10_rojo_pasajeros_hacia_puerta.png
  6. `ref_infectados` — https://v3b.fal.media/files/b/0aaeee57/acsDjue9s2V4HF70fQcO-_ref_infectados.jpg

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 3 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 4 is Iván: shaved head, broken nose, canvas worker jacket. Identity and wardrobe only. Image 5 is carriage 5 geometry in red emergency light, looking toward the front door. Image 6 is infection look only (eyes, skin, veins); ignore faces, wardrobe and setting. MOMENT: the stampede, camera inside it, facing the front of carriage 5 as the group runs toward camera (toward Hugo, behind camera). Close at frame RIGHT, Tomás drags Martina by the hand (his RIGHT hand gripping her LEFT hand); Martina at frame LEFT, just behind him, glances back over her shoulder for an instant. Mid-ground, Iván and Carmen bump against seatbacks as they run. At the far end, the front door bursts open and the first infected silhouettes pour in. CAMERA: handheld, running backward with them between the seats, bumped by a shoulder, motion blur, 24mm. LIGHT: Carriage 5 in red emergency light: the narrow continuous red strip along the centre of the ceiling is the dominant source (#B3001B), deep and dark, not pink or magenta; faces half in shadow, real black zones, no white fill. Side windows black with rain on the outside of the glass. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Corre con ellos ✓ · Tomás arrastra a Martina de la mano, manos naturales ✓ · ella mira atrás ✓ · choques con respaldos (peso) ✓ · infectados entran por la puerta delantera, lejos de Hugo ✓

### b5_p1 · bloque 5 P1 · llamada c05a · 0:41.5 (1.3 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_hugo` — https://v3b.fal.media/files/b/0aaca77b/Y0NtlR1O9i2eW4avjrp79_HOJA_hugo.png
  2. `PROP_llave_y_cerradura` — https://v3b.fal.media/files/b/0aaeee79/7TfwxCV9IVD0Q6DbwH8wL_PROP_llave_y_cerradura.png
  3. `F04_rojo_puerta_desde_fuelle` — https://v3b.fal.media/files/b/0aaca77b/c73vbo2QXGczuqRsrS3Yx_F04_rojo_puerta_desde_fuelle.png
  4. `F12_rojo_detalle_llave_0-23` — https://v3b.fal.media/files/b/0aaeee79/XGpg_1idNsx_qO94-6B2i_F12_rojo_detalle_llave_0-23.png

```text
FILM STILL, vertical 9:16. Image 1 is Don Hugo: grey moustache, conductor cap with a plain wheel badge (no letters), conductor jacket below the hip, whistle on a cord. Identity and wardrobe only. Image 2 is the antique key and the worn bronze lock plate (keyhole above, handle below). Image 3 is the last carriage's door seen from the gangway, red light. Image 4 is close detail of the key in the lock, red light (lens and texture reference). MOMENT: close shot of the lock on the last carriage's door from the gangway side: the worn bronze plate on the right side of the door, keyhole above, handle below. Hugo's two hands force the antique key, jammed half-turned in the keyhole; knuckles white, fingers clearly separate from the key, the cuffs of his conductor jacket. CAMERA: handheld, close, 75mm, f/2.8, focus on the key. LIGHT: Gangway vestibule lit only by red emergency light (#B3001B), dark corners falling to black, no side windows; the gangway's side door is closed. A thin cold highlight on the brass. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Cerradura a la der. desde fuera, bocallave arriba ✓ · llave trabada, dos manos ✓ · dedos separados de la llave (falla de a05 v1) ✓

### b5_p2 · bloque 5 P2 · llamada c05a · 0:42.8 (1.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_ivan` — https://v3b.fal.media/files/b/0aaca77b/jKxRb5IV8dbedLGy4_Kdq_HOJA_ivan.png
  2. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  3. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  4. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  5. `F07_rojo_fuelle_vestibulo` — https://v3b.fal.media/files/b/0aaeee79/pQXCNTot3k6RNoQ7y4qXm_F07_rojo_fuelle_vestibulo.png
  6. `ref_infectados` — https://v3b.fal.media/files/b/0aaeee57/acsDjue9s2V4HF70fQcO-_ref_infectados.jpg

```text
FILM STILL, vertical 9:16. Image 1 is Iván: shaved head, broken nose, canvas worker jacket. Identity and wardrobe only. Image 2 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 3 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 4 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 5 is the gangway vestibule in red emergency light. Image 6 is infection look only (eyes, skin, veins); ignore faces, wardrobe and setting. MOMENT: medium shot from beside the last carriage's door looking back across the gangway toward the carriage 5 door. Iván, last out, has just slammed the carriage 5 door shut behind the group with his left hand flat on it; his right arm shoves Tomás and Martina forward past camera toward Hugo (off frame behind camera). Through the carriage 5 door's window, infected figures run toward it, close. Carmen is last, nearest the carriage 5 door, her back to it, bag on her left shoulder. CAMERA: handheld, 28mm, chest height. LIGHT: Gangway vestibule lit only by red emergency light (#B3001B), dark corners falling to black, no side windows; the gangway's side door is closed. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Infectados solo tras la puerta del vagón 5, lejos de Hugo (nota de métricas) ✓ · Iván cierra y empuja ✓ · Carmen de espaldas a la puerta ✓ · no hay ventanas laterales ✓ · FALTA plancha de la puerta del vagón 5 vista desde el fuelle (se usa F07) ⚠

### b5_p3 · bloque 5 P3 · llamada c05a · 0:44.3 (1.0 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  2. `ref_infectados` — https://v3b.fal.media/files/b/0aaeee57/acsDjue9s2V4HF70fQcO-_ref_infectados.jpg
  3. `F07_rojo_fuelle_vestibulo` — https://v3b.fal.media/files/b/0aaeee79/pQXCNTot3k6RNoQ7y4qXm_F07_rojo_fuelle_vestibulo.png

```text
FILM STILL, vertical 9:16. Image 1 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 2 is infection look only (eyes, skin, veins); ignore faces, wardrobe and setting. Image 3 is the gangway vestibule in red emergency light. MOMENT: the carriage 5 door window bursts: an infected arm has smashed through the glass, shards in mid-air, its grey hand gripping the back of Carmen's brown coat at the shoulder and yanking her backward; Carmen's face in shock, mouth open, glasses swinging on the cord. CAMERA: handheld, violently shaken, 28mm. LIGHT: Gangway vestibule lit only by red emergency light (#B3001B), dark corners falling to black, no side windows; the gangway's side door is closed. Through the broken window, only the dark red interior of carriage 5 and the shapes of the infected. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Causa antes del efecto: vidrio roto antes de la herida ✓ · brazo agarra el abrigo ✓ · sin cielo ✓

### b5_p4 · bloque 5 P4 · llamada c05b · 0:45.3 (1.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** espera ESTADO_carmen_palma
- **Referencias (en este orden):**
  1. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  2. `HOJA_ivan` — https://v3b.fal.media/files/b/0aaca77b/jKxRb5IV8dbedLGy4_Kdq_HOJA_ivan.png
  3. `ESTADO_carmen_palma` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §5)
  4. `ref_infectados` — https://v3b.fal.media/files/b/0aaeee57/acsDjue9s2V4HF70fQcO-_ref_infectados.jpg
  5. `F07_rojo_fuelle_vestibulo` — https://v3b.fal.media/files/b/0aaeee79/pQXCNTot3k6RNoQ7y4qXm_F07_rojo_fuelle_vestibulo.png

```text
FILM STILL, vertical 9:16. Image 1 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 2 is Iván: shaved head, broken nose, canvas worker jacket. Identity and wardrobe only. Image 3 is the state of Carmen's RIGHT palm: one thin cut and a dark red-black smear. Image 4 is infection look only (eyes, skin, veins); ignore faces, wardrobe and setting. Image 5 is the gangway vestibule in red emergency light. MOMENT: medium shot. Carmen has crashed back against the broken carriage 5 door, facing camera; to stop her fall her RIGHT palm (at frame LEFT) presses flat on the jagged glass still stuck in the window frame. Iván, at frame RIGHT, grips her LEFT hand and wrenches her forward; the infected arm through the window is letting go of her coat. CAMERA: handheld, 32mm, chest height. LIGHT: Gangway vestibule lit only by red emergency light (#B3001B), dark corners falling to black, no side windows; the gangway's side door is closed. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Palma DERECHA en los vidrios ✓ · Iván la saca de la otra mano (izquierda) ✓ · brazo suelta el abrigo ✓ · lados del cuadro coherentes ✓

### b5_p5 · bloque 5 P5 · llamada c05i · 0:46.8 (1.0 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** espera ESTADO_carmen_palma (o usarlo directo como fotograma guía)
- **Referencias (en este orden):**
  1. `ESTADO_carmen_palma` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §5)
  2. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  3. `F07_rojo_fuelle_vestibulo` — https://v3b.fal.media/files/b/0aaeee79/pQXCNTot3k6RNoQ7y4qXm_F07_rojo_fuelle_vestibulo.png

```text
FILM STILL, vertical 9:16. Image 1 is the state of Carmen's RIGHT palm: one thin cut and a dark red-black smear. Image 2 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 3 is the gangway vestibule in red emergency light. MOMENT: insert of Carmen's RIGHT palm the instant it lifts off the broken glass in the door frame, palm turned toward camera, thumb at frame LEFT so it reads as a right hand: one thin, clean cut across the heel of the palm and a dark red-black smear that comes from the infected arm, thicker on the glass edge than on her skin; no exposed flesh. Brown coat sleeve and white uniform cuff at her wrist. CAMERA: locked off, close, 85mm, f/2.8. LIGHT: Gangway vestibule lit only by red emergency light (#B3001B), dark corners falling to black, no side windows; the gangway's side door is closed. A cold thin highlight along the glass edges. This frame is the guide frame for call c05i. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Palma DERECHA, pulgar a la izq. del cuadro ✓ · corte fino + mancha negra rojiza ✓ · sin carne expuesta ✓ · sin palabras prohibidas ✓

### b5_p6 · bloque 5 P6 · llamada c05b · 0:47.8 (1.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_hugo` — https://v3b.fal.media/files/b/0aaca77b/Y0NtlR1O9i2eW4avjrp79_HOJA_hugo.png
  2. `PROP_llave_y_cerradura` — https://v3b.fal.media/files/b/0aaeee79/7TfwxCV9IVD0Q6DbwH8wL_PROP_llave_y_cerradura.png
  3. `F04_rojo_puerta_desde_fuelle` — https://v3b.fal.media/files/b/0aaca77b/c73vbo2QXGczuqRsrS3Yx_F04_rojo_puerta_desde_fuelle.png
  4. `previs/b5_p1.png` — (fotograma aprobado de b5_p1; generar antes)

```text
FILM STILL, vertical 9:16. Image 1 is Don Hugo: grey moustache, conductor cap with a plain wheel badge (no letters), conductor jacket below the hip, whistle on a cord. Identity and wardrobe only. Image 2 is the antique key and the worn bronze lock plate (keyhole above, handle below). Image 3 is the last carriage's door seen from the gangway, red light. Image 4 is composition, framing and light of shot b5_p1: keep the same camera position and framing. MOMENT: the same lock close-up as the composition reference (b5_p1). The key has turned fully; Hugo's RIGHT hand has pulled it out and is sliding it into the pocket of his conductor jacket, half in; his left shoulder presses the door, which is just opening a crack onto darkness. CAMERA: handheld, close, 75mm. LIGHT: Gangway vestibule lit only by red emergency light (#B3001B), dark corners falling to black, no side windows; the gangway's side door is closed. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Mismo encuadre que b5_p1 ✓ · la llave va al BOLSILLO de la chaqueta (Estado bloque 5) ✓ · hombro empuja la puerta ✓

### b5_p7 · bloque 5 P7 · llamada c05b · 0:49.3 (1.2 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  2. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  3. `HOJA_ivan` — https://v3b.fal.media/files/b/0aaca77b/jKxRb5IV8dbedLGy4_Kdq_HOJA_ivan.png
  4. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  5. `HOJA_hugo` — https://v3b.fal.media/files/b/0aaca77b/Y0NtlR1O9i2eW4avjrp79_HOJA_hugo.png
  6. `F01_rojo_ultimo_vagon_hacia_puerta` — https://v3b.fal.media/files/b/0aaca77b/cjnHyHuvZXot98Es7F2wd_F01_rojo_ultimo_vagon_hacia_puerta.png
  7. `F03_rojo_puerta_desde_dentro_0-45` — https://v3b.fal.media/files/b/0aaca77b/I6kNLxhGD5kjj6UWzbGV0_F03_rojo_puerta_desde_dentro_0-45.png

```text
FILM STILL, vertical 9:16. Image 1 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 2 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 3 is Iván: shaved head, broken nose, canvas worker jacket. Identity and wardrobe only. Image 4 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 5 is Don Hugo: grey moustache, conductor cap with a plain wheel badge (no letters), conductor jacket below the hip, whistle on a cord. Identity and wardrobe only. Image 6 is the last carriage looking toward its front door, red light with the cold tube above the door. Image 7 is the last carriage's door and its small wired-glass window seen from inside, red light. MOMENT: from inside the last carriage toward its front door. The group bursts through the open door in a tumble: Tomás first at frame LEFT dragging Martina by the hand, Martina at frame RIGHT stumbling; Iván behind shoving Carmen, whose RIGHT hand is clenched against her chest; Don Hugo holds the door open at the frame edge with his shoulder, empty-handed (the key is in his pocket). Through the open doorway only the dark red gangway. CAMERA: handheld, backing away as they come in, 24mm, chest height. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Desde el lado de la puerta: Martina der./Tomás izq. ✓ · entran en tropel ✓ · Hugo sin llave en la mano ✓ · Carmen protege la mano derecha ✓

### b5_p8 · bloque 5 P8 · llamada c06a · 0:50.5 (1.3 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_hugo` — https://v3b.fal.media/files/b/0aaca77b/Y0NtlR1O9i2eW4avjrp79_HOJA_hugo.png
  2. `ref_infectados` — https://v3b.fal.media/files/b/0aaeee57/acsDjue9s2V4HF70fQcO-_ref_infectados.jpg
  3. `F03_rojo_puerta_desde_dentro_0-45` — https://v3b.fal.media/files/b/0aaca77b/I6kNLxhGD5kjj6UWzbGV0_F03_rojo_puerta_desde_dentro_0-45.png

```text
FILM STILL, vertical 9:16. Image 1 is Don Hugo: grey moustache, conductor cap with a plain wheel badge (no letters), conductor jacket below the hip, whistle on a cord. Identity and wardrobe only. Image 2 is infection look only (eyes, skin, veins); ignore faces, wardrobe and setting. Image 3 is the last carriage's door and its small wired-glass window seen from inside, red light. MOMENT: close on the door from inside. Hugo has slammed the door with his body, shoulder and back against it; an infected grey hand with dark nails is jammed in the gap on the lock side (frame LEFT, where the bronze lock plate is from inside), being crushed by the door edge. Hugo's RIGHT hand is on the lock handle, about to lock it. CAMERA: handheld, close, 35mm. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Cerradura a la izq. desde dentro, bisagras a la der. ✓ · aplasta la mano con la puerta ✓ · sin llave en mano ✓ · «cerrojo»: ver informe ⚠

### b5_p9 · bloque 5 P9 · llamada c06a · 0:51.8 (1.0 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `F03_rojo_puerta_desde_dentro_0-45` — https://v3b.fal.media/files/b/0aaca77b/I6kNLxhGD5kjj6UWzbGV0_F03_rojo_puerta_desde_dentro_0-45.png
  2. `ref_infectados` — https://v3b.fal.media/files/b/0aaeee57/acsDjue9s2V4HF70fQcO-_ref_infectados.jpg

```text
FILM STILL, vertical 9:16. Image 1 is the last carriage's door and its small wired-glass window seen from inside, red light. Image 2 is infection look only (eyes, skin, veins); ignore faces, wardrobe and setting. MOMENT: the door's small wired-glass window from inside: an infected face has just slammed into the glass, pressed against the rhombic wire mesh, leaving dark red-black smears; the frame jolts with the impact. CAMERA: locked off, 35mm, the impact shakes the frame. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. Behind the face only the dark red gangway: no sky, no rain. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Fija, sacudida por el golpe ✓ · deja el vidrio manchado (continuidad bloques 6–7) ✓ · sin cielo ni lluvia ✓

### b6_p1 · bloque 6 P1 · llamada c06a · 0:52.8 (2.0 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  3. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  4. `HOJA_ivan` — https://v3b.fal.media/files/b/0aaca77b/jKxRb5IV8dbedLGy4_Kdq_HOJA_ivan.png
  5. `HOJA_hugo` — https://v3b.fal.media/files/b/0aaca77b/Y0NtlR1O9i2eW4avjrp79_HOJA_hugo.png
  6. `F01_rojo_ultimo_vagon_hacia_puerta` — https://v3b.fal.media/files/b/0aaca77b/cjnHyHuvZXot98Es7F2wd_F01_rojo_ultimo_vagon_hacia_puerta.png
  7. `ref_infectados` — https://v3b.fal.media/files/b/0aaeee57/acsDjue9s2V4HF70fQcO-_ref_infectados.jpg

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 3 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 4 is Iván: shaved head, broken nose, canvas worker jacket. Identity and wardrobe only. Image 5 is Don Hugo: grey moustache, conductor cap with a plain wheel badge (no letters), conductor jacket below the hip, whistle on a cord. Identity and wardrobe only. Image 6 is the last carriage looking toward its front door, red light with the cold tube above the door. Image 7 is infection look only (eyes, skin, veins); ignore faces, wardrobe and setting. MOMENT: wide shot from the back of the last carriage toward the door. The small window is full of palms and dark smears; Iván stands with his back pressed against the door, arms braced; Hugo beside the door on the lock side, empty-handed. Mid-ground, the group backs toward camera, faces to the door: Martina to the LEFT of Tomás, Carmen beside them clutching her right hand to her chest. CAMERA: locked off at standing chest height, 24mm, f/4. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Fija ✓ · desde atrás: Martina a la izq. de Tomás ✓ · Iván de espaldas a la puerta ✓ · ventanita con manos y manchas ✓ · Hugo sin llave ✓

### b6_p2 · bloque 6 P2 · llamada c06b · 0:54.8 (1.5 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** espera ESTADO_carmen_palma
- **Referencias (en este orden):**
  1. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  2. `ESTADO_carmen_palma` — sin URL — ⚠ PENDIENTE fase 3 (prompt del productor, assets_v10 §5)
  3. `F05_rojo_tres_cuartos_hacia_puerta` — https://v3b.fal.media/files/b/0aaeee79/y37VCdVQneuEQHi7tmsc1_F05_rojo_tres_cuartos_hacia_puerta.png

```text
FILM STILL, vertical 9:16. Image 1 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 2 is the state of Carmen's RIGHT palm: one thin cut and a dark red-black smear. Image 3 is the last carriage at three-quarters toward the door, red light. MOMENT: close-up of Carmen, chest up. She has just looked at her open RIGHT palm (the thin cut and dark red-black smear visible, thumb at frame left); her fingers start to curl into a fist and move toward the opening of her brown coat, while her eyes have already lifted off the palm and glance sideways toward frame left, checking whether the others saw. CAMERA: locked off, 50mm, f/2. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. Glasses on the cord, bag on her left shoulder. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Palma DERECHA cortada (igual que b5_p5) ✓ · empieza a esconderla ✓ · mirada con destino (los demás) ✓

### b6_p3 · bloque 6 P3 · llamada c06b · 0:56.3 (2.0 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  2. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  3. `F05_rojo_tres_cuartos_hacia_puerta` — https://v3b.fal.media/files/b/0aaeee79/y37VCdVQneuEQHi7tmsc1_F05_rojo_tres_cuartos_hacia_puerta.png
  4. `F01_rojo_ultimo_vagon_hacia_puerta` — https://v3b.fal.media/files/b/0aaca77b/cjnHyHuvZXot98Es7F2wd_F01_rojo_ultimo_vagon_hacia_puerta.png

```text
FILM STILL, vertical 9:16. Image 1 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 2 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 3 is the last carriage at three-quarters toward the door, red light. Image 4 is the last carriage looking toward its front door, red light with the cold tube above the door. MOMENT: two-shot from the door side, facing them. Tomás at frame LEFT, head turned toward frame RIGHT, looking at Martina; Martina at frame RIGHT, eyes down at the floor, jaw set, not answering his look. Behind them the dark carriage in red, the seats facing camera. CAMERA: locked off at standing eye height, 50mm, f/2.8. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. The cold tube above the door (above camera) gives a cold top light on their hair and brows. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Lado de la puerta: Tomás izq. mira a la der., Martina der. mira el piso ✓ · ejes de mirada ✓

### b7_p1 · bloque 7 P1 · llamada c07a · 0:58.3 (0.8 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  3. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  4. `HOJA_ivan` — https://v3b.fal.media/files/b/0aaca77b/jKxRb5IV8dbedLGy4_Kdq_HOJA_ivan.png
  5. `HOJA_hugo` — https://v3b.fal.media/files/b/0aaca77b/Y0NtlR1O9i2eW4avjrp79_HOJA_hugo.png
  6. `F05_rojo_tres_cuartos_hacia_puerta` — https://v3b.fal.media/files/b/0aaeee79/y37VCdVQneuEQHi7tmsc1_F05_rojo_tres_cuartos_hacia_puerta.png
  7. `F03_rojo_puerta_desde_dentro_0-45` — https://v3b.fal.media/files/b/0aaca77b/I6kNLxhGD5kjj6UWzbGV0_F03_rojo_puerta_desde_dentro_0-45.png

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 3 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 4 is Iván: shaved head, broken nose, canvas worker jacket. Identity and wardrobe only. Image 5 is Don Hugo: grey moustache, conductor cap with a plain wheel badge (no letters), conductor jacket below the hip, whistle on a cord. Identity and wardrobe only. Image 6 is the last carriage at three-quarters toward the door, red light. Image 7 is the last carriage's door and its small wired-glass window seen from inside, red light. MOMENT: medium shot of the group from behind, backs to camera, facing the door: Martina to the LEFT of Tomás, Carmen beside them, Iván next to the door, Hugo at the door with his RIGHT hand resting on the lock handle (no key in hand). All heads have just snapped up toward the door at a knock. Carmen keeps her right hand closed and hidden inside her brown coat. The small window: the same dark smears on the wired glass, behind it the dark red gangway, empty, no face yet. The door is closed. CAMERA: handheld, slight, 35mm, shoulder height. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Desde atrás: Martina a la IZQ. de Tomás ✓ · mano de Carmen dentro del abrigo ✓ · Hugo mano en la cerradura, sin llave ✓ · manchas en el vidrio ✓ · sin cielo ni lluvia, puerta lateral cerrada ✓

### b7_p2 · bloque 7 P2 · llamada c07a · 0:59.1 (3.6 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `ESTADO_diego_mojado_herido_v3` — https://v3b.fal.media/files/b/0aaeeeed/F5MBlqPWd-MGyoUFRsOQv_estado_diego_mojado_herido_v3_t2_flare_0.png
  2. `HOJA_diego` — https://v3b.fal.media/files/b/0aaca77b/pWC2LbPmSFhdVQl7vDgPe_HOJA_diego.png
  3. `F03_rojo_puerta_desde_dentro_0-45` — https://v3b.fal.media/files/b/0aaca77b/I6kNLxhGD5kjj6UWzbGV0_F03_rojo_puerta_desde_dentro_0-45.png
  4. `F07_rojo_fuelle_vestibulo` — https://v3b.fal.media/files/b/0aaeee79/pQXCNTot3k6RNoQ7y4qXm_F07_rojo_fuelle_vestibulo.png

```text
FILM STILL, vertical 9:16. Image 1 is Diego in his current state: soaked pale stone canvas jacket darkened at the shoulders, RIGHT sleeve torn and stained dark red-black, no visible wound. Identity, wardrobe and state only; ignore the grey backdrop. Image 2 is Diego's face and three-day beard (backup identity only; the state comes from the previous image). Image 3 is the last carriage's door and its small wired-glass window seen from inside, red light. Image 4 is the gangway vestibule in red emergency light. MOMENT: the door's small wired-glass window from inside, filling the middle of the frame. Diego's face is right up against the stained glass, mouth open mid-shout of a name, pleading, voice breaking, eyes searching toward frame LEFT where Martina stands inside. Diego: wet hair plastered to his forehead, three-day beard, pale stone canvas jacket soaked and darkened at the shoulders, RIGHT sleeve torn and stained dark red-black, the right forearm held against his chest, no wound and no skin of the injury visible. He is wet because he crossed outside the train earlier; there is no rain in frame. The dark smears from before remain on the glass. Behind him only the dark gangway in red light; at its far end the carriage 5 door with its broken window, and dark shadows moving behind that broken glass. No sky, no rain, no open door; the gangway side door is closed. CAMERA: slow push toward the glass, handheld, 35mm, f/2.8, focus on his eyes. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. His wet skin catches the cold tube from above the door. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Diego mojado, manga DERECHA oscura (a la izq. del cuadro), sin herida ✓ · manchas del vidrio ✓ · detrás solo fuelle rojo + puerta del vagón 5 rota con sombras ✓ · sin cielo, sin lluvia, sin puerta abierta ✓ · mira hacia Martina ✓

### b7_p3 · bloque 7 P3 · llamada c07a · 1:02.7 (2.9 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  3. `HOJA_carmen` — https://v3b.fal.media/files/b/0aaca77b/h4Q1Ei5g6JWNhFmrLCnu__HOJA_carmen.png
  4. `HOJA_ivan` — https://v3b.fal.media/files/b/0aaca77b/jKxRb5IV8dbedLGy4_Kdq_HOJA_ivan.png
  5. `F05_rojo_tres_cuartos_hacia_puerta` — https://v3b.fal.media/files/b/0aaeee79/y37VCdVQneuEQHi7tmsc1_F05_rojo_tres_cuartos_hacia_puerta.png
  6. `F01_rojo_ultimo_vagon_hacia_puerta` — https://v3b.fal.media/files/b/0aaca77b/cjnHyHuvZXot98Es7F2wd_F01_rojo_ultimo_vagon_hacia_puerta.png

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 3 is Carmen: face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord. Identity and wardrobe only. Image 4 is Iván: shaved head, broken nose, canvas worker jacket. Identity and wardrobe only. Image 5 is the last carriage at three-quarters toward the door, red light. Image 6 is the last carriage looking toward its front door, red light with the cold tube above the door. MOMENT: close-up of Martina from the door side: she is in the foreground at frame RIGHT, sharp, chest up, motionless, eyes fixed on the door window next to the camera, breath held. Behind her, out of focus, the heads turn toward her one by one: Tomás at frame left already turned and looking at her (toward frame right), Carmen beside him mid-turn. At the LEFT edge of frame, in the foreground near the door and camera, Iván's head and shoulder, out of focus, turning toward her. Carmen keeps her right hand closed and hidden inside her brown coat. CAMERA: handheld, slight, 50mm, f/2, focus on Martina. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. Cold top light from the tube above the door on her face. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Lado de la puerta: Martina der. enfocada ✓ · ola solo Tomás → Carmen detrás ✓ · Iván en primer término, borde izq., desenfocado ✓ · mano de Carmen dentro del abrigo ✓

### b7_p4 · bloque 7 P4 · llamada c07b · 1:05.6 (2.7 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_tomas` — https://v3b.fal.media/files/b/0aaca77b/QIGG8k0Xlw4BBGntsymsW_HOJA_tomas.png
  2. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  3. `F05_rojo_tres_cuartos_hacia_puerta` — https://v3b.fal.media/files/b/0aaeee79/y37VCdVQneuEQHi7tmsc1_F05_rojo_tres_cuartos_hacia_puerta.png

```text
FILM STILL, vertical 9:16. Image 1 is Tomás: face, thin full metal-frame glasses, navy quilted jacket. Identity and wardrobe only; ignore layout and background. Image 2 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 3 is the last carriage at three-quarters toward the door, red light. MOMENT: close-up of Tomás from the door side, chest up, at frame LEFT, looking toward frame RIGHT at Martina (her shoulder soft at the right edge). Confused, slowly realizing: brow knitting, lips just forming the first word of a low, cold question. CAMERA: handheld, still, 50mm, f/2, focus on his eyes behind the glasses. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. The cold tube light glints on his metal frames. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Lado de la puerta: Tomás izq. mira a la der. (corrige a07b v1) ✓ · entrega 7B ✓

### b7_p5 · bloque 7 P5 · llamada c07b · 1:08.3 (1.2 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `ESTADO_diego_mojado_herido_v3` — https://v3b.fal.media/files/b/0aaeeeed/F5MBlqPWd-MGyoUFRsOQv_estado_diego_mojado_herido_v3_t2_flare_0.png
  2. `HOJA_diego` — https://v3b.fal.media/files/b/0aaca77b/pWC2LbPmSFhdVQl7vDgPe_HOJA_diego.png
  3. `F03_rojo_puerta_desde_dentro_0-45` — https://v3b.fal.media/files/b/0aaca77b/I6kNLxhGD5kjj6UWzbGV0_F03_rojo_puerta_desde_dentro_0-45.png
  4. `F07_rojo_fuelle_vestibulo` — https://v3b.fal.media/files/b/0aaeee79/pQXCNTot3k6RNoQ7y4qXm_F07_rojo_fuelle_vestibulo.png
  5. `previs/b7_p2.png` — (fotograma aprobado de b7_p2; generar antes)

```text
FILM STILL, vertical 9:16. Image 1 is Diego in his current state: soaked pale stone canvas jacket darkened at the shoulders, RIGHT sleeve torn and stained dark red-black, no visible wound. Identity, wardrobe and state only; ignore the grey backdrop. Image 2 is Diego's face and three-day beard (backup identity only; the state comes from the previous image). Image 3 is the last carriage's door and its small wired-glass window seen from inside, red light. Image 4 is the gangway vestibule in red emergency light. Image 5 is composition, framing and light of shot b7_p2: keep the same camera position and framing. MOMENT: the same window framing as the composition reference (b7_p2). Diego slaps the glass with his LEFT palm (flat on the glass at frame RIGHT) while turning his head over his shoulder to look behind him. Diego: wet hair plastered to his forehead, three-day beard, pale stone canvas jacket soaked and darkened at the shoulders, RIGHT sleeve torn and stained dark red-black, the right forearm held against his chest, no wound and no skin of the injury visible. He is wet because he crossed outside the train earlier; there is no rain in frame. Behind him only the dark gangway in red light; at its far end the carriage 5 door with its broken window, and dark shadows moving behind that broken glass. No sky, no rain, no open door; the gangway side door is closed. The shadows behind the broken carriage 5 door window are closer and larger now. CAMERA: handheld, 35mm. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Golpea con la palma IZQUIERDA ✓ · brazo derecho al pecho, manga oscura ✓ · sombras más cerca, detrás del vidrio roto del vagón 5 ✓ · sin cielo, sin lluvia, puerta lateral cerrada ✓

### b7_p6 · bloque 7 P6 · llamada c07b · 1:09.5 (2.6 s)

- **Modelo:** `openai/gpt-image-2.5/flare/edit` · `image_size: portrait_16_9` (9:16) · `quality: high` · **Estado:** lista
- **Referencias (en este orden):**
  1. `HOJA_martina` — https://v3b.fal.media/files/b/0aaca77b/gxJvG_NylXQWPnPye25qY_HOJA_martina.png
  2. `HOJA_hugo` — https://v3b.fal.media/files/b/0aaca77b/Y0NtlR1O9i2eW4avjrp79_HOJA_hugo.png
  3. `F05_rojo_tres_cuartos_hacia_puerta` — https://v3b.fal.media/files/b/0aaeee79/y37VCdVQneuEQHi7tmsc1_F05_rojo_tres_cuartos_hacia_puerta.png
  4. `F03_rojo_puerta_desde_dentro_0-45` — https://v3b.fal.media/files/b/0aaca77b/I6kNLxhGD5kjj6UWzbGV0_F03_rojo_puerta_desde_dentro_0-45.png

```text
FILM STILL, vertical 9:16. Image 1 is Martina: face, hair, oat knit sweater, open charcoal wool coat, dark jeans, brown boots. Identity and wardrobe only; ignore the sheet layout and background. Image 2 is Don Hugo: grey moustache, conductor cap with a plain wheel badge (no letters), conductor jacket below the hip, whistle on a cord. Identity and wardrobe only. Image 3 is the last carriage at three-quarters toward the door, red light. Image 4 is the last carriage's door and its small wired-glass window seen from inside, red light. MOMENT: final close-up of Martina from the door side, right of centre, sharp. Her eyes have just moved from Tomás (off frame left) to the door right next to the camera, looking almost into the lens at its right; she does not answer, lips slightly parted, breath held. In the extreme foreground at the bottom-RIGHT corner, out of focus, Don Hugo's RIGHT hand rests on the door's bronze lock handle, waiting; the hand is empty, no key (it stays in his jacket pocket). The group soft in the background. CAMERA: locked off, 50mm, f/2, focus on her eyes. LIGHT: Last carriage in red emergency light: the narrow red ceiling strip is dominant; the single cold white fluorescent tube (#E8F1F2) above the front door is the only white light and only catches heads and shoulders from above near the door; deep black zones; side windows black with rain only on the outside of the glass. Cold top light from the tube above the door on her face. Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, real skin texture with pores, no HDR, no glow halos, no orange-teal rim light, not everything in focus, natural hands with five separate fingers. No text, no captions, no watermark.
```
- **Revisión (§5 + Estado del mundo + pauta de look):** Mirada llega a la puerta junto a la cámara ✓ · mano DERECHA de Hugo en la cerradura, SIN llave ✓ · cerradura a la der. del cuadro desde este eje ✓ · fija ✓
