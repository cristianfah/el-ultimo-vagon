# Cama-empanada · decisiones de los fotogramas

Fecha: 2026-10-21. Pieza de fahren.tv, aparte de El Último Vagón. Ocho fotogramas de una sola toma cenital fija, 20 s, 9:16, para animar después en Kling 4.0 con primer fotograma, intermedios y fotograma final.

## Dirección que quedó fija

- **Luz de día, natural y suave.** El guion v2 y el plan del productor decían dormitorio de noche con lámpara cálida. El encargo pide luz natural. La lámpara del velador está apagada y solo sirve de ancla del cuarto.
- **Una sola cámara.** El guion v2 alternaba cenital, plano medio e inserto. Acá todo es cenital, eje vertical, cama entera con piso alrededor, cabecera arriba. No hay cortes.
- **Una persona, inventada.** Mujer, piel oliva clara, pelo castaño oscuro en moño bajo, camiseta gris sin estampa, pantalón azul marino, sin joyas ni marcas. En KF0 mira hacia el lente para que la cara quede en la referencia. De KF1 a KF5 mira el trabajo. En KF6 y KF7 mira hacia arriba porque está acostada adentro.
- **Geometría de la empanada.** Borde recto a la izquierda, curva a la derecha. El relleno (plumón y dos almohadas) va en la mitad izquierda. La mitad de sábana que sobra cuelga a la derecha y después se dobla encima. La cabeza sale por la punta de abajo.
- **Talco, no harina.** El guion lo aclara entre paréntesis. El polvo es blanco y el colador es de metal.
- **Perilla ciega.** Dial redondo, sin números ni letras, para no generar texto. Aparece con el plumón (KF2) y ella la toma en KF6.
- **Cada imagen sale desde cero.** KF0 es text-to-image, sin referencia. KF1–KF7 se generan de nuevo con KF0 como única imagen de referencia. Si una sale mal, el reintento también parte de KF0, nunca de la imagen rechazada. El tope fue dos intentos por etapa.
- **Por qué el endpoint de edición.** `sunburst/edit` es el que acepta `image_urls`. El prompt no pide un retoque chico: pide reconstruir la etapa y usar la imagen solo para cámara, cuarto, cama, luz, ropa, pelo y cara.

## Precio

`GET https://api.fal.ai/v1/models/billing-events` y `/v1/models/usage` respondieron **403** con esta clave. No hay cobro real por llamada. Se anotó la tabla.

| Componente | USD | De dónde sale |
|---|---|---|
| Salida, high, 1152×2048 | 0,0424 | Mismos 2.359.296 px que 2048×1152. Calculadora de OpenAI para GPT Image 2.5 high: 1413 tokens × 30 USD/1M = 0,04239. fal publica el mismo rate y el mismo 0,05268 USD para 1024×1024 high (1756 tokens). 1152×2048 no tiene fila propia. |
| Texto | ~0,003 | 5 USD por millón de tokens de entrada. Tokens ≈ caracteres/4. |
| Referencia (solo edit) | 0,010 | La tabla de fal suma ~0,008 USD si la referencia es de hasta 1024×1024 y ~0,012 USD si es 3840×2160. 0,010 es el punto medio, no una fila. |

Diez llamadas (8 etapas + 2 reintentos). **Total de tabla: 0,5488 USD.** Tope del encargo: 3 USD.

## Revisión

| Etapa | Intento | Decisión | Por qué |
|---|---|---|---|
| KF0 talco | 1 | Aceptada | Cenital, cama completa, colchón pelado, colador con talco, una persona, dos manos, cara legible. |
| KF1 uslero | 1 | Aceptada | Sábana estirada y mitad colgando a la derecha. Las dos manos comparten el mango cercano del uslero; el gesto igual se lee. |
| KF2 relleno | 1 | Aceptada | Plumón y dos almohadas en la mitad izquierda, palmas encima, perilla visible. |
| KF3 media luna | 1 | Aceptada | Doblez en media luna, palmas en el borde, sin repulgue, lino pálido. |
| KF4 repulgue | 1 | Aceptada | Las dos manos pinzan la curva y arman la cuerda de pliegues. |
| KF5 huevo | 1 | Rechazada | La brocha pinta el centro, no el borde. |
| KF5 huevo | 2 | Aceptada con reserva | El repulgue se lee mejor y ya tiene huevo, pero la brocha sigue en la cara plana, justo por dentro de la cuerda. No había un tercer intento. |
| KF6 adentro | 1 | Aceptada | Solo la cabeza afuera, mano en la perilla, piso izquierdo vacío. La empanada queda más chica que en KF3–KF5. |
| KF7 dorada | 1 | Rechazada | Quedó arrodillada fuera, con el tenedor junto a la cara. |
| KF7 dorada | 2 | Aceptada | Está adentro y la mano sale con el tenedor contra el repulgue. Las púas apoyan; no se ven clavadas. |

**La etapa más débil es KF5.** En los dos intentos la brocha cae en la masa plana y no en el repulgue. El borde se ve húmedo, pero el gesto no es el del encargo.

Lo que más va a pelear la animación, además de esa brocha, es el **salto de tamaño** entre KF5, KF6 y KF7: en KF6 la media luna se achica y se centra.

## Qué se podría volver determinístico

Hoy cada fotograma se vuelve a inventar. La referencia de KF0 alinea cámara, cuarto y persona, pero no fija píxeles. El endpoint no expone semilla, así que repetir la llamada no repite la imagen.

1. **Placa vacía del cuarto.** Una sola imagen de cama, piso, velador y luz, sin persona. Todas las etapas la usan como fondo y el modelo solo cambia el colchón y el cuerpo. Eso frena el drift del velador, del marco y del encuadre.
2. **Máscara de la media luna.** Una curva fija, la misma de KF3 a KF7. El modelo cambia textura (lino, repulgue, huevo, dorado) dentro de esa máscara. KF6 dejó de respetar el tamaño porque no había máscara.
3. **Cara aparte.** Un recorte de la cara de KF0 como segunda referencia, además del plano general. En KF6 y KF7 la cara se ve de frente y es donde más se puede ir.
4. **Contacto de la herramienta.** Brocha sobre el repulgue y púas clavadas en el borde son un parche chico. Se pueden resolver con una máscara de esa zona, o componiendo la brocha y el tenedor en post sobre el fotograma que ya está bien de cuerpo y de cuarto. Es lo único que los dos intentos de KF5 no clavaron.
5. **Prompts versionados.** El bloque de cámara, cuarto y persona ya es una constante del script de esta tanda. Falta guardarlo como archivo con un hash dentro del log, para que un rerun use el mismo texto y no una copia editada a mano.
6. **Costo.** Con permiso de `billing-events` el log guardaría el cargo real en vez de la tabla. La fórmula (1413 tokens de salida, texto a 5 USD/1M, referencia entre 0,008 y 0,012) ya está escrita y se puede aplicar sola.
7. **Contrato con Kling, no con la imagen.** Primer fotograma KF0, final KF7, intermedios KF2, KF4 y KF6. KF1, KF3 y KF5 quedan de guía si el video se salta un paso. Eso no hace falta generarlo de nuevo.
