# Registro de decisiones

Formato: fecha · decisión · motivo.

## 2026-09-28
- **Reel de zombies con acción y gore melee**, con estructura de microdrama: gancho a los 3 s, un giro y cliffhanger.
- **Proyecto VAGÓN 7** (dos agentes, un traidor): se escribió el guion v1–v3. Hoy está archivado en `archivo/vagon7/`.
- **Dirección de arte:** una luz dominante por acto, toda motivada por fuentes reales; se mantiene como base visual.

## 2026-09-29
- **Midjourney solo para explorar arte.** Las imágenes finales se hacen en Weavy.
- **Flujo de Weavy «VAGÓN 7 — Assets base»:** 52 nodos, armado pegando un JSON en el canvas.
- **Los prompts de imagen se reescriben con la plantilla de rodaje.** Motivo: la prueba de look salió con estética genérica de IA (ruido, luz sin fuente, composición de afiche).

## 2026-09-30
- **Formato de serie interactiva:** el público vota cada capítulo. Motivo: el referente de Fruit Love Island y de Love Island.
- **9:16 directo.** Se descarta el flujo 4:5 → outpaint.
- **Sin teaser.** Cristian maneja las encuestas en las plataformas.
- **Se cambia la premisa, de agentes a pasajeros comunes** (EL ÚLTIMO VAGÓN). Motivo: la gente no se ve reflejada en un agente; el conflicto tiene que ser cotidiano.
- **Triángulo en el centro.** Motivo: con dos personajes no hay a quién elegir.
- **Don Hugo tiene un revólver con dos balas.**
- **Reglas del mundo: opción 1, primer día.** Nadie sabe las reglas. Se descartó un tren de evacuación con control sanitario porque resolvía todo demasiado bien.
- **El tren se detiene más adelante** por el freno de emergencia. Motivo: da razones para entrar y salir del vagón y lo aleja de Snowpiercer.
- **Método de assets:** en Midjourney 8.2 la cara y el vestuario se exploran por separado, y se unen en GPT Image 2.5 (en paralelo con Nano Banana Pro) en Weavy. Motivo: MJ 8.2 no sostiene una cara entre imágenes; separadas, la cara no cambia con cada variación de ropa. Plan en `produccion/assets/plan_assets_v1.md`.
- **Los sets salen de una plancha maestra:** los estados de luz y los ángulos se editan sobre la misma imagen, no se generan de cero. Motivo: en la prueba 1 el vagón cambiaba de un plano a otro.
- **La manija del freno de emergencia se planta desde el capítulo 1** en el set, junto a la puerta. Motivo: cuando alguien la tire en el capítulo 3, el público tiene que poder decir que estaba ahí.
- **Propuestas de casting visual pendientes de aprobación** (`direccion_arte/personajes/fichas_personajes_v1.md`): herida de Diego en el antebrazo izquierdo, reloj de enfermera para Carmen y sin hacha en el último vagón.
- **fal.ai entra al pipeline** para las ediciones con GPT Image 2.5 (Flare y Sunburst) y Nano Banana Pro, con `tools/fal_gen.py`. Weavy se mantiene para los flujos de nodos. Motivo: es más rápido, se puede automatizar y cada corrección queda guardada como archivo de prompt.
- **El repositorio de imágenes vive en Drive**, en la carpeta privada del proyecto, y se sube con `tools/drive_sync.py`. Motivo: falta de espacio en disco local.
- **Ninguna imagen se propone para aprobación sin pasar por el equipo de agentes** (continuidad y DP/arte). Las correcciones son de una sola variable. Motivo: lo pidió Cristian, para cuidar la continuidad.
- **Set del último vagón, v2** (`direccion_arte/sets/set_ultimo_vagon_v2.md`). Pendiente de la aprobación de Cristian.
  - Son 6 filas de 2 + 2.
  - El compartimento del revisor es una cabina construida en la esquina trasera, del mismo lado que el freno.
  - No hay llave en las placas.
  - La cinta va en la fila 5 izquierda.
  - Motivo: la revisión de continuidad encontró la puerta del revisor dando al exterior, la llave en planos donde no corresponde y la cinta en filas distintas.
- **La luz roja sale de una tira de emergencia en el centro del cielo del vagón.** Motivo: Cristian la prefiere; tiene más sentido que las rejillas.
- **En el vagón de pasajeros, los asientos miran hacia su puerta delantera, igual que en el último vagón.** Motivo: es el mismo modelo de vagón, y en los contraplanos los asientos tienen que verse de frente.
- **La cámara de la utilería no puede parecerse a la de un modelo de marca** (por ejemplo, el celular de Martina). Motivo: es propiedad intelectual ajena; la revisión descartó dos versiones del celular.
- **Las vistas con luz neutra pasan a ser el plano técnico del set, no planchas finales.** La dirección de arte se fija antes de las planchas finales, con un cuadro de referencia por estado de luz. Cada plancha final se genera en una sola pasada (referencia de look más plano técnico) y admite como máximo una corrección, siempre sobre la pasada limpia. Motivo: con las ediciones en cadena aparece el ruido típico de la IA y se pierde el look cinematográfico de la referencia ámbar y azul.
- **2026-10-01 · Cristian aprueba los assets v1**, que pasan a `imagenes/04_aprobados` en Drive (registro con URLs en `produccion/assets/aprobados_v1.md`). Incluye las planchas F01 a F12, los cuadros de look y las vistas técnicas, los cuatro props, las referencias y hojas de los seis personajes y la pareja extra, el estado de Diego y los keyframes KF01 a KF03. Motivo: hacen falta para la prueba de video con otro agente. Los cambios posteriores se hacen como `v2`, sin reemplazar lo aprobado. Las notas de revisión abiertas (contextura de Tomás, cuello de Iván, Martina y la camisa azul bajo luz roja) quedan para esa v2.
