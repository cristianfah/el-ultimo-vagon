# 02 · Método de producción y de prompting (destilado)

Abreviaturas: **REGLAS** = `kit/REGLAS_PRODUCCION.md` · **GUÍA** = `produccion/prompting/guia_direccion_video.md` · **MÉTODO** = `produccion/metodo.md` · **SKILL** = `.cursor/skills/director-de-prompts/SKILL.md` · **K-REF** = su `references/kling.md` · **K-RES** = `produccion/kling/kling_4_0_resumen.md` · **MCP** = `kit/contexto/kling_mcp_modelos.md` · **PAUTA** = `kit/contexto/local/pauta_look_cap01_v3.md`. «L» = línea.

Orden de mando: REGLAS > MÉTODO §8 > MÉTODO > GUÍA y SKILL > `pipeline.md`, `motores.md` y `agentes/*`.

## A. Prompting de video: lista accionable

1. **Simple no es corto.** Lo que no está escrito, el modelo lo rellena con un promedio. Se parte de la ficha de dirección del bloque; si falta un dato, se pregunta (GUÍA §1, §4; SKILL L8–10, L52).
2. **Emoción como conducta, nunca la palabra** (GUÍA §3): miedo = `breathes short through the nose; her eyes return to the door every two seconds`; mentira = `the answer comes before the question has finished`. Objetivo y obstáculo no se escriben: se vuelven conducta (`produccion/actuacion.md` §1).
3. **Estados, no transiciones; un gesto a la vez:** `at 2.0s her hand is already on her lap, still` (GUÍA §5; `actuacion.md` §5).
4. **Mirada con destino y segundo;** los ojos llegan antes que la cabeza; la reacción empieza antes de que el otro termine (`actuacion.md` §2, §4). Regla 1, **nadie mira a cámara:** `Nobody looks into the lens; every gaze has a target in the carriage.` (`kit/metodos_camara_previz.md` L419).
5. **Manos con tarea física, mano y lado:** `her LEFT hand, on the window side, frame right`. El golpe es cuando la tarea se detiene (GUÍA §5; SKILL L42).
6. **Movimiento no generado** (GUÍA §5): el tren balancea los cuerpos, no la cámara; peso e inercia; la tela responde; microgestos en primeros planos; reacciones de grupo en ola.
7. **Corte de cuadro explícito:** `framed from mid-chest up, hands out of frame` (GUÍA §6).
8. **Ritmo** (GUÍA §10; MÉTODO §8.1–2): acción de 1–1,5 s que empieza en marcha (`at 0.0s he is already lunging`); diálogo = línea + 0,3 s, entra a 0,2–0,3 s del corte; se escribe cuándo termina la acción (`fully crouched by 1.5 s, then still`, solo si la quietud es el beat).
9. **Orden dentro del plano** (SKILL §3): primer fotograma y bloqueo → mapa y fondo → actuación → cámara (frase propia) → física → luz (protegerla: `the red emergency light stays steady`) → sonido y diálogo → candados.
10. **Continuidad** (GUÍA §13; MÉTODO §8.4–5): filas de «Estado del mundo» en positivo (`the briefcase stays under his seat, its metal corner visible, through the whole shot`); detrás de cada vidrio (`behind him only the dark red-lit gangway, no sky, no rain`); objeto sin uso, fuera; cada personaje en cuadro con su hoja.
11. **Diálogo con pista** (GUÍA §12): `Audio 1 is the exact dialogue of this scene: use it as the soundtrack and sync every line to the lips of the speaker. Voices only from Audio 1.` Por línea: `At 0.3s Tomás speaks the first line of Audio 1`. Texto idéntico al guion; entrega física = toma elegida; `Spanish with a soft Chilean accent`.
12. **Formato Kling 4.0** (GUÍA §7; K-REF): `REFERENCES` (un rol por referencia: `identity, face, hair and wardrobe only — [anchors]. Ignore the sheet layout and background.`) → `LOOK` (`Live-action, cinematic, 9:16 vertical.` + lente, fuentes, `Held for the whole clip: …`) → `SHOTS` (`Shot 1 (0.0–X.Xs) — [framing]. Camera: [type, amplitude, speed], [motive]. …`; `Shot 2 — The camera cuts to …`) → `SOUND` (`Dialogue only as sound`) → cierre.
13. **Cierre fijo:** `No music. No subtitles, no captions, no on-screen text.` Candado: `The frame contains no text of any kind; the line exists only as sound` (SKILL L46, L75).
14. **Negativos:** el positivo manda; un «no X» solo para una falla conocida, junto a lo que protege (`prompting/investigacion.md` §4). Lista del repo: `push-in, zoom, dolly, warped hands, extra fingers, morphing faces, text, subtitles, captions, logos, music` (GUÍA L97); el MCP no tiene ese campo (ver E).
15. **Fijos** (SKILL L71–77; MÉTODO §6): prompt completo y cerrado; nunca `blood`/`gore` (`dark red-black stains`); `plain unbranded phone, no notch`; contextura declarada; dos tomas por llamada y, si fallan, se corrige la ficha.

## B. Cámara: reglas vigentes

**Vigente (MÉTODO L106; GUÍA L68 y §11):** sin push-in por defecto, **pero tampoco cámara fija por defecto**. Cada plano lleva tamaño, altura, tipo, amplitud (`small/large`), velocidad (`slow/fast`) y **motivo escrito**. La energía del bloque decide:

| Energía | Gramática | Frase |
|---|---|---|
| 1–2 | Fija o en mano muy suave | `locked off at seated eye height` · `handheld, barely breathing with the actor` |
| 3 | En mano cercana, paneo corto por mirada | `a quick short pan from him to her, because it is what she is looking at` |
| 4 | En mano activa, llega tarde, barridos | `the camera arrives late to the scream` · `a fast whip pan to the rear door` |
| 5 | Dentro de la acción | `the camera runs with them between the seats, bumped by shoulders` |

- **Permitido con motivo:** static, handheld, pan, tilt, truck, track, arc, pull out; push-in solo si la gramática de la escena lo justifica (`.cursor/rules/20-prompts.mdc` L17). En secuencia sí; superpuestos no (`agentes/director_fotografia.md` L25).
- **Vetado:** push-in, dolly-in y zoom no pedidos («delatan la IA»; Control de calidad los rechaza, `control_calidad.md` L32); movimiento sin motivo («se ve generado», GUÍA L198); fondo que se mueve sin motivo; `random shake`; balanceo del tren convertido en movimiento de cámara (GUÍA L126).
- **Siempre:** sin movimiento, escribir `no push-in`; cámara en frase aparte, con altura, distancia y lente.

## C. Prompting de imagen (GPT Image 2.5 y Nano Banana Pro)

- **Siete bloques** (`produccion/plantilla_prompt_rodaje.md` L5–13): `FILM STILL / MOMENT / COMPOSITION / LENS / LIGHT / TEXTURE / FINISH`. Orden de rodaje, no descripción de look.
- **Referencias con rol:** `Image 1 is Martina: match her face, hair and sweater exactly. Image 3 is the reverse shot: match its light.` (`references/imagen.md` L10).
- **MOMENT** = primer instante del plano (mirada con destino, manos con lado). **COMPOSITION** = mapa: qué hay detrás y por cada vidrio. Positivo antes que negativo (`empty aisle`).
- **Frases fijas:** `Only practical sources.` · `Kodak Vision3 500T film scan look, fine organic grain, soft natural micro-contrast, no digital sharpening, no HDR look.` · dónde hay agua y dónde no · foco explícito · sin texto · sujetos en el tercio medio (20-prompts L8–14).
- **Edición de una variable** (imagen.md L16–27): `Edit the image: … CHANGE: … PRESERVE EXACTLY: … ONLY CHANGE: …`. NBP primero, **sobre el original**.
- **Regla 2 (manda):** frame ya editado o con dos cambios = se **regenera** en `openai/gpt-image-2.5/sunburst/edit`, `quality: high`, con el frame como referencia y todos los cambios en un prompt. Fórmula de v1c: `Rebuild this shot clean, in one pass, from Image 1.`
- **Parámetros** (`tools/fal_gen.py`): GPT 9:16 = 1152×2048, `quality: high`; NBP (`fal-ai/nano-banana-pro/edit`) `resolution 2K`, hasta 5 personas. `flare/edit` es el default del script; `sunburst`, para fotogramas clave y regeneraciones.
- **Contraplano:** describir objeto por objeto dónde queda cada cosa (imagen.md L31–32).

## D. Voces

`produccion/voces.md` (aprobadas el 18-oct-2026; ElevenLabs `eleven_v4`, chileno suave). Voice id: Tomás `32TKm2yo0S1caJHTYiFJ` · Martina `v4QCZzj0PB6WaqO3Sn6D` · Don Hugo `nAxzHfcP2MxLUcx3Gzo7` · Diego `qXAGWqslOQWtQyyko9NJ`.

Tomas elegidas (letra según `guion/cap01/cap01_v10.md` L240–248; `generation_id` en `voces.md` L29–38; archivos en `produccion/pruebas/cap01_animatic/voces/`; duración medida con ffprobe):

| Bl. | Línea | Toma | Archivo | Dur. |
|---|---|---|---|---|
| 2 | Tomás «¿Dónde estabas?» | 1C | `tomas_b2_1.mp3` | 1,65 s |
| 2 | Martina «En el baño.» | 2B | `martina_b2_1.mp3` | 1,15 s |
| 2 | Tomás «¿Tu papá sabe que vienes en este tren?» | 3C | `tomas_b2_2.mp3` | 2,51 s |
| 2 | Martina «No. … Esa era la idea.» | 4D | `martina_b2_2.mp3` | 3,08 s |
| 4 | Hugo «¡Al último vagón! ¡Rápido!» | A | `hugo_b4_1.mp3` | 2,35 s |
| 7 | Diego «¡Martina! ¡Martina, ábreme!» | 5C | `diego_b7_1.mp3` | 2,93 s |
| 7 | Diego «¡Te vi en el vagón 2!» | 6C | `diego_b7_2.mp3` | 2,51 s |
| 7 | Tomás «¿No estabas en el baño?» | 7B | `tomas_b7_1.mp3` | 2,27 s |

**Pistas por llamada** (tomas montadas en los tiempos del guion): `kit/contexto/pistas_v3/` y `produccion/pruebas/cap01_animatic_v3/pistas/`. Tiempos internos: `kit/contexto/local/video_v3/prompts_video_v3.md` L225, L272, L813, L872.

| Pista | Dur. | Contenido |
|---|---|---|
| `c02a` | 5,2 s | Tomás 1C a 0,80 s; Martina 2B 2,56–3,20 |
| `c02b` | 7,7 s | Tomás 3C 0,71–2,67; «No.» 3,40–3,68; «Esa era la idea.» 5,23–6,15 |
| `c04b` | 7,55 s | Hugo A a ~2,6 s; pitazo en post a 2,1 s |
| `c07a_v2` | 8,15 s | Diego 5C 1,63–3,95; 6C (off) 5,00–7,06 |
| `c07b_v2` | 6,74 s | Tomás 7B 0,70–2,52 |

**Uso (regla 6):** la pista entera va como audio de referencia **desde el segundo 0** (en Kling, `audio_1` de `omni_ref_video`); el prompt da segundo y hablante de cada línea; entre semillas gana la boca calzada; en el montaje se repone la misma pista en el mismo tiempo. Las cinco duran 5 s o más: cumplen el mínimo de Kling.

## E. Ficha Kling 4.0 por MCP (`who_am_i`, v1.3.3, 9-nov-2026)

| | `omni_ref_video` · `kling-video-v4_0` | `image_to_video` · `kling-video-v4_0` |
|---|---|---|
| Entradas | `image_1..10` (≤30 MB, aspecto 2:5–5:2); `video_1..5` (3–30 s cada uno **y en total**); `audio_1..3` (5–30 s, ≤50 MB); `elements` (≤7, ≤3 de video). Tope combinado: 15 | `first_image`. `tail_image` y `keyframe_1..10` existen, pero la **regla 1 los prohíbe** |
| Argumentos | `prompt`, `duration` 3–30, `aspect_ratio` (pasar `9:16`), `resolution` 720p/1080p, `imageCount` 1–4, `prefer_multi_shots` (**debe quedar true**), `enable_audio` / `keepOriginalSound` (solo uno en true) | `prompt`, `duration` 3–30, `resolution`, `imageCount`, `aspect_ratio` (omitir: sigue al primer fotograma) |
| Sintaxis | `图片1` = image_1, `视频1` = video_1, `音频1` = audio_1. Element: `<<<id>>>` en el prompt y el id en `elements` (`[{"id","bindName","type"}]`, de `element_get`) | Sin tokens: manda el primer fotograma |

- **Archivos:** URL de `file_upload` o pública; nunca ruta local.
- **Cobro:** por segundo, **incluido el video de entrada**. El MCP no da el costo por segundo: se mide con el saldo antes y después (REGLAS L38).
- **NO se puede:** audio, Elements o imágenes de referencia en `image_to_video` 4.0; `negative_prompt` (no existe en ninguna); 4K; apagar `prefer_multi_shots` en omni; semilla (dos tomas = `imageCount: 2`). **Consecuencia:** todo plano con diálogo va por `omni_ref_video`, y ahí el fotograma de previsualización es referencia (`图片N`), no primer fotograma exacto.
- **No verificado:** que `audio_1` suene tal cual como banda sonora con lipsync en español (prueba pendiente, `kit/ESTADO_Y_DECISIONES.md` L56, L106) y qué `enable_audio` conviene; primer fotograma + video de referencia a la vez (REGLAS L19: no se usa sin OK); que `@Image1`/`@Audio1` funcione (el MCP solo documenta `图片N`); el tope de 8.000 tokens (K-RES L20); el multi-shot forzado en llamadas de un plano; Elements + audio juntos; el acento chileno (K-RES L49). El repo no registra Elements creados.
- **4.0 Flash:** 720p, 3–20 s, sin audio de referencia; solo exploración.

## F. Look y dirección de arte

1. Acción práctica bajo la lluvia; **toda luz tiene fuente en el plano**; nada de afiche (`direccion_arte/direccion_de_arte.md` L4).
2. Vagón 2: ámbar bajo, solo 2–3 lámparas de lectura (~2700–3200 K), negro entre lámparas; ventanas negras con reflejo tenue (PAUTA L13–17).
3. Emergencia (vagón 5, fuelle, último vagón): rojo `#B3001B` saturado pero oscuro, medio rostro en sombra; falla si se ve rosado o parejo (PAUTA L19–22).
4. Último vagón: el tubo frío `#E8F1F2` sobre la puerta es la única luz blanca; recorta cabezas, no ilumina el vagón.
5. Ventanita: fuelle oscuro con luz roja; nunca cielo, lluvia ni puerta abierta (PAUTA L23).
6. Cuarto del rapto: gris concreto, cenital blanca dura, cian del monitor; cero ámbar y rojo (PAUTA L25–29).
7. Exterior: azul petróleo `#0E2A33` con sodio `#F28C28`. Sangre casi negra `#1A0505`, seca.
8. Lentes: interiores en mano 24–35 mm a la altura del pecho; reacciones 50–85 mm con poca profundidad.
9. Grano Vision3 500T parejo; negros que caen a negro; piel con poros; sin HDR ni nitidez digital.
10. Señales de IA: simetría perfecta, todo en foco, manos fundidas, texto inventado, rim naranja-azul (PAUTA L10).

**Obsoleto:** la silla con brazos del cuarto del rapto. Vale **la silla aprobada, sin brazos**, con las muñecas juntas con cinta gris sobre los muslos (PAUTA L28); los prompts antiguos de `produccion/pruebas/cap01_animatic/notas.md` no se corren (`…/cap01_animatic_v3/previs/prompts_previs_v1.md` L24). También el F08 con todas las lámparas encendidas (lo reemplaza `F08_v2_ambar_bajo`).

## G. Roles y gates (`agentes/`)

| Rol | Qué hace | Gate |
|---|---|---|
| Showrunner, Guionista | Temporada y capítulo | Cristian aprueba el guion |
| Director | Planos, intención, actuación | Checklist de `actuacion.md` §10 |
| Productor de impacto (borrador) | Gancho, ritmo, picos | Solo propone; decide el Director |
| Director de fotografía | Cámara, lente, luz | Motivo escrito por movimiento |
| Continuista | Hechos, entrada, salida, eje | La salida calza con la entrada siguiente |
| Asistente de dirección | Assets, bloques, motor, costo | Asset no aprobado bloquea el plano |
| Prompter | Compila, no inventa | Revisión de la SKILL; huecos a `alertas` |
| Control de calidad | Revisión previa (`lista`/`vuelve`) y de toma (`aprobada`/`corregir`/`descartar`) | Una corrección por toma; tras 2 fallidas, vuelve a revisión previa |
| Montajista | Plan de montaje | Alertas, no corte cerrado |
| Cristian | Aprueba previsualización, animatic, toma final y gasto | MÉTODO §5, §6.10–12 |

## H. Contradicciones, desactualizado y huecos

**Contra las 7 reglas**
1. **R1, último fotograma:** MÉTODO L24–25 y L75, K-REF L6, `agentes/asistente_direccion.md` L22–26 y `produccion/formato_guion_tecnico.md` L91 lo permiten en insertos; R1 no admite `tail_image`.
2. **R1 + R6:** MÉTODO L40 y GUÍA L215 piden primer fotograma + referencias + Audio 1 en una llamada; por MCP son herramientas distintas (ver E).
3. **R1, mirar a cámara:** ningún checklist del repo lo incluye (SKILL L79–96, GUÍA §9); `references/ejemplo_c01_b02.md` L20 dice `almost grazing the camera`.
4. **R2:** `references/imagen.md` L14 e `investigacion.md` L47 («se edita en vez de regenerar») no limitan el encadenado; MÉTODO L51 y `tools/generar_desde_yaml.py` L24 usan `flare`.
5. **R3:** nada exige paralelismo; `tools/fal_run.py` y `generar_desde_yaml.py` corren una llamada por vez; `fal_gen.py` solo paraleliza entre modelos.
6. **R4:** ningún script lee el cobro real ni tiene tope. H3 a 768p: 0,05 USD/s (MÉTODO L48) contra 0,08 (`motores.md` L27).
7. **R5:** 75–90 s sigue como meta en `AGENTS.md` L9, `.cursor/rules/10-guion.mdc` L9, `agentes/montajista.md` L14 y `formato_guion_tecnico.md` L14.
8. **R6:** `produccion/compilador_prompts.md` L57 dice que el audio «en las pruebas se omite»; GUÍA L82 y `voces.md` L20 tratan `@Audio1` como voz por personaje, «una pista por línea». Mínimo de audio: 5 s (MCP L35) contra 4,9 s (REGLAS L24).
9. **R7:** `README.md` L16–20 indica `git push -u origin main`.

**Entre documentos**
10. **Cámara:** `director_fotografia.md` L19, `impacto.md` L11 («máximo un movimiento por escena») y `prompter.md` L12 mantienen la base fija; MÉTODO L106 y GUÍA L68 la derogan. K-RES L43 cierra su plantilla con `The camera slowly pushes in on [face]`.
11. **Kling desactualizado:** K-RES L6, MÉTODO L57 y `motores.md` L71 dudan de que el MCP exponga 4.0 (ya lo expone). No calzan con el MCP: 4K (K-RES L15), `prefer_multi_shots` en false (L32), llamada de hasta 15 s (MÉTODO L21) y el campo negativo (GUÍA L97, K-REF L10).
12. **Torso:** `average, slightly soft build` (K-REF L11) contra `slim build` (K-RES L26). **Diálogo:** `[Character: …]: "línea"` (K-RES L29) contra `X says in Spanish…` (GUÍA §7). **Acento:** `neutral Latin American Spanish` (`ejemplo_c01_b02.md` L20) contra chileno suave (`voces.md` L14).
13. **Animatic:** 480p en `AGENTS.md` L21, `motores.md` L9 y GUÍA L130; 768p en MÉTODO L48.
14. **Plan vigente:** `README.md` L11 apunta a `cap01_animatic/plan.md`; `AGENTS.md` L22, a `cap01_animatic_v3/plan.md`. La SKILL (L3) depende de `produccion/shotlists/cap01.yaml`, obsoleto según `AGENTS.md` L23.
15. **Voces:** `voces.md` no trae letras de toma ni duraciones y deja a Hugo en «Pendiente» (L38); `pistas/tiempos.json` describe las pistas antiguas, no las `_v2` ni `c02a`/`c02b`.
16. **Luz:** lámpara de 2400 K (GUÍA L112) contra ~2700–3200 K (PAUTA L15).
17. **Silla:** `cap01_v10.md` L258 remite al «prompt listo» de `cap01_animatic/notas.md`, que es el antiguo (ver F).
