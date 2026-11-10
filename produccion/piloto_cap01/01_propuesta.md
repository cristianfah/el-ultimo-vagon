# 01 · Propuesta · qué haría distinto en el piloto del cap. 1

9-nov-2026. Nada generado ni gastado. Los precios en USD son de fal (leídos hoy con `get_pricing` y los schemas). Los créditos de Kling son **estimación**: el MCP no entrega el costo por segundo.

**La idea en una línea:** la cámara se dirige en Blender en las 17 llamadas, como en una película; la **voz manda el tiempo**, **Blender manda la cámara** y el **fotograma rehecho manda el look**. Antes de producir, apruebas el capítulo entero en gris con las voces, y dos pruebas chicas confirman el motor.

> **Instrucción de Cristián (9-nov, 22:40):** «podemos rehacer las tomas sí, la idea es que quede realmente cinemática, en el control de la cámara, por eso la idea de dirigir la cámara con Blender, con intención de película, y la imagen tiene que verse así y no IA slop». Mi primer borrador proponía previz solo en 6 llamadas para ahorrar créditos. Lo cambié: el previz va en todas, y el ahorro se busca en el número de tomas.

---

## 1. Formas de animar la cámara

Base de comparación: las 17 llamadas del v3 = 95 s de salida en Kling (duraciones enteras, mínimo 3 s), una toma.

| Método | Qué controla | Qué no | Costo por toma del capítulo | Riesgo en este capítulo |
|---|---|---|---|---|
| **A. Kling 4.0 `image_to_video`, un solo `first_image`** | Composición, vestuario y luz exactos del cuadro 0 | No acepta audio, hojas ni Elements. La cámara va solo en texto | 95 s ≈ 950 créditos (est.) | **No sirve para las 5 llamadas con voz** (regla 6). La cámara la decide el modelo: es lo que ya no funcionó |
| **B. Kling 4.0 Omni-Ref sin video** (hojas + fotogramas como referencia + `audio_1`) | Identidad y voz desde el segundo 0 | No hay primer fotograma: el encuadre queda aproximado. Cámara en texto | 95 s ≈ 950 créditos (est.) | Sin video de referencia, en este modo **nada fija el encuadre ni el lente** |
| **C. Previz en Blender → `video_1` en Kling Omni-Ref** (la que propongo) | Cámara, lente, encuadre, blocking y tiempos al cuadro. Geografía fija del vagón. Con `audio_1`, también la voz | Se cobra el video de entrada (el doble de segundos). El modelo copia la rigidez y los errores del previz | 190 s ≈ 1.900 créditos (est.). En fal: 17,9 USD | Ningún flujo del kit lo probó en Kling: toda la evidencia es de Seedance. Por eso hay prueba antes |
| **C2. El mismo previz en Seedance 2.5** | Tiene modo oficial para previz de arcilla; acepta `audio_urls` | Sin primer fotograma, mínimo 4 s. Su doc prohíbe caras reales y ya rechazó caras generadas en Disco vaquero | 25,7 USD a 480p; 55 USD a 720p | No cabe entero en el tope. Planos puntuales, o plan B si Kling no sigue el previz |
| **D. H3 Max como está preparado** | Primer fotograma + hojas + pista. Lipsync medido a 768p (correlación 0,85) | Cámara en texto | 7,2 USD (14,34 con dos semillas) | Respaldo del diálogo si Kling y Seedance fallan el lipsync |

**Por qué C en las 17, también en el diálogo:** en Omni-Ref (el único modo de Kling que acepta nuestra pista) no existe primer fotograma. Lo único que fija el lente, la altura y el encuadre es el video de referencia. Sin previz, los primeros planos de diálogo vuelven a quedar a criterio del modelo.

**Primer fotograma + video de referencia a la vez:** no lo propongo. Sin verificar y contra la regla 1.

### Dirigir la cámara como en una película

En Blender, cada plano se define con datos de cámara reales, no con adjetivos:

- **Lente y distancia:** 24–28 mm para el vagón y el pasillo, 35–40 mm para el plano medio y el two-shot, 50 mm para el diálogo, 85 mm para los ojos y la manija. Sensor de 36 mm, 9:16.
- **Altura con sentido:** a ras de piso para el maletín; a la altura de los ojos sentados en el diálogo; baja en la embestida; a la altura de la cerradura en la llave.
- **Motivo escrito por plano.** La cámara se mueve porque alguien mira, corre, golpea o entra. Si no hay motivo, va fija con el vaivén del tren.
- **La energía decide:** bloques 0–2, fija o en mano muy suave. Bloque 3, en mano que llega tarde al grito. Bloques 4–5, dentro de la acción: barrido a Hugo, cámara que corre con ellos y que retrocede cuando entran. Bloque 6, fija a propósito: el silencio después del caos. Bloque 7, en mano leve y el avance lento a la ventanita.
- **Movimiento con peso:** arranca y frena, no es lineal. La mano tiene temblor de operador, no ruido parejo.
- **Primer término:** hombros, respaldos, el marco de la ventanita, la malla del vidrio. El cuadro limpio y centrado es lo que delata la IA.
- **El golpe cae en un cuadro exacto:** el brazo que revienta el vidrio, la embestida, la cara contra la ventanita. La cámara reacciona 2 a 4 cuadros después.
- **Push-in solo donde el guion lo pide** (b2_p3 y b7_p2).

Las figuras son de tres bloques, con un color por personaje, sin caras y sin brazos salvo cuando la mano es la acción (la llave, la palma en el vidrio, la mano en la manija). El set es gris, sin textos.

### Que la imagen se vea cine y no «IA slop»

| Qué delata la IA | Qué hago |
|---|---|
| Cámara por defecto | Blender, como arriba |
| Todo iluminado y parejo | Solo fuentes que existen en el plano. Negro real entre lámparas. Media cara en sombra en el rojo. Las frases de luz van en cada prompt |
| Fotogramas base flojos | Rehacer 17 cuadros desde cero en sunburst high: 14 con fallas y 3 primeros fotogramas con luz o resolución mala |
| Grano y nitidez del modelo | Fuera de los prompts. Una sola capa de grano en el montaje, igual en toda la pieza |
| Cada toma con otro color | Un ajuste de color por locación en el montaje |
| Caras que posan y miran al lente | Actuación por tramos (qué quiere, qué gesto, qué no hace). Nadie mira a cámara. Quien no habla, boca cerrada |
| Planos que duran más que su acción | Se corta en la acción real. La voz fija el tiempo |
| Arreglar en post lo que salió mal | La toma se descarta y se rehace con la ficha corregida |

---

## 2. Cómo llevaría el proyecto

**Subagentes** (cada uno con entradas cerradas y un archivo de salida):

| Rol | Entra | Sale |
|---|---|---|
| Ficha de plano | guion, tiempos, fotograma, estado del mundo | una ficha por llamada: planos, lente, altura, motivo de cámara, actuación por tramos, lo que no se mueve |
| Previz | ficha + medidas del set | `shots/<id>.json`, render gris, copia con contador para revisar |
| Prompter | ficha + plantilla Kling | prompt en inglés con las líneas fijas |
| Corredor | payload aprobado | toma bajada, fila en `tomas.json`, saldo antes y después |
| Revisor | toma + lista §5 + pasada de vestuario | veredicto por punto, con cuadro y segundo |
| Segundo revisor | la misma toma, sin ver el primer veredicto | la falla más grave que encuentre |
| Métricas | toma o corte | duración de cada acción, entrada de cada línea contra el corte, prueba sin sonido |

Los agentes ya aprobaron caras rotas en otros proyectos. Por eso la revisión se apoya en mediciones y en dos revisores que no se ven entre sí. Lo que mide un script no lo opina un agente.

**Cómo revisa Cristián: tres páginas de visto bueno.**

1. **La película en gris + pruebas:** el capítulo completo en Blender con las voces puestas, el lipsync lado a lado, la prueba de cámara y los fotogramas rehechos. Aquí se corrige la cámara gratis.
2. **Corte 1:** el capítulo con las tomas elegidas, la §5 marcada y el costo.
3. **Final.**

Cada página trae el video, la §5 marcada, el costo real y **una** pregunta.

**Orden:** preparación y pruebas en paralelo → página 1 → diálogo → acción e insertos por locación → montaje.

---

## 3. La prueba de lipsync en español, primero

- **Plano:** c02a (dos personajes, dos líneas, 5,2 s). Tiene el caso difícil: uno habla y el otro debe tener la boca cerrada.
- **La misma pista limpia en los tres motores**, desde el segundo 0:

| Brazo | Setting | Tomas | Costo estimado |
|---|---|---:|---|
| H3 Max | 768P, pista como audio de referencia, primer fotograma | 2 semillas | ~0,9 USD |
| Kling 4.0 Omni-Ref | 720p, `audio_1`, hojas + fotograma como referencia, 6 s | 2 | ~120 créditos |
| Seedance 2.5 | 480p, `audio_urls`, hojas + fotograma como referencia, 6 s | 1 | ~1,3 USD (0 si rechaza las caras) |

- **Criterio, en este orden:** la boca calza con cada línea (desfase ≤ 2 cuadros en la entrada); quien no habla tiene la boca cerrada; la pista sale sin cambios (correlación con la original ≥ 0,8); nadie mira a cámara; las caras son las de las hojas.
- **Cómo se mide:** correlación y desfase de audio con un script. La boca, con una tira de recortes alineada con la onda de la pista, para que lo veas en un minuto.
- **Tope:** 4 USD de fal y 150 créditos.
- **Si ninguno calza:** el diálogo va en H3 a 768p (lo único medido). Si H3 tampoco convence, propongo otra cobertura para esas líneas (la voz sobre el que escucha, o de espaldas), y eso lo decides tú.

**Segunda prueba, en paralelo: cámara.** c05a (acción) y c00a (el gancho) con su previz en Kling, el previz de c05a también en Seedance, y dos controles sin previz. Responde tres cosas: si Kling sigue la cámara de Blender, si copia la rigidez de los bloques, y cuánto cuesta de verdad el video de entrada.

---

## 4. Calidad final

- **Resolución:** todo a 720p en Kling. A 1080p los créditos no alcanzan.
- **Entrega 1080×1920:** escalado en el montaje. Un escalado con modelo se decide mirando el Corte 1, con su tope aparte (precio sin verificar).
- **Grano y color:** en el montaje, como en la tabla de arriba.
- **Sonido:** un ambiente de tren continuo bajo todo el capítulo; golpes, vidrio y pitazo como efectos en sus tiempos; las voces limpias encima, con el ambiente bajando en cada línea. Los efectos pueden salir del audio que Kling genera en las tomas sin voz o de ElevenLabs (precio por verificar antes de usarlo).
- **Montaje:** se corta en la acción real de cada toma. Tope de 0,3 s entre corte y línea. La línea de Hugo entra hoy a +0,63 s: se corrige adelantando el corte, sin tocar la pista.

---

## 5. Qué no haría

- **Dos tomas en todo.** Con el previz en las 17, dos tomas de todo no caben en los créditos. Propongo dos tomas en las 5 llamadas con voz (gana la boca calzada) y una toma más retoma en las 12 sin voz. Va contra el «dos tomas siempre» del método: lo decides tú.
- **Generar a 1080p.** No cabe en créditos ni en el tope.
- **Seedance para el capítulo entero.** Cuesta más del doble y puede rechazar las caras.
- **Interpolar fotogramas** o usar último fotograma (regla 1).
- **Arreglar el lipsync en post.** Si la boca no calza, la toma se descarta.
- **Usar las voces que genere el modelo.** Siempre vuelve la pista limpia.
- **Rellenar para llegar a 75–90 s.** El capítulo dura ~70 s (regla 5).
- **Elements de Kling, captura de movimiento, set con texturas, más roles de agente.** Van al banco de ideas.
- **Cambiar de GPT Image 2.5 a otro modelo de imagen.** La regla 2 dice 2.5 sunburst high.

---

## Fuentes de precios y créditos

- fal: `get_pricing` y `get_model_schema` del conector (9-nov-2026).
- Kling, créditos por segundo (10 a 720p, 15 a 1080p): dato de un tercero, sin página oficial. [kie.ai](https://kie.ai/blog/kling-4-0-release-analysis-30-second-clips-keyframes-pricing). Otro tercero dice que no hay tarifa publicada: [nemovideo.com](https://www.nemovideo.com/blog/ai-video-models/kling-4-0-cost). **Se mide en la primera llamada.**
