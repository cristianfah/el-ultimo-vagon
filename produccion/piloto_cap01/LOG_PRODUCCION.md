# Log de producción · piloto cap. 1

Una entrada por decisión, instrucción o llamada paga. Se escribe en el momento, no al final. Horas en hora de Chile.

## Formato de entrada

```
### AAAA-MM-DD HH:MM · <fase> · <id plano/llamada/tanda>
- Tipo: decisión | instrucción de Cristián | llamada paga | revisión | corrección
- Qué: …
- Por qué: …
- Quién decidió: Cristián | agente | subagente <nombre>
- Modelo / endpoint / setting: … (si aplica)
- Costo: estimado X · real Y (fuente: factura fal / créditos Kling antes→después)
- Resultado: archivo(s) / URL / veredicto contra revision_v1.md §5
- Repetible: sí/no. Si sí, ¿qué entrada fija haría falta para automatizarlo?
```

## Gasto acumulado

| Tanda | Tope (USD fal / créditos) | Estimado | Real | Acumulado fal | Créditos Kling (saldo) |
|---|---:|---:|---:|---:|---:|
| (antes del piloto) | 60 (tope del piloto) | ~13,85 | **sin confirmar** (el historial de fal no entrega montos) | ~13,85 (estimado) | 3.176 (leído el 9-nov-2026, 21:56) |
| T2 | 5 USD | ~3,7 (34 imágenes) | sin dato de fal | ~17,6 (estimado) | — |
| T0 | 4 USD · 150 créditos | 2,2 USD · 120 créditos | **120 créditos** · fal sin dato | ~19,8 (estimado) | **3.056** |
| T1 | 2 USD · 300 créditos | 1,3 USD · 270 créditos | **198 créditos** · fal sin dato | ~21,1 (estimado) | **2.858** |

**Llamadas pagas:** ver las entradas de cada tanda. Créditos de Kling medidos; fal no entrega el cobro por llamada.

---

## Entradas

### 2026-11-09 21:40 · fase (a) · arranque
- Tipo: instrucción de Cristián
- Qué: Cristián entrega `claude_pilot_kit.zip` y `PROMPT_MAESTRO.md`. Encargo: dirigir y producir el piloto del cap. 1; fases (a) a (d) sin generar nada; parar en (d).
- Quién decidió: Cristián
- Costo: 0
- Resultado: kit descomprimido (389 archivos, 7,5 MB). El `PROMPT_MAESTRO.md` del zip es idéntico al adjunto.
- Repetible: sí (descomprimir + verificar).

### 2026-11-09 21:45 · fase (a) · rama
- Tipo: decisión
- Qué: rama `claude/piloto-cap01` creada desde `origin/cursor/assets-v10-5f62` (`1a7c35b`) con `origin/main` (`3af1c19`) mezclado **solo en local**. Mezcla automática, sin conflictos: entraron los cambios de main en `guion/cap01/cap01_v10.md` (12 líneas) y `produccion/pruebas/cap01_animatic_v3/plan.md` (4 líneas). No se tocó `main` ni la rama del PR #14. Nada subido todavía.
- Por qué: regla 7 y fase (a) paso 2.
- Quién decidió: agente (lo pide el prompt)
- Costo: 0
- Resultado: commit de mezcla `a752cbe` (local).
- Repetible: sí.

### 2026-11-09 21:50 · fase (a) · lectura con subagentes
- Tipo: decisión
- Qué: seis subagentes de lectura en paralelo, cada uno con encargo cerrado y un archivo de salida: historia y guion; método y prompting; previs y revisiones; video v3 preparado; lecciones y flujos; binarios (mirando las imágenes). Las reglas, el estado, las herramientas y el aporte del productor los leyó el agente principal completo.
- Por qué: regla 3 (lo independiente va en paralelo) y fase (a) paso 1.
- Quién decidió: agente
- Costo: 0 (solo lectura)
- Resultado: `lectura/01…06_*.md` (carpeta de trabajo, fuera del repo).
- Repetible: sí; los encargos están escritos y sirven para el cap. 2.

### 2026-11-09 21:56 · fase (a) · estado real de las herramientas (solo lectura)
- Tipo: revisión
- Qué se consultó, sin generar nada:
  - Kling MCP `query_membership_and_credits`: plan Pro, **3.176 créditos** (igual que el kit).
  - Kling MCP `who_am_i` (v1.3.3): `omni_ref_video` con `kling-video-v4_0`: duración 3–30 s enteros, 720p o 1080p, `imageCount` 1–4, `prefer_multi_shots` fijo en `true`, `enable_audio` **o** `keepOriginalSound`; entradas `image_1..10`, `video_1..5` (3–30 s), `audio_1..3` (**5–30 s**, ≤50 MB). `image_to_video` con `kling-video-v4_0`: `first_image`, sin entrada de audio. El MCP **no entrega el costo en créditos**.
  - fal (conector MCP, cuenta de Cristián): estado `ready`. `get_pricing`: Kling 4.0 r2v 0,157 USD/s; Seedance 2.5 r2v 0,0214 USD por 1.000 tokens; H3 Max r2v 0,05 USD/s (base 480P); NBP edit 0,15 por imagen; GPT Image 2.5 sunburst edit cobra por «units» (sin precio por imagen en la tabla).
  - fal `get_model_schema`: confirmados los campos que cita el productor (Kling 4.0 en fal sin audio de entrada; Seedance 2.5 con `audio_urls`, mínimo 4 s y sin primer fotograma; H3 con `reference_audio_urls` 2–15 s y `target_audio_url`).
  - fal `search_request_history`: la cuenta se usa en otros proyectos y el historial no trae montos. **No sirve para confirmar el gasto del piloto.**
- Por qué: fase (a) paso 4 y regla 7 del prompt (no inventar parámetros ni precios).
- Quién decidió: agente
- Costo: 0
- Resultado: ver `00_lectura.md`. Pendiente de Cristián: el monto real de fal del 18 y 19 de octubre.
- Repetible: sí (chequeo de arranque de cada capítulo).

### 2026-11-09 21:58 · fase (a) · entorno de esta máquina
- Tipo: revisión
- Qué: en esta máquina **no están** `ffmpeg`, `ffprobe`, Blender ni Homebrew. `FAL_KEY` y `ELEVENLABS_API_KEY` no están exportadas (fal responde igual por su conector MCP con la cuenta de Cristián). `git` y `gh` tienen sesión. Python 3.9.6.
- Por qué: hay que saberlo antes de planificar el previz y el montaje.
- Quién decidió: —
- Costo: 0
- Resultado: va como requisito previo en la fase (d). Nada instalado.
- Repetible: sí (`check_entorno.sh` candidato a script).

### 2026-11-09 22:10 · fase (a) · guion consolidado
- Tipo: decisión
- Qué: `guion/cap01/cap01_v10.md` consolidado. Base: la versión de `main`. De la copia del box entra solo el plano final (unos 2 s, corte al llegar a la manija, ≈1:11,5). Se agregan las decisiones vigentes que ninguna versión tenía: manga del abrigo gris con puño avena en b0_p2, una sola puerta en el último vagón, «nunca un pasillo iluminado» en la ventanita, encuesta decidida, c02a · c02b. La versión del PR #14 no aporta nada propio. 10 cambios; la historia no cambia.
- Por qué: fase (a) paso 3; ESTADO §1 y §3.
- Quién decidió: agente, sobre decisiones ya tomadas por Cristián. Lo revisa Cristián en la fase (d).
- Costo: 0
- Resultado: `produccion/piloto_cap01/guion_v10_consolidado.diff`. Sin commit todavía.
- Repetible: el diff de a pares sí; elegir qué gana, no.

### 2026-11-09 22:30 · fase (a) · resultado de la lectura
- Tipo: revisión
- Qué: seis informes en `produccion/piloto_cap01/lectura/`. Hallazgos que cambian el plan:
  - Las 5 pistas de voz duran 5,2–8,15 s: cumplen el mínimo de `audio_1` en Kling. c02a es la más justa (5,25 s).
  - `omni_ref_video` no tiene primer fotograma; `image_to_video` no acepta audio. Con voz, el encuadre solo se fija con video de referencia.
  - Revisión visual de los 43 cuadros: 11 OK, 18 con observación, 14 por rehacer. Fuera de la lista de siete: b5_p4 y b5_p7 (miran a cámara), b4_p5 (probable), b3_p2, b6_p3, b7_p2, b7_p5. El agente principal miró a ojo b0_p2, b5_p4, b5_p7 y b7_p5 y coincide.
  - Dos informes se contradicen sobre b0_p2. Queda fuera de la lista y se le muestra a Cristián.
  - 38 de 38 URLs de fal vivas. Las hojas no tienen copia en el repo.
  - Gasto del v3 en fal: ~13,85 USD, todo estimado.
  - Ningún flujo del kit probó Kling 4.0 con previz ni con audio de referencia, ni lipsync en español.
- Quién decidió: —
- Costo: 0
- Resultado: `00_lectura.md`.
- Repetible: sí. La revisión visual por agente da falsos OK: siempre con chequeo a ojo de los críticos.

### 2026-11-09 22:40 · fase (b) · instrucción de Cristián
- Tipo: instrucción de Cristián
- Qué: «podemos rehacer las tomas sí, la idea es que quede realmente cinemática, en el control de la cámara, por eso la idea de dirigir la cámara con Blender, con intención de película y la imagen tiene que verse así y no IA slop».
- Efecto: el borrador proponía previz solo en 6 llamadas para ahorrar créditos. Se cambia a **previz en Blender en las 17 llamadas**. El ahorro pasa al número de tomas (2 con voz, 1 + retoma sin voz) y las retomas sin voz van a fal. Se agrega a la propuesta la sección de lenguaje de cámara y la de look. La lista de fotogramas por rehacer sube a 17.
- Lectura del agente: es dirección creativa, **no es el OK de la fase (d)**. No se generó nada.
- Quién decidió: Cristián
- Costo: 0
- Resultado: `01_propuesta.md` y `02_plan.md` reescritos.

### 2026-11-09 23:00 · fase (d) · PARAR
- Tipo: decisión
- Qué: entregados `00_lectura.md`, `01_propuesta.md`, `02_plan.md`, el diff del guion, este log, el manual (secciones 1, 2, 4, 5 y 7) y el banco de ideas. Se espera el OK escrito de Cristián.
- Pendiente antes de subir la rama: esta máquina no tiene identidad de git configurada y el commit de mezcla local quedó con el nombre de la máquina. Se corrige en local antes del primer push (no es force-push: no hay nada subido).
- Costo acumulado del piloto: 0 USD, 0 créditos.

### 2026-11-09 23:10 · fase (d) → (e) · OK de Cristián
- Tipo: instrucción de Cristián
- Qué: «creo que si están instalados, partamos». Responde a la pregunta «¿Das el OK para la preparación sin costo y las tandas T0, T1 y T2?».
- Alcance que leo: preparación (P) + T0 + T1 + T2, con sus topes (11 USD de fal y 450 créditos en total). T3 en adelante sigue sin OK.
- Verificado: Blender 4.5 LTS está en `~/Applications` y hay un ffmpeg 7.1 dentro de Python (`imageio_ffmpeg`). No hay `ffprobe`. El agente había buscado solo en el PATH: error del agente.
- Quién decidió: Cristián

### 2026-11-09 23:15 · T2 · instrucción de Cristián sobre modelos de imagen
- Tipo: instrucción de Cristián
- Qué: «para T2 podemos probar nano banana 2.1 y gpt imagen 2.6. lo que salga más cinemático, si una imagen sale mal podemos hacerle un edit puntual».
- Efecto: en T2 la regla 2 cambia por decisión suya: cada cuadro se genera en `fal-ai/nano-banana-2.1/edit` y en `fal-ai/gpt-image-2.6-sunburst/edit` con el mismo prompt, y gana el más cinematográfico. Se permite **un** edit puntual sobre un cuadro que salió mal (no ediciones apiladas).
- Verificado sin generar: los dos endpoints existen y sus schemas responden. `get_pricing` da «1 USD por unit» sin decir cuántas units cuesta una imagen: el precio por imagen **no se puede saber antes** ni lo devuelve la respuesta.
- Quién decidió: Cristián

### 2026-11-09 23:20 · P · referencias y git
- Tipo: decisión
- Qué: bajadas las 38 referencias aprobadas desde fal a la carpeta de trabajo (171 MB, fuera del repo para no engordarlo; siguen en el Drive). Identidad de git puesta **solo en este repo** (usuario de GitHub de Cristián con correo `noreply`) y el commit de mezcla local corregido con esa identidad. Nada subido.
- Decisión de continuidad (la confirma Cristián en la página 1): Martina lleva la bandolera de cuero café de su hoja en todos los planos.
- Quién decidió: agente
- Costo: 0

### 2026-11-09 23:26 · T2 · b2_p1 · primera llamada de cada modelo de imagen (medir costo)
- Tipo: llamada paga
- Qué: b2_p1 rehecho desde cero, mismo prompt y mismas 5 referencias (cuadro vigente, hoja de Martina, hoja de Tomás, F09, F08_v2) en los dos modelos.
- Setting: `fal-ai/gpt-image-2.6-sunburst/edit` 1152×2048 `quality: high` · `fal-ai/nano-banana-2.1/edit` 9:16 `2K` (salió a 1536×2752).
- Costo: estimado ~0,07 (GPT) y ~0,15 (NB) · **real: no disponible.** Ni la respuesta ni el historial de fal traen el cobro. Pedido a Cristián: leerlo en el panel de fal (peticiones `01a1c30f-9d5b…` y `01a1c30f-9d8e…`).
- Resultado: **gana GPT Image 2.6.** Dejó tres lámparas con negro real entre ellas, banca sin apoyabrazos al medio, bandolera y pelo de Tomás como la hoja. Nano Banana 2.1 casi no cambió el cuadro original: siguen las 7 lámparas, el relleno en las caras, el apoyabrazos y el pelo engominado. Archivos: `t2/b2_p1/`.
- Repetible: sí.

### 2026-11-09 23:29 · T0 · c02a · Kling 4.0 Omni-Ref con `audio_1` (medir costo)
- Tipo: llamada paga
- Qué: prueba de lipsync, brazo Kling. 2 tomas (`imageCount: 2`), 6 s, 720p, 9:16, `enable_audio: true`. Referencias: b2_p1 nuevo (composición), hoja de Martina, hoja de Tomás. `audio_1`: `c02a.mp3` (5,25 s).
- Costo: estimado 120 créditos · **real 120 créditos** (saldo 3.176 → 3.056, leído antes y después). **10 créditos por segundo de salida a 720p**, sin video de entrada. El audio de referencia no sumó cobro.
- Resultado: en curso.
- Repetible: sí.

### 2026-11-09 23:33 · T0 · c02a · H3 Max 768P y Seedance 2.5 480p
- Tipo: llamada paga
- Qué: H3 con el payload ya preparado del v3 (2 semillas, 5,2 s, primer fotograma = b2_p1 nuevo, pista como audio de referencia). Seedance con la misma pista en `audio_urls`, 6 s, 1 toma.
- Costo: estimado ~0,9 USD (H3) y ~1,3 USD (Seedance) · real: pendiente.
- Resultado: en curso (lo corre un subagente corredor con los payloads cerrados).

### 2026-11-10 00:05 · T0 · resultado de la prueba de lipsync en español
- Tipo: revisión
- Qué se midió (script `scripts/medir_lipsync.py`, misma pista `c02a` en los tres motores):

| Toma | Correlación con la pista | Desfase | Boca del que habla / del que calla | Veredicto |
|---|---:|---:|---|---|
| Kling 4.0 Omni, toma 1 | 0,987 | 0,00 s | calza | pista intacta; Martina mira a Tomás (no debía) |
| **Kling 4.0 Omni, toma 2** | **0,992** | **0,00 s** | **calza: Tomás habla con Martina callada, y al revés** | **gana** |
| H3 Max 768P, semilla 1019 | 0,982 | 0,00 s | calza, boca exagerada | conserva la pista; luz más pareja, la marca sale como pulsera |
| H3 Max 768P, semilla 7342 | 0,986 | 0,00 s | igual | igual |
| Seedance 2.5 480p | 0,629 | +0,63 s | **Tomás con la boca cerrada en su línea** | **falla**: rehízo y atrasó la pista. No rechazó las caras |

- Decisión del agente (la confirma Cristián en la página 1): **el diálogo va en Kling 4.0 Omni-Ref con `audio_1`.** H3 a 768P queda de respaldo. Seedance, descartado para diálogo.
- Costo real: Kling 120 créditos (medido). fal: H3 ×2 y Seedance ×1 corridos; **fal no devuelve el cobro** (estimado ~0,9 + ~1,3 = 2,2 USD; tope 4).
- Observación para T3: Kling abrió el encuadre respecto de la imagen de referencia (cuerpo entero en vez de rodillas arriba). Sin primer fotograma, el encuadre lo tiene que fijar el previz.
- Resultado: `tomas.json` (5 tomas con su medición); comparativo `pagina1/T0_lipsync_lado_a_lado_pista_limpia.mp4`.
- Repetible: sí, entero. La medición es un script; las cajas de boca hoy se ponen a mano mirando un cuadro.

### 2026-11-10 00:20 · T2 · comentario de Cristián sobre la referencia
- Tipo: instrucción de Cristián
- Qué: «quizás usar la misma foto como referencia no sirve para generar un nuevo render de las imágenes».
- Efecto: las 32 imágenes ya estaban enviadas con el cuadro viejo como Imagen 1 y se dejaron correr para medir cuánto copia cada modelo. Los cuadros que haya que repetir van **sin la foto vieja**: composición con el cuadro gris de Blender del plano, más hojas y plancha de set.
- Quién decidió: Cristián (la idea), agente (cómo aplicarla).

### 2026-11-10 00:45 · T2 · 16 cuadros × 2 modelos (32 imágenes)
- Tipo: llamada paga
- Qué: los 16 cuadros restantes, mismo prompt en `fal-ai/gpt-image-2.6-sunburst/edit` (1152×2048, high) y `fal-ai/nano-banana-2.1/edit` (9:16, 2K). Prompts escritos por dos subagentes (`t2/prompts_A.json`, `prompts_B.json`), corridos por dos subagentes corredores con payloads cerrados. 32 de 32 terminaron, sin rechazos.
- Costo: estimado ~3,5 USD (16 × 0,07 + 16 × 0,15) · **real: fal no lo devuelve.** Acumulado estimado de T2: ~3,7 USD de un tope de 5.
- Resultado, mirado por el agente en las comparaciones lado a lado:
  - **GPT Image 2.6 gana en 16 de 17.** Reconstruye la luz (2–3 lámparas con negro real; rojo sin relleno), corrige miradas y lados, y respeta la composición. Nano Banana 2.1 gana solo en b1_f1 (cenital más duro en el flash del rapto).
  - Nano Banana 2.1 tiende a quedarse con el cuadro de referencia: mantuvo las lámparas de más (b2_p1, b2_p4, b3_p1, b4_p1), dejó a Diego mirando al lente (b7_p2), un pasillo iluminado con siluetas detrás de Diego (b7_p5) y una segunda puerta en el fondo (b6_p2).
  - Corregido en los elegidos: maletín bajo la banca (b3_p1, b3_p2), hombre sentado (b3_p2), Tomás en su asiento (b2_p4), Carmen y Tomás ya no miran a cámara (b5_p4, b5_p7), Diego con la manga derecha manchada y la izquierda limpia y solo fuelle oscuro detrás (b7_p2, b7_p5), palma abierta de Carmen (b6_p2), fondo del último vagón sin segunda puerta (b6_p3).
  - Dudas que quedan para el segundo revisor: color de las manchas en la mano de Carmen (b5_p4) y en la manga de Diego (se ven algo rojas), uñas de la mano infectada (b5_p8), qué mano toca el vidrio en b7_p5.
- Archivos: candidatos en `t2/<id>/`, elegidos en `t2/elegidos/`, mapa con URL en `t2/elegidos.json`, hojas en `pagina1/T2_fotogramas_antes_despues_{1,2}.jpg`.
- Repetible: el envío, la descarga y las hojas, sí (ya son scripts o encargos cerrados). Elegir entre dos candidatos, no.

### 2026-11-10 00:55 · P · instrucción de Cristián: dónde parar
- Tipo: instrucción de Cristián
- Qué: «detente justo antes de comenzar la película en gris de las 17 llamadas».
- Efecto: se termina el previz de c05a y c00a y la prueba de cámara (T1). **No se construye el previz de las otras 15 llamadas ni el montaje gris** hasta que Cristián lo pida. La página 1 sale con T0, T1 y T2.
- Quién decidió: Cristián

### 2026-11-10 01:20 · P · previz en Blender de c05a y c00a
- Tipo: decisión
- Qué: un subagente construyó el motor de previz por script (set del tren en bloques, elenco de tres bloques con color por personaje, cámara con lente y sensor reales, cortes secos por marcador, temblor de cámara en mano, vaivén del tren) y rindió c05a (5 s) y c00a (4 s). Render de ~10 s por llamada.
- Revisión del agente: c05a se lee bien en gris. c00a es flojo: el primerísimo plano a 85 mm es una esfera roja sin información, y el «bajo el asiento» del inserto se lee a medias.
- Costo: 0
- Resultado: `previz/scripts/` y `previz/shots/{c05a,c00a}.json` en el repo; videos y hojas en la carpeta de trabajo (`previz/out`, `previz/qa`).
- Repetible: sí, todo por script desde la ficha JSON. La ficha (cámara y blocking) es lo creativo.

### 2026-11-10 01:35 · T1 · prueba de cámara · costos medidos en Kling
- Tipo: llamada paga
- Qué y costo real (saldo antes 3.056; el MCP ahora devuelve `creditsConsumed` en cada envío):

| Llamada | Setting | Créditos | Por segundo de salida |
|---|---|---:|---:|
| c05a con previz | Omni-Ref 720p, 5 s, `video_1` de 5 s, 8 imágenes | **60** | **12** |
| c05a sin previz | Omni-Ref 720p, 5 s, 8 imágenes | 50 | 10 |
| c00a con previz | Omni-Ref 720p, 4 s, `video_1` de 4 s, 4 imágenes | 48 | 12 |
| c00a primer fotograma | `image_to_video` 720p, 4 s | 40 | 10 |

- **Hallazgo de costo:** con un previz de la misma duración que la salida, Kling cobra **12 créditos por segundo de salida, no 20.** El plan suponía que el video de entrada doblaba el cobro. El previz encarece 20 %.
- Con eso, la ruta completa (17 llamadas con previz) cuesta ~1.140 créditos por toma: dos tomas de todo el capítulo son ~2.280.
- Total T1 en Kling: 198 créditos (tope 300).

### 2026-11-10 01:50 · T2 · segunda revisión independiente de los 17 fotogramas
- Tipo: revisión · corrección
- Qué: un segundo revisor, sin ver el veredicto del agente, miró los 17 elegidos a resolución completa con recortes de manos, caras y llaves. **Resultado: 5 OK, 7 con un edit puntual, 5 por rehacer.** El agente los había dado por buenos mirando las comparaciones reducidas: **falso OK del agente en 12 cuadros.**
- OK: b1_p1, b2_p1, b3_p1, b4_p1, b4_p4.
- Edit puntual (una corrección cada uno): b1_f1 (recortar: se ve boca y mentón), b2_p3 (anteojos rectangulares), b2_p4 (bolso de la bandolera del lado equivocado), b3_p2 (a la esposa le falta media pierna), b5_p8 (uñas parejas), b6_p3 (manga sin mano), b7_p2 (gotas de agua en la puerta).
- Rehacer: b4_p5 (Hugo casi mira al lente; llave malformada), b5_p4 (sangre roja y brillante; la mano se lee izquierda), b5_p7 (acolchado en rombos; Carmen con dos pares de anteojos), b6_p2 (la mano es anatómicamente izquierda), b7_p5 (un solo brazo: la manga manchada termina en la mano del vidrio).
- Hallazgo transversal: en los cuadros rojos, la luz roja tiñe el set pero no la piel ni la ropa (se leen con luz neutra). Es el mismo look del KF02 aprobado; **es una decisión de look para Cristián.**
- Decisión del agente: **no se corren los arreglos todavía.** Los 5 por rehacer piden composición nueva (con cuadro gris de Blender, según lo conversado), y eso es parte de lo que Cristián pidió no empezar. Los 7 edits puntuales esperan su visto bueno. T2 queda en ~3,7 USD estimados de 5.
- Lección para el manual: la revisión visual de un solo agente sobre imágenes reducidas no sirve. Siempre segundo revisor con recortes a resolución completa y preguntas de lado concretas.
- Resultado: `revision/T2_revision_2_fotogramas.{md,json}`.

### 2026-11-10 02:10 · T1 · resultado de la prueba de cámara
- Tipo: revisión
- Qué: comparación cuadro a cuadro del previz contra cada toma.
  - **Kling con previz (c05a):** sigue los tres encuadres, el lente y los cortes del previz en el mismo cuadro. Fallas: un tubo blanco en el plano 2 que nadie pidió, y Carmen grita hacia el lente al final del plano 3.
  - **Kling sin previz (c05a):** el fuelle se alarga y se ilumina de más, el grupo corre de frente al lente y Tomás aparece duplicado.
  - **Kling con previz (c00a):** primerísimo plano de ojos y corte al inserto en el cuadro del previz. El primer plano sale del cuadro de look, no de la esfera gris.
  - **Seedance con previz (c05a, 480p):** también sigue encuadres y cortes. No rechazó las caras. No mejora a Kling.
  - **Kling `image_to_video` (c00a):** enviado (40 créditos) y **sigue en cola** al cerrar; sin resultado.
- Decisión propuesta (la confirma Cristián): previz en todas las llamadas con geografía o blocking; en primerísimos planos el previz solo fija lente y corte.
- Costo: Kling 198 créditos (medido). Seedance ~1,3 USD estimado (fal no devuelve el cobro).
- Resultado: `tomas.json` (10 tomas), comparativos en `pagina1/T1_*.mp4`.

### 2026-11-10 02:15 · PARAR · antes de la película en gris
- Tipo: decisión
- Qué: T0, T1 y T2 corridas. Se para aquí por instrucción de Cristián. Entregada `pagina_1.md` con cuatro decisiones pendientes.
- Acumulado: **318 créditos de Kling** (saldo 2.858, medido) y **~7,2 USD de fal estimados** (T0 ~2,2 · T1 ~1,3 · T2 ~3,7), dentro de los topes (450 créditos y 11 USD). Acumulado de fal del piloto con lo anterior: ~21 USD estimados de 60.
- Pendiente: el cobro real de fal (panel) y la toma de `image_to_video` en cola.

### 2026-11-10 02:30 · cierre del día · dónde retomar
- Tipo: instrucción de Cristián
- Qué: «súbelo al repo y seguimos mañana». Rama `claude/piloto-cap01` subida a `origin` (push normal, sin force, sin PR todavía).
- Estado: fases (a) a (d) cerradas; de la fase (e), corridas T0, T1 y T2. Detenido antes de la película en gris de las 17 llamadas.
- Para retomar:
  1. Decisiones pendientes de Cristián, en `pagina_1.md`: seguir con la película en gris; look del rojo en las caras; correr los 7 edits puntuales; bandolera de Martina.
  2. Toma de control `T1_c00a_kling_i2v` en cola en Kling (40 créditos cobrados). Consultarla con su `generationId` de `tomas.json` y bajarla apenas termine: la URL vence en 24 h.
  3. Cobro real de fal de T0, T1 y T2: solo en el panel de fal (Usage).
  4. Los videos, fotogramas candidatos, referencias bajadas y renders de previz **no están en el repo**: viven en la carpeta de trabajo de la sesión (`trabajo/`). Lo que se elija como toma o fotograma final se copia al repo y al Drive en la entrega.
- Saldo de Kling: 2.858 créditos. fal del piloto: ~21 USD estimados de 60.

### 2026-11-10 02:40 · avance al Drive del proyecto
- Tipo: instrucción de Cristián
- Qué: «sube a drive para que los bots revisen el avance». Carpeta nueva dentro del Drive del proyecto: `piloto_cap01 · avance 2026-11-10 (T0, T1, T2)` (id `1FEH1t-U7G8SJWa422ioh23kPJ2YbWClO`).
- Contenido (26 archivos): `00_LEEME.md` con qué mirar y qué revisar, la página 1, el log, `tomas.json`, 4 videos comparativos, 2 hojas de antes y después, 6 zips (fotogramas elegidos y comparaciones en dos partes cada uno, mediciones de lipsync con la pista, previz) y la subcarpeta `tomas_originales/` con las 9 tomas.
- Límite encontrado: el conector de Drive admite ~7 MB por archivo (10 MB de carga en base64). Por eso los zips van partidos y `T1_c05a_kling_previz` subió recodificada (x264 crf 17, audio intacto); el original de 7,6 MB queda en la carpeta de trabajo.
- Quedó un `zz_LEEME_v1_obsoleto.md` (la primera versión, renombrada; el conector no permite reemplazar el contenido de un archivo). Se puede borrar.
- No subido: los PNG originales de los fotogramas (van en JPEG 95), los candidatos descartados, las 38 referencias aprobadas (ya están en el Drive) y los cuadros sueltos del render de previz.
- Costo: 0
- Repetible: sí. Armar el paquete es un script; la subida es una llamada por archivo y pide aprobación en cada una.
