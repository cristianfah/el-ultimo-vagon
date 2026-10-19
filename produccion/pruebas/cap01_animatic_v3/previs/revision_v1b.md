# Retomas previs v1b (Parte A)

19-oct-2026. Ediciones de una variable, Nano Banana Pro, sobre el fotograma existente. Luz y tiempos no se tocan. Corte: `previs/cap01_previs_v1b.mp4` (misma pista y duraciones que v1; Hugo entra a los 37,0 s).

## Armado (sin fal)

La primera v1b se salteó PNG de otra resolución (NBP 1536×2752 y F3 1152×2048) y alargó el plano anterior. Causa: concat de imágenes a distinto tamaño, no nombres `_v1b`. Los 43 cuadros ya estaban en `frames/{id}.png`.

`monta_previs.py` ahora normaliza cada still a 480×832 y concatena. Re-armado **sin llamadas a fal**. Duración del mp4: **72,125 s / 1731 fotogramas**, igual que v1. Pistas iguales (c02@10,00, c04b@35,00, c07a@58,30, c07b@65,60).

**Corregidos que entran (5, no 6):** `b3_p1`, `b5_p5`, `b7_p2`, `b7_p5`, `b7_p6`. **`b0_p2` no se tocó.**

Verificado fotograma a fotograma contra `frames/{id}.png`: 43/43 coinciden con el EDL de v1 (Δ duración ≤ 1 fotograma por redondeo a 24 fps). Los huecos de métricas (b2_p4, b3_p1, b7_p1, b7_p2, b7_p4) ya no están. `b5_p5` corregido entra a 46,80 s.

| t in | dur | archivo | vs v1 |
| ---: | ---: | --- | --- |
| 0.00 | 1.20 | `frames/b0_p1.png` | igual |
| 1.20 | 1.80 | `frames/b0_p2.png` | igual (no retoma) |
| 3.00 | 1.50 | `frames/b0_p3.png` | igual |
| 4.50 | 1.50 | `frames/b0_p4.png` | igual |
| 6.00 | 0.80 | `frames/b1_p1.png` | igual |
| 6.80 | 0.70 | `frames/b1_f1.png` | igual |
| 7.50 | 0.70 | `frames/b1_f2.png` | igual (v1 saltaba F3 y alargaba) |
| 8.20 | 0.80 | `frames/b1_f3.png` | entra (v1 lo saltaba por 1152×2048) |
| 9.00 | 1.00 | `frames/b1_p2.png` | igual |
| 10.00 | 3.50 | `frames/b2_p1.png` | igual |
| 13.50 | 1.00 | `frames/b2_p2.png` | igual |
| 14.50 | 3.00 | `frames/b2_p3.png` | igual |
| 17.50 | 4.00 | `frames/b2_p4.png` | igual |
| 21.50 | 1.30 | `frames/b3_p1.png` | **nuevo** NBP |
| 22.80 | 1.50 | `frames/b3_p2.png` | igual |
| 24.30 | 2.20 | `frames/b3_p3.png` | igual |
| 26.50 | 1.50 | `frames/b3_p4.png` | igual |
| 28.00 | 1.00 | `frames/b3_p5.png` | igual |
| 29.00 | 1.50 | `frames/b3_p6.png` | igual |
| 30.50 | 1.80 | `frames/b4_p1.png` | igual |
| 32.30 | 1.50 | `frames/b4_p2.png` | igual |
| 33.80 | 1.20 | `frames/b4_p3.png` | igual |
| 35.00 | 1.50 | `frames/b4_p4.png` | igual |
| 36.50 | 2.50 | `frames/b4_p5.png` | igual |
| 39.00 | 2.50 | `frames/b4_p6.png` | igual |
| 41.50 | 1.30 | `frames/b5_p1.png` | igual |
| 42.80 | 1.50 | `frames/b5_p2.png` | igual |
| 44.30 | 1.00 | `frames/b5_p3.png` | igual |
| 45.30 | 1.50 | `frames/b5_p4.png` | igual |
| 46.80 | 1.00 | `frames/b5_p5.png` | **nuevo** NBP (mano derecha) |
| 47.80 | 1.50 | `frames/b5_p6.png` | igual |
| 49.30 | 1.20 | `frames/b5_p7.png` | igual |
| 50.50 | 1.30 | `frames/b5_p8.png` | igual |
| 51.80 | 1.00 | `frames/b5_p9.png` | igual |
| 52.80 | 2.00 | `frames/b6_p1.png` | igual |
| 54.80 | 1.50 | `frames/b6_p2.png` | igual |
| 56.30 | 2.00 | `frames/b6_p3.png` | igual |
| 58.30 | 0.80 | `frames/b7_p1.png` | igual |
| 59.10 | 3.60 | `frames/b7_p2.png` | **nuevo** NBP |
| 62.70 | 2.90 | `frames/b7_p3.png` | igual |
| 65.60 | 2.70 | `frames/b7_p4.png` | igual |
| 68.30 | 1.20 | `frames/b7_p5.png` | **nuevo** NBP |
| 69.50 | 2.60 | `frames/b7_p6.png` | **nuevo** NBP |

## b5_p5: no se volteó

El cuadro no es mano sobre fondo neutro: se ve el marco remachado, el vidrio roto y el interior rojo del vagón. **Edición NBP** que deja la mano derecha (pulgar abajo, dorso a cámara, muñeca entra por la izquierda). No se invierte el 180° respecto de b5_p4 (puerta a la izquierda del plano ancho) ni de b5_p6 (otra puerta, último vagón). `ESTADO_carmen_palma.png` no se tocó.

## Fotogramas

| Plano | Qué cambió | Toma |
| --- | --- | --- |
| b7_p6 | Hugo de cuerpo entero borrado; queda la mano en la manija, sin llave | nbp_0 |
| b7_p2 | Vidrio seco, fuelle oscuro, manchas oscuras (2.ª pasada: menos rojo vivo) | nbp_1 |
| b7_p5 | Igual que b7_p2; mano derecha de Diego en el vidrio | nbp_1 |
| b3_p1 | Edición de b0_p2 actual: sin mano ni bota; maletín al pasillo; el hombre sigue sentado | nbp_0 |
| b5_p5 | Mano derecha, puerta intacta (no flip) | nbp_0 |

## Gasto de esta tanda

7 llamadas NBP × 0,15 USD = **1,05 USD** (5 primeras + 2 para oscurecer manchas de b7_p2/p5).

Acumulado fal de la rama: **5,56 USD** de 40.
