# Cómo se escriben hoy los prompts de video e imagen (2026-09-30)

Pedido de Cristian después de la prueba de montaje v1: los prompts salen muy cortos. Los agentes hacen mucho trabajo que después no llega al prompt, y si no está en el prompt, no sirve. Aquí se revisa qué dicen las guías oficiales de cada modelo y las guías de la comunidad que trajo Cristian. De esto sale la skill `.cursor/skills/director-de-prompts/`.

## 1. Diagnóstico: qué hicimos en la v1

| Qué | Dato |
|---|---|
| Regla de oro del compilador | «Un prompt de video = una acción, un movimiento de cámara y un sonido». Largo pedido: 60–110 palabras por plano y 90–160 por bloque |
| Keyframe contra video (c01_p02) | El prompt del keyframe tiene unas 600 palabras; el del video, unas 110. En el video no se dice qué hay detrás de Martina ni que el fondo es el interior quieto del vagón, y el modelo lo movió como una ventana lateral |
| Bloque b03 (12 s, cinco planos) | Unas 150 palabras, o sea unas 30 por plano. La guía oficial de H3 pide entre 350 y 500 para un bloque con referencias |
| Hechos de continuidad | Solo entraban los «frágiles». Los demás se daban por resueltos en el keyframe, pero el video los pierde a mitad del clip (el celular que se deforma, las balas de b06) |
| Formato | Prosa libre, sin la estructura que espera H3 |
| `prompt_expansion_mode` | Apagado, porque encendido reescribía el prompt e invertía la acción. Resultado: el modelo recibió nuestra prosa corta sin reescribir y sin la estructura oficial |

**Conclusión:** el trabajo de los agentes se perdía en la compilación, y el problema no era el modelo. La regla de oro confundía un prompt **simple** (una intención clara por beat) con un prompt **corto**.

## 2. Guías oficiales por modelo

### MiniMax H3 (nuestro motor de video principal)
Fuente: skill oficial `h3-prompt-writing` en [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) (`skills/h3-prompt-writing/references/base-en.txt` y `ref-en.txt`). Se instala con `npx skills add https://github.com/MiniMax-AI/MiniMax-H3 --skill h3-prompt-writing`. No tiene licencia publicada: aquí se resume, no se copia.

- **Formato fijo por campos:** `integrated_multimodal_description`, `overall_soundscape` y `non_diegetic_music`, en ese orden. En modo referencias (Ref2VA, nuestra ruta `reference-to-video`) son seis secciones: `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape` y `non_diegetic_music`.
- **Primera línea según el modo:** en imagen a video (I2VA) y en primer y último fotograma (FL2VA), una frase fija que alinea cada imagen con su segundo exacto.
- **Largo:** en Ref2VA, `detailed_description` va de 350 a 500 palabras en inglés. Un solo plano no justifica una descripción más corta: el detalle se reparte según la información de cada plano.
- **Qué va en la descripción:** composición inicial, aspecto y posición de cada sujeto, entorno y luz, acciones y cambios de estado, cámara, sonido del momento y dónde actúa cada referencia. **Nada de resumen de trama.**
- **Planos:** `[Shot 1]` sin tiempo; los siguientes, `[Shot 2] At 00:03.500, the camera cuts to…`. Un corte tiene que traer información nueva; si solo cambia la distancia o un poco el ángulo, es un movimiento de cámara.
- **Cámara = tipo + amplitud + velocidad,** escrito como una acción dentro de la frase: *The camera pushes in with small amplitude at slow speed toward…* Vocabulario: *push in / pull out, zoom, pan, truck, tilt, pedestal, arc shot, tracking shot, static shot, shake slightly / strongly, POV, roll.*
- **Diálogo:** cada voz tiene un id estable, `(S1)`, `(S2)`. La línea va dentro de `<d>[Spanish] …</d>`, tal cual, sin traducir. Fuera de `<d>` van quién habla, el timbre, el ritmo y la entrega.
- **Sonido:** `overall_soundscape` resume ambiente, sonidos físicos y sonidos humanos no verbales en 1–4 frases. `non_diegetic_music` describe la música que solo oye el público; si no hay, `N/A`.
- **Referencias con etiqueta:** `<Subject N>` es contenido reutilizable (persona, lugar, prop), `<Picture N>` es un fotograma concreto. La etiqueta se define una vez y se usa igual en todo el prompt.
- **FL2VA favorece un solo plano:** la descripción es el camino entre los dos fotogramas, no la descripción de las dos imágenes. Esto confirma la regla nueva de FL.

### Kling 4.0
Fuentes: [blog de Kling](https://kling.ai/blog/kling-ai-prompt-guide) (3.0) y [guía de Morphic para 4.0](https://morphic.com/resources/how-to/kling-4-0-guide), que no es oficial. Hay que confirmar con la guía oficial cuando salga la versión completa.
- **Acepta prompts de hasta 8.000 tokens.** «Lo que dejas fuera se rellena con un promedio.»
- Se escribe como una orden de rodaje, no como un pie de foto: sujeto y acción, lugar y luz, cámara, tiempos y sonido.
- **Beats con rangos de tiempo** (`0-3s: … 3-8s: …`), con una acción principal por rango.
- Hasta 10 keyframes y 15 referencias. **Los videos de referencia sirven para actuación, movimiento, cámara y ritmo.** Es el camino para la referencia de actuación grabada con el celular.
- El diálogo va entre comillas, con el idioma y el acento.

### Nano Banana Pro (keyframes)
Fuente: [Ultimate prompting guide for Nano Banana](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana) (Google Cloud).
- Lenguaje natural en frases completas, nunca listas de palabras clave. Hay que ser específico: sujeto, luz, composición.
- Se describe en positivo lo que se quiere («empty street», no «no cars»).
- A cada imagen de referencia se le asigna un rol y se dice cómo se combinan.
- **Se edita en vez de regenerar:** si la imagen está bien en un 80 %, se pide solo el cambio y se fija todo lo demás.

### GPT Image 2.5 (hojas y ediciones)
Fuente: [Image prompting, OpenAI](https://developers.openai.com/api/docs/guides/image-prompting).
- Se define el resultado y su uso. En pedidos complejos se usan secciones con nombre: escena, sujeto, detalles, restricciones.
- En las personas se describen el encuadre del cuerpo, la escala, la mirada y el contacto con los objetos («looking down at the open book»).
- En una edición: «change only X» más la lista de lo que se preserva.
- Las referencias se nombran por número y rol.

## 3. Guías de la comunidad (las que trajo Cristian)

Son para Seedance 2.0 e imagen en Higgsfield, pero el método sirve para cualquier motor:

| Guía | Qué tomamos |
|---|---|
| **CINEDANCE V4** (director de prompts para Seedance) | Método interno en cuatro pasos: descomponer, diagnosticar, desarrollar y entregar. Mapa de la locación (primer término, término medio, fondo, dónde está cada cosa). Primer fotograma con todos los personajes en su lugar. Bloqueo con medidas («a menos de 1 m», «a la izquierda del cuadro»), nunca «cerca». Cuerpo y mirada por separado. Física (peso, inercia, tela). La luz como prioridad, no como decoración. Cada prompt aislado: sin personajes ni props que no estén en el plano. Candados locales en positivo en vez de listas de negativos. Revisión silenciosa antes de entregar. **Densidad solo donde importa el control.** |
| **Lira** (prompts de imagen) | Prosa natural. El positivo manda sobre el negativo. Luz técnica, no de ánimo. Paleta 60/30/10. Ediciones con «CHANGE / PRESERVE EXACTLY». Contraplano de una locación: describir objeto por objeto dónde queda cada cosa en la vista nueva |
| **Acting System** | Todo el sistema de actuación (`produccion/actuacion.md`): objetivo, obstáculo, tácticas, beats, ojos, estados en vez de transiciones, perfil por personaje |
| **Referencia de Seedance 2.0** | Orden de prioridad: sujeto, acción, entorno, cámara, estilo, restricciones. Lo primero pesa más. Separar la cámara del sujeto. La palabra *fast* en cámara, sujeto y fondo a la vez es la causa más común de artefactos |

## 4. Contradicciones y cómo se resuelven

| Tema | Qué dicen | Decisión |
|---|---|---|
| Largo | Seedance: 60–100 palabras. H3 oficial: 350–500 en Ref2VA. Kling: hasta 8.000 tokens | **Manda la guía oficial de cada modelo.** En H3 se usa su formato y su largo |
| Lentes | CINEDANCE: campo de visión en grados, no milímetros. Guía oficial de OpenAI: los datos de cámara son pistas de apariencia | En video, el lente se describe por su **efecto visible** (compresión, fondo, distorsión). Los milímetros solo van como apoyo. Hay que probarlo en H3 |
| Negativos | Todas coinciden: el positivo manda | Candados locales en positivo. Un «no X» solo para una falla conocida y junto a la regla que protege |
| Expansión del prompt en H3 | La reescritura del modelo invirtió la acción | Se mantiene apagada: **nosotros escribimos directamente en el formato oficial** |

## 5. Prueba propuesta
Reescribir b02 (un plano) y b03 (cinco planos) con la skill, con los mismos keyframes y el mismo seed, a 480P, y comparar contra la v1. Costo: unos 0,85 USD. Si mejora, se recompila todo el capítulo.
