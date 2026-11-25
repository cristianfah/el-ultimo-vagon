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

---

## Sesión del 17 y 18-nov-2026 · el gris con cilindros (prompt 07)

### 2026-11-17 23:50 · retomar · instrucción de Cristián
- Tipo: instrucción de Cristián
- Qué: «Olvida el 06c que te pasé. Este md reemplaza al 06 y al 06c: retoma el piloto del cap. 1 donde quedó, en claude/piloto-cap01, sobre el gris que ya existe, y aplica lo que dice. Personajes como cilindros con nariz, cada uno de su color y nada más; cuerpo y look solo desde las hojas de personaje. Plano secuencia solo si el guion lo pide. Nada pagado sin mi OK.» El md es `07_retomar_piloto_cap01_2026-11-17.md` (Drive del proyecto).
- Lectura: sigue el plan del 05 (gris → PARADA 1 → b5_p7 → PARADA 2). Hoy se llega hasta la PARADA 1. Las respuestas de Cristián a la página 1 están en el 05 (gris: sí; look del rojo: pendiente; fotogramas desde el gris; bandolera: pendiente).
- Quién decidió: Cristián
- Costo: 0

### 2026-11-17 23:55 · P · entorno de esta sesión
- Tipo: decisión
- Qué: esta sesión corre en la nube, no en el Mac. Blender 4.5.16 LTS bajado del sitio oficial (`download.blender.org`) a `/opt/blender`; Mesa (EGL por software) instalado para renderizar sin GPU. ffmpeg 7 del sistema. Workbench: ~0,6 s por cuadro; EEVEE con luz real: ~6–10 s por cuadro a 12–16 muestras.
- Costo: 0
- Repetible: sí (tres comandos; van al manual).

### 2026-11-18 00:05 · P · el motor del gris, versión cilindros
- Tipo: decisión
- Qué cambió en `previz/scripts/` (todo por script, sin tocar las fichas que ya funcionaban):
  - **Cilindros con nariz** (`previz_lib.crear_cilindro`, por defecto en `build_cast.py`; las figuras de bloques quedan con `--bloques`): un cilindro de 0,32 m de diámetro para todos (sin contextura), a la altura real (sentado nace en el cojín), con una nariz (cono más oscuro del mismo color) a la altura de los ojos. Solo posición, giro y mirada: `lean`, `side`, `head_roll`, brazos y bota ya no se dibujan; la acción de manos va al texto.
  - **Luz solo de fuentes del set** (`previz_luz.py`, EEVEE): una luz bajo cada lámpara de lectura encendida, con potencias distintas (1,0 · 0,68 · 0,45); rojo de emergencia a lo largo de cada tira del cielo; **tubo frío sobre la puerta, por dentro, solo en el último vagón** (nuevo en el set); foco duro y frío en el cuarto del rapto (nuevo en el set). Mundo casi negro, sin relleno. **El rojo se ajusta en una línea** (`LUZ["rojo"]`), porque el look del rojo sigue pendiente. Los cilindros emiten su color para leerse igual bajo cualquier luz.
  - **Una cámara por plano con nombre** `CAM_<plano>_<TAG>` y un marcador en cada corte con lente, altura, hacia dónde mira y movimiento.
  - **Marcas fijas en el piso** con el nombre del personaje (`MARCA_<plano>_<personaje>_A/C`): no salen en el cuadro de cámara, solo en la planta.
  - **Datos por cuadro** (`<llamada>_datos.json`): cámara y personajes, para el chequeo y la planta.
  - **Herramientas nuevas:** `storyboard.py` (stills A/B/C desde la cámara real, planta por plano con el recorrido y la cuña de la cámara, chequeo automático y páginas de storyboard de 3300×2550 con paneles 9:16), `cenital.py` y `montaje_gris.py` (película en gris con voces y tabla de ritmo).
  - **Chequeo automático** (`storyboard.py revisar`): tiempos contra `llamadas_tiempos.json`, **nariz a menos de 14° de la cámara = mira al lente**, lados declarados por cuadro (regla de 180°) y cilindros superpuestos. En la c05a del 10-nov ya marcó lo que Kling después hizo mal: el grupo corre con la cara hacia el lente en b5_p2.
- Por qué: 07 (cilindros, stills, páginas, cámaras con nombre) y 05 (luz real, ritmo).
- Quién decidió: agente, sobre las instrucciones del 05 y el 07
- Costo: 0

### 2026-11-18 00:10 · P · colores de los cilindros
- Tipo: decisión (la confirma Cristián en la PARADA 1)
- Qué: un color por personaje sacado de su vestuario (`fichas_personajes_v1.md`), fijo en todos los planos:

| Personaje | Color | De dónde sale |
|---|---|---|
| Martina | avena | suéter de lana |
| Tomás | azul marino | chaqueta acolchada |
| Diego | piedra clara | chaqueta de lona |
| Carmen | celeste | uniforme clínico (el abrigo café lo tiene también Iván) |
| Iván | café oscuro | chaqueta de lona de obra |
| Hugo | bronce | botones del uniforme (el azul marino ya es de Tomás) |
| Hombre de camisa azul | azul fuerte | su camisa, el único azul fuerte del elenco |
| Esposa | beige rosado | chaqueta de punto |
| Figura con máscara | gris liso | la máscara |
| Pasajeros | gris oscuro | — |
| Infectados | casi negro | — |

- Riesgo anotado (07): sin cuerpos en el gris, el modelo puede inventar la contextura. Se mide en la prueba de 4 s; si el cuerpo sale mal, se para y se avisa.

### 2026-11-18 00:15 · P · geografía fija y nombres de muros
- Tipo: decisión (la confirma Cristián en la PARADA 1)
- Qué:
  - **Vagón 2: la pareja pasa al lado derecho (+X)**, fila 12. El guion pide a la esposa a la **derecha del cuadro** en los frontales del bloque 3 (b3_p3, b3_p4, b3_p5), y con la pareja del lado izquierdo (como en la ficha c00a del 10-nov) quedaba a la izquierda. La lectora va al otro lado del pasillo y más hacia la cola (fila 15 izq), para que en b0_p4, que mira hacia la cola, quede «al fondo». Lámparas encendidas del vagón 2: fila 12 der, fila 15 izq y fila 5 der. La toma candidata de c00a no se afecta: el inserto del maletín mira hacia la cola, con el asiento a la izquierda del cuadro, como en esa toma.
  - **Vagón 5:** Martina en la ventana derecha y Tomás en el pasillo, fila 11, con su lámpara encendida encima.
  - **Último vagón:** marcas fijas del grupo después de entrar (Martina a la izquierda de Tomás mirando la puerta; Iván en la puerta; Hugo del lado de la cerradura) y de Diego afuera, frente a la ventanita.
  - **Nombres (07):** en los vagones 2 y 5, «puerta delantera» = hacia la cabeza del tren y «puerta trasera» = hacia el fuelle; «muro de la ventana» = la pared del lado de Martina en su escena y «muro del pasillo» = la del otro lado. En el último vagón hay una sola puerta, «la puerta del último vagón (la del tubo frío)»; al fondo, la pared trasera con la ventana negra y la cabina del revisor.
- Todo esto está en `previz/BRIEF_fichas.md` (el encargo común de los agentes de fichas).

### 2026-11-18 00:20 · 05 paso 1 · c00a i2v
- Tipo: corrección
- Qué: la toma `image_to_video` de c00a (Drive, `tomas_originales/T1_c00a_kling_i2v.mp4`) queda registrada en `tomas.json` como **candidata a final**: le gana a la toma con previz, que tiene los dedos derretidos en la manija del maletín (~3 s).
- Costo: 0 (los 40 créditos ya estaban cobrados el 10-nov)

### 2026-11-18 00:20 · P · fichas de las 17 llamadas con subagentes
- Tipo: decisión
- Qué: siete subagentes en paralelo, uno por grupo de bloques (vagón 2 completo, bloques 0 y 3, en uno solo, para que el inserto del maletín sea el mismo): cada uno escribe sus fichas, mira sus stills, corre el chequeo hasta 0 problemas y entrega notas de layout y planos difíciles. Encargo común en `previz/BRIEF_fichas.md`; tiempos fijos en `previz/llamadas_tiempos.json` (c02 partida en c02a y c02b; duraciones enteras para Kling).
- Costo: 0

### 2026-11-18 00:24 · P · pistas c02a y c02b
- Tipo: decisión
- Qué: el kit (`pistas_v3`) no está en esta máquina. c02a y c02b se derivan de `c02_v2.wav` del repo (recortes 0–5,251 s y 4,20–11,93 s) y se verifican las entradas contra `lectura/04_video_v3.md`: c02a 0,80 · 2,56 s; c02b 0,71 · 3,40 · 5,23 s. Calzan. Solo se usan para el montaje gris; para Kling vale la pista del kit.
- Costo: 0

### 2026-11-18 00:25 · voces · brief corto por personaje (07; hoy solo se escribe)
- Tipo: decisión
- Qué: el brief de voz de cada personaje, para el **AUDIO LOCK** de los prompts. Sale de `biblia/personajes.md` («Cómo habla») y de las voces aprobadas el 18-oct (`produccion/voces.md`). Acento: **chileno suave, de Santiago**; nunca mexicano, neutro ni de España. Las voces de ElevenLabs ya existen: el diálogo del cap. 1 entra como pista (`audio_1`); el brief sirve para que Kling no le invente otra voz en los planos sin pista (respiraciones, gritos) y para el plan B.

| Personaje | Edad | Timbre | Ritmo | Cómo dice su línea clave |
|---|---|---|---|---|
| Martina | 29 | baja, cálida, cansada, algo ronca; casi susurra | responde demasiado rápido cuando miente; si no, casi no habla | «En el baño.»: casual forzado, rápido, sin mirarlo · «No. … Esa era la idea.»: plana, la mandíbula apretada en la pausa |
| Tomás | 31 | media grave, tranquila y educada | pausado; cuando duda baja la voz y se enfría | «¿Dónde estabas?»: curioso con un dejo de sospecha · «¿No estabas en el baño?»: confundido, lento, cayendo en cuenta |
| Diego | 30 | cálida y rasposa | sin aire, se le quiebra el final de las frases | «¡Martina! ¡Martina, ábreme!»: suplicando a través del vidrio · «¡Te vi en el vagón 2!»: sin aire, la voz se le raja |
| Carmen | 54 | cálida pero firme, voz de enfermera | pregunta en vez de ordenar | En el cap. 1 no habla: grito ahogado al chocar con el vidrio y un quejido contenido al cortarse |
| Iván | 45 | grave, seca | frases cortas | En el cap. 1 no habla: respiración fuerte y el esfuerzo al cerrar la puerta y empujar |
| Hugo | 62 | grave y gastada | pausado, de pocas palabras; el silbato antes que la voz | «¡Al último vagón! ¡Rápido!»: grito de autoridad de revisor; la voz se le raja pero manda |

- Plan B si Kling Omni no sostiene la voz o el acento entre planos: grabar cada línea primero con su voz fija (ya está hecho para el diálogo) y reemplazar el audio en el montaje (`flujos/voces_doblaje_tts_primero/`). La guía de voces de PJ Ace (`NOMBRE_voice_v1` + VOICE LOCK) está hecha para Seedance: **no probada**.
- Costo: 0

### 2026-11-18 00:25 · después del piloto · anotado, no se hace ahora (07)
- **Votación:** el bot de métricas propone votar por comentarios («Comenta A o B») y abrir el cap. 2 con «XX % ELIGIÓ…» en la edición, nunca dentro de la imagen, mirando a LINE 9 (serie de terror en un tren nocturno con votación; ~6,5 M de vistas en 8 días según posts de X, sin verificar). **Lo decide Cristián**; hoy la encuesta sigue siendo «Si fueras Martina, ¿lo dejas entrar?».
- **Diferenciarse de LINE 9:** que en los primeros 2 s se vea lo nuestro: personajes con cara y voz.
- **Guion:** gancho en 3 s, giro a los 30–45 s y cierre en pregunta; el cap. 2 abre en la consecuencia, sin recap (`flujos/guion_series_verticales_x/FLUJO.md`).
- **Continuidad automática:** cinewright (plugin de Claude Code, 0 estrellas). No se instala sin que Cristián lo pida. El chequeo de `storyboard.py revisar` ya cubre lo medible (miradas al lente, lados, choques, tiempos).
- **Midjourney:** fondos y refs de look en 9:16, no motor de video; su filtro puede bloquear las manchas.

### 2026-11-18 00:27 · pruebas de 4 s · instrucción de Cristián: Seedance 2.5 draft también
- Tipo: instrucción de Cristián
- Qué: «Usemos seedance 2,5 draft en fal como motor de prueba también». Cambia lo que el 07 dejaba fuera («Seedance/Dreamina… no adoptamos»): Seedance 2.5 entra **como motor de prueba**, al lado de Kling, en las pruebas de 4 s. La ruta del capítulo sigue siendo la del 05 hasta que las pruebas digan otra cosa. Es el motor con el que Kiber Alla probó los cilindros de colores.
- Verificado sin generar (schema y precio de fal, solo lectura):
  - Endpoint: `bytedance/seedance-2.5/us/reference-to-video` con `draft: true` → sale a **480p** (pisa `resolution`) y devuelve un `draft_id`; ese borrador se puede completar a 1080p o 4K dentro de 7 días con `bytedance/seedance-2.5/us/draft/complete`, sin volver a tirar los dados.
  - Entradas: `video_urls` (1,8–30,2 s cada uno; el gris de 4 s sirve), `image_urls` (hasta 30), `audio_urls` (1,8–30,2 s), `duration` de 4 a 30 s (la prueba de 4 s es justo el mínimo), `aspect_ratio: 9:16`, `seed`, `generate_audio`. En el prompt: `@Video1`, `@Image1`, `@Audio1`.
  - Precio: 0,0214 USD por 1.000 tokens (el completado, igual). Estimado de una prueba de 4 s a 480p: **~0,8 USD** solo por la salida; puede acercarse a ~1,6 USD si fal cobra también los tokens del video de entrada (no lo dice el precio publicado). fal no devuelve el cobro por llamada: el real se lee en el panel.
  - Lo ya medido en el piloto: en T1 Seedance siguió el previz de c05a igual que Kling, a 480p; en T0 rehízo la pista de voz y la atrasó (no sirve para diálogo con pista).
- Efecto: cada prueba de 4 s se deja en borrador con dos motores (Kling Omni 720p y Seedance 2.5 draft 480p), cada uno con dos brazos (A: el gris como video de referencia; B: la hoja de storyboard como imagen). **No se corre nada sin el OK de Cristián.**
- Costo: 0

### 2026-11-18 01:23 · P · fichas de las 17 llamadas: resultado de los siete agentes
- Tipo: revisión
- Qué: las 17 fichas (`previz/shots/`) pasan el chequeo automático con **0 problemas**; los únicos avisos son buscados (la embestida de b3_p5–b3_p6: él cae sobre la esposa). c00a y c05a quedaron rehechas para cilindros conservando lo que funcionó el 10-nov (lentes, cámaras, cortes, tiempos).
- Lo que los cilindros no muestran (manos, palma, llave en la mano, ojos blancos, niebla, manchas del vidrio, la mano de Hugo en la manija) va en la `descripcion` de cada plano y después al prompt.
- Correcciones de continuidad que pidió el director durante el armado:
  - **Lados entre los bloques 4 y 5:** en la estampida (b4_p6) Martina va a la izquierda del cuadro; en b5_p2, con la cámara mirando en la misma dirección, estaba a la derecha. Se invirtió en c05a: Martina en −X y Tomás en +X desde b5_p2 hasta las marcas del último vagón.
  - **Infectados en el fuelle:** b5_p8 necesita una mano infectada en la ranura, así que en c05b los infectados revientan la puerta del vagón 5 (fuera de cuadro, durante b5_p6) y entran al fuelle.
  - **Marca de Carmen en el último vagón:** pasa de (0,80; −1,85), que caía dentro del asiento de la fila 1 y la dejaba fuera de los planos cerrados del bloque 7, a (0,05; −2,20), en el pasillo detrás y entre Martina y Tomás. En b7_p3 ahora se ven girar hacia Martina, en orden, Tomás y Carmen; el giro de Iván (junto a la puerta, como dice la tabla) queda fuera de cuadro y va en el texto.
  - **b1_p2:** la ventana de montaje pasa de 1,30–2,30 a 1,60–2,60 s (empieza cuando abre los ojos e incluye el empujón de la puerta; propuesta del agente del bloque 1). Mismo largo en el montaje.
  - **b2_p1:** el set no permitía el plano de dos frontal desde el asiento de enfrente (el respaldo de la fila 10 tapa a la pareja). Se oculta solo ese par de asientos («asiento salvaje», como en un rodaje) y no todo el vagón.
- Cambios del set que salieron del armado (todos por script): asientos por fila y lado (para el asiento salvaje), fuelles cortos y oscuros detrás de la puerta delantera del vagón 5 y de la trasera del vagón 2 (antes se veía vacío), la tercera lámpara del vagón 2 pasa de la fila 5 der a la fila 19 izq (la puerta trasera del bloque 1 quedaba negra; siguen siendo tres lámparas encendidas), colores de los cilindros convertidos a lineal (los infectados salían grises) y el tubo frío más suave (lavaba el vidrio en b5_p9).
- Lentes fuera de la regla general, por la distancia real del set: b2_p3 40 mm, b2_p4 35 mm, b6_p3 32 mm. Los primerísimos planos (b0_p1, b3_p4) quedan más abiertos que en el guion porque el cilindro llenaría el cuadro; el prompt conserva el tamaño del guion.
- Quién decidió: agentes de fichas (encuadres) y director (correcciones de continuidad)
- Costo: 0

### 2026-11-18 01:23 · plano secuencia · no se propone
- Tipo: decisión
- Qué: el guion no pide un plano secuencia. El bloque 5, el candidato natural, está escrito en planos de 1 a 1,5 s con cortes secos; P1 y P6 repiten el encuadre de la cerradura a propósito (la llave es el reloj) y P5 sale de un fotograma guía, así que necesitan cortes. b5_p7 ya es un solo plano corto con la cámara retrocediendo, con su recorrido dibujado en la planta. Un plano secuencia de ~11 s con cinco personas y dos espacios separados por una puerta es justo lo que más rompe el modelo. Por la regla de Cristián («plano secuencia solo si el guion lo pide»), se descarta.
- Quién decidió: director, con la opinión del agente del bloque 5
- Costo: 0

### 2026-11-18 02:13 · P · revisión independiente del gris
- Tipo: revisión
- Qué: un revisor que no armó ninguna ficha revisó las 9 páginas proyectando cada cuadro desde los datos de Blender (no a ojo). El chequeo automático daba 0 problemas en las 17 llamadas, pero tenía puntos ciegos: lados solo en los stills, choques con el set, continuidad entre llamadas y miradas entre 14° y 25° del lente, que en cuadro se leen de frente.
- Hallazgos graves: Diego casi mira al lente durante su línea (b7_p2, b7_p5: 15–17°); Martina y Carmen casi de frente en b7_p3 y b7_p6; la mano de Hugo en la manija de b7_p6 es imposible en esta geometría (la manija queda detrás de la cámara); Iván no puede girarse «detrás de ella» en b7_p3; una ventana detrás de Tomás en b2_p3 (la v10 dice nunca); cilindros que llenan el cuadro en el bloque 2.
- Hallazgos medios: b5_p3 cruza el eje (la huida va a la izquierda y en b5_p1/b5_p6 a la derecha); Iván salta de lado entre b5_p2 y b5_p4; en b5_p2 la cámara ocupa el lugar de Hugo; la puerta del vagón 5 cambia de estado entre c05b y c06a; Carmen atraviesa un asiento en b6_p1; varias miradas casi de frente en momentos clave; Martina al centro en b4_p6.
- Lo que no tiene problemas (verificado con datos): los lados del guion en el vagón 5 y en el último vagón, las miradas que el guion fija, la dirección de pantalla en la huida y en los diálogos, el elenco por bloque, la llave, el tubo frío solo en el último vagón, una sola puerta en el último vagón y el inserto del maletín repetido.
- Efecto: se paran los videos (casi todas las llamadas cambian) y tres agentes corrigen por zona. El chequeo automático ahora también avisa las miradas «casi de frente» (14–22°).
- Decisiones del director, a confirmar por Cristián en la PARADA 1:
  - **b7_p6:** la mano de Hugo en la manija no entra en cuadro; la última mirada de Martina baja hacia la manija, fuera de cuadro abajo a la derecha. (El guion la pide en primer término, desenfocada.)
  - **b7_p3:** solo se giran hacia Martina Tomás y Carmen; Iván, junto a la puerta, no entra en cuadro. Se saca del prompt de ese plano para que el modelo no invente a una cuarta persona.
  - **Puerta del vagón 5:** queda reventada y abierta en los bloques 5 y 6 y se cierra fuera de cuadro antes del bloque 7 (la tabla prohíbe una puerta abierta detrás de Diego).
  - **Maletín:** queda bajo el par de asientos de la pareja, entrando desde el pasillo (en la práctica bajo el cojín de la esposa), para que su esquina se vea desde el pasillo. La tabla dice «bajo el asiento del hombre, por el lado del pasillo». Propuesta de texto para el prompt: «bajo el asiento de la pareja, del lado del pasillo».
  - **b4_p3:** se mantiene la nota del montaje v1c: el medio segundo de negro va en post y el video parte ya en rojo.
- Quién decidió: revisor (hallazgos) y director (correcciones)
- Costo: 0

### 2026-11-18 03:29 · P · correcciones y verificación independiente
- Tipo: revisión · corrección
- Qué: tres agentes corrigieron los hallazgos de la revisión y un verificador escéptico los midió con los datos (no con lo que decían los agentes). Resultado: **14 resueltos**, 1 parcial (el infectado de b5_p9) y 3 que no le tocaba medir. El raccord entre llamadas y los lados del guion quedaron bien en todos los pares y planos.
- Lo que se corrigió después de la verificación (director):
  - **Vidrio de las ventanitas:** salía lechoso bajo el tubo frío y tapaba a Diego y a los infectados (b5_p9). Ahora es oscuro y casi transparente.
  - **b7_p2 y b7_p5:** las sombras (infectados) se acercan para recortarse contra la tira roja del techo del fuelle, y se saca del texto «contra la luz de la puerta del vagón 5», que invitaba a dibujar la puerta abierta y el pasillo iluminado que la tabla prohíbe.
  - **b5_p9:** el infectado choca más al centro de la ventanita.
  - **b2_p3:** el pasajero dormido que parecía salir de la cabeza de Tomás se corre de lugar.
  - **b4_p5:** el pasajero de la fila 19 parte delante de su asiento, no dentro.
  - **c05b:** Carmen sin el salto de 19 cm en el corte de b5_p3 a b5_p4.
  - Textos: b7_p6 dice que Tomás asoma desenfocado en el borde izquierdo; b7_p4, que Martina queda cortada por el borde derecho y nunca mira a cámara; b7_p3 ya no promete la pared trasera (la cámara baja ve el techo).
- Queda anotado, sin cambiar: la marca de Martina en el último vagón roza 10 cm la esquina del asiento de la fila 1 izq (se ve en b6_p1 y b7_p1); algunos infectados miran al lente (b5_p4, b5_p7, b6_p1): el chequeo no les aplica la regla de «nadie mira al lente».
- Quién decidió: verificador (hallazgos) y director (correcciones)
- Costo: 0

### 2026-11-18 05:35 · P · ritmo del gris (05)
- Tipo: revisión
- Qué: el montaje de ritmo (`previz/scripts/montaje_gris.py`; tabla en `previz/ritmo_gris_v1.md`) dura **70,51 s** más la encuesta. Cada plano entra en su ventana de montaje con las voces en su segundo. Va con luz plana (Workbench) para leer el blocking; las referencias de video van con luz real.
- **Todos los planos cumplen «acción + 0,5 s».** No se rellena nada.
- **Líneas que entran más de 0,3 s después del corte (no se tocan sin tu OK):**
  - **b4_p5, Hugo: +0,63 s.** El guion pone el pitazo a los 0,1 s y la voz a los 0,5 s del plano, así que el +0,3 no aplica entero. Propuesta: correr las ventanas de c04b a b4_p4 0,63–2,13 s, b4_p5 2,13–5,13 s y b4_p6 5,13–7,13 s. La voz queda a +0,50 s, como dice el guion, y b4_p4 sigue durando 1,5 s.
  - **b7_p2, Diego: +0,33 s.** Propuesta: cortar de b7_p1 a b7_p2 en 1,33 s en vez de 1,30. b7_p1 pasa a 0,83 s (su acción más 0,5 da 1,1) y la voz queda a +0,30.
- Las otras líneas entran a 0,10–0,30 s del corte. Las que caen dentro de un plano (Martina en b2_p1 y b2_p4) no son entradas después de corte.
- Pendiente del gang: el test en silencio de Métricas sobre `cap01_gris_v1_qa.mp4`.
- Costo: 0

### 2026-11-18 06:06 · PARADA 1 · entrega al Drive
- Tipo: decisión
- Qué: carpeta nueva «piloto_cap01 · avance 2026-11-18 (gris con cilindros · PARADA 1)» dentro de la carpeta del proyecto, con las páginas de storyboard de los 8 bloques (9 JPG), stills A/B/C y plantas por bloque, 6 de los 8 MP4 de referencia con luz real, 6 de las 7 pruebas de 4 s en borrador, la página 2 y este log. Índice: `avance_2026-11-18_drive.md`.
- **No subió (límite de ~3 MB por archivo en la subida desde esta sesión):** el montaje de ritmo (`cap01_gris_v1_qa.mp4` y `cap01_gris_v1.mp4`, 4,4–4,6 MB a 720p), `c06a_ref.mp4` (5,0 MB), `c07a_ref.mp4` (9,0 MB) y la prueba de 4 s de c06a (4,0 MB). Se le pregunta a Cristián cómo los quiere.
- Se para aquí (05: «PARADA 1: sube el gris y muéstraselo a Cristián para que corrija cámara y dirección de arte. No sigas hasta que responda»). No se corrió la prueba de b5_p7 ni nada pagado.
- **Gasto de la sesión: 0 USD y 0 créditos.** Acumulado del piloto: 318 créditos de Kling (saldo 2.858, sin cambios) y ~21 USD de fal estimados (sin cambios).
- Siguiente paso: las respuestas de Cristián a la página 2. Con el OK, la prueba de b5_p7 en GPT Image 2.6 (máx. 2 tiradas, tope 1 USD) desde su cuadro gris; después la PARADA 2.

### 2026-11-25 · pruebas 4s · c05b_2.0-6.0 · formato ORIGINS (borrador)
- Tipo: instrucción de Cristián · decisión
- Qué: prueba pequeña con el formato de prompt de ORIGINS EP. 01: ZARA (Higgsfield Selected, 23-nov): CRITICAL al principio, secciones STYLE/CAMERA/TEXTURE/SOUND/SCRIPT/ASSETS y RECAP al final. Plano: b5_p7, dentro de la ventana c05b 2,0–6,0, con un corte duro en 1,5 s. Las entradas y la semilla son las mismas del brazo A de Seedance. Archivos en `previz/pruebas4s/c05b_2.0-6.0/origins/`.
- Por qué: aislar el efecto del formato contra el brazo A ya escrito.
- No verificado: los prompts de ORIGINS. El hilo de X no se pudo leer y la ficha de Higgsfield no los muestra sin login: el formato sale de la descripción de Cristián.
- Quién decidió: Cristián (encargo) · agente (plano y redacción)
- Modelo / endpoint / setting propuesto: fal `bytedance/seedance-2.5/us/reference-to-video`, 480p, 9:16, 4 s, 1 toma, seed 1019
- Costo: 0 en esta entrada. Propuesto: ~0,98–1,03 USD (precio público de fal leído el 25-nov), tope 1,10 USD. **Sin correr: se espera el OK.**
- Repetible: sí; el payload queda con marcadores `<subir: …>`.
