# 04 · Video v3 (H3, nunca corrido): ficha de las 17 llamadas para replanificar en Kling 4.0

Lectura del 9-nov-2026. No se generó nada ni se ejecutó ningún script del kit. Audio medido con `afinfo`. El archivo pasa de las ~2.500 palabras pedidas porque D, E y F van textuales.

**Tres avisos antes de las tablas**
1. Las 17 llamadas son c00a, c00b, c01, c01f, c02a, c02b, c03a, c03b, c04a, c04b, c05a, c05b, c05i, c06a, c06b, c07a, c07b (el bloque 0 también cuenta; total montaje 70,5 s).
2. `tiempos_montaje_v3.json` todavía trae **c02 como una sola llamada** (11,9 s, pista `c02_v2.mp3`). La partición c02a/c02b solo existe en `build_prompts_v3.py` (`SPLIT`) y en `prompts_video_v3.md`. `pistas/tiempos.json` describe las pistas anteriores (c02 12,5 s, c07a 8,3 s, c07b 7,5 s), no las `_v2`.
3. Configuración común del v3: `minimax/h3-max/reference-to-video`, 9:16, `prompt_expansion_mode: disabled`, 0,5 s de colchón al inicio y al final, semillas 1019 y 7342.

---

## A. Las 17 llamadas

### A1. Ficha general

| id | Bloque | Planos | Locación y luz | En cuadro | Pedida / montada (s) | Res. v3 | Refs img | Costo v3 ×2 semillas (USD) |
|---|---|---|---|---|---|---|---:|---:|
| c00a | 0 El maletín | b0_p1, b0_p2 | Vagón 2, ámbar bajo (2–3 lámparas) | Martina (ojos; mano y bota), zapatos del hombre de camisa azul, maletín | 4,0 / 3,0 | 480P | 3 | 0,46 |
| c00b | 0 | b0_p3, b0_p4 | Vagón 2, ámbar bajo | Pareja (hombre azul y esposa), Martina, lectora, esquina del maletín | 4,0 / 3,0 | 480P | 5 | 0,58 |
| c01 | 1 El recuerdo | b1_p1, b1_p2 | Puerta del fondo del vagón 2, ámbar bajo | Martina | 3,5 / 1,8 | 480P | 2 | 0,35 |
| c01f | 1 (flashes) | b1_f1, b1_f2 | Cuarto del rapto, cenital frío y duro | Martina (muñecas con cinta), figura con máscara lisa, maletín | 2,5 / 1,4 | 480P | 3 | 0,30 |
| c02a | 2 El regreso | b2_p1, b2_p2 | Vagón 5, ámbar | Martina, Tomás; inserto de la muñeca | 5,2 / 4,2 | 768P | 3 | 0,90 |
| c02b | 2 | b2_p3, b2_p4 | Vagón 5, ámbar | Tomás (P3), Martina y la mano de Tomás (P4) | 7,7 / 6,7 | 768P | 3 | 1,31 |
| c03a | 3 El maletín se abre | b3_p1, b3_p2, b3_p3 | Vagón 2, ámbar bajo | Maletín, niebla, hombre azul y esposa | 6,0 / 5,0 | 480P | 3 | 0,66 |
| c03b | 3 | b3_p4, b3_p5, b3_p6 | Vagón 2, ámbar bajo | Hombre azul (se infecta), esposa, lectora, pasajeros | 5,0 / 4,0 | 480P | 4 | 0,61 |
| c04a | 4 El grito | b4_p1, b4_p2, b4_p3 | Vagón 5, ámbar → rojo de emergencia en P3 | Iván, Carmen, pasajeros; Martina y Tomás (P2) | 5,5 / 4,5 | 480P | 6 | 0,82 |
| c04b | 4 | b4_p4, b4_p5, b4_p6 | Vagón 5, rojo | Siluetas infectadas, Hugo (llave y silbato), Martina, Tomás, Carmen, Iván | 7,5 / 6,5 | 768P | 8 | 1,63 |
| c05a | 5 La huida | b5_p1, b5_p2, b5_p3 | Fuelle entre vagón 5 y el último, rojo | Hugo (manos, llave), Iván, Carmen, Martina, Tomás, brazo infectado | 4,8 / 3,8 | 480P | 8 | 0,88 |
| c05b | 5 | b5_p4, b5_p6, b5_p7 | Fuelle rojo → interior del último vagón | Carmen, Iván, brazo infectado; Hugo y llave; grupo entrando | 5,2 / 4,2 | 480P | 8 | 0,94 |
| c05i | 5 (inserto P5) | b5_p5 | Fuelle, rojo | Mano derecha de Carmen sobre el vidrio roto | 2,0 / 1,0 | 480P | 2 | 0,20 |
| c06a | 5 (P8–P9) y 6 (P1) | b5_p8, b5_p9, b6_p1 | Último vagón, rojo, tubo frío sobre la puerta | Hugo, mano y cara infectadas; grupo completo en 6·P1 | 5,3 / 4,3 | 480P | 8 | 0,93 |
| c06b | 6 El encierro | b6_p2, b6_p3 | Último vagón, rojo | Carmen (palma); Tomás y Martina | 4,5 / 3,5 | 480P | 5 | 0,65 |
| c07a | 7 Diego | b7_p1, b7_p2, b7_p3 | Último vagón, rojo; Diego solo con el tubo frío | Grupo de espaldas; Diego tras la ventanita; Martina en PP con el grupo detrás | 8,1 / 7,1 | 768P | 8 | 1,74 |
| c07b | 7 | b7_p4, b7_p5, b7_p6 | Último vagón, rojo | Tomás; Diego tras el vidrio; Martina y la mano de Hugo en la manija | 6,7 / 5,7 | 768P | 6 | 1,37 |

Total v3: 480p 52,3 s + 768p 35,2 s → **14,34 USD** con dos semillas (15,54 si `image_url` cuenta como referencia). Precio H3: 0,05 USD/s a 480P y 0,08 a 768P, más recargo por referencias.

### A2. Primer fotograma y cámara que pide el prompt

Todos los primeros fotogramas se llaman `video_v3/primeros_fotogramas/<id>_<plano>_9x16.png` (ninguno existe hoy, ver G).

| id | Primer fotograma (fuente) | ¿En la lista por rehacer? | Cámara por plano |
|---|---|---|---|
| c00a | `c00a_b0_p1_9x16.png` (v1c, 1530×2720) | No | P1 primerísimo plano de ojos, handheld mínima · P2 inserto fijo a ras de piso (locked off) |
| c00b | `c00b_b0_p3_9x16.png` (v1c, 1152×2048) | No | P3 medio handheld con paneo corto y rápido de él a ella · P4 general fijo del pasillo; Martina se aleja caminando |
| c01 | `c01_b1_p1_9x16.png` (previs/frames, 603×1072) | No | Un solo plano medio fijo y continuo (el montaje usa el inicio y el final) |
| c01f | `c01f_b1_f1_9x16.png` (v1c, 603×1072) | **Sí** (b1_f1, luz) | Dos planos fijos (muñecas; algo más abierto) |
| c02a | `c02a_b2_p1_9x16.png` (v1c, 1530×2720) | **Sí** (b2_p1, luz) | P1 two-shot frontal, handheld muy suave · P2 inserto fijo del regazo |
| c02b | `c02b_b2_p3_9x16.png` (v1c, 1152×2048) | Primer fotograma no; **b2_p4 sí** (va en texto) | P3 PP de Tomás, handheld con push-in lento y corto · P4 PP de Martina, handheld quieta |
| c03a | `c03a_b3_p1_9x16.png` (v1c, 1152×2048) | **Sí** (b3_p1, maletín) | P1 detalle fijo a ras de piso · P2 plano bajo con tilt-up lento siguiendo la niebla · P3 medio handheld con temblor |
| c03b | `c03b_b3_p4_9x16.png` (v1c, 1530×2720) | No | P4 PP muy cerrado, handheld quieta · P5 medio, embestida, cámara sacudida por el impacto · P6 general handheld que llega tarde al grito |
| c04a | `c04a_b4_p1_9x16.png` (v1c, 1530×2720) | No | P1 general handheld con temblor leve · P2 PP handheld · P3 general fijo, ya en rojo |
| c04b | `c04b_b4_p4_9x16.png` (previs/frames, 603×1072, PLACEHOLDER) | **Sí** (b4_p4, resolución) | P4 plano cerrado de la ventanita con push corto y rápido · P5 whip pan de la puerta delantera a la trasera, handheld que se asienta en Hugo · P6 estampida, la cámara corre con ellos |
| c05a | `c05a_b5_p1_9x16.png` (v1c, 1530×2720) | No | P1 plano cerrado de la cerradura, handheld · P2 medio handheld (portazo y empujones) · P3 handheld con sacudida fuerte, revienta el vidrio |
| c05b | `c05b_b5_p4_9x16.png` (v1c, 1530×2720) | No | P4 medio handheld · P6 plano cerrado de la cerradura, handheld · P7 desde dentro del último vagón, handheld retrocediendo mientras entran |
| c05i | `c05i_b5_p5_9x16.png` (v1c, 1530×2720) | No | Inserto handheld con sacudida leve |
| c06a | `c06a_b5_p8_9x16.png` (v1c, 1152×2048) | **Sí** (b5_p8, uñas) | P8 plano cerrado handheld a la altura de la cerradura · P9 fijo de la ventanita, el impacto sacude el cuadro · 6·P1 general fijo |
| c06b | `c06b_b6_p2_9x16.png` (v1c, 1152×2048, PLACEHOLDER que «NO sirve para generar») | **Sí** (b6_p2, desde cero) | P2 PP fijo · P3 two-shot fijo |
| c07a | `c07a_b7_p1_9x16.png` (v1c, 1152×2048) | No | P1 medio del grupo de espaldas, handheld con temblor leve · P2 ventanita (60 % del ancho) con push-in lento · P3 PP de Martina, handheld casi quieta |
| c07b | `c07b_b7_p4_9x16.png` (v1c, 1152×2048) | No | P4 PP de Tomás, handheld quieta · P5 ventanita, handheld · P6 PP final fijo de Martina |

### A3. Diálogo y pista de voz (solo 5 llamadas tienen; las otras 12 van sin audio)

| id | Diálogo exacto (tiempo dentro de la llamada) | Pista | Duración medida |
|---|---|---|---|
| c02a | Tomás: «¿Dónde estabas?» 0,80–1,84 s · Martina: «En el baño.» 2,56–3,20 s | `KIT/contexto/pistas_v3/c02a.mp3` (+ `.wav`) | mp3 **5,251 s** · wav 5,200 s |
| c02b | Tomás: «¿Tu papá sabe que vienes en este tren?» 0,71–2,67 s · Martina: «No.» 3,40–3,68 s · Martina: «Esa era la idea.» 5,23–6,15 s | `KIT/contexto/pistas_v3/c02b.mp3` (+ `.wav`) | mp3 **7,732 s** · wav 7,700 s |
| c04b | Hugo: «¡Al último vagón! ¡Rápido!» 2,63–4,56 s (pitazo a 2,1 s va en post, no está en la pista) | `pistas_v3/c04b.mp3` = `REPO/.../pistas/c04b.mp3` (mismo md5; mono; sin wav) | mp3 **7,549 s** |
| c07a | Diego: «¡Martina! ¡Martina, ábreme!» 1,63–3,95 s · Diego (en off): «¡Te vi en el vagón 2!» 5,00–7,06 s | `pistas_v3/c07a_v2.mp3` = `REPO/.../pistas/c07a_v2.mp3` (mismo md5); wav solo en REPO | mp3 **8,150 s** · wav 8,100 s |
| c07b | Tomás: «¿No estabas en el baño?» 0,70–2,52 s | `pistas_v3/c07b_v2.mp3` = `REPO/.../pistas/c07b_v2.mp3` (mismo md5); wav solo en REPO | mp3 **6,740 s** · wav 6,700 s |

Pistas anteriores en `REPO/.../cap01_animatic_v3/pistas/` (el v3 no las usa): c02.mp3 12,539 s; c02_v2.mp3 11,938 s; c07a.mp3 8,333 s; c07b.mp3 7,549 s.

Tomas sueltas por línea en `REPO/produccion/pruebas/cap01_animatic/voces/`: martina_b2_1 1,149 s · tomas_b2_1 1,646 s · tomas_b7_1 2,273 s · hugo_b4_1 2,351 s · diego_b7_2 2,508 s · tomas_b2_2 2,508 s · diego_b7_1 2,926 s · martina_b2_2 3,082 s.

---

## B. Límites de Kling 4.0 (MCP) y Seedance 2.5

Kling MCP (`omni_ref_video`, `kling-video-v4_0`): `duration` entero 3–30; `video_1` 3–30 s (se cobra entrada + salida); `audio_1` **5–30 s** según el `who_am_i` del MCP (el §4.1 de métodos dice 4,9–30); hasta 10 imágenes y 15 referencias en total; `prefer_multi_shots` fijo en `true`. Seedance 2.5 (fal): `duration` entero 4–30; **sin primer ni último fotograma**; `audio_urls` 1,8–30,2 s.

| id | Pedida | Entero Kling (techo; mín. 3) | Kling duración | Kling `audio_1` | Seedance ≥4 s |
|---|---:|---:|---|---|---|
| c00a | 4,0 | 4 | Cumple | Sin pista | Cumple |
| c00b | 4,0 | 4 | Cumple | Sin pista | Cumple |
| c01 | 3,5 | 4 (o 3: el montaje usa hasta 2,3 s) | Hay que redondear | Sin pista | **No** (3,5 < 4) |
| c01f | 2,5 | 3 | **No** (2,5 < 3): subir a 3 | Sin pista | **No** |
| c02a | 5,2 | 6 | Redondear | **Cumple por poco**: 5,251 s (margen 0,25 s; wav 5,200) | Cumple |
| c02b | 7,7 | 8 | Redondear | Cumple (7,732) | Cumple |
| c03a | 6,0 | 6 | Cumple | Sin pista | Cumple |
| c03b | 5,0 | 5 | Cumple | Sin pista | Cumple |
| c04a | 5,5 | 6 | Redondear | Sin pista | Cumple |
| c04b | 7,5 | 8 | Redondear | Cumple (7,549) | Cumple |
| c05a | 4,8 | 5 | Redondear | Sin pista | Cumple |
| c05b | 5,2 | 6 | Redondear | Sin pista | Cumple |
| c05i | 2,0 | 3 | **No** (2,0 < 3): subir a 3 | Sin pista | **No** |
| c06a | 5,3 | 6 | Redondear | Sin pista | Cumple |
| c06b | 4,5 | 5 | Redondear | Sin pista | Cumple |
| c07a | 8,1 | 9 (8 corta 0,15 s de cola de la pista) | Redondear | Cumple (8,150) | Cumple |
| c07b | 6,7 | 7 | Redondear | Cumple (6,740) | Cumple |

- **Solo 4 llamadas piden ya un entero** (c00a, c00b, c03a, c03b). Las otras 13 hay que redondearlas, y el previz debe durar lo mismo que la salida.
- **Menos de 3 s (Kling):** c01f (2,5) y c05i (2,0).
- **Menos de 4 s (Seedance):** c01 (3,5), c01f (2,5) y c05i (2,0). El §4.2 dice fusionarlas con la vecina o subirlas a 4 s. Para c05i el v3 ya da una salida sin costo: imagen fija con empuje en post.
- **Pista de voz de menos de 5 s en las llamadas del v3: ninguna.** Las cinco pistas montadas miden entre 5,25 y 8,15 s. La más justa es c02a.
- **Donde sí aparece el problema de los 5 s:** si se sigue lo que dice `voces.md` («una pista por línea… como referencia de audio en Kling 4.0»), las ocho tomas sueltas quedan todas bajo 5 s. Lo que le falta a cada una: martina_b2_1 3,85 s · tomas_b2_1 3,35 s · tomas_b7_1 2,73 s · hugo_b4_1 2,65 s · diego_b7_2 2,49 s · tomas_b2_2 2,49 s · diego_b7_1 2,07 s · martina_b2_2 1,92 s. Además, martina_b2_1 y tomas_b2_1 tampoco llegan al mínimo de 1,8 s de Seedance.
- **Sin verificar:** si Kling acepta una pista más larga que la salida (c02a a 5 s, c07a a 8 s) y si usa `audio_1` como banda sonora exacta o solo como referencia de voz. El prompt del v3 lo pide como banda sonora exacta con sincronía labial.
- **Primer fotograma:** Seedance no lo acepta. En el MCP de Kling `omni_ref_video` solo lista `image_1..10` como referencias (`start_image_url` existe en fal).
- **Referencias:** el máximo del v3 es 8 imágenes + 1 pista; con el previz son 10, dentro de las 15 de Kling.
- **H3 con previz:** el §4.3 advierte no combinar primer fotograma con video de referencia; video y audio de referencia de 2–15 s.

---

## C. Clasificación por tipo de cámara y acción

| Tipo | Llamadas |
|---|---|
| (1) Diálogo o reacción casi fija | c01, c02a, c02b, c04a, c06b, c07b |
| (2) Inserto o detalle | c00a, c01f, c03a, c05i |
| (3) Cámara que viaja o acción con blocking | c00b (leve), c03b, c04b, c05a, c05b, c06a, c07a |

**Las 6 «de acción» del productor (c04b, c05a, c05b, c06a, c07a, c07b):**
- **De acuerdo sin reservas con c04b, c05a, c05b y c06a.** Son las que piden whip pan, cámara que corre o retrocede con el grupo, portazos, vidrio que revienta y agarres; calzan con las recetas de tracking y embestida del §6.1 (previz obligatorio).
- **c07a, de acuerdo en parte:** P2 es la receta «POV por la ventanita» del §6.1 (push-in lento hacia Diego, previz obligatorio). P1 y P3 son reacción casi fija con ola de cabezas.
- **c07b, en desacuerdo según el prompt:** es PP de Tomás con diálogo, 1,2 s de Diego golpeando el vidrio y un PP fijo de Martina. El propio checklist del v3 la marca «—» en R5 (bloques de acción). Su dificultad es de ejes y continuidad (placa a la derecha, mano de Hugo en la manija), no de movimiento.
- **Falta c03b:** P5 es la embestida del hombre de camisa azul sobre su esposa, justo la receta «embestida zombie» del §6.1, y el checklist la marca como bloque de acción. Si la lista debe ser de seis, c03b entra mejor que c07b.
- Casos leves: c00b (paneo corto y Martina caminando por el pasillo con cámara fija) y c03a P2 (tilt-up lento con la niebla).

---

## D. Criterios de revisión de cada toma (textual de `prompts_video_v3.md`)

### D1. Checklist de `revision_v1.md` §5, por llamada

✔ = el prompt lo fija · ✔·t = se revisa en la toma (el prompt pide la duración justa y no hay relleno) · — = no aplica · ⚠ = depende del primer fotograma corregido o de su resolución. Los tres puntos de **Montaje** (cortar en la acción y en los cortes reales, flashes con motivo, prueba sin sonido) son de último vagón y Métricas sobre las tomas, no del prompt.

| Punto | c00a | c00b | c01 | c01f | c02a | c02b | c03a | c03b | c04a | c04b | c05a | c05b | c05i | c06a | c06b | c07a | c07b |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| R1 · Ningún plano dura más que su acción + 0,5 s | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ (silencio) | ✔ (silencio) | ✔ | ✔ |
| R2 · Cada plano empieza con la acción en marcha | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| R3 · Ninguna línea entra > 0,3 s después del corte | — | — | — | — | ✔ | ✔ | — | — | — | ✔ | — | — | — | — | — | ✔ | ✔ |
| R4 · Sin cuadros congelados | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t | ✔·t |
| R5 · Bloques de acción: planos de 1–1,5 s | — | — | — | — | — | — | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | — | ✔ | — |
| C1 · Tamaño, altura, tipo de cámara y motivo | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ⚠ b4_p4 a 1152×2048 (sunburst) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| C2 · Ejes de mirada | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| C3 · 180° | — | ✔ | — | — | ✔ | ✔ | — | — | ✔ | ✔ | — | ✔ | — | ✔ | ✔ | ✔ | ✔ |
| K1 · Props donde dice la tabla | ✔ | ✔ | — | — | — | — | ⚠ b3_p1 | — | ✔ | ✔ | ✔ | ✔ | — | ✔ | — | ✔ | ✔ |
| K2 · Detrás de cada vidrio, lo de la tabla; ventanita sin cielo ni lluvia | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| K3 · Heridas, manchas y ropa mojada del lado correcto | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ⚠ b5_p8 | ⚠ palma DERECHA en b6_p2 nuevo | ✔ | ✔ |
| K4 · Nadie aparece de la nada | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| K5 · Causa antes que efecto | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| A1 · Entrega física = toma de voz | — | — | — | — | ✔ | ✔ | — | — | — | ✔ | — | — | — | — | — | ✔ | ✔ |
| A2 · Nadie mira la nada | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| A3 · Reacciones en ola | ✔ | ✔ | — | — | — | — | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | — | ✔ | — | ✔ | — |
| A4 · Manos y objetos naturales, o sin objeto | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ⚠ b6_p2 nuevo (sunburst) | ✔ | ✔ |

«También revisado» (resumen): diálogo idéntico al guion, en español dentro de `<d>`; sin «blood» ni «gore»; gorra de Hugo sin letras; en la ventanita solo el fuelle oscuro, vidrio seco, sin cielo ni lluvia; ventana del vagón 5 siempre del lado de Martina; pared trasera del último vagón sin segunda puerta; luz roja desde arriba con media cara en sombra; el tubo frío es la única luz sobre Diego.

### D2. Pasada de vestuario en la revisión de tomas

Revisar cuadro a cuadro (sobre todo el primero y el último de cada plano) y comparar con la toma elegida de la llamada anterior en que sale el mismo personaje:

| Qué mirar | Debe verse | Llamadas | Si falla |
| --- | --- | --- | --- |
| **Manga de Diego** | Solo la manga DERECHA rota y con manchas dark red-black, del codo al puño; la IZQUIERDA limpia, clara y entera (en c07b es la que golpea el vidrio). Chaqueta de lona clara empapada y más oscura en los hombros, capucha gris oscura debajo, pelo mojado pegado a la frente. Nunca manchas en el pecho ni en la manga izquierda | c07a P2, c07b P2 | Otra semilla. Si las dos fallan, se descarta; no se corrige en post |
| **Puño avena de Martina** | El puño del suéter avena asoma bajo la manga del abrigo y le cubre los nudillos en todos los planos donde se le ven las manos. Solo deja ver la muñeca derecha cuando la manga se sube a propósito (c02a P2) | c00a P2, c01, c01f, c02a, c02b P2, c04a P2, c04b P3, c05b P3 | Elegir la otra semilla; anotarlo si en c02a no se alcanza a ver la marca |
| **Abrigo gris de Martina** | Abrigo largo de lana gris carbón, siempre abierto, del mismo tono en ámbar y en rojo (con luz roja se ve más oscuro, pero no cambia de color ni de largo); suéter avena debajo, jeans oscuros, botas cafés | Todas donde sale Martina | Comparar el mismo plano entre las dos semillas y entre llamadas vecinas (c02b→c04a, c06a→c06b→c07a→c07b) |
| **Gorra de Hugo** | Gorra azul marino siempre puesta, con una insignia de rueda lisa sin letras ni logo. Chaqueta larga azul marino con botones de bronce mate, silbato colgando del cordón. En c07b solo se le ve la mano derecha en la manija, sin llave | c04b, c05a, c05b, c06a, c07a | Si la gorra desaparece o la insignia trae letras, se descarta la toma |
| **Llave** | En c04b, en alto en la mano derecha desde que aparece; en c05b, gira por fuera, sale y se queda en el puño; en c06a gira por dentro y no se guarda en cuadro; en c07b no hay llave | c04b, c05a, c05b, c06a, c07b | Se descarta |
| **Maletín** | Debajo del asiento del hombre de camisa azul, por el lado del pasillo, asomando solo la esquina metálica; cuerpo oscuro, esquinas y dos cierres metálicos. En el flash, sobre las rodillas de Martina. Desde el bloque 4 no se ve | c00a P2, c00b P2, c03a, c01f P2 | Si queda al lado del asiento o cambia de forma, se descarta |
| **Carmen** | Abrigo café sobre el uniforme celeste, bolso en el hombro IZQUIERDO, anteojos en el cordón. Desde c05b P1, el corte en la palma DERECHA; desde c06b, la mano derecha cerrada dentro del abrigo (también en c07a) | c04a–c07a | Comparar el lado de la herida y del bolso |
| **Tomás e Iván** | Tomás siempre con los anteojos de marco metálico y la chaqueta acolchada azul marino; Iván con la chaqueta de lona de obrero y la cabeza rapada | c02a–c07b | Se descarta si pierde los anteojos o cambia la chaqueta |

Anotar en `tomas.json`, por toma elegida, «vestuario OK» o el problema concreto, para que montaje no mezcle dos tomas incompatibles.

---

## E. Estructura del prompt H3 del v3 y ejemplo completo

Formato Ref2VA oficial de MiniMax, en inglés, con el diálogo en español. Secciones, en este orden:

1. **`subject_definitions:`** una línea por referencia (ancla de identidad + vestuario inmutable), la frase del primer fotograma y, si hay voz, la declaración de Audio 1.
2. **`summary:`** etiqueta de tarea, resumen de los planos y qué define cada Picture.
3. **`retention_analysis:`** por Subject, en qué planos aparece y `fully_preserved`.
4. **`detailed_description:`** un párrafo de look y uno por `[Shot N]`: corte con tiempo, tamaño y cámara con su motivo, acción con tiempos, diálogo como `(S1) … says <d>[Spanish] …</d>` y la línea «What stays still in this shot: …» (empieza con la frase de luz). Cierre fijo «No music. No subtitles, no captions, no on-screen text.»
5. **`overall_soundscape:`** ambiente y efectos.
6. **`non_diegetic_music:`** `N/A`.

Para Kling: `<Picture N>` pasa a 图片N (MCP) o `@ImageN` (fal), el previz entra como 视频1 y la frase del primer fotograma se reemplaza.

**Ejemplo textual: c02a** (5.505 caracteres; referencias 1 `HOJA_martina`, 2 `HOJA_tomas`, 3 `F09`; Audio 1 `c02a.mp3`):

```text
subject_definitions:
<Subject 1> is Martina, 29, from <Picture 1> (character sheet; identity, face, hair and wardrobe only, ignore the sheet layout and grey backdrop): narrow face, a small mole on her LEFT cheekbone, shoulder-length dark brown wavy hair tucked behind her right ear, an oversized oatmeal chunky wool sweater whose cuffs reach over her knuckles, a long charcoal wool coat worn open, faded dark jeans, brown boots. Wardrobe identical to Picture 1 in every frame; it does not change color and does not change during the shot: the charcoal grey wool coat always open, the cuff of the oatmeal sweater always showing below the coat sleeve and covering her knuckles, faded dark jeans, brown boots.
<Subject 2> is Tomás, 31, from <Picture 2> (character sheet; identity and wardrobe only): thin full metal-frame glasses, short neat dark brown hair with a clean side part, no curls and no fringe on the forehead, clean-shaven, a fitted navy quilted jacket over a charcoal sweater, an average, slightly soft build. Wardrobe identical to Picture 2 in every frame; it does not change color and does not change during the shot: the navy quilted jacket over the charcoal sweater, the thin metal-frame glasses always on his face.
<Subject 3> is carriage 5, the couple's seats and the amber light, from <Picture 3>: pairs of blue seats, the window on the LEFT of the pair with rain on the outside of the glass, a warm reading lamp under the luggage rack.
The start frame (image_url) is the first frame of [Shot 1]; the video opens exactly on it.
Audio 1 is the exact dialogue of this scene: use it as the soundtrack and sync every line to the lips of the speaker. Voices only from Audio 1.

summary:
[keyframe completion + reference generation] Two shots in carriage 5: a frontal two-shot of Martina and Tomás as she returns to her seat and lies about where she was, then a close insert of her wrist mark being covered. The video opens exactly on the given start frame ([Shot 1]). Picture 1 defines Martina, Picture 2 Tomás, Picture 3 the seats and the amber light; Audio 1 is the dialogue.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - face, mole on the left cheekbone, wavy hair behind the right ear, oatmeal sweater, open charcoal coat.
<Subject 2> (appears in [Shot 1]): fully_preserved - metal-frame glasses, side-parted short hair, navy quilted jacket.
<Subject 3> (appears in [Shot 1], [Shot 2]): fully_preserved - blue seats, window on Martina's side with rain outside, warm reading lamp.

detailed_description:
The target video is live-action, cinematic, 9:16 vertical, 50mm lens at T2, shallow depth of field, fine film grain, crisp natural skin. Carriage 5 at night in warm amber: the reading lamp under the luggage rack lights faces from above and in front. The window is always on Martina's side of the pair (the left of the pair as seen from the seat facing them), deep night blue with rain streaks on the outside of the glass. A few other passengers doze far behind, out of focus. The whole carriage sways gently with the rails and the bodies sway with it.
[Shot 1] A frontal two-shot from the seat facing them, at seated eye height, framed from the knees up, exactly as the start frame. <Subject 1> is in the window seat at frame LEFT, the rainy window beside her; <Subject 2> is in the aisle seat at frame RIGHT. The camera is handheld, very gentle, barely breathing with them. At 00:00.000 she has just dropped into her seat and is still settling, slightly out of breath. He turns toward her; his eyes reach her before his head does. At 00:00.800 Tomás speaks the first line of Audio 1, curious, with a trace of suspicion, looking at her one second longer than normal: (S1) A 31-year-old Chilean man with a soft Santiago accent and a calm, mid-low voice says <d>[Spanish] ¿Dónde estabas?</d>. At 00:02.560 Martina speaks the second line of Audio 1, too casual, straightening her coat with both hands and not looking at him, her eyes on the seat back in front of her: (S2) A 29-year-old Chilean woman with a soft Santiago accent and a low, tired voice says <d>[Spanish] En el baño.</d>. Tomás's lips stay closed while she speaks. What stays still in this shot: only 2–3 warm amber ceiling lamps, darkness between them, no added fill; Martina keeps her eyes on the seat back in front of her and never turns to him; Tomás stays seated, his hands resting on his own lap; Martina's lips stay closed and still while Tomás speaks, and Tomás's lips stay closed and still while she speaks; the rain stays on the outside of the window glass.
[Shot 2] At 00:03.700, the camera cuts to a static close insert on her lap, framed from her knee to her sleeve. As she straightens the coat, the sleeve has ridden up and shows a thin faint red line around her RIGHT wrist; at 00:04.000 the fingers of her LEFT hand pull the sleeve down over it in one tug and hold it there, still. Nobody speaks in this shot. What stays still in this shot: only 2–3 warm amber ceiling lamps, darkness between them, no added fill; the camera stays locked off; her knee and the coat stay still; after the tug her left hand stays on her right wrist, holding the sleeve down; no face is in the frame. No music. No subtitles, no captions, no on-screen text.

overall_soundscape:
Dialogue comes only from Audio 1. Ambience and effects: Continuous rail rhythm and soft carriage rattle; rain ticking on the window; the rustle of her coat as she sits and straightens it.

non_diegetic_music:
N/A
```

Los otros 16 prompts están completos en `prompts_video_v3.md` (c07b en las líneas 889–921) y en `payloads_fal_v3.json` (`llamadas[].input.prompt`).

---

## F. Los 7 fotogramas por rehacer (textual)

«Hay que rehacerlos o corregirlos antes de llamar a H3. Mientras tanto, la ruta actual queda como placeholder. Después de corregirlos, recortar con `prep_frames.py` usando el mismo nombre de salida.»

| Cuadro | Llamada | Qué corregir |
| --- | --- | --- |
| b1_f1 | c01f (primer fotograma) | Luz del cuarto del rapto: un cenital frío y duro desde arriba, oscuridad alrededor, sin relleno |
| b2_p1 | c02a (primer fotograma) | Luz del vagón 5: dejar solo 2–3 lámparas de techo ámbar con negro entre ellas, sin relleno (ref. F08_v2) |
| b2_p4 | c02b (P4; no es primer fotograma, va en texto) | Igual que b2_p1: 2–3 lámparas de techo con negro entre ellas (ref. F08_v2). Hay que corregirlo para que la previs y el animatic queden coherentes |
| b3_p1 | c03a (primer fotograma) | Maletín debajo del asiento, por el lado del pasillo; no al lado |
| b4_p4 | c04b (primer fotograma) | Rehacer a 1152×2048 en sunburst (hoy es de 608×1088 para una llamada a 768p) |
| b5_p8 | c06a (primer fotograma) | Uñas cortas, rotas y sucias en la mano infectada |
| b6_p2 | c06b (primer fotograma) | Rehacer desde cero en sunburst: palma derecha abierta cerca del pecho, la mirada sobre el corte |

Son 7 cuadros pero solo **6 primeros fotogramas** (c01f, c02a, c03a, c04b, c06a, c06b); b2_p4 no entra como imagen. Las notas por llamada agregan:
- **c03a:** b3_p1 debe quedar «BAJO el asiento del hombre, lado pasillo, con el mismo encuadre que b0_p2 y la tapa cerrada».
- **c06b:** el cuadro nuevo «mostrará a Carmen en primer plano, con la palma derecha abierta cerca del pecho y la mirada sobre ella; se ve el corte fino con la mancha dark red-black, igual que ESTADO_carmen_palma_v2_palma». El actual (puño en el pecho) «NO sirve para generar».

---

## G. Qué referencian los scripts y no existe ni en KIT ni en REPO

Scripts (todos locales, ninguno llama a fal): `prep_frames.py` recorta a 9:16 el primer fotograma de cada llamada y arma el JSON y la hoja de contacto; `p1_refs.py` define URLs, anclas de identidad, frases de luz y «Estado del mundo»; `p2_calls_a/b/c.py` definen las 17 llamadas; `p2d_quietud.py` agrega vestuario inmutable y la línea de quietud por plano; `build_prompts_v3.py` importa todo y escribe `prompts_video_v3.md`, `payloads_fal_v3.json` y `costo_video_v3.json`.

| Referenciado | Estado | Cómo recuperarlo |
|---|---|---|
| `/workspace/fahren-tv/el-ultimo-vagon/video_v3/` (`ROOT`, fijo en `p1_refs.py`) | No existe en esta máquina | Los scripts no corren sin cambiar `ROOT` y `SRC` |
| `video_v3/src_1a7c35b/` (copia de PR #14) | No existe | REPO trae lo que leen los scripts: `tiempos_montaje_v3.json`, `produccion/assets/fal_urls_v1.json` (38 claves, todas las que se usan) y los cuadros de previs |
| `video_v3/primeros_fotogramas/*.png` (17 recortes) | **No existen.** Solo están `primeros_fotogramas.json` y `hoja_primeros_fotogramas.jpg` | Sin costo: las 17 fuentes están en `REPO/.../previs/v1c/frames/` (c01 y c04b en `previs/frames/`). Hay que repetir el recorte de `prep_frames.py` |
| `video_v3/refs/HOJA_hugo_1536x858.png` | **No existe**, y tampoco hay `HOJA_hugo.png` local | Bajar la hoja (URL en `fal_urls_v1.json`, enlace en `INDICE_DRIVE.md`) y reducirla. La de 2752 px dio `image_load_error` en fal |
| `video_v3/refs/lectora_b0_p4.png` | No existe en esa ruta | Sí está en `REPO/.../previs/v1c/refs/lectora_b0_p4.png`; nunca se subió a fal |
| `video_v3/pistas/*.mp3` | La carpeta no existe con ese nombre | Las 5 pistas están en `KIT/contexto/pistas_v3/` (c02a y c02b solo ahí) |
| Hojas, props y sets como archivo local: `HOJA_martina`, `HOJA_tomas`, `HOJA_carmen`, `HOJA_ivan`, `HOJA_hugo`, `HOJA_extra_pareja_camisa_azul`, `PROP_llave_y_cerradura`, `F01`, `F02`, `F03`, `F07`, `F09`, `F10` | **Sin archivo local**; solo URL de `v3b.fal.media` de octubre (no comprobé si siguen vivas) | Si caducaron, bajarlas de Drive y subirlas con `file_upload` de Kling |
| Cuadros corregidos de los 7 de la sección F | No existen | Hay que generarlos (único punto con costo de imagen) |
| `tomas.json` del video v3 | No existe | Se crea al elegir tomas |
| Previz de Blender por llamada | No hay ningún `.blend` ni video de previz en KIT ni en REPO | Hay que producir los 17 (o los de acción) |

Sí hay archivo local en REPO de: `ESTADO_hombre_azul_infectado`, `ESTADO_carmen_palma_v2_palma`, `F08_v2_ambar_bajo`, `cuarto_rapto_martina_v2` (`cap01_animatic_v3/assets/`), `estado_diego_mojado_herido_v3`, `prop_maletin_v2_nbp_0` (`produccion/assets/generados/`) y `ref_infectados.jpg` (`direccion_arte/referencias/`).
