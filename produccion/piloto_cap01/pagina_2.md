# Página 2 · PARADA 1 · el gris del cap. 1 con cilindros · 18-nov-2026

**En una línea:** el capítulo entero está dirigido en Blender con los personajes como cilindros con nariz, cada uno del color de su vestuario. Cada plano tiene sus stills A/B/C, su planta y su página de storyboard, y las 17 llamadas pasan el chequeo automático y una revisión independiente. **No se gastó nada: 0 USD y 0 créditos.**

Carpeta del Drive: «piloto_cap01 · avance 2026-11-18 (gris con cilindros · PARADA 1)», dentro de la carpeta del proyecto.

## Qué mirar, en este orden

1. **Las páginas de storyboard** (`paginas/`, una o dos por bloque, 3300×2550). En cada plano hay tres cuadros de la cámara real (A inicio, B momento clave, C final), una planta vista desde arriba con la cámara y los recorridos, la cámara con nombre, lente, altura, hacia dónde mira y movimiento, y qué hay en cuadro. La luz es la del set: lámparas ámbar distintas entre sí, rojo de emergencia, tubo frío solo dentro del último vagón y el foco del rapto.
2. **El montaje de ritmo** (`cap01_gris_v1_qa.mp4`, con el plano y el segundo sobreimpresos, y `cap01_gris_v1.mp4` limpio): todo el capítulo con las voces en su segundo, en luz plana para que se lea el blocking. **No está en el Drive todavía:** pesa 4,4–4,6 MB a 720p y desde esta sesión solo suben archivos de hasta ~3 MB (ver abajo). La tabla de ritmo está en el repo (`previz/ritmo_gris_v1.md`).
3. **Los MP4 de referencia con luz real** (`refs/`) de las 8 llamadas de blocking y geografía. Son lo que va como video de referencia a Kling.
4. **Las pruebas de 4 s en borrador** (`pruebas4s/`): el video de 4 s y la hoja de storyboard de cada una. Los prompts y payloads están en el repo.

## Lo que decidí y tienes que confirmar

| Qué | Por qué |
|---|---|
| **Colores de los cilindros:** Martina avena, Tomás azul marino, Diego piedra clara, Carmen celeste, Iván café oscuro, Hugo bronce, hombre de camisa azul azul fuerte, esposa beige rosado | Salen del vestuario de cada uno. Hugo va en el bronce de sus botones porque el azul marino ya es de Tomás; Carmen va en el celeste del uniforme porque el café ya es de Iván |
| **Vagón 2: la pareja va del lado derecho** (antes, izquierdo) | El guion pide a la esposa a la derecha del cuadro en b3_p3–b3_p5. La toma candidata de c00a no se afecta |
| **Marcas fijas del grupo en el último vagón**, con Carmen en el pasillo detrás y entre Martina y Tomás | Así se la ve girar hacia Martina en b7_p3, y no queda dentro de un asiento |
| **b7_p6: la mano de Hugo en la manija no entra en cuadro;** la última mirada de Martina baja hacia la manija, fuera de cuadro abajo a la derecha | En esta geometría la manija queda detrás de la cámara. El guion la pide en primer término, desenfocada |
| **b7_p3: solo se giran hacia Martina Tomás y Carmen** | Iván está junto a la puerta y no entra en ese encuadre. Si el prompt lo nombra sin que esté en la referencia, el modelo inventa a otra persona |
| **Carmen se mira la mano** en b7_p3 y b7_p6 | Para que no mire al lente. No está en el guion; refuerza su secreto |
| **La puerta del vagón 5** queda reventada y abierta en los bloques 5 y 6, y se cierra fuera de cuadro antes del bloque 7 | Los infectados tienen que llegar al fuelle para meter la mano por la ranura (b5_p8), y la tabla prohíbe una puerta abierta detrás de Diego |
| **El maletín** queda bajo el par de asientos de la pareja, del lado del pasillo | Si va del todo bajo el asiento del hombre, el pedestal lo tapa y su esquina no se ve desde el pasillo |
| **b1_p2** se usa desde que Martina abre los ojos (1,6–2,6 s de la llamada) | Mismo largo en el montaje; incluye el empujón de la puerta |
| **b2_p1, b2_p2 y b2_p4:** se ocultan solo los asientos donde va la cámara («asiento salvaje») | Todos los asientos miran hacia adelante y el respaldo de enfrente tapaba a la pareja |
| **Plano secuencia: no** | El guion no lo pide: está escrito en planos de 1 a 1,5 s con cortes secos |

## Siguen pendientes de antes

- **Look del rojo:** sigue pendiente. El rojo del gris se ajusta en una línea (`previz/scripts/previz_luz.py`).
- **Bandolera de Martina:** sigue como está.
- **b1_f1:** con el mismo lente de b1_p1 (corte por coincidencia), la cara de Martina queda en cuadro. La revisión T2 pedía cortar en el mentón.

## Ritmo

70,51 s más la encuesta. Todos los planos cumplen «acción + 0,5 s». Dos líneas entran más de 0,3 s después del corte, y no las toqué sin tu OK:
- **b4_p5, Hugo: +0,63 s.** El guion pone el pitazo a los 0,1 s y la voz a los 0,5 s. Propuesta: correr las ventanas de c04b para que la voz quede a +0,50 s, como en el guion; b4_p4 sigue durando 1,5 s.
- **b7_p2, Diego: +0,33 s.** Propuesta: cortar 0,03 s más tarde (b7_p1 pasa a 0,83 s).

## Lo que no se ve en el gris (va en el prompt)

Las manos (la llave, la palma de Carmen, la manga de la muñeca, la bota), los ojos blancos, la niebla, las manchas del vidrio y lo que pasa de la cara. Los cilindros fijan solo dónde está cada uno, hacia dónde mira y por dónde va.

## Pruebas de 4 s (borrador; no se corre nada sin tu OK)

Hay siete, cada una con dos motores (Kling Omni a 720p y Seedance 2.5 draft a 480p) y dos brazos (A: el gris como video; B: la hoja de storyboard). **La primera recomendada es c05b, 2,0–6,0 s** (la llave gira y el grupo entra en tropel): 88 créditos de Kling y ~1,6–2,4 USD en fal por las cuatro corridas. Las siete juntas: 616 créditos y ~11–17 USD. Detalle en `previz/pruebas4s/README.md`.

## La pregunta

**¿Apruebas el gris (cámara y dirección de arte) para pasar a la prueba de b5_p7 en GPT Image 2.6 (máximo 2 tiradas, tope 1 USD), o qué planos corrijo antes?**
