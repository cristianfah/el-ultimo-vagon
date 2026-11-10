# Página 1 · pruebas T0, T1 y T2 · 10-nov-2026

**En una línea:** las dos apuestas del plan funcionan: Kling calza el lipsync en español con nuestra pista y sigue la cámara de Blender al cuadro, y el previz cuesta solo 20 % más. Los fotogramas rehechos están a medio camino: 5 listos, 12 con trabajo pendiente.

Paré aquí, antes de la película en gris de las 17 llamadas, como pediste.

## T0 · Lipsync en español → gana Kling

Plano c02a, la misma pista limpia en los tres motores. Medido con `scripts/medir_lipsync.py`.

| Motor | Correlación con la pista | Desfase | Bocas | Imagen |
|---|---:|---:|---|---|
| **Kling 4.0 Omni + `audio_1`** | **0,99** | **0,00 s** | Tomás habla con Martina callada, y al revés | La mejor: oscura, tres lámparas |
| H3 Max 768P | 0,98 | 0,00 s | Calzan, boca exagerada | Luz pareja, ventana azul |
| Seedance 2.5 480p | 0,63 | +0,63 s | **Tomás con la boca cerrada en su línea** | Buena, pero rehízo la pista |

- **Decisión propuesta:** el diálogo va en Kling 4.0 Omni-Ref con `audio_1`. H3 queda de respaldo. Seedance, fuera del diálogo.
- Video: `T0_lipsync_lado_a_lado_pista_limpia.mp4`. Tiras de bocas: `T0_*_bocas.png`.

## T1 · Cámara → Kling sigue a Blender

| Prueba | Resultado |
|---|---|
| c05a con previz | Mismos tres encuadres que el gris y cortes en el mismo cuadro |
| c05a sin previz | El fuelle se alarga y se ilumina, el grupo corre hacia el lente, Tomás sale duplicado |
| c00a con previz | Ojos de Martina y corte al inserto del maletín, de una sola toma |
| c05a con previz en Seedance | También lo sigue, a 480p. No supera a Kling |
| c00a con primer fotograma | Sigue en la cola de Kling; sin resultado todavía |

- **El previz importa donde hay geografía y blocking** (c05a). En un primerísimo plano (los ojos), la esfera gris no aporta: ahí manda el fotograma de look.
- Fallas de la toma c05a con previz, para la ficha final: aparece un tubo blanco en el plano 2 y Carmen grita hacia el lente al final.
- Videos: `T1_c05a_previz_con_sin.mp4`, `T1_c05a_previz_kling_seedance.mp4`, `T1_c00a_previz_vs_kling.mp4`.

## T2 · Fotogramas → 5 listos, 7 con un edit, 5 por rehacer

Los 17 se generaron en Nano Banana 2.1 y GPT Image 2.6 con el mismo prompt. **GPT 2.6 ganó en 16**: reconstruye la luz y los lados. Nano Banana se queda pegado al cuadro de referencia.

Un segundo revisor independiente, con recortes a resolución completa, encontró lo que yo no vi mirando en chico:

| Estado | Cuadros |
|---|---|
| **OK** | b1_p1, b2_p1, b3_p1, b4_p1, b4_p4 |
| **Un edit puntual** | b1_f1 (recorte), b2_p3 (anteojos), b2_p4 (bolso), b3_p2 (pierna), b5_p8 (uñas), b6_p3 (mano), b7_p2 (gotas) |
| **Rehacer** | b4_p5 (Hugo casi mira al lente), b5_p4 (sangre roja; mano izquierda), b5_p7 (acolchado; dos anteojos), b6_p2 (mano izquierda), b7_p5 (un solo brazo) |

- Lo que sí quedó resuelto: maletín bajo la banca, hombre sentado, Tomás en su asiento, nadie mira directo a cámara, luz ámbar con negro real.
- Hojas: `T2_fotogramas_antes_despues_{1,2}.jpg`. Detalle: `revision/T2_revision_2_fotogramas.md`.

## Costos reales

| | Tope | Gastado |
|---|---:|---:|
| Créditos de Kling, T0 + T1 | 450 | **318** (saldo 3.176 → 2.858) |
| fal, T0 + T1 + T2 | 11 USD | **~7,2 USD estimados** (fal no entrega el cobro: hay que leerlo en el panel) |

**Tarifas medidas en Kling a 720p:** 10 créditos por segundo sin video; **12 con previz** de la misma duración. El plan suponía 20.

**Qué cambia en el plan:** las 17 llamadas con previz cuestan ~1.140 créditos por toma. **Dos tomas de todo el capítulo son ~2.280 créditos y quedan 2.858.** Ya no hace falta bajar a una toma en las llamadas sin voz.

## Lo que necesito que decidas

1. **¿Sigo con la película en gris de las 17 llamadas?** Es gratis (Blender local) y es donde se corrige la cámara antes de gastar.
2. **Look del rojo:** hoy la luz roja tiñe el vagón pero no las caras. ¿Lo quieres así (como el KF02 aprobado) o con las caras en rojo de verdad?
3. **Fotogramas:** ¿corro los 7 edits puntuales ahora y dejo los 5 por rehacer para cuando exista su cuadro gris de Blender?
4. **Bandolera de Martina:** la dejé en todos los planos, como su hoja. ¿Confirmas?
