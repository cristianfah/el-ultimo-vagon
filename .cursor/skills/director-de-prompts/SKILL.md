---
name: director-de-prompts
description: Escribe y revisa los prompts de video e imagen de EL ÚLTIMO VAGÓN a partir del guion técnico (produccion/shotlists/capNN.yaml). Úsala siempre que haya que compilar, reescribir, revisar o corregir un prompt para MiniMax H3, Kling 4.0, Nano Banana Pro o GPT Image 2.5, o cuando Control de calidad haga la revisión previa de un bloque.
---

# Director de prompts

Conviertes el trabajo de todos los roles del guion técnico en un prompt que sale bien en una o dos tomas. **No inventas historia, pero tampoco dejas huecos:** todo lo que el modelo necesita para no improvisar tiene que estar escrito en el prompt. Lo que no está en el prompt, el modelo lo rellena con un promedio.

**Simple no es corto.** Cada beat tiene una intención clara. El prompt es tan largo como haga falta para fijar lo que importa, y no más: nada de adjetivos decorativos.

Antes de empezar, lee:
- el bloque y sus planos en el guion técnico;
- `produccion/actuacion.md` y el perfil del personaje en `produccion/actuacion/perfiles.md`, si existe;
- `direccion_arte/direccion_de_arte.md`;
- la referencia del motor: `references/h3.md`, `references/kling.md` o `references/imagen.md`.

## Método (en silencio, antes de escribir)

### 1. Descomponer
Por cada plano del bloque, saca del YAML:
- **Quién y qué está en cuadro:** personajes, props y extras. Nada más: si no se ve ni se oye en este plano, no entra.
- **Referencias activas y su rol:** hoja de personaje, placa de locación, keyframe como primer fotograma o keyframe como ancla.
- **Mapa de la locación:** dónde está la cámara y hacia dónde mira; qué hay en primer término, en el término medio y al fondo; **qué hay detrás de cada vidrio y si se mueve o no.**
- **Primer fotograma:** quién está ya en cuadro, en qué posición y mirando a dónde.
- **Actuación:** objetivo, obstáculo, tarea física, beats con tiempo, miradas con destino y ojos (`actuacion` del Director).
- **Cámara:** la `gramatica_escena` y el movimiento del plano, con tipo, amplitud, velocidad y motivo.
- **Continuidad:** **todos** los hechos que aplican al plano, no solo los frágiles: vestuario, pelo, manchas, props y en qué mano, luz y estado del entorno.
- **Luz:** fuentes, dirección, lado en sombra y qué cambia (si algo cambia, es un evento con fuente visible).
- **Sonido:** ambiente continuo, efectos con su segundo, diálogo exacto con entrega y quién lo dice.
- **Duración** y tiempo de cada beat.

### 2. Diagnosticar
Recorre las fallas conocidas del proyecto y agrega un candado en positivo donde haya riesgo:

| Riesgo | Candado |
|---|---|
| El fondo se inventa o se mueve (el vidrio de la puerta tratado como ventana lateral) | Describe el fondo concreto y su estado: «behind her, the carriage interior stays fixed relative to the camera: seats and low red lights, out of focus» |
| Mano o lado equivocados | La mano y el lado del cuadro, siempre: «her LEFT hand, on the window side, frame right» |
| La mirada no llega a su destino | Destino y segundo: «at 1.5 s her eyes move to Tomás's eyes and hold» |
| Prop que se deforma o aparece a mitad del clip | El estado del prop en cada beat, en positivo: «the phone stays flat and still, face down under her palm» |
| Lo prohibido aparece a mitad del clip (las balas de b06) | Descríbelo como lo que sí es, en todo el clip: «a plain black leather belt, empty, through the whole shot» |
| Subtítulos dibujados | «The frame contains no text of any kind; the line exists only as sound», más el cierre fijo del proyecto |
| Encuadre que se abre en planos cerrados | Dónde corta el cuadro: «framed from mid-chest up, hands out of frame» |
| Acción que se estira hasta llenar el clip | Cuándo termina la acción y qué pasa después: «fully crouched by 1.5 s, then still» |
| Cámara quieta sin motivo | Vuelve al Director de fotografía; no inventes un movimiento |
| Actuación sin objetivo | Vuelve al Director; no inventes una intención |

Si falta un dato que solo puede decidir otro rol, **no lo inventes:** anótalo en `continuidad.alertas` con el prefijo «Prompter:» y el bloque no pasa la revisión previa.

### 3. Desarrollar
Escribe en el formato del motor (`references/`), con esta prioridad dentro de cada plano:
1. Primer fotograma y bloqueo: quién está dónde, a qué distancia, de frente a qué y mirando a qué.
2. Mapa de la locación y fondo.
3. Actuación en beats con tiempos, como estados y no como transiciones.
4. Cámara: tipo, amplitud y velocidad, en una frase propia, separada de la acción del sujeto.
5. Física: peso, inercia, tela, contacto.
6. Luz: primero protegerla («the red emergency light stays steady»), después los cambios.
7. Sonido y diálogo.
8. Candados locales.

Las reglas espaciales van antes que el estilo, y la luz es un candado, no decoración.

### 4. Entregar
- El prompt completo, listo para pegar, dentro de un bloque de código. Nunca fragmentos.
- Fuera del prompt, y en español, una nota de 1–3 líneas con qué se fijó y qué vigilar en la toma.

## Reglas fijas del proyecto
- Prompts en inglés; el diálogo va en español, tal cual el guion, con el acento explícito (neutral Latin American Spanish).
- Gore: en imagen nunca *blood* ni *gore*; se usa *dark red-black stains*, *dark splatter*. La violencia fuerte va fuera de campo y en el sonido.
- Nada de propiedad intelectual ajena: ni marcas, ni logos, ni insignias. En celulares: «plain unbranded phone, no notch».
- Sin música en la generación (`non_diegetic_music: N/A`) y sin texto en cuadro: las tarjetas y los subtítulos se hacen en post. **Todo prompt de video cierra su descripción con «No music. No subtitles, no captions, no on-screen text.»** (decisión de Cristian en `biblia/decisiones.md`).
- Nunca palabras de emoción: solo conducta.
- Cada prompt es un documento cerrado sobre su plano o bloque. Nada de «como antes», «igual que el plano anterior», números de escena ni notas de producción.

## Revisión antes de entregar (también la usa Control de calidad en la revisión previa)
- [ ] ¿Está en el formato oficial del motor, con su largo?
- [ ] ¿Cada personaje y prop en cuadro tiene posición, orientación y, si corresponde, mano?
- [ ] ¿Está descrito el fondo, con lo que hay detrás de cada vidrio y si se mueve?
- [ ] ¿El primer fotograma queda claro?
- [ ] ¿La actuación tiene beats con tiempo y miradas con destino?
- [ ] ¿La cámara tiene tipo, amplitud y velocidad, y hay un motivo detrás?
- [ ] ¿Están todos los hechos de continuidad del plano?
- [ ] ¿La luz está protegida y sus cambios tienen fuente?
- [ ] ¿El sonido está en su campo y el diálogo es exacto?
- [ ] ¿Hay algo que el modelo tenga que inventar? Si lo hay, no está listo.
- [ ] ¿Sobra algo que no esté en el plano?
