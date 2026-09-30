# Plan de generación de assets — v1

**Para:** EL ÚLTIMO VAGÓN, capítulo 1 (guion `cap01_v3`, con los cambios de la v4 pendientes) y lo que ya se sabe de los capítulos 2 y 3.
**Objetivo:** tener un banco de personajes, sets y props con **identidad fija** antes de hacer cualquier keyframe. Si un asset no está congelado, no entra a un plano.

Documentos que salen de este plan:
- `direccion_arte/personajes/fichas_personajes_v1.md`: una ficha por personaje, con los prompts de Midjourney, GPT Image y Nano Banana Pro.
- `direccion_arte/sets/set_ultimo_vagon_v1.md`: plano del vagón, estados de luz y prompts de los sets y props.

**Copia de lectura en Google Drive** (carpeta [EL ÚLTIMO VAGÓN — Assets v1](https://drive.google.com/drive/folders/1k6qZp9R2WelrOqcd_ZRsrzW1kzXWxBBl), dentro de Fahren.tv). Si cambia un archivo del repo, se actualiza también el Doc.

---

## 1. El método en una línea

**Midjourney para encontrar la idea → GPT Image 2.5 para corregirla → Weavy para congelarla → prueba en situación para validarla.**

```
MJ 8.2 · cara (luz neutra)        ─┐
                                   ├→ GPT Image 2.5 · unión y corrección → cuerpo entero → hoja de personaje → prueba en el set → CONGELADO
MJ 8.2 · vestuario (sin cara)     ─┘
MJ 8.2 · set (exploración de look) → GPT/NBP · plancha maestra del set con luz de trabajo → reiluminar la misma plancha (ámbar, rojo) → vistas por eje → CONGELADO
```

**Por qué separar cara y vestuario en Midjourney:** MJ 8.2 no tiene `--oref`, así que no puede sostener una cara entre imágenes. Si pedimos cara y ropa juntas, cada variación de ropa nos cambia la cara. Separadas, se exploran por su lado y se unen una sola vez con un modelo de edición que sí respeta referencias.

---

## 2. Qué aprendimos de la prueba 1 (y qué hace este plan al respecto)

| Problema | Por qué pasó | Qué hacemos ahora |
|---|---|---|
| Estética genérica de IA: ruido, luz sin fuente, composición de afiche | Palabras de look en vez de órdenes de rodaje | Los assets se generan en **luz neutra**; el look se pone recién en el keyframe, con la plantilla de rodaje |
| La piel mojada de `ref_soto` se arrastra a todo | La referencia de identidad tenía brillo | Toda referencia de identidad va con **piel seca y mate**. Lo mojado es un **estado** aparte (ver sección 5) |
| El vagón cambia de un plano a otro | Cada plano generaba su propio vagón | **Una sola plancha maestra** del set. Las otras luces y ángulos se sacan editando esa plancha, no generando de cero |
| Caras de IA «de siempre» | Prompts tipo «mujer de 29, atractiva» | Casting como de calle: rasgos concretos e imperfectos (sección 4) |
| Todo en foco | Sin lente declarado | Se resuelve en el keyframe, no en el asset |

> **Pendiente de Cristian:** si en la prueba 1 hubo otros problemas (manos, props que cambian, proporciones, etc.), agrégalos a esta tabla y ajustamos el plan.

---

## 3. Lista de assets (capítulo 1 + lo que se planta para los capítulos 2 y 3)

Nombres en minúsculas, exactos, iguales en el repo y en los nodos de Weavy. `_v1`, `_v2`… nunca se sobreescribe.

### Personajes

| ID | Qué es | Prioridad |
|---|---|---|
| `cara_martina`, `cara_tomas`, `cara_diego`, `cara_carmen`, `cara_ivan`, `cara_hugo` | Retrato de identidad: luz neutra, piel seca, fondo gris | 1 |
| `vest_<nombre>` | Vestuario completo, sin cara | 1 |
| `ref_<nombre>` | Cuerpo entero: cara + vestuario unidos | 1 |
| `sheet_<nombre>` | Hoja de personaje: 3 vistas de cuerpo + 3 de cara | 1 |
| `estado_diego_mojado` | Diego empapado, con la manga manchada (plano 0:45) | 1 |
| `extra_camisa_azul`, `extra_esposa` | El hombre de camisa azul y su esposa (plano 0:19) | 2 |
| `ref_infectados` | Ya existe. Se reutiliza tal cual como firma visual | — |

### Sets

| ID | Qué es | Planos del cap. 1 | Prioridad |
|---|---|---|---|
| `set_ultimo_vagon_base` | Plancha maestra, luz de trabajo neutra, sin personajes | Todos desde 0:31 | 1 |
| `set_ultimo_vagon_ambar` / `_rojo` | La misma plancha, reiluminada | 0:31–1:23 (rojo) | 1 |
| `set_ultimo_vagon_eje_puerta` / `_eje_fondo` | Vistas hacia la puerta y hacia el fondo, desde la plancha | Contraplanos | 1 |
| `set_puerta_ventanita` | La puerta vista desde adentro y desde afuera, con la cerradura | Cold open, 0:45–1:19 | 1 |
| `set_vagon_pasajeros_ambar` | El vagón de la escena 1 (antes del brote) | 0:03–0:28 | 1 |
| `set_pasillo_exterior` | Lo que se ve por la ventanita: el vagón de al lado, rojo, y la esquina de donde llegan los infectados | 0:28, 1:08 | 2 |
| `loc_bosque`, `ref_tren` | Ya existen (VAGÓN 7). Se revisan por si la librea cambia | Transiciones | 3 |

### Props

| ID | Por qué importa | Prioridad |
|---|---|---|
| `prop_llave` + cerradura | Es el poder: pasa de mano en mano | 1 |
| `prop_revolver` | Dos balas = dos decisiones futuras. Tiene que verse igual en todos los insertos | 1 |
| `prop_celular_martina` | Los mensajes de «D». Pantalla simple, sin interfaz de marcas | 1 |
| `prop_freno_emergencia` | **Se planta desde el capítulo 1** en la pared del vagón, para que en el capítulo 3 el público diga «estaba ahí» | 1 |
| `prop_radio`, `prop_botiquin`, `prop_linternas` | Compartimento del revisor (capítulos 2 y 3) | 3 |

---

## 4. Cómo evitamos la «cara de IA»

Midjourney tiende a devolver la misma cara bonita y simétrica. Lo que funciona es escribir como un **director de casting de calle**, no como un fotógrafo de moda:

1. **Nada de palabras de belleza:** ni *beautiful*, *attractive*, *stunning*, *model*, *perfect skin*, *flawless*. Se agrega `--no` con esas palabras.
2. **Tres rasgos concretos e imperfectos por cara:** una nariz con un quiebre, cejas desparejas, orejas un poco salidas, un lunar, ojeras. Uno de ellos es el **ancla de identidad**: el rasgo que tiene que sobrevivir en todos los planos (el lunar de Martina, los anteojos de Tomás, el bigote de Hugo).
3. **El historial en la cara y en el pelo:** tinte crecido, piel con sol de obra, marcas de anteojos, pelo cortado en casa. La cara cuenta una vida.
4. **Lenguaje de documental:** *documentary portrait*, *street casting, non-actor*, *real person*. Película de negativo, no digital.
5. **Mirada quieta, no emoción:** *guarded stillness*, *looking straight into the lens*. Nada de *sad*, *angry*, *scared*: el modelo sobreactúa.
6. **Una variable por ronda:** cada ficha trae una lista de variables. Se cambia una sola por ronda (primero la estructura de la cara, después el pelo, después la edad aparente), así sabemos qué movió el resultado.

**Prueba de miniatura:** el público ve la serie en un teléfono. Cada cara elegida se mira reducida a unos 3 cm. Si no se distingue de otro personaje del elenco a ese tamaño, no sirve.

---

## 5. Fases de trabajo

### Fase 1 · Casting en Midjourney (la parte creativa)
Por personaje:
1. **Cara:** 3 rondas como máximo, 4 grids por ronda, una variable por ronda. Se eligen 2 o 3 candidatas.
2. **Vestuario:** 2 rondas. Se elige una.
3. Se arma un **tablero de casting** con las candidatas de los seis personajes juntas.

**Aprobación 1 (Cristian):** el elenco elegido junto, en una sola imagen. Se revisa:
- ¿Se distinguen los seis por la silueta, aunque estén a contraluz?
- ¿Se leen las edades (29–31, 45, 54, 62)?
- **El triángulo:** Tomás y Diego tienen que ser dos opciones creíbles para Martina. Si uno es obviamente «el bueno» o «el malo», la votación se desbalancea.
- ¿Cada uno parece alguien que conoces?

### Fase 2 · Corrección y unión en GPT Image 2.5 (en Weavy)
1. **Corregir la cara elegida:** manos, orejas, dientes, simetría rara, brillo de la piel. Se piden cambios de a uno.
2. **Unir cara + vestuario** en un cuerpo entero 9:16, sobre fondo gris.
3. Correr la unión **en paralelo en GPT Image 2.5 y Nano Banana Pro** y quedarse con la mejor (regla del estudio: GPT se deforma con prompts largos).

### Fase 3 · Hoja de personaje (Weavy)
- 3 vistas de cuerpo (frente, perfil, espalda) + 3 de cara (frente, tres cuartos, perfil).
- **Estados:** solo los que pide el guion. En el capítulo 1: Diego mojado y con la manga manchada. Los demás personajes no necesitan estado mojado (están adentro del tren).

### Fase 4 · Sets (en paralelo con las fases 2 y 3)
1. Midjourney solo para el **look** del vagón (materiales, época, desgaste). Aquí entran tus imágenes de referencia.
2. Weavy: **una plancha maestra** con luz de trabajo neutra, siguiendo el plano del vagón de `set_ultimo_vagon_v1.md`.
3. Desde esa plancha se editan los **estados de luz** (ámbar y rojo) y las **vistas por eje** (hacia la puerta, hacia el fondo).

**Aprobación 2 (Cristian):** set y props congelados.

### Fase 5 · Prueba en situación
Dos keyframes con la plantilla de rodaje, que prueban lo más difícil del capítulo (prompts completos en `set_ultimo_vagon_v1.md`, sección 6):
- **PS-01:** Martina y Tomás en el vagón de pasajeros, luz ámbar (0:03). Prueba si las caras aguantan la luz cálida y si el triángulo ya se siente en la distancia entre los dos.
- **PS-02:** Diego en la ventanita, visto desde adentro bajo luz roja (0:45). Prueba lo más frágil: identidad a través de un vidrio sucio y con poca luz, y si la manga se lee.

**Aprobación 3 (Cristian):** si las dos pruebas pasan, los assets se congelan y se crean los elements de Kling. Si una cara se pierde bajo la luz roja, se vuelve a la fase 2 para reforzar el ancla de identidad.

---

## 6. Cómo ir rápido sin perder la creatividad

- **Lo lento es la fase 1, y está bien que lo sea.** El resto es mecánico y se puede plantillar.
- **Orden de casting:** primero el triángulo (Martina, después Diego y Tomás juntos, porque se eligen uno contra el otro), después Hugo, Iván y Carmen.
- **Mientras exploras caras en MJ,** el set y los props avanzan en Weavy. No dependen de los personajes.
- **Todo lo elegido se sube al repo** con su nombre (`direccion_arte/referencias/elenco/`, `.../sets/`, `.../props/`) y se marca en la tabla de estado (sección 7).
- **Weavy:** cuando tengamos las caras elegidas, el agente de pipeline arma el JSON del flujo «EL ÚLTIMO VAGÓN — Assets v2», con un grupo por personaje (cara → corrección → unión → hoja) y un grupo por set (plancha → estados → ejes).

---

## 7. Estado

| Asset | MJ | Corrección | Unión / plancha | Hoja / estados | Prueba | Congelado |
|---|---|---|---|---|---|---|
| Martina | — | — | — | — | — | — |
| Tomás | — | — | — | — | — | — |
| Diego | — | — | — | — | — | — |
| Carmen | — | — | — | — | — | — |
| Iván | — | — | — | — | — | — |
| Don Hugo | — | — | — | — | — | — |
| Último vagón | — | — | — | — | — | — |
| Vagón de pasajeros | — | — | — | — | — | — |
| Props del cap. 1 | — | — | — | — | — | — |

---

## 8. Lo que opinan los agentes

Cada rol leyó el plan desde su responsabilidad (`agentes/roles.md`):

- **Showrunner:** Diego no puede verse culpable ni peligroso. Si tiene cara de «malo», el público vota NO sin pensar y se pierde el debate. Tiene que ser alguien a quien te dé pena dejar afuera. Tomás tampoco puede verse como el villano: su frialdad tiene que sorprender.
- **Abogado del diablo:**
  - ¿Por qué Carmen anda con uniforme en un tren nocturno? Porque viene saliendo de turno: el uniforme va arrugado, debajo del abrigo, con la credencial dada vuelta.
  - Si hay una caja con hacha de emergencia en el vagón (como en VAGÓN 7), ¿por qué no la usan? **Recomendación: no poner hacha en el último vagón** en el capítulo 1. Si se agrega, es una decisión de historia.
- **Director y DP:** bajo la luz roja de emergencia **desaparecen los colores**: todo se vuelve rojo y negro. Los personajes se distinguen por **valor** (claro u oscuro), **silueta** y **textura**, no por el color. Por eso cada ficha declara si el personaje «se lee claro» o «se lee oscuro» en rojo. Y la manga de Diego tiene que ser de tela clara, para que la mancha oscura se lea a través del vidrio.
- **Prompter:** los assets van en luz neutra y piel seca. El look se pone en el keyframe, nunca en la referencia.
- **Pipeline:** los nombres de este plan son los nombres de los nodos de Weavy. Si cambia un nombre, cambia en los dos lados.

---

## 9. Lo que necesito de ti para seguir

1. **Imágenes de referencia del set** (tren, vagón, materiales). Van a `direccion_arte/referencias/sets/`.
2. **Confirmar o cambiar** las propuestas de las fichas que tocan la historia: el brazo herido de Diego (propuesta: antebrazo izquierdo), el reloj de enfermera de Carmen y que no haya hacha en el último vagón.
3. **Dónde ocurre la serie:** las fichas dicen *South American*, sin país. Si quieres que sea explícitamente Chile (el bosque del sur de VAGÓN 7), se ajustan los prompts de cara.
4. **Los primeros resultados de MJ:** me pasas las grillas y elegimos juntos qué variable cambiar en la siguiente ronda.
