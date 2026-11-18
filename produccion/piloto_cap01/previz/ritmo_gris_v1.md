# Ritmo del gris v1

Duración total sin la encuesta: **70.51 s**. Regla de Cristian (05): se recorta solo un plano que dura más que su acción + 0,5 s, nunca dentro de una línea, sin relleno; cada línea entra a 0,3 s o menos después del corte.

Las duraciones salen de `llamadas_tiempos.json` (v1c). La acción es la estimada en `tiempos_montaje_v3.json`; en el gris se verifica a ojo que la acción de cada plano quepa en su ventana.

| Plano | Llamada | Entra en el montaje | Dura | Acción (v1c) | ¿≤ acción + 0,5 s? | Línea que entra | Entra después del corte |
|---|---|---:|---:|---:|---|---|---:|
| b0_p1 | c00a | 0.00 s | 1.21 s | 1.00 s | sí |  |  |
| b0_p2 | c00a | 1.21 s | 1.79 s | 1.50 s | sí |  |  |
| b0_p3 | c00b | 3.00 s | 1.50 s | 1.00 s | sí |  |  |
| b0_p4 | c00b | 4.50 s | 1.50 s | 1.00 s | sí |  |  |
| b1_p1 | c01 | 6.00 s | 0.79 s | 0.60 s | sí |  |  |
| b1_f1 | c01f | 6.79 s | 0.71 s | 0.50 s | sí |  |  |
| b1_f2 | c01f | 7.50 s | 0.71 s | 0.50 s | sí |  |  |
| b1_f3 | post | 8.21 s | 0.80 s | 0.80 s | sí |  |  |
| b1_p2 | c01 | 9.01 s | 1.00 s | 0.80 s | sí |  |  |
| b2_p1 | c02a | 10.01 s | 3.21 s | 2.70 s | sí | Tomás: «¿Dónde estabas?» (después: «En el baño.» a 2.06 s) | 0.30 s |
| b2_p2 | c02a | 13.22 s | 1.00 s | 0.80 s | sí |  |  |
| b2_p3 | c02b | 14.22 s | 2.71 s | 2.17 s | sí | Tomás: «¿Tu papá sabe que vienes en este tren?» | 0.21 s |
| b2_p4 | c02b | 16.93 s | 4.00 s | 3.50 s | sí | Martina: «No.» (después: «Esa era la idea.» a 2.03 s) | 0.20 s |
| b3_p1 | c03a | 20.93 s | 1.29 s | 0.80 s | sí |  |  |
| b3_p2 | c03a | 22.22 s | 1.50 s | 1.20 s | sí |  |  |
| b3_p3 | c03a | 23.72 s | 2.21 s | 1.70 s | sí |  |  |
| b3_p4 | c03b | 25.93 s | 1.50 s | 1.20 s | sí |  |  |
| b3_p5 | c03b | 27.43 s | 1.00 s | 0.60 s | sí |  |  |
| b3_p6 | c03b | 28.43 s | 1.50 s | 1.00 s | sí |  |  |
| b4_p1 | c04a | 29.93 s | 1.79 s | 1.30 s | sí |  |  |
| b4_p2 | c04a | 31.72 s | 1.50 s | 1.00 s | sí |  |  |
| b4_p3 | c04a | 33.22 s | 1.21 s | 1.20 s | sí |  |  |
| b4_p4 | c04b | 34.42 s | 1.50 s | 1.00 s | sí |  |  |
| b4_p5 | c04b | 35.92 s | 3.00 s | 2.56 s | sí | Hugo: «¡Al último vagón! ¡Rápido!» | 0.63 s **(> 0,3 s)** |
| b4_p6 | c04b | 38.92 s | 2.00 s | 1.50 s | sí |  |  |
| b5_p1 | c05a | 40.92 s | 1.29 s | 1.00 s | sí |  |  |
| b5_p2 | c05a | 42.22 s | 1.50 s | 1.20 s | sí |  |  |
| b5_p3 | c05a | 43.72 s | 1.00 s | 0.60 s | sí |  |  |
| b5_p4 | c05b | 44.72 s | 1.50 s | 1.00 s | sí |  |  |
| b5_p5 | c05i | 46.22 s | 1.00 s | 0.60 s | sí |  |  |
| b5_p6 | c05b | 47.22 s | 1.50 s | 1.20 s | sí |  |  |
| b5_p7 | c05b | 48.72 s | 1.21 s | 1.00 s | sí |  |  |
| b5_p8 | c06a | 49.92 s | 1.29 s | 1.00 s | sí |  |  |
| b5_p9 | c06a | 51.22 s | 1.00 s | 0.50 s | sí |  |  |
| b6_p1 | c06a | 52.22 s | 2.00 s | 2.00 s | sí |  |  |
| b6_p2 | c06b | 54.22 s | 1.50 s | 1.20 s | sí |  |  |
| b6_p3 | c06b | 55.72 s | 2.00 s | 1.50 s | sí |  |  |
| b7_p1 | c07a | 57.72 s | 0.79 s | 0.60 s | sí |  |  |
| b7_p2 | c07a | 58.51 s | 3.62 s | 3.25 s | sí | Diego: «¡Martina! ¡Martina, ábreme!» | 0.33 s **(> 0,3 s)** |
| b7_p3 | c07a | 62.13 s | 2.67 s | 2.16 s | sí | Diego (off): «¡Te vi en el vagón 2!» | 0.10 s |
| b7_p4 | c07b | 64.80 s | 2.50 s | 2.02 s | sí | Tomás: «¿No estabas en el baño?» | 0.20 s |
| b7_p5 | c07b | 67.30 s | 1.21 s | 0.80 s | sí |  |  |
| b7_p6 | c07b | 68.51 s | 2.00 s | 2.00 s | sí |  |  |

## No cumplen

- b4_p5: «¡Al último vagón! ¡Rápido!» entra 0.63 s después del corte (tope 0,3 s)
- b7_p2: «¡Martina! ¡Martina, ábreme!» entra 0.33 s después del corte (tope 0,3 s)
