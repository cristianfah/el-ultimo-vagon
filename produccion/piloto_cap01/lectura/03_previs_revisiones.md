# 03 · Previs, revisiones y gasto · cap. 1

Lectura del 9-nov-2026. Solo lectura: no se generó nada. Rutas relativas a `el-ultimo-vagon/` (rama `claude/piloto-cap01`) o al kit (`KIT/`). `revision_v1.md` del repo y la copia del kit (`contexto/local/v10_trabajo/`) son idénticas byte a byte.

## A. Lista de fallas (§5 de `revision_v1.md`, textual)

Encabezado original: «Cada bot revisa su entrega contra esta lista **antes** de entregarla: el director revisa la previsualización, el productor los prompts, último vagón cada toma y el montaje, y Métricas el corte completo. Si un punto falla, se corrige antes de que llegue a Cristian.» La numeración es mía; el texto es el del archivo.

**Ritmo**
1. [ ] Ningún plano dura más que su acción más 0,5 s (salvo un silencio escrito en el guion).
2. [ ] Cada plano empieza con la acción ya en marcha.
3. [ ] Ninguna línea de diálogo entra más de 0,3 s después del corte, salvo una pausa escrita.
4. [ ] No hay cuadros congelados para estirar un plano. Si falta duración, se regenera.
5. [ ] En los bloques de acción, los planos duran entre 1 y 1,5 s.

**Cámara y encuadre**
6. [ ] Cada plano tiene tamaño, altura, tipo de cámara y motivo, y la toma los cumple.
7. [ ] Los ejes de mirada se respetan: quien mira a alguien que está a la izquierda, mira hacia la izquierda.
8. [ ] Se respeta la regla de los 180°: Martina a la izquierda de Tomás.

**Continuidad (contra «Estado del mundo»)**
9. [ ] Los props están donde dice la tabla en cada plano (el maletín no cambia de lugar ni desaparece).
10. [ ] Detrás de cada vidrio se ve lo que dice la tabla. **Por la ventanita nunca se ve cielo ni lluvia.**
11. [ ] Heridas, manchas y ropa mojada, del lado correcto y desde el plano correcto.
12. [ ] Ningún personaje aparece de la nada: si entra, se ve de dónde viene.
13. [ ] Cada causa se ve antes que su efecto (el vidrio roto antes de la herida, el infectado antes del ataque).

**Actuación y diálogo**
14. [ ] La entrega física de cada línea coincide con la toma de voz elegida (tabla de voces del guion).
15. [ ] Nadie mira la nada: cada mirada tiene destino.
16. [ ] En un grupo, las reacciones van en ola, no todas a la vez (salvo que el guion lo pida).
17. [ ] Las manos que sostienen algo lo hacen de forma natural, o el objeto no está.

**Montaje**
18. [ ] Se cortó en la acción y en los cortes reales de la toma, no en los tiempos del plan.
19. [ ] Los flashes y los saltos de lugar tienen un motivo visible (corte por coincidencia, sonido, mirada).
20. [ ] Prueba sin sonido: Métricas confirma que se entiende quién hace qué y por qué.

Regla que la acompaña (§1): «Un error de esta lista que llegue a Cristian es un error del proceso, no del modelo.»

## B. Feedback de Cristián por prueba

Ningún archivo trae citas literales entre comillas salvo «IA slop»; lo demás es la redacción de quien tomó la nota.

**Montaje v1 (30-sep, `cap01_montaje_v1/feedback_proceso.md`).** Es feedback de proceso, no de contenido.
- Lo que se vio: «planos quietos. Con la cámara quieta se nota más la IA y el reel pierde atención»; «Martina dice «Diego…» sin intención. En la pareja, ella nunca mira a Tomás»; fondo que se mueve sin motivo; Hugo agachándose dura más que la acción.
- Sus decisiones: «No se trata de generar hasta que salga. Todo tiene que estar definido antes de generar»; «Los prompts son muy cortos.»

**Montaje v2 (3-oct, `cap01_montaje_v2/feedback_montaje_v2.md`).**
- «Está mucho mejor que la v1, pero los fondos y los personajes se ven "IA slop", con ese grano típico.»
- «El dolly in en todos los planos no ayuda y hace que todo se vea generado por IA. No impacta, así que no sirve como gancho.»
- Martina «literalmente pegada al vidrio» y dice «Diego» «sin ninguna expresión»; en la pareja «no se siente tensión»; él «mira hacia un lado, a la nada»; clips de presentación «muy largos»; Hugo «se agacha sin ningún motivo».
- Meta: «que el reel se vea de alta producción, con todos los detalles cuidados».

**Animatic v1 y v2 (18-oct, `revision_v1.md` §1–§2).**
- Veredicto: «la historia se entiende. Pero falta mucha dirección de cámara y de encuadres, muchos planos quedan mal cortados y el ritmo no es frenético. Los personajes esperan mucho tiempo muerto antes de hablar y, con las voces puestas, la intención de los prompts no calza con lo que dicen.»
- Por bloque: gancho «solo una cámara fija»; flashes «sin razón»; bloque 4 «no hay gancho, el ritmo es muy lento»; «el señor cerrando dura mucho»; «aparece un zombie de la nada»; entran «muy lento… como si nada pasara»; Diego «sin actuación y sin peligro. Se ve llover al fondo»; la gente mira «como robots»; la línea de Tomás «tarda demasiado».

**Previs v1 / v1b (18-oct).** Aprobó a las 22:45 (después de la parte A, v1b) y pidió la parte B más siete arreglos. No hay palabras suyas escritas. Lo único atribuido: b7_p6 «~2 s, mira a Tomás y luego a la manija; corte justo al llegar a la manija, sin el segundo extra» (`tiempos_montaje_v3.json`) y el puño avena de b0_p2 (`plan.md`).

**Previs v1c (19-oct).** Hubo una corrección suya a mitad de la corrida (no apilar ediciones, piel «crujiente», banca compartida en b2_p4: «el asiento de b2_p4 era individual»). No encontré su veredicto sobre el corte v1c terminado.

**Patrón.** (1) Cámara por defecto, sea fija (montaje v1, animatic v1) o dolly-in (v2): «se nota la IA». (2) Planos más largos que su acción y esperas antes de hablar. (3) Actuación sin intención, miradas a la nada, voces que no calzan con el gesto. (4) Continuidad y geografía: vidrios, props, lados, personajes que aparecen de la nada. (5) Textura «IA slop». (6) Proceso: definir antes de generar, no iterar hasta que salga.

## C. Los 43 planos del montaje v3 (`tiempos_montaje_v3.json`)

Total 70,5 s. 16 llamadas más F3 (imagen fija). «Pedida» es la duración de la llamada completa (colchón de 0,5 s por lado). Fotograma: `v1c` = `previs/v1c/frames/`, `v1` = `previs/frames/` (regla de `monta_previs_v1c.py`). SB = regenerado en sunburst; ED = edición NBP o flare.

| Plano | Bl. | Llamada | Montada s | Pedida s | Res. | Diálogo | Fotograma vigente |
|---|---|---|---|---|---|---|---|
| b0_p1 | 0 | c00a | 1,2 | 4,0 | 480P | — | v1c · ED V14 t1 |
| b0_p2 | 0 | c00a | 1,8 | 4,0 | 480P | — | v1c · SB t2 |
| b0_p3 | 0 | c00b | 1,5 | 4,0 | 480P | — | v1c · SB t0 |
| b0_p4 | 0 | c00b | 1,5 | 4,0 | 480P | — | v1c · ED V07 |
| b1_p1 | 1 | c01 | 0,8 | 3,5 | 480P | — | v1 · original |
| b1_f1 | 1 | c01f | 0,7 | 2,5 | 480P | — | v1c · recorte local |
| b1_f2 | 1 | c01f | 0,7 | 2,5 | 480P | — | v1c · ED V15 |
| b1_f3 | 1 | F3 (fija) | 0,8 | — | — | — | v1 · asset PANTALLA |
| b1_p2 | 1 | c01 | 1,0 | 3,5 | 480P | — | v1 · original |
| b2_p1 | 2 | c02 | 3,2 | 11,9 | 768P | Tomás 1C + Martina 2B | v1c · ED V19 |
| b2_p2 | 2 | c02 | 1,0 | 11,9 | 768P | — | v1c · ED V16 t1 |
| b2_p3 | 2 | c02 | 2,7 | 11,9 | 768P | Tomás 3C | v1c · ED V17 (flare) |
| b2_p4 | 2 | c02 | 4,0 | 11,9 | 768P | Martina 4D | v1c · SB t0 |
| b3_p1 | 3 | c03a | 1,3 | 6,0 | 480P | — | v1c · SB t0 |
| b3_p2 | 3 | c03a | 1,5 | 6,0 | 480P | — | v1 · original (V04 marcado) |
| b3_p3 | 3 | c03a | 2,2 | 6,0 | 480P | — | v1c · ED V08 |
| b3_p4 | 3 | c03b | 1,5 | 5,0 | 480P | — | v1c · ED V13 |
| b3_p5 | 3 | c03b | 1,0 | 5,0 | 480P | — | v1c · ED V09 |
| b3_p6 | 3 | c03b | 1,5 | 5,0 | 480P | — | v1c · SB t1 |
| b4_p1 | 4 | c04a | 1,8 | 5,5 | 480P | — | v1c · ED V20 t0 |
| b4_p2 | 4 | c04a | 1,5 | 5,5 | 480P | — | v1 · original |
| b4_p3 | 4 | c04a | 1,2 | 5,5 | 480P | — | v1 · original (+0,5 s negro en post) |
| b4_p4 | 4 | c04b | 1,5 | 7,5 | 768P | — | v1 · original |
| b4_p5 | 4 | c04b | 3,0 | 7,5 | 768P | Hugo A | v1 · original |
| b4_p6 | 4 | c04b | 2,0 | 7,5 | 768P | — | v1c · SB t0 |
| b5_p1 | 5 | c05a | 1,3 | 4,8 | 480P | — | v1c · ED V23 |
| b5_p2 | 5 | c05a | 1,5 | 4,8 | 480P | — | v1c · ED V24 t1 |
| b5_p3 | 5 | c05a | 1,0 | 4,8 | 480P | — | v1 · original |
| b5_p4 | 5 | c05b | 1,5 | 5,2 | 480P | — | v1c · ED V25 |
| b5_p5 | 5 | c05i | 1,0 | 2,0 | 480P | — | v1c · ED V26 |
| b5_p6 | 5 | c05b | 1,5 | 5,2 | 480P | — | v1c · SB t0 |
| b5_p7 | 5 | c05b | 1,2 | 5,2 | 480P | — | v1c · ED V32 |
| b5_p8 | 5 | c06a | 1,3 | 5,3 | 480P | — | v1c · SB t0 |
| b5_p9 | 5 | c06a | 1,0 | 5,3 | 480P | — | v1c · ED V31 |
| b6_p1 | 6 | c06a | 2,0 | 5,3 | 480P | — | v1c · SB t0 |
| b6_p2 | 6 | c06b | 1,5 | 4,5 | 480P | — | v1c · SB t0 |
| b6_p3 | 6 | c06b | 2,0 | 4,5 | 480P | — | v1c · SB t0 |
| b7_p1 | 7 | c07a | 0,8 | 8,1 | 768P | — | v1c · SB t0 |
| b7_p2 | 7 | c07a | 3,6 | 8,1 | 768P | Diego 5C | v1c · SB t1 |
| b7_p3 | 7 | c07a | 2,7 | 8,1 | 768P | Diego 6C | v1c · SB t0 |
| b7_p4 | 7 | c07b | 2,5 | 6,7 | 768P | Tomás 7B | v1c · SB t0 |
| b7_p5 | 7 | c07b | 1,2 | 6,7 | 768P | — | v1c · SB t1 |
| b7_p6 | 7 | c07b | 2,0 | 6,7 | 768P | — | v1c · SB t1 |

Resumen: 34 cuadros salen de `v1c/frames` (17 SB, 16 ED, 1 recorte) y 9 de `previs/frames`. Suma pedida: 86,5 s por semilla (52,3 s a 480P y 34,2 s a 768P). Resolución de los PNG (medida): 15 a 1536×2752, 19 a 1152×2048 y 9 a 608×1088 (b1_p1, b1_f1, b1_p2, b3_p2, b4_p2, b4_p3, b4_p4, b4_p5, b5_p3).

## D. Estado de la previs v1c

`cap01_previs_v1c.mp4`: 70,5 s, 43 planos, 44 segmentos. Los siete arreglos no están listados en ningún archivo; los reconstruyo de las etiquetas «Extra N» de `lote_v1c.json`.

| Arreglo pedido | Planos | Resultado |
|---|---|---|
| 1 · Maletín bajo el asiento, lado pasillo; hombre sentado | b3_p1, b3_p2 (y b0_p2) | **Falla.** b0_p2 (tres sunburst) y b3_p1 lo dejan al lado, contra el riel. b3_p2: dos tomas marcadas; el corte usa el original, con el hombre **de pie** en el pasillo y el maletín delante (lo confirmé mirando el PNG) |
| 2 · La marca roja se lee antes de bajar la manga | b2_p2 | Aceptado (V16 t1), sin observación |
| 3 · Martina mira al hombre que se remueve | b0_p3 | Bien |
| 4 · Carmen mira la palma, cierra el puño, lo mete al abrigo | b6_p2 | Con observaciones: puño en el pecho, no entra al abrigo, la mancha no se lee |
| 5 · Manchas negro rojizo; Diego solo en la manga derecha | b5_p4, b5_p5, b7_p2, b7_p5 | Palma: aceptada. Diego: **falla** (b7_p2 manchas en la espalda; b7_p5 marca rojo vivo). b7_p1: manos del vidrio rojas |
| 6 · Pelo de Tomás corto con partidura | b2_p1, b2_p3, b4_p6, b5_p7, b7_p4 | Bien en b4_p6 y b7_p4; aceptado en el resto; b6_p3 «no es una partidura estricta» |
| 7 · Ventana del lado de Martina | b2_p3 | Bien (b2_p3 y b2_p4) |

También quedaron bien: b7_p6 a 2,0 s; puño avena en b0_p2; último vagón sin segunda puerta (b6_p3, b7_p3, b7_p4, b7_p6); Iván de espaldas a la puerta (al tercer intento); forcejeo y lectora en b3_p6; ventanita seca en b5_p8 y b5_p9; llave en b5_p6 y b5_p8.

Quedaron con observaciones: b5_p8 (uñas largas), b2_p4 (encuadre abierto, lámparas de más), b2_p1 (apoyabrazos entre asientos), b7_p3 (Iván grande en primer término), b4_p6 (el brazo de Martina sale del abrigo), b5_p3 (sin edición; mano y vidrio «como gotas»), tira roja larga en varios planos del último vagón.

**Degradados por apilar ediciones:** b2_p4 (V18 más tres ediciones de banca) y b3_p1 (editado sobre el b0_p2 ya corregido); así lo fija `KIT/REGLAS_PRODUCCION.md`. El log añade el efecto: lámparas de más y maletín que se corre. Por esa regla se regeneraron también b0_p2, b0_p3, b3_p6, b4_p6, b5_p6, b5_p8, b6_p2 y todo el bloque 7. Inferencia mía: b5_p5 sigue apilado (asset → NBP en v1b → NBP V26).

Pendientes de rehacer antes del video (ESTADO §5): b3_p1, b5_p8, b6_p2, b4_p4, b2_p1, b2_p4, b1_f1. b3_p2 no está en esa lista.

## E. Gasto

| Prueba | Llamadas | Modelo | Costo USD | Tipo de cifra |
|---|---|---|---|---|
| Montaje v1 | sin log | H3 Max 480p | ~4,5 | Solo ESTADO §2; no verificado |
| Montaje v2 | 6 clips + 26 keyframes | H3 480p, GPT Image | ~1,9 de video | Solo ESTADO §2 (el plan decía 2,4) |
| Animatic v1 | 11 de video (1 descartada) + 3 partidas de imagen | H3 Max 480p; NBP; flare | 6,06 (5,51 + 0,55) | `cap01_animatic/tomas.json`; parece cálculo a 0,05 USD/s (a02: 14 s → 0,70), no factura |
| Prueba de voces (§4) | 2 | H3 Max 480p y 768p | ~1,0 | «unos» |
| Assets v10 | 6 de 2 tomas (12 imágenes) | 3 NBP, 3 flare | 1,33 | NBP a tarifa de lista; flare por `billable_units` de fal |
| Previs v1 | 44 con PNG + 5 rechazos | 42 flare, 2 sunburst | 3,18 | Registrado por llamada (valores irregulares; origen no documentado) |
| Previs v1b | 7 | NBP | 1,05 | Tarifa de lista (7 × 0,15) |
| Previs v1c | 73 (2 sin PNG) | 43 NBP, 5 flare, 25 sunburst | 8,29 (6,45 + 0,40 + 1,44) | **Todo estimado**: fal no devolvió montos |
| Video v3 | 0 | — | 0 | No se corrió |

- **Medido:** nada tiene factura. Lo más cercano son los `billable_units` de assets y previs v1.
- **Estimado:** toda la v1c. De esos 8,29, unos 2,5 son tomas `retry` o `flag` que no entraron al corte; 0,14 son dos llamadas sin PNG con cobro no confirmado.
- **Riesgo:** el sunburst de v1c se estimó en 0,046–0,070 por imagen a 1152×2048, mientras la previs v1 registró 0,052 por un sunburst a 608×1088. La cifra de v1c puede quedar corta.
- **Mejor cifra del v3 en fal: ~13,85 USD** (1,33 + 3,18 + 1,05 + 8,29), contra el tope de 60. Sumando animatic v1 y la prueba de voces, ~21 USD desde el 18-oct; con los montajes, ~27 USD históricos (cifra débil). Falta confirmarlo con el panel de fal.

## F. Métricas de ritmo

**Prueba sin sonido, previs v1 (`KIT/contexto/local/notas_metricas_cap01_previs_v1.md`).** «En general sí» se entiende. Confuso: gancho 0–2 s (mano apoyada, no «escondiendo»), caras en la ventanita 35,0–36,5 s, brazo que rompe el vidrio a los 44,3 s. Errores: maletín en el pasillo en b3_p1, lluvia en b7_p2 y b7_p5, lectora con otra cara. Duración 72 s, bajo el formato de 75–90 s. **No hay prueba sin sonido de v1b ni de v1c.**

**Animatic v1.** Gancho «casi»; tramos muertos en s18–21, s55–59 y s80–85; sin sonido el final no se entiende. Sugiere subtítulos quemados.

**Entrada de línea contra el corte (tope 0,3 s).**

| Línea | Previs v1, medido | v3, según el JSON |
|---|---|---|
| Tomás 1C (b2_p1) | +0,45 s | +0,3 |
| Tomás 3C (b2_p3) | — | +0,2 |
| Martina 4D (b2_p4) | — | +0,2 |
| Hugo A (b4_p5) | +0,6 s | **+0,63** (pitazo a +0,1) |
| Diego 5C (b7_p2) | +0,4 s | +0,2 |
| Diego 6C (b7_p3) | — | +0,1 |
| Tomás 7B (b7_p4) | +0,24 s | +0,2 |

Los valores del v3 son de diseño; nadie los midió sobre `cap01_previs_v1c.mp4`.

**Planos marcados como largos.** Métricas marcó b2_p4 (4 s; la línea termina a los 2,9), b4_p5 y b4_p6, b7_p2 (3,6), b7_p3, b7_p4 y b7_p6. La v1c recortó b2_p1, b2_p3, b4_p6, b7_p3, b7_p4 y b7_p6; **b2_p4 (4,0 s) y b7_p2 (3,6 s) siguen igual.** Sobre el punto 5 de la lista: en los bloques 3 a 5, b3_p3 (2,2), b4_p1 (1,8) y b4_p6 (2,0) pasan de 1,5 s.

## G. Contradicciones y cosas que no encontré

1. **Llamada de dos planos.** `previs/montaje.md:17` pone b0_p3 en c00a y `:37` pone b4_p4 en c04a; `tiempos_montaje_v3.json:35` y `:255` dicen c00b y c04b (igual que `plan.md:52` y `:60`).
2. **`revision_v1c.md` tiene dos estados.** Arriba (`:5`) la corrida hecha; abajo (`:24`) «Falta, con fal: las 47 ediciones». `KIT/…/revision_previs_v1.md:170` también dice «No se corrió… 5,56 / 40».
3. **FIX de b2_p4.** `log_decisiones_v1c.md:10` dice que sus 0,45 USD están dentro de los 6,85 del corredor; la nota de costo de `FIX_b2_p4_t0..t2` en `log_generaciones_v1c.json` dice que no. La aritmética da la razón al primero (6,40 + 0,45); el total de 8,29 no cambia.
4. **Conteo de cuadros.** `log_decisiones_v1c.md:9` dice 33 de fal y 10 originales; en disco hay 34 en `v1c/frames` (b1_f1 es recorte local) y 9 originales.
5. **b4 P5/P6.** `KIT/…/revision_previs_v1.md:156` fija 2,5 + 2,5 s y descarta 3,0/2,0; `revision_v1c.md:35-36` y el JSON usan 3,0 + 2,0 «v10». Depende de cuál de las tres v10 se lea (ESTADO `:8-11`).
6. **Último plano.** Guion «corte a negro un segundo después» (`revision_v1c.md:45`), Cristián 2,0 s, Métricas 1,0–1,2 s (`notas_metricas_cap01_previs_v1.md:29`).
7. **Hugo y la regla de 0,3 s.** `pistas/tiempos.json:79-80` marca `seccion5_ok: true` con 0,5 s después del corte; el inicio real es 2,63 s (`tiempos_montaje_v3.json:720`), o sea +0,63. Solo pasa si el pitazo cuenta como pausa escrita. Además `revision_v1c.md:29` dice que las líneas entran «0,2 s después del corte», y Métricas midió +0,4 a +0,6 en la v1.
8. **Animatic v2.** ESTADO `:27` le asigna «~1,9 USD más»; `plan.md:3` dice que el v2 es el v1 con voces, y `notas_productor_cap01_animatic.md:18` y `:26` hablan de retomas propuestas, «NO correr». No hay log de ese gasto.
9. **«Costo real» de assets.** `assets/revision.md:5` contra `assets/tomas.json:7` (tarifa de lista y unidades pendientes).
10. **Número de llamadas.** ESTADO `:30` y `:53` hablan de 17 con c02 partida; `tiempos_montaje_v3.json` tiene 16, con c02 entera a 11,9 s. `plan.md:69` dice ~88 s pedidos; el JSON suma 86,5.
11. **b6_p2.** El lote (V34) pide que no muestre la palma y meta el puño al abrigo; ESTADO `:67` pide «palma derecha abierta cerca del pecho». Puede ser estado inicial contra final, pero no está escrito.
12. **b3_p2** no figura entre los siete pendientes aunque el corte usa el cuadro fallado; `prompts_video_v3.md:319` lo deja «solo en texto».
13. **Copias.** `FEEDBACK_CRISTIAN.md` del kit difiere del repo solo en la última línea (el repo agrega la decisión del 3-oct sobre Tomás). `NOTAS.md` es idéntico a `notas_montaje_v2.md`.
14. **No encontré:** palabras textuales de Cristián sobre la previs; la lista de los siete arreglos; su veredicto sobre la v1c; prueba sin sonido de v1b o v1c; `previs/v1c/raw/` (el registro apunta a `/workspace/…`, no está en el repo); logs de costo de los montajes v1 y v2; ninguna factura de fal.
