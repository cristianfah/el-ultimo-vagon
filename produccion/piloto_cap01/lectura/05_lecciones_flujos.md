# 05 · Lecciones y flujos: lectura para el piloto del cap. 1

Leído: los dos archivos de `lecciones/`, los 22 de `flujos/` y `local/overview.md`. No leí el guion ni las notas del capítulo.
Fuentes: primer tramo del nombre de archivo en `flujos/` (`ezheng` = `ezheng_fight_57_planos…md`; `acting §n` = entrada n de `acting_micro_episodios.md`).

**Avisos**
1. Los flujos son reportes de terceros, sin probar por el equipo; varios son contenido pagado (aiehon, pjace, evals).
2. Ningún flujo usa Kling 4.0 con previz ni con audio de referencia, y ninguno menciona el español. La evidencia es casi toda de Seedance 2.5: el plan base (Kling Omni-Ref + previz + pista de voz) no tiene respaldo aquí y hay que probarlo.
3. Los ejemplos en inglés de la sección C son redacción mía según el patrón de cada fuente, no citas; el literal está en el archivo citado.

## A. Disco vaquero (lo nuestro)

**Observado en producción** (un solo dato medido)
- Medido: el guion llegó a la v1.21 para 15 s.
- Partir con stills como primer y último frame se comió generaciones en P2 (sin cifra).
- H3 mezcla los movimientos si recibe la ref completa; hay que recortarla a la toma que se copia. También le cuesta la destrucción.
- Seedance y GPT Image bloquean caras de franquicia; Nano Banana las acepta.
- Funcionó calcar la referencia beat a beat y cerrar con un clip aprobado en reversa.

**Opinión (receta no validada como conjunto)**
1. Congelar el guion antes de la primera generación.
2. Sheets de 3 vistas por personaje y guía del escenario.
3. Generar con referencias (Image 1..n + Video 1 recortado), sin first/last por defecto.
4. Personajes propios.

## B. Previz en Blender → video de referencia

| Tema | Regla | Fuente |
|---|---|---|
| Figuras | Tres bloques sin brazos: Blender fija ritmo y cámara, el modelo actúa. El maniquí completo dio movimiento tieso. | ezheng |
| Qué no poner | El modelo copia todo: una puerta muy rápida, una toalla rígida, un salto no pedido. Se arregla el previz, no el prompt. | ezheng, jjj, alessia |
| Props | Dentro del cuadro, con el mismo nombre y una imagen etiquetada con su tamaño. | ezheng |
| Superficie | Gris, sin textura (la textura deja look 3D y pedirlo por texto no bastó) y con caras lisas. | ashizawa, tapehead |
| Color → personaje | Un color plano por figura y un mapa en el prompt (rojo = A). Declarar que el video aporta cámara y puesta en escena, nunca apariencia. | aiehon, pjace |
| Escenario | Bloque "visto desde arriba" con posiciones fijas, o SVG cenital aprobado antes. | aiehon, film_agent |
| Cámara | Se anima en el previz: la cámara de la ref manda sobre el texto. | alessia, comfyui |
| Timing | El susto va en un frame exacto; corregirlo en Blender toma un minuto. | comfyui |
| Duración | Ref de 15 s como máximo en Seedance (partió 13 + 9 s); diálogo de 10–15 s por unidad en H3. | aiehon, film_agent |
| Cortes | Caben en el previz ([S1]…[Sn]; 10–20 planos por corrida), con una línea por plano. | aiehon, ezheng |
| Velocidad y encuadre | A mitad de velocidad, quitando frames después, salió más limpio (H3 fast). De cintura arriba da mejor cara. | ashizawa |
| QA humano | El agente aprobó caras rotas y una pierna extra. Previz cuadro a cuadro, en playblast. | ashizawa, jjj, lavanderia |
| Overlay | Bordes de Blender en rojo sobre las imágenes de ángulo: a ojo 4 de 6 parecían bien; con las líneas, las 6 estaban mal. | ezheng |

**Contradicciones**
- **Detalle de la figura.** Bloques (ezheng) y cilindro para caminatas (alessia) contra maniquí completo (alessia en baile, ashizawa). En jjj el mismo maniquí salió humano en look real y robótico en anime. Inferencia mía: en los zombies la rigidez puede servir.
- **Gris o color.** ashizawa y comfyui piden gris; aiehon y pjace, un color por personaje. Compatible: set gris, figuras de color.
- **Cámara.** Fija (aiehon), movimientos simples (pjace), en mano (second_bassoon).
- **Posición en pantalla.** ezheng la prohíbe en el prompt (le dio pantalla dividida); pjace y davidm bloquean en izquierda y derecha.
- **Largo del prompt.** Más de 6.500 caracteres mató cámara en mano y cortes (ezheng); davidm se limita a 4.000; cAI_works usa ~8.000 (acting §2).

## C. Actuación: técnicas de prompt

| Técnica | Ejemplo (redacción propia) | Fuente |
|---|---|---|
| Línea de tiempo por tramos | `0–1.5s: Martina frozen, eyes on the window slot. 1.5–3s: she whispers "Diego…".` | gilles, manish |
| Objetivo → gesto → negativos | `2–4s. Her goal: confirm it is him. Only her eyes move. No tears, no frown before 4s.` | manish |
| Pausa en segundos y palabra gatillo | `First 2 seconds silent. On "Tú decides" Hugo looks at Martina for the first time.` | limewrite |
| Una línea, una acción | `{Fue un rasguño.} Pulls his sleeve over the wrist.` | godsway |
| Una expresión por toma | `Only change in this shot: Carmen's doubt turns to alarm.` | kling_skill, plantilla |
| Gesto como puntuación | `Between the two sentences Diego swallows and wipes rain from his mouth.` | second_bassoon |
| Reacción del que escucha | `Then the listener, Tomás: goes still, jaw tightens, looks at Martina, not the door.` | davidm, film_agent |
| Cara contenida, ambiente en movimiento | `Faces nearly still; flickering light and swaying handles carry the motion.` | smoermeow |

Otras fuentes: orden estímulo → darse cuenta → respiración → decisión (film_agent) y brief de qué sabe y oculta cada personaje (second_bassoon).

**Trampas**
- Seedance dijo en voz alta palabras de expresión escritas junto a silencios; se indica que solo se habla el diálogo entre comillas (davidm).
- En H3 el lipsync solo deja la cara sin expresión; se agregan acciones faciales (acting, MireilleDartois).
- manish usa negativos por tramo; pjace dice que los negativos se ignoran seguido.

## D. Lipsync y diálogo

**Seedance 2.5**
- davidm: diálogo de ElevenLabs terminado como audio ref, con tres sheets y sin start frames; dos personajes, ~113 s en 5 clips. Funcionó: voces iguales entre clips, diálogo etiquetado por hablante, labios cerrados entre líneas. Su instrucción: «add, change and re-time no words».
- Falló (davidm): parchar voces después; las voces del modelo derivan entre clips; los tags de pausa dan solo ~1,7 s; Whisper no sirve para susurros ni líneas de una palabra, como «Diego…». ~15 USD finales y ~50 de exploración.
- godsway: un recorte corto de voz por personaje como audio ref de todos sus clips. El modelo deduce la voz del sheet aunque se le dé el acento.
- evals y Disco vaquero: rechazó caras claras, incluso de un actor generado. Riesgo para un elenco fotorreal.

**H3 Max**
- techhalla: audio ref de 15 s + una imagen + prompt de 5 planos, con 1 s de solape entre trozos. Es canto de un personaje en Hailuo; sin probar en diálogo ni en fal.
- film_agent: descripción de voz copiada literal en cada unidad.
- evals: la cara no se sostuvo entre planos. overview: `target_audio_url` nunca se probó.

**Kling 4.0**
- Solo diálogo escrito en el prompt con voz nativa: acting §4 y limewrite (japonés), kling_skill (lotes de 10 s).
- evals: su agente esquivó el lipsync en Kling y Seedance.
- Nada sobre audio ref ni previz como video ref.

**Español y hablantes**
- Cero menciones del español; la evidencia es en inglés y japonés. Con pista propia el acento viene del audio; falta saber si las bocas calzan.
- Ningún flujo muestra más de dos personajes hablando con audio ref, y la escena 4 tiene seis.

## E. Continuidad entre clips

- **Cola del clip anterior** como ref de video: últimos 5–15 s (smoermeow) o últimos 10 s más el previz nuevo (ezheng).
- **Frame de continuación:** de los últimos 3 s, sin el último medio segundo (smoermeow). Si no calza con el primer plano del prompt siguiente, falla.
- **Costura:** el arreglo real es cortar a la otra persona; los first frames calzados igual dejaron un salto (davidm). Cada lote termina en la pose inicial del siguiente (kling_skill).
- **Estado del mundo:** un estado por generación, con su hoja. Una herida en el prompt o en la hoja existe desde el frame 1, y las imágenes le ganan al texto (ezheng).
- **Eje:** cláusula de 180° en cada prompt y chequeo de frame por plano (davidm).
- **Hojas:** frente y espalda (jjj); cara, cuerpo con la cara tapada y espalda (kling_skill); sin armas (acting §28); luz visible en la placa y nombrada (acting §15).
- **Contradicción:** Disco vaquero y davidm evitan start frames; eianlu y pjace parten cada clip desde su frame.

## F. Agentes directores

**Cómo se organizan**
- eianlu: el error visible en texto no pasa a imagen, y el visible en imagen no pasa a video. Gates en historia (revisor nuevo que solo ve la historia), frames, prompt con imágenes y film final.
- ezheng: el humano dirige y elige tomas; el agente arma previz y prompts, corta los clips por los tiempos del prompt y entrega un XML.
- limewrite: nota humana → Claude la separa en sentimiento, pausa y ojos → el humano tacha y decide.
- film_agent y kling_skill: pausas para aprobación, lints de prompt, un rol que solo hace cuentas y tope de reintentos.

**Qué advierten**
- ashizawa: Claude Code aprobó una cara rota, una pierna extra y un set con 45 intersecciones.
- evals: el agente dijo que la cara se mantenía y no era así; admite que no escuchó la mezcla.
- acting §15: no dejarle la dirección al agente.

**Cómo lo compensan**
- Chequeos mecánicos: overlay de bordes, lint de largo, transcripción del audio, hoja de contacto de costuras.
- Revisor sin contexto, y agente que lista lo que no verificó.
- Contradicción: eianlu confía en agentes revisores (detectaron una taza 13 % distinta); ashizawa no.

## G. Ideas para este capítulo

| # | Qué cambia | Queja que ataca y por qué | Costo / riesgo | Fuente |
|---|---|---|---|---|
| 1 | Prueba de humo de lipsync en español: una línea, mismo frame y prompt, una toma por motor (Kling Omni-Ref, Seedance) a resolución mínima. | Voces: es el supuesto del plan sin ninguna evidencia | 3–6 generaciones baratas; Seedance puede rechazar la cara | manish, davidm, techhalla |
| 2 | La voz como reloj: pista revisada por transcripción, silencios re-espaciados, trozos de hasta 15 s con 1 s de solape, rol `AUDIO ONLY`. | Voces y tiempos muertos: el ritmo queda fijado en el audio, no lo decide el modelo | Horas de edición, sin generar | davidm, techhalla, pjace |
| 3 | Cámara decidida en el previz y con motivo: frontal a la altura de los ojos dos veces como máximo; cada susto en un frame exacto. | Cámara fija o dolly-in: el texto no logra cambiar la cámara de la ref | Minutos en Blender; copia también los errores | alessia, comfyui, eianlu |
| 4 | Una línea por plano, un cambio por toma, beats con hora de término, prompt de hasta 4.000 caracteres. | Tiempos muertos: el prompt largo congeló cámara y se comió cortes | Cero; obliga a recortar acotaciones | ezheng, kling_skill, pjace |
| 5 | Reacción del que escucha tras cada línea y corte a la otra persona en cada costura; secundarios que reaccionan en secuencia. | Continuidad y slop: tapa el salto entre clips y evita caras congeladas | Cero en generación; más planos de reacción | davidm, film_agent, eianlu |
| 6 | Set gris, figura de color plano por personaje, mapa en el prompt y rol declarado del video. | Continuidad: seis personajes no se confunden ni heredan look 3D | Bajo | aiehon, pjace, ezheng |
| 7 | QA mecánico con humano: previz cuadro a cuadro, overlay de bordes, hoja de contacto. | Continuidad: el agente da por bueno lo roto | Un script; tiempo de Cristián | ezheng, ashizawa, film_agent |
| 8 | Actuación por conducta: pausas dentro del audio; el prompt dice qué hace el cuerpo en el silencio y qué palabra mueve la mirada. | Slop: reemplaza adjetivos de emoción por conducta observable | Cero; el modelo puede "narrar" el prompt | limewrite, second_bassoon, acting §15 |
| 9 | Cola del clip anterior + frame de continuación; un estado por generación con su hoja. | Continuidad: movimiento y estado siguen entre clips | Ocupa cupos de ref; no sé si Kling acepta dos videos | smoermeow, ezheng |
| 10 | Plano difícil primero y a baja resolución; regenerar solo el pasaje que falla. Plan B sin lipsync: voz en off, de espaldas, inserto de manos. | Voces y slop: salida si el lipsync falla | Cero; el plan B cambia la cobertura | smoermeow, eianlu, evals, acting §33 |

**No lo haría en el piloto**
1. **Captura de movimiento o motion transfer** (ashizawa, alessia): más herramientas sin probar, y transfiere rigidez.
2. **Set fotorreal procedural en Blender** (lavanderia): días de trabajo, y la textura empuja a look 3D.
3. **Escena completa de 20–30 s para cosechar ángulos** (pjace, acting §2): multiplica generaciones; el previz ya fija la cobertura.
4. **First y last frame en cada clip** (eianlu): choca con Disco vaquero y con el salto que reporta davidm.
5. **Agente director autónomo o más roles** (evals): los agentes fallan como QA y el proceso ya creció más que el contenido (overview).

## H. Plantilla de micro episodio

**Exige (30 s):** gancho en 0–3 s con acción en curso y pregunta implícita; un beat cada 3–5 s y 7–11 tomas; por toma, una expresión con nombre, una línea como máximo y pose sostenida; secundarios que destapan la contradicción; giro con corte de música; reveal por partes; cierre sin resolver; ep. 2 sin recap y en menos de 24 h.

**Capítulo 1** (inferido solo del overview, que dice 90 s para la v7; el encargo dice ~70 s):

| Exigencia | ¿Cumple? |
|---|---|
| Gancho 0–3 s y reveal por partes | Sí: mano en la ventanita, «Diego…», Diego en la puerta. |
| Cierre abierto | Sí, reforzado por la votación. |
| Densidad | Equivale a 16–26 tomas a 70 s (21–33 a 90 s). El arranque desglosado es más denso (10 planos en ~12 s); sin datos de las escenas 2–5. |
| Una línea por toma | En riesgo en las escenas 4–5: casi todo diálogo y seis personajes. |
| Secundarios y sonido que marcan el giro | No verificable; la v1 no tenía ambiente ni voces propias. |
| Ep. 2 en menos de 24 h | No, por diseño: votación de 48 h más producción. |
| Notas de actuación por toma | No estaban en el YAML al 3-oct. |
