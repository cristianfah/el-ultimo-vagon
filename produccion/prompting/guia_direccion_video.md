# Guía de dirección para prompts de video

Para el bot productor, el Prompter y cualquier agente que escriba un prompt de video de EL ÚLTIMO VAGÓN. Complementa (no reemplaza) la skill `.cursor/skills/director-de-prompts/`, el sistema de actuación (`produccion/actuacion.md`) y el método (`produccion/metodo.md`). Escrita el 18-oct-2026.

## 1. La idea

Un prompt de video es una orden de rodaje para un actor, un director de fotografía y un sonidista a la vez. El modelo rellena con un promedio todo lo que no está escrito, y el promedio es lo que se ve como «IA»: caras quietas, cámara que flota, gente que no mira a nadie. **Simple no es corto:** cada plano tiene una intención, y el prompt fija todo lo que el modelo no debe inventar.

## 2. Escribir una vez, compilar dos

Cada bloque del guion se convierte primero en una **ficha de dirección** (sección 4). La ficha se compila en dos formatos:
- **H3 Max (Ref2VA)** para el animatic. Formato en `.cursor/skills/director-de-prompts/references/h3.md`.
- **Kling 4.0** para la versión final. Formato en la sección 7 de esta guía.

El contenido es el mismo; solo cambia la sintaxis. Si el animatic funciona, la versión final parte del mismo texto. Si el animatic falla, se corrige la ficha, no el prompt suelto.

## 3. Las emociones se escriben como conducta

Nunca se escribe la emoción («scared», «guilty look», «angry»): el modelo la sobreactúa o pone una cara de catálogo. Se escribe **lo que el cuerpo hace** porque siente eso. Esta tabla traduce los estados de la serie:

| Lo que siente | Lo que se escribe (conducta visible) |
| --- | --- |
| Miedo contenido | Breathes short through the nose; shoulders slightly raised; her eyes return to the door every two seconds; her hands look for something to grip |
| Culpa | Avoids the other person's eyes; answers a beat too fast; tugs her sleeve or touches her neck; a smile that arrives late and leaves early |
| Mentira | The answer comes before the question has finished; holds the gaze one second too long, or never meets it; the hand stays still on purpose |
| Sospecha | Looks one second longer than normal; head still while the eyes move; stops what he was doing |
| Celos fríos | Voice drops; the body goes still; does not blink while listening; the jaw tightens and releases |
| Desesperación | Knocks in an irregular rhythm; the voice breaks at the end of the line; the eyes search left and right without landing |
| Shock | The body freezes in the middle of a gesture; lips part without sound; one second of delay before any reaction |
| Pánico | Big, mistimed movements; pushes past people; looks back while running |
| Alivio | The shoulders drop; one long exhale; the eyes close for an instant |
| Decisión | Stops moving; the hand closes on the object; the gaze goes to the target and does not come back |
| Ternura que no se dice | Takes the other's hand without looking at them; the thumb moves once over the knuckles |

Y en cada personaje en cuadro, los cinco pilares de `produccion/actuacion.md`: **objetivo** (un verbo dirigido a otra persona), **obstáculo**, **táctica**, **beats con segundo** y **subtexto** que se escapa. El objetivo y el obstáculo no se escriben en el prompt como frases: se convierten en conducta.

## 4. La ficha de dirección (una por bloque)

Antes de escribir el prompt, se llena esta ficha desde el guion. Si un campo no se puede llenar con lo que dice el guion, se pregunta; no se inventa.

```
Bloque: [número y nombre] · [duración] · [set y luz]
Referencias (en orden): [hojas] · [estados] · [plancha] · [props] · [voces] · [video anterior] · [fotograma guía]
Mapa: dónde está la cámara, qué hay en primer término, al medio y al fondo; qué se ve por cada vidrio y si se mueve.
Continuidad: vestuario, pelo, manchas, heridas (con lado), props y en qué mano, luz.
Por plano:
  - Tiempo, tamaño de plano y dónde corta el cuadro.
  - Cámara: tipo + amplitud + velocidad + motivo.
  - Bloqueo: quién está dónde, a qué distancia, mirando a qué.
  - Actuación: beats con segundo, como estados; miradas con destino; manos con lado; tarea física.
  - Diálogo: línea exacta, quién la dice, entrega física.
  - Sonido del momento.
```

## 5. Movimiento que no se ve generado

- **El tren se mueve:** todos se balancean apenas con el traqueteo; por las ventanas laterales pasa la noche; lo que se ve por la ventanita de la puerta (el fuelle) está quieto respecto de la cámara.
- **Peso e inercia:** al levantarse empujan con las manos en el asiento; al correr chocan con los respaldos; al frenar el cuerpo sigue un poco hacia adelante.
- **La tela responde:** el abrigo abierto de Martina se mueve al girar; la ropa mojada de Diego pesa y se pega; el pelo mojado no flota.
- **Manos siempre ocupadas** con una tarea física. El golpe dramático es cuando la tarea se detiene.
- **Microgestos en primeros planos:** parpadeo, respiración, tragar saliva, un músculo de la mandíbula. Un primer plano sin ellos es un maniquí.
- **Un gesto a la vez,** escrito como estado: «at 2.0s her hand is already on her lap, still», no «she moves her hand down to her lap and then…».
- **Reacciones en ola:** en un grupo, uno reacciona primero, otro medio segundo después, otro no reacciona.

## 6. La cámara

- **Vocabulario:** static (locked off), handheld (shakes slightly / strongly), push in, pull out, pan, tilt, truck, track, arc. Siempre con **amplitud** (small / large) y **velocidad** (slow / fast), en una frase propia, separada de la acción del actor.
- **Sin push-in por defecto.** Cada escena tiene su gramática en la ficha del guion. En el capítulo 1, el único movimiento de cámara es el avance hacia la ventanita cuando aparece Diego.
- **Cámara en mano con intención:** «the camera shakes slightly, as if held by a passenger, and arrives late to the scream».
- **Escribir dónde está la cámara:** altura (seated eye height, floor level), distancia y lente (50mm, 35mm).
- **Tamaño de plano con corte:** «close-up framed from mid-chest up, hands out of frame». Si no se dice, el modelo abre el plano.

## 7. Formato Kling 4.0 (versión final)

Kling acepta hasta 8.000 tokens y clips de 3 a 30 s. Plantilla del proyecto:

```text
REFERENCES
@Image1 is [Character]: identity, face, hair and wardrobe only — [anchors]. Ignore the sheet layout and background.
@Image2 is [...].
@ImageN is [location] with its light: match layout, seats, lamps and windows exactly.
@Audio1 is [Character]'s voice for every line [Character] says.   (only in the final, with ElevenLabs)

LOOK
Live-action, cinematic, 9:16 vertical. [Lens, light sources with color temperature, film look in two sentences.] [Train motion.] Held for the whole clip: [continuity list].

SHOTS
Shot 1 (0.0–X.Xs) — [framing and where the frame cuts]. Camera: [type, amplitude, speed], [motive]. [Blocking]. [Acting beats with seconds, as states; gaze targets; hands with side]. [Character] says in Spanish with a soft Chilean accent, [physical delivery]: "[exact line]".
Shot 2 (X.X–Y.Ys) — The camera cuts to [...].

SOUND
[Continuous ambience]. [Effects with their second]. Dialogue only as sound.

No music. No subtitles, no captions, no on-screen text.
```

Si la interfaz tiene campo negativo: `push-in, zoom, dolly, warped hands, extra fingers, morphing faces, text, subtitles, captions, logos, music`.

## 8. Ejemplo completo: bloque 2 del capítulo 1 («El regreso», 14 s)

Ficha en `guion/cap01/cap01_v9.md`. Referencias: `HOJA_martina`, `HOJA_tomas`, `F09_ambar_asiento_pareja`.

### 8.1 Versión final · Kling 4.0

```text
REFERENCES
@Image1 is Martina, 29: identity, face, hair and wardrobe only — narrow face, a small mole on her LEFT cheekbone, shoulder-length dark brown wavy hair tucked behind her right ear, an oversized oatmeal chunky wool sweater with the sleeves pulled over her hands, a long charcoal wool coat worn open, faded dark jeans. Ignore the sheet layout and the grey backdrop.
@Image2 is Tomás, 31: identity, face, hair and wardrobe only — thin wire-rimmed glasses, short neat dark brown hair with a side part, clean-shaven, a fitted navy quilted jacket over a charcoal merino sweater, an average, slightly soft build. Ignore the sheet layout and the grey backdrop.
@Image3 is the passenger carriage at night: match the blue seats, the window with its curtain, the luggage rack and the reading lamp exactly. Martina sits by the window, frame left; Tomás sits on the aisle side, frame right.

LOOK
Live-action, cinematic, 9:16 vertical, 50mm lens at T2, shallow depth of field. Only practical light: the warm 2400K reading lamp under the luggage rack lights their faces from above and in front; the window beside Martina is deep night blue with rain streaks on the outside of the glass; further back, a few other passengers doze out of focus under dim amber pools and do not react. The whole carriage sways gently and continuously with the rhythm of the rails, and their bodies sway with it. Held for the whole clip: the same seats, the same lamp and light, the same wardrobe; Martina's coat stays open; Tomás's glasses stay on.

SHOTS
Shot 1 (0.0–4.0s) — Two-shot from the seat facing them, at seated eye height, framed from the top of their heads to their laps. Camera: static, locked off, because the couple is trapped in the frame together. At 0.0s Martina is already lowering herself into the window seat, slightly out of breath, and settles with her hands hidden inside her sleeves on her lap. Tomás, already seated, turns toward her as she lands; his eyes reach her before his head does. Tomás says in Spanish with a soft Chilean accent, softly, without reproach: "¿Dónde estabas?" Martina answers before he has finished the last word, too fast, looking at the back of the seat in front of her, not at him: "En el baño." Her eyes stay off him.
Shot 2 (4.0–5.5s) — The camera cuts to an insert on Martina's lap, framed from her knee to the cuff of her sweater. Camera: static. Her left hand pulls the oatmeal sleeve down over a thin red mark around her right wrist and holds it there. Once the mark is covered, her fingers stay still.
Shot 3 (5.5–9.0s) — The camera cuts to a close-up of Tomás, three-quarter profile from Martina's side, framed from mid-chest up. Camera: static. He looks at her face one second longer than normal; his jaw tightens and releases; he decides not to push. A small smile arrives late. Tomás says in Spanish with a soft Chilean accent, half joking, lightly: "¿Tu papá sabe que vienes en este tren?" His eyes stay on her for the answer.
Shot 4 (9.0–14.0s) — The camera cuts to a close-up of Martina, three-quarter profile from Tomás's side, framed from mid-chest up, the night window soft behind her. Camera: handheld, shakes very slightly with the train, no push-in. From 9.0s her eyes are fixed ahead, down the aisle toward the front of the train. Martina says in Spanish with a soft Chilean accent, quietly: "No." She holds a breath. At 11.0s, almost to herself, barely moving her lips: "Esa era la idea." At 12.0s Tomás's hand enters from the bottom edge of the frame and takes her left hand; she lets him, without looking at him. Her eyes stay ahead and blink twice, quickly. She holds still until the end.

SOUND
Continuous rail rhythm and a soft carriage rattle; rain ticking on the window; at 10.0s a distant cough from the front of the carriage. Dialogue only as sound, voices dry and close.

No music. No subtitles, no captions, no on-screen text.
```

**Qué fija y qué vigilar:** la mentira de Martina vive en el tiempo (responde antes de que él termine) y en la mirada (nunca lo mira). Vigilar que Tomás no hable en el plano 4, que la marca de la muñeca esté en la derecha y que el balanceo del tren no se convierta en un movimiento de cámara.

### 8.2 Animatic · H3 Max (Ref2VA)

Mismo contenido en el formato de H3. Llamada a `minimax/h3-max/reference-to-video` con `aspect_ratio: 9:16`, `resolution: 480P`, `duration: 14`, `prompt_expansion_mode: disabled` y `reference_image_urls` = [hoja de Martina, hoja de Tomás, F09], en ese orden.

```text
subject_definitions:
<Subject 1> is Martina, from <Picture 1> (character sheet): narrow face, a small mole on her LEFT cheekbone, shoulder-length dark brown wavy hair tucked behind her right ear, an oversized oatmeal chunky wool sweater with the sleeves pulled over her hands, a long charcoal wool coat worn open, faded dark jeans.
<Subject 2> is Tomás, from <Picture 2> (character sheet): thin wire-rimmed glasses, short neat dark brown hair with a side part, clean-shaven, a fitted navy quilted jacket over a charcoal merino sweater, an average, slightly soft build.
<Subject 3> is the passenger carriage of a night train, from <Picture 3>: pairs of blue seats, a window with a curtain on the left, a luggage rack with a warm reading lamp beneath it, other seats receding into dim amber pools.

summary:
[reference generation] Four shots in the passenger carriage: a two-shot of Martina and Tomás, an insert of her wrist, a close-up of Tomás and a close-up of Martina. Pictures 1 and 2 define the two people; Picture 3 defines the carriage and its light.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 4]): fully_preserved - face, mole on the left cheekbone, wavy hair behind the right ear, oatmeal sweater, open charcoal coat.
<Subject 2> (appears in [Shot 1], [Shot 3]): fully_preserved - wire-rimmed glasses, side-parted hair, navy quilted jacket.
<Subject 3> (appears in [Shot 1]–[Shot 4]): fully_preserved - blue seats, window with rain, reading lamp, warm amber light.

detailed_description:
The target video is live-action, cinematic, shot on a 50mm lens at T2 with shallow depth of field, lit only by practical sources: a warm 2400K reading lamp under the luggage rack lights both faces from above and in front, and the window is deep night blue with rain streaks on the outside of the glass. The whole carriage sways gently with the rails and the bodies sway with it. A few other passengers doze far behind, out of focus, and do not react.
[Shot 1] A static two-shot from the seat facing them, at seated eye height, framed from the top of their heads to their laps. <Subject 1> sits by the window on the left of the frame; <Subject 2> sits on the aisle side on the right. At 00:00.000 she is already lowering herself into her seat, slightly out of breath, and settles with her hands hidden in her sleeves on her lap. He turns toward her; his eyes reach her before his head does. (S1) A 31-year-old Chilean man with a soft Santiago accent and a calm, mid-low voice says softly, without reproach <d>[Spanish] ¿Dónde estabas?</d>. (S2) A 29-year-old Chilean woman with a soft Santiago accent and a low, tired, slightly husky voice answers before he finishes, too fast, looking at the seat back in front of her and not at him <d>[Spanish] En el baño.</d>.
[Shot 2] At 00:04.000, the camera cuts to a static insert on her lap, framed from her knee to the cuff of her sweater. Her left hand pulls the oatmeal sleeve down over a thin red mark around her right wrist and holds it there; then her fingers stay still.
[Shot 3] At 00:05.500, the camera cuts to a static close-up of <Subject 2>, three-quarter profile from her side, framed from mid-chest up. He looks at her one second longer than normal; his jaw tightens and releases; a small smile arrives late. (S1) says half joking, lightly <d>[Spanish] ¿Tu papá sabe que vienes en este tren?</d>. His eyes stay on her.
[Shot 4] At 00:09.000, the camera cuts to a close-up of <Subject 1>, three-quarter profile from his side, framed from mid-chest up, the night window soft behind her. The camera shakes very slightly with the train, with no push-in. Her eyes are fixed ahead, down the aisle toward the front of the train. (S2) says quietly <d>[Spanish] No.</d>. She holds a breath. At 00:11.000, almost to herself, barely moving her lips, (S2) says <d>[Spanish] Esa era la idea.</d>. At 00:12.000 his hand enters from the bottom edge of the frame and takes her left hand; she lets him without looking at him; her eyes stay ahead and blink twice, quickly, then she holds still. His lips stay out of frame and silent. The warm lamp light stays steady through all four shots. No music. No subtitles, no captions, no on-screen text.

overall_soundscape:
Continuous rail rhythm and a soft carriage rattle; rain ticking on the window; a distant cough from the front of the carriage at 10 seconds.

non_diegetic_music:
N/A
```

## 9. Revisión antes de entregar un prompt

Además de la lista de la skill `director-de-prompts`:
- [ ] ¿Cada emoción quedó escrita como conducta, sin palabras de emoción?
- [ ] ¿Cada personaje con cara tiene mirada con destino y segundo?
- [ ] ¿Hay una tarea física para las manos, con lado?
- [ ] ¿Los planos cerrados dicen dónde corta el cuadro?
- [ ] ¿La cámara tiene tipo, amplitud, velocidad y motivo, y no hay push-in sin motivo?
- [ ] ¿El balanceo del tren está escrito y es del cuerpo, no de la cámara?
- [ ] ¿El diálogo es idéntico al guion, con idioma y entrega física?
- [ ] ¿Cierra con «No music. No subtitles, no captions, no on-screen text.»?
