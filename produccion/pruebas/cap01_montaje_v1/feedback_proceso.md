# Feedback de Cristian sobre el proceso (prueba de montaje v1, 2026-09-30)

**No es feedback del contenido.** Faltan los assets definitivos, el prompting y la iluminación. Esto trata sobre **qué herramientas y qué reglas necesita cada rol** para que el proceso sea casi automático y no repita estos errores.

Cada observación tiene la causa en el proceso (con evidencia del repo), la herramienta o regla que falta y el rol responsable. Se aplican de a una, como el resto de `mejoras.md`.

---

## 1. La cámara no trabaja

**Lo que se vio:** planos quietos. Con la cámara quieta se nota más la IA y el reel pierde atención.

**Causa:** nosotros lo pedimos. En `cap01.yaml`, 8 de los 10 planos llevan `locked-off, static camera` o `handheld, subtle breathing, no reframing`. El prompt del Director de fotografía empuja a eso: «una sola intención de cámara… los modelos fallan con movimientos compuestos» y «interiores: cámara en mano». Nadie tenía como tarea que el plano **se viera atractivo**.

**Qué falta:**
- **Regla nueva:** ningún plano queda fijo por defecto. La cámara quieta solo se usa con motivo, y ese motivo se escribe en el plano.
- **Gramática de cámara por escena** (ya está en `mejoras.md` #2): qué se mueve, cuándo y por qué. El movimiento tiene que ser coherente con la escena y a la vez dinámico para reel.
- **Herramienta: catálogo de movimientos probados** (`produccion/camara/catalogo.md`). Cada movimiento lleva la frase exacta que obedece H3 Max o Kling, un clip de ejemplo, en qué tipo de plano funciona y en cuál falla. Se llena con una tanda de prueba barata: el mismo keyframe con 6–8 movimientos a 480P, unos 2 USD. El Director de fotografía elige solo desde el catálogo, así sabe qué va a salir.
- **Herramienta de post: movimiento digital.** El Montajista puede agregar empujes, reencuadres y temblor de impacto sobre el clip escalado (con ffmpeg `zoompan` o en After Effects). Es barato, se automatiza y rescata planos que salieron quietos. No reemplaza al movimiento real; es la red de seguridad.

**Rol:** Director de fotografía (catálogo y gramática), Productor de impacto (lo exige y lo revisa), Montajista (movimiento digital).

## 2. La actuación no tiene intención

**Lo que se vio:** la mano solo toca el vidrio. Martina dice «Diego…» sin intención. En la pareja, ella nunca mira a Tomás.

**Causa:** el Director escribe la actuación con la regla «quietud y mirada, nunca emociones». Eso evita la sobreactuación, pero deja al modelo sin objetivo. Además, la mirada no tiene un destino: nadie escribe *a quién* mira ni *cuándo*.

**Qué falta:**
- **Actuación escrita como acción con objetivo:** qué quiere el personaje en el plano, qué verbo hace el cuerpo (golpea para que le abran, se aferra, rechaza) y el beat con tiempos (0–1 s, 1–2 s…). Ya está propuesto en `mejoras.md` #1; aquí se suma la intención.
- **Miradas con destino y tiempo:** «mira la ventana (0–1,5 s), gira hacia Tomás (1,5 s) y le sostiene la mirada». En planos de dos personas es obligatorio.
- **Herramienta a probar: referencia de actuación en video.** H3 Max `reference-to-video` acepta videos de 2–15 s. Cristian o alguien del equipo graba el gesto con el celular (la mano en el vidrio, el giro de cabeza) y entra como `Video 1`. Cuesta más en tokens, así que se usa solo en planos clave. Hay que probarlo (prueba 5 de `investigacion_referencias.md`).

**Rol:** Director (intención y miradas), Prompter (lo compila en el beat), Control de calidad (revisa que la mirada ocurra).

## 3. El set no está delimitado

**Lo que se vio:** en el plano de Martina con luz roja, el fondo se mueve como si fuera la ventana lateral del tren, pero ella mira la ventanita de la puerta. En el plano abierto de la pareja, el celular se deforma en el regazo.

**Causa:** la locación existe solo como una o dos fotos («placas»). El modelo no sabe qué hay detrás de cada vidrio ni qué se mueve y qué no. Los props chicos no tienen referencia propia.

**Qué falta:**
- **Herramienta: biblia del set** (`direccion_arte/set_ultimo_vagon.md` + assets en Weavy):
  - Plano de planta del vagón: asientos numerados, dónde está cada personaje, puertas, fuentes de luz.
  - **Tabla de vidrios:** las ventanas laterales muestran bosque nocturno y lluvia en movimiento; la ventanita de la puerta muestra el vestíbulo, **quieto respecto del vagón**. Cada plano hereda la frase correcta según hacia dónde mira la cámara.
  - Placas del set desde 4–6 ángulos fijos (hacia la cabeza, hacia la cola, lateral, puerta de cerca), con las mismas luces.
- **Herramienta: hoja de props clave:** el celular (frente, dorso, pantalla apagada y encendida, en la mano y en el regazo), el revólver y la llave. Entran como referencia en todo plano donde aparecen, aunque sean chicos.
- **Regla:** en planos abiertos, el prop chico va quieto o fuera de cuadro, salvo que la acción lo necesite.

**Rol:** Asistente de dirección (lista de assets de set y props), Continuista (tabla de vidrios y posiciones en cada plano), Control de calidad (lo verifica).

## 4. El ritmo interno es lento

**Lo que se vio:** los planos de presentación, sobre todo el de Hugo agachándose, duran más de lo que la acción pide.

**Causa:** H3 Max genera 5 s como mínimo y estira la acción para llenar el clip.

**Qué falta:**
- **Prompter:** la acción termina en un tiempo fijo («he is fully crouched by 1.5 s») y después pasa otra cosa o hay un corte.
- **Herramienta de montaje: retiming.** El Montajista puede acelerar un clip entre 1,2× y 1,5× (con ffmpeg `setpts`) cuando la acción se lee lenta. Lo anota en el plan.

**Rol:** Prompter y Montajista.

## 5. Primer y último fotograma (FL): solo en casos especiales

**Lo que se vio:** el plano del revólver (b06) sale raro. El primer y el último fotograma tienen encuadre y foco distintos, y la chaqueta del primero estaba mal puesta. Al interpolar, el modelo inventa otra chaqueta.

**Causa:** usamos FL en tres bloques (b01, b04 y b06) con dos keyframes generados por separado. `investigacion_referencias.md` lo registró como «funciona» porque la acción llegaba al final, pero **no revisó lo que pasa en el medio**. Con esta prueba, ese veredicto se cambia a «funciona solo con control total de las dos imágenes».

**Qué falta (propuesta; Cristian todavía lo está pensando):**
- **La referencia es la opción por defecto** (REF o FF + referencias).
- **FL solo cuando:**
  1. el último fotograma es una **edición** del primero (misma imagen de base, mismo encuadre, lente y luz); y
  2. el cambio es de **estado**, no de movimiento: algo aparece o desaparece, una luz se prende, una puerta se cierra.
- **Chequeo previo, a cargo de Control de calidad:** antes de gastar el video, se comparan los dos fotogramas uno al lado del otro. Si cambian el encuadre, el foco o el vestuario, el bloque no sale en FL.
- **Alternativa a probar:** darle al modelo el último fotograma como imagen de referencia (REF) en vez de `end_image_url`. Así guía el resultado sin obligar la interpolación.

**Rol:** Asistente de dirección (elige el método), Control de calidad (chequeo previo).

## 6. Control de calidad no ve el video en el tiempo

**Lo que se vio:** errores que aparecen a mitad del clip (fondo que corre, celular que se deforma, balas que aparecen). Llegaron al armado sin alerta.

**Causa:** la revisión fue sobre todo de keyframes y del resultado final de cada clip.

**Qué falta:**
- **Herramienta: tira de fotogramas por clip.** Se extraen 4 fotogramas por segundo en una hoja de contacto por bloque. Se automatiza con ffmpeg dentro del orquestador (`mejoras.md` #17).
- **Checklist de video nueva:** ¿el fondo se mueve cuando no debe (tabla de vidrios)? ¿Algún prop cambia de forma o aparece? ¿La mirada llega a su destino? ¿La cámara hace el movimiento del catálogo? ¿La acción termina a tiempo?
- **Revisión con un modelo que vea video**, no solo imágenes sueltas, para los clips que pasen la tira.

**Rol:** Control de calidad y Pipeline (el orquestador genera las tiras).

---

## Cambios por rol (resumen)

| Rol | Regla nueva | Herramienta nueva |
|---|---|---|
| Director | Actuación con objetivo y verbo; miradas con destino y tiempo | Referencia de actuación en video (a probar) |
| Productor de impacto | Revisa que ningún plano quede fijo sin motivo | — |
| Director de fotografía | Sin cámara fija por defecto; gramática de cámara por escena | Catálogo de movimientos probados |
| Continuista | Tabla de vidrios y posiciones en cada plano | Biblia del set |
| Asistente de dirección | La referencia por defecto; FL solo con las dos condiciones | Hoja de props clave, placas del set desde varios ángulos |
| Prompter | La acción termina en un tiempo fijo | — |
| Control de calidad | Chequeo de FL antes de generar; checklist de video | Tira de fotogramas, revisión con modelo de video |
| Montajista | Puede acelerar y agregar movimiento digital, anotado en el plan | Retiming y reencuadre con ffmpeg o After Effects |

## Orden sugerido

1. **Catálogo de movimientos:** es lo que más se nota y es una prueba barata.
2. **Biblia del set y tabla de vidrios:** evita errores de mundo en todos los capítulos siguientes.
3. **Actuación con objetivo y miradas:** cambia el prompt del Director y del Prompter.
4. **Regla de FL:** cuando Cristian la confirme.
5. **Tiras de fotogramas y checklist de video en Control de calidad.**
6. **Retiming y movimiento digital en el Montajista.**
7. **Referencia de actuación en video:** cuando haya un plano clave para probarla.
