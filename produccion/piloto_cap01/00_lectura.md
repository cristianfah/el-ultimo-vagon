# 00 · Lectura del contexto · piloto cap. 1

9-nov-2026. Solo lectura: nada generado, nada gastado. Leí completos las reglas, el estado, las herramientas y el aporte del productor. El resto lo leyeron seis subagentes, cada uno con un informe.

## 1. Qué entendí, en una página

**La historia.** Martina, hija del Presidente, fue obligada a dejar un maletín en el vagón 2 de un tren nocturno. Le miente a Tomás, su novio. El maletín se abre solo, suelta una niebla y el tren se llena de infectados. Don Hugo, el revisor, encierra al grupo en el último vagón. Entonces Diego, el ex, golpea la puerta desde afuera y la delata sin querer: «¡Te vi en el vagón 2!». Tomás pregunta «¿No estabas en el baño?». Martina mira a Tomás, después la manija, y corta a negro. Encuesta: «Si fueras Martina, ¿lo dejas entrar?».

**La pieza.** ~70,5 s, 9:16, 8 bloques, 43 planos, 17 llamadas de video. Cuatro personajes hablan, en 5 llamadas. Los últimos ~13 s son casi todo diálogo.

**Qué existe.**
- Guion v10 (ahora consolidado en una sola versión).
- Previs v1c: un fotograma por plano, aprobada por Cristián el 18-oct.
- Voces aprobadas: 8 tomas, montadas en 5 pistas por llamada. Las cinco duran entre 5,2 y 8,15 s: **cumplen el mínimo de 5 s de `audio_1` en Kling.**
- 17 prompts de H3 escritos y nunca corridos.
- Hojas de personaje y planchas de set aprobadas.

**Qué dijo Cristián, prueba tras prueba.** Cámara por defecto (fija o dolly-in): «se nota la IA». Planos más largos que su acción y esperas antes de hablar. Actuación sin intención, miradas a la nada, voces que no calzan con el gesto. Continuidad rota (maletín, vidrios, lados). Textura «IA slop, con ese grano típico». Y una de proceso: «todo tiene que estar definido antes de generar».

**Lo que eso me dice.** El problema no fue el modelo, fue quién mandaba en cada cosa. La cámara la decidió el modelo. El tiempo lo decidió el plan, no la voz ni la acción. La continuidad se escribió después de generar. El plan de este piloto reparte ese mando antes de gastar (ver `01_propuesta.md`).

**La lista contra la que se revisa todo** son los 20 puntos de `revision_v1.md` §5: ritmo (1–5), cámara (6–8), continuidad (9–13), actuación y diálogo (14–17), montaje (18–20).

## 2. Estado real, confirmado hoy

| Qué | Resultado |
|---|---|
| Créditos de Kling | **3.176**, plan Pro. Igual que el kit |
| Kling 4.0 por MCP | `omni_ref_video`: 3–30 s enteros, 720p o 1080p, `audio_1` de **5–30 s**, `video_1` de 3–30 s, hasta 4 tomas por pedido. `image_to_video`: `first_image`, sin audio. **No entrega el costo en créditos** |
| fal | La cuenta responde por el conector. Precios y campos del productor, confirmados en los schemas |
| **Gasto de fal** | **No se puede confirmar desde aquí.** El historial no trae montos y la cuenta se usa en otros proyectos. La mejor cifra es ~13,85 USD del v3 (assets 1,33 + previs v1 3,18 + v1b 1,05 + v1c 8,29), **toda estimada**. El sunburst de la v1c puede estar subestimado |
| Rama | `claude/piloto-cap01` desde la rama del PR #14, con `main` mezclado en local. Sin conflictos. Nada subido |
| Drive del proyecto | Carpeta accesible y con permiso para agregar archivos |
| Esta máquina | **Faltan `ffmpeg` y Blender.** `FAL_KEY` y `ELEVENLABS_API_KEY` no están exportadas (fal funciona igual por su conector) |
| URLs de fal de las hojas | **38 de 38 vivas** hoy. Las hojas no tienen copia en el repo |

## 3. Guion consolidado

Base: la versión de `main`. De la copia del box entra solo el plano final. La versión del PR #14 no aporta nada propio. **La historia no cambia.** Diff: `guion_v10_consolidado.diff` (10 cambios).

| Cambio | De dónde sale |
|---|---|
| Plano final «unos 2 s», corte cuando los ojos llegan a la manija, ≈1:11,5 | Copia del box + decisión vigente |
| Duración ~71 s y bloque 7 hasta ≈1:11,5 | Se deriva del anterior |
| b0_p2: manga del abrigo gris, con el puño avena asomando | Decisión vigente (ninguna versión lo tenía) |
| Último vagón: una sola puerta; al fondo, pared trasera y cabina a la izquierda | Decisión vigente (ninguna lo tenía) |
| Ventanita: «nunca un pasillo iluminado» | Decisión vigente |
| Encuesta decidida, sin «pendiente» | Decisión vigente |
| c02 pasa a c02a · c02b | Como quedó el video v3 |

Se mantienen de `main`: la ventana del lado de Martina, las muñecas juntas sobre los muslos, la llave (en la mano en P6, gira por dentro en P8), b4 P5/P6 en 3 s + 2 s y la voz de Hugo lista.

## 4. Qué está desactualizado o se contradice

**Afecta la producción:**
1. **El maletín sigue mal en la previs:** b3_p1 (al lado del asiento) y b3_p2 (el hombre de pie, el maletín en medio del pasillo). En b0_p3 y b0_p4 tampoco queda claramente debajo. b3_p2 no estaba en la lista de siete por rehacer.
2. **Posible causa:** el guion pone al hombre en la ventana y a su esposa en el pasillo, pero el maletín «bajo el asiento del hombre, por el lado del pasillo». Hay que decir en el prompt cuál asiento y desde dónde se ve.
3. **Tres cuadros con mirada a cámara** (b5_p4, b5_p7 y probablemente b4_p5) y **Diego mal en b7_p2 y b7_p5**. Ninguno estaba en la lista. Detalle en la sección 5.
4. **Luz detrás de Diego:** el guion dice fuelle «con luz roja»; la frase de luz dice «one cold tube above the glass is the only light». Leo: el tubo frío lo ilumina a él y el fondo queda oscuro. Lo confirmo contigo.
5. **La línea de Hugo entra a +0,63 s del corte** y el tope es 0,3 s. Está marcada OK por el pitazo. Se arregla en el montaje.
6. **`omni_ref_video` no tiene primer fotograma.** El método del repo pide primer fotograma + hojas + pista en una llamada. En Kling por MCP eso no existe: con voz, el cuadro aprobado entra como referencia.
7. **`tiempos_montaje_v3.json` trae 16 llamadas** (c02 entera). La partición c02a/c02b solo está en los scripts del video v3.
8. **9 cuadros de la previs están a 608×1088**, entre ellos b4_p4 y b1_p1, que son primeros fotogramas.
9. **Los scripts del video v3 tienen la ruta del box fija** y no corren aquí sin cambiarla. Los 17 recortes de primeros fotogramas no existen (se rehacen gratis).

**No afecta el capítulo, pero conviene saberlo:**
- `cap01.yaml` apunta a la v8. Los tiempos vigentes están en el JSON.
- La biblia tiene un vagón 6 antes del último; el guion pone el fuelle entre el 5 y el último.
- `decisiones.md` no registra la llave, la encuesta, la ventana ni el plano final, y sigue con «cerrojo» y tope de 40.
- `director_fotografia.md`, `impacto.md` y `prompter.md` siguen con «cámara fija por defecto», que el método ya derogó.
- Varios archivos mantienen la meta de 75–90 s (contra la regla 5) y `README.md` indica `git push -u origin main` (contra la regla 7).
- `kling_4_0_resumen.md` y `motores.md` dudan de que el MCP tenga Kling 4.0. Ya lo tiene.
- ESTADO le asigna ~1,9 USD al animatic v2, pero eran retomas propuestas y no corridas.
- `revision_v1c.md` dice a la vez «corrida hecha» y «faltan las 47 ediciones».

## 5. Revisión visual de los fotogramas

Un subagente miró los 43 cuadros vigentes uno por uno. Yo revisé a ojo seis de los críticos y coincido. **Resultado: 11 OK, 18 con observación, 14 por rehacer.** La lista de siete del kit se confirma entera, y aparecen otros siete.

| Fuera de la lista de siete | Qué se ve |
|---|---|
| **b5_p4** | Carmen mira directo a cámara. Es el primer fotograma de c05b |
| **b5_p7** | Tomás mira directo a cámara. Luz blanca en las caras |
| **b4_p5** | Hugo parece mirar al lente (probable). Además está a 608×1088 |
| **b3_p2** | El hombre de pie en el pasillo y el maletín en medio. Debería estar sentado |
| **b6_p3** | Luz blanca plana, otra cara de Tomás, y el fondo parece una puerta |
| **b7_p2** | Diego: manchas grises por toda la chaqueta, nada rojo-negro en la manga derecha |
| **b7_p5** | Diego: una mano roja estampada en el hombro, y detrás se ven asientos y una puerta, no el fuelle |

Además, tres primeros fotogramas necesitan arreglo aunque el plano esté bien: **b2_p3** y **b4_p1** tienen 4 a 7 lámparas encendidas (la frase de luz dice 2–3), y **b1_p1** está a 608×1088.

**b0_p2:** un informe lo da por malo (el log de la v1c dice «al lado, contra el riel») y el otro por bueno. Lo miré: la mano está empujando el maletín bajo el borde del asiento, del lado del pasillo. Como primer cuadro de esa acción sirve. Lo dejo fuera de la lista y te lo muestro en la página 1.

**Continuidad que no está escrita en el «Estado del mundo» y hay que fijar antes de generar:**
- La **bandolera de Martina** aparece en 5 planos y falta en 7.
- La **placa de la cerradura** del último vagón cambia de lado (b7_p1 contra b5_p8 y b5_p9), y el **tubo frío** sobre la puerta está encendido en unos planos y ausente en otros.
- **Tomás** es el personaje menos estable: pelo, forma de la cara y acolchado de la chaqueta cambian entre planos.
- Las **esquineras del maletín** son doradas en los bloques 0 y 3 y plateadas en el flash.
- Las dos referencias de la **palma de Carmen** parecen una mano izquierda; la decisión dice derecha.
- Martina y Tomás **se cruzan de lado** entre b4_p6 y b5_p2/b5_p7.

**URLs de fal: 38 de 38 vivas** (solo se pidió la cabecera). Los 193 binarios del índice están en el clon. Pero las hojas de personaje, las planchas F01–F12 y los props **no están en el repo**: solo en fal y en el Drive. Conviene bajarlas ya, con tu OK.

**Referencias que no se deben usar:** `estado_diego_mojado_herido_v2` (lluvia en cuadro y herida abierta), el estado v1 de Diego (brazo izquierdo) y `cuarto_rapto_martina_nbp_0` (cuerda). La correcta de Diego es la v3.

## 6. Qué no encontré

- Ninguna factura ni monto real de fal.
- Las palabras de Cristián sobre la previs, la lista escrita de sus siete arreglos y su veredicto sobre la v1c terminada.
- Una prueba sin sonido de la v1b o la v1c. Las entradas de línea del v3 son de diseño, nadie las midió.
- El costo en créditos de Kling 4.0 en una fuente oficial.
- Evidencia, en los 22 flujos, de Kling 4.0 con previz como video de referencia o con audio de referencia. Tampoco de lipsync en español en ningún motor. Lo único medido es nuestro H3 a 768p (correlación 0,85).
- Archivo local de las hojas de Martina, Tomás, Carmen, Iván, Hugo y la pareja, ni de F01–F03, F07, F09 y F10: solo URLs de fal de octubre.

## 7. Dudas para Cristián (ninguna frena la fase d)

1. El monto real de fal del 18 y 19 de octubre.
2. Detrás de Diego: ¿fondo oscuro con el tubo frío solo sobre él? (punto 4 de arriba).
3. Martina, ¿con bandolera o sin bandolera?
4. ¿Vagón 6 o no? Solo importa para la biblia; va al banco de ideas.

Informes de lectura completos: `lectura/01…06_*.md` en esta misma carpeta (historia y guion, método y prompting, previs y revisiones, video v3, lecciones y flujos, binarios).
