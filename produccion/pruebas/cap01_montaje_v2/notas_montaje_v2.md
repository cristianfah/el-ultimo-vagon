# Montaje de revisión v2: cap. 1, cold open y escena 1 (video tanda 1)

Armado el 3-oct-2026 en la box. No se gastaron créditos, no se generó nada y no se tocó GitHub ni Drive.

## Archivos

| Archivo | Qué es |
|---|---|
| `cap01_montaje_v2.mp4` | **El armado.** 480×854 (9:16), 24 fps, H.264 High + AAC 48 kHz estéreo, `+faststart`. 20,92 s, 3,5 MB |
| `cap01_v2_clips_completos.mp4` | Extra: los 6 clips enteros, b01→b06, sin recortar y con la etiqueta del bloque en la esquina. 38,2 s, 5,3 MB. Sirve para ver lo que el armado deja fuera |
| `contact_sheet.png` | 2×3, un fotograma por clip |
| `tiras/bNN.png` | Tira de cada clip a 2 fotogramas por segundo, con el tiempo, para revisar el medio del clip |
| `edl_v2.txt` + `build.py` | EDL y script de armado. `python3 build.py` lo rehace |
| `src/c01_b0N.mp4` | Los 6 clips fuente originales (H3 Max 480P) |

**Fuente:** CDN de fal (`produccion/pruebas/cap01_montaje_v2/urls_video_tanda1.json`). Las 6 URLs respondieron 200 el 3-oct-2026 a las 00:52 (hora de Chile). No hizo falta Drive.

## Cómo se armó (mismo método que la v1)

- La v1 se armó con ffmpeg desde una EDL (`cap01_montaje_v1/edl.txt`): un corte por plano, cortes secos, audio del modelo con un fundido de 20–40 ms en cada corte, sin música, sin textos ni subtítulos. La v2 hace lo mismo con fundidos de 30 ms.
- El orden de los planos sale de `produccion/montaje/cap01.md`, p01→p10. Por eso b03 se parte en cinco planos y el inserto del celular (b04) entra entre p04 y p06.
- Los in/out de la v1 no sirven para las tomas nuevas. Se recalcularon sobre los clips v2 para mantener más o menos la duración de cada plano en la v1. En b03 se usaron los cortes internos que hizo el modelo (3,21 / 5,42 / 8,08 / 10,75 s), con 2 fotogramas de margen.
- Normalización: los fuentes vienen en 480×832 (b02 en 480×864) a 24 fps con AAC de 32 kHz. Se escalan a 480×854, recortando para llenar (unos 13 px por lado en los de 832), y el audio se pasa a 48 kHz.
- **Sin subtítulos:** la v1 no los llevaba. **Sin ambiente continuo de lluvia y tren** (mejoras #15 / plan paso 11): no hay pista de ambiente en el repo y no se generó ninguna.

## Línea de tiempo

| # | Plano | Clip | In–Out (s) | Dura | Acumulado | Qué se ve (según el repo) |
|---|---|---|---|---|---|---|
| 1 | c01_p01 | b01 · mano en ventanita | 1,70–3,30 | 1,60 | 1,60 | La mano mojada de Diego golpea el vidrio de la ventanita y la palma queda apoyada. Luz roja, pasillo vacío |
| 2 | c01_p02 | b02 · Martina «Diego…» | 2,40–3,75 | 1,35 | 2,95 | Martina de pie bajo luz roja, mechones y sudor. Susurra «Diego…» (voz en 3,05–3,47 del clip) |
| 3 | c01_p03 | b03 beat 1 | 0,00–3,13 | 3,13 | 6,08 | Plano de dos con luz ámbar. Tomás: «Este viaje es para arreglarlo, ¿cierto?» |
| 4 | c01_p04 | b03 beat 2 | 3,29–5,33 | 2,04 | 8,12 | Primer plano de Martina: «Sí.» |
| 5 | c01_p05 | b04 · celular | 0,70–2,50 | 1,80 | 9,92 | Inserto: el celular se enciende, 23:38 y mensaje de D. Entra la mano izquierda por la derecha |
| 6 | c01_p06 | b03 beat 3 | 5,50–8,00 | 2,50 | 12,42 | Plano de dos: Martina da vuelta el celular sobre el muslo |
| 7 | c01_p07 | b03 beat 4 | 8,17–10,67 | 2,50 | 14,92 | Carmen duerme contra la ventana |
| 8 | c01_p08 | b03 beat 5 | 10,83–12,21 | 1,38 | 16,30 | Iván, de brazos cruzados, recorre los asientos con la mirada |
| 9 | c01_p09 | b05 · Hugo y boleto | 0,50–3,20 | 2,70 | 19,00 | Don Hugo se agacha a recoger el boleto del pasajero dormido |
| 10 | c01_p10 | b06 · revólver | 0,40–2,20 | 1,80 | 20,80 | Inserto: se abre la chaqueta y aparece el revólver en la funda café |

Total nominal: 20,80 s. El archivo dura 20,92 s por el redondeo a fotogramas. La v1 duraba 20,4 s y el guion técnico pide 16 s.

Duración de los clips fuente: b01, b02, b04, b05 y b06 duran 5,18 s cada uno; b03 dura 12,26 s. Todos traen audio (AAC estéreo, 32 kHz).

## Lo que se notó (solo se anota, no se corrigió)

**Conocidos:**
1. **b04 / c01_p05:** la pantalla dice «Estoy en el tren.» (texto v3). La v7 dice «Ya subí. Vagón 4.» El keyframe aprobado ya traía el texto viejo y hay que regenerarlo (plan §0).
2. **b01 / herida de Diego:** según la v7, la herida va en el brazo **derecho**. En el clip, la mano es la derecha (el pulgar queda a la derecha del cuadro, como pide el YAML), pero el brazo entra desde abajo a la izquierda. La manga está empapada y manchada, y no se distingue una herida clara en ningún brazo. Hay que revisarlo contra la regla del brazo derecho.

**Nuevos:**
3. **b02 trae el subtítulo «Diego…» dibujado** en el centro de la imagen, más o menos entre 2,9 y 4,05 s del clip. Es el mismo error que obligó a regenerar b02 en la v1. Queda a la vista en el armado (plano 2), porque cae justo sobre la línea. Hay que regenerar el bloque o borrarlo en post.
4. **b01, glitch en el medio del clip:** entre 1,5 y 2,5 s la mano queda limpia y clara, y después vuelve a estar ensangrentada. Además, las manchas del vidrio y la luz saltan cerca de los 2,0 s. Es la falla de interpolación FL que ya se había visto en la v1. Golpea varias veces (picos de audio en 0,64 / 1,02 / 1,28 / 1,79 / 2,05 s) en vez de los dos golpes pedidos. Parte del glitch entra en el plano 1.
5. **b06, una mano entra al cuadro** entre 0,25 y 1,25 s: un puño de camisa blanca abre la chaqueta, cuando el prompt dice «No hand enters the frame». En el armado se ve. El martillo y la parte de arriba del revólver salen deformados (forma de púas). Lo bueno: **ya no hay balas en el cinturón** (falla de b06 en la v1) y el tambor se ve cerrado.
6. **Uniforme de Hugo (b05, b06):** la chaqueta y la gorra se leen azul marino o negras, con botones dorados, y el YAML pide gris («grey cap», «grey jacket»). La v1 tuvo lo mismo con la gorra. Hay que revisarlo también contra hc18 (nadie con nombre viste de azul).
7. **Mirada de Martina en b02:** mira hacia la **derecha** del cuadro. El prompt dice «door window off-screen left» y la v1 cortaba con la mirada a cuadro izquierdo. Hay que ver si calza con la mano de b01 (el brazo entra desde abajo a la izquierda).
8. **b03 beat 3 (p06):** Tomás mira a Martina, no al pasillo como pide el prompt. El celular encendido no se deforma (problema de la v1 resuelto, al menos a 2 fps).
9. **b05:** el agachado ocupa unos 3 s (con el in en 0,50 se ve casi entero). En la tira no se distingue el boleto en la mano.
10. **Audio:** todos los clips traen sonido, pero con niveles muy distintos: b01 y b06 rondan −21/−22 dB de media, b05 queda en −34 dB. Se dejaron tal cual, como el audio nativo de la v1. Los saltos de ambiente entre clips se notan; el ambiente continuo de lluvia queda pendiente (mejoras #15).
11. **b04:** el celular muestra una ranura de auricular arriba y la barra de estado. No hay muesca ni marca. La mano entra a los ~2,0 s.
12. **Duración:** 20,8 s contra los 16 s del guion técnico. Además, el plan v2 §0 dice que en la v7 p04 se alarga por «Solo nosotros.», línea que este b03 no tiene.
