# Plan de montaje: capítulo 1, prueba de cold open y escena 1

Armado de prueba v1: `produccion/pruebas/cap01_montaje_v1/cap01_prueba_montaje_v1.mp4` (480×854, 24 fps, 20,4 s). Tiene el audio que generó el modelo, sin música, sin textos ni sobreimpresiones. Lo arma ffmpeg desde `edl.txt`, en la misma carpeta. Las URLs de los keyframes y videos elegidos están en `urls.json`; las de fal pueden vencer, así que conviene descargar lo que se quiera conservar.

## 1. Línea de tiempo

| # | Plano | Clip | In | Out | Dura | Acumulado | Qué se ve |
|---|---|---|---|---|---|---|---|
| 1 | c01_p01 | c01_b01 | 1,80 | 3,30 | 1,50 | 1,50 | La mano de Diego se apoya en el vidrio, con luz roja |
| 2 | c01_p02 | c01_b02 | 2,10 | 3,40 | 1,30 | 2,80 | Martina, luz roja: «Diego…» (la voz cae en 2,49–2,90) |
| 3 | c01_p03 | c01_b03 | 0,00 | 3,50 | 3,50 | 6,30 | Plano de dos, Tomás y Martina, luz ámbar (tarjeta de Tomás) |
| 4 | c01_p04 | c01_b03 | 3,66 | 5,30 | 1,64 | 7,94 | Primer plano de Martina (tarjeta de Martina) |
| 5 | c01_p05 | c01_b04 | 1,60 | 3,00 | 1,40 | 9,34 | Inserto: el celular se enciende, 23:38 «Estoy en el tren.» |
| 6 | c01_p06 | c01_b03 | 5,46 | 7,80 | 2,34 | 11,68 | Plano de dos: Martina da vuelta el celular |
| 7 | c01_p07 | c01_b03 | 7,96 | 10,46 | 2,50 | 14,18 | Carmen duerme contra la ventana (tarjeta de Carmen) |
| 8 | c01_p08 | c01_b03 | 10,62 | 12,20 | 1,58 | 15,76 | Iván, brazos cruzados (tarjeta de Iván) |
| 9 | c01_p09 | c01_b05 | 0,50 | 3,20 | 2,70 | 18,46 | Hugo se agacha a recoger el boleto (tarjeta de Hugo) |
| 10 | c01_p10 | c01_b06 | 0,20 | 1,80 | 1,60 | 20,06 | Inserto: se abre la chaqueta y se ve el revólver |

Los cortes internos de c01_b03 los hizo el modelo en 3,58, 5,38, 7,88 y 10,54 s. Los in y out dejan 2–3 fotogramas de margen a cada lado del corte.

Duración: 20 s, contra los 16 s del guion técnico. La diferencia está en p06, p07 y p09, que se dejaron largos para ver la actuación. Si hay que acercarse a los tiempos del guion, se recortan en este orden: p06 a 1,4 s, p09 a 2,0 s y p07 a 2,0 s.

## 2. Cortes
- **1 → 2:** corte seco sobre el golpe en el vidrio. La mirada de Martina a cuadro izquierdo responde a la mano.
- **2 → 3:** el salto de tiempo es por corte, sin sobreimpresión. Lo explican el cambio de luz de rojo a ámbar, el pelo de Martina (suelto contra cola ordenada) y la hora 23:38 del plano 5. Se corta sobre el silencio que sigue a «Diego…».
- **3 → 4 → 5 → 6:** cortes secos. En 4 → 5 la mirada de Martina baja al celular; en 5 → 6 se corta sobre la mano que entra.
- **6 → 7 → 8 → 9:** presentación de pasajeros con cortes secos, uno por tarjeta.
- **9 → 10:** corte sobre el movimiento de la chaqueta al agacharse.

## 3. Sonido
- Se conserva el audio del modelo en todos los planos, con un fundido de 20–40 ms en cada corte para que no haya clics.
- En la versión final, el «Diego…» y los diálogos de la escena 1 se hacen con ElevenLabs y entran al video como audio de referencia, para el lipsync.
- Falta un ambiente continuo de lluvia y tren por debajo de la escena 1, para tapar los saltos de ambiente entre clips.

## 4. Textos (referencia para Cristian; no van en el armado)
Las tarjetas de nombre entran en los planos 3, 4, 7, 8 y 9, con al menos 2 s en pantalla. La de Martina (plano 4, 1,64 s) queda corta: habría que alargar el plano o pasar la tarjeta al plano 6.

## 5. Post opcional (a decidir por Cristian)
- p05: reemplazar la pantalla del celular por el gráfico propio, sin muesca.
- p09: etalonar la gorra de Hugo a gris.
- p10: borrar las balas del cinturón, o volver a generar el plano.

## Alertas
- Montajista: en c01_b06 aparecen dos balas en el cinturón entre 1 y 2 s, contra lo fijado para el revólver. Lo primero es volver a generar; el borrado en post es la alternativa.
- Montajista: c01_b02 se generó de nuevo porque la primera toma traía el «Diego…» dibujado como subtítulo. La toma descartada está en `renders/cap01/video/c01_b02_con_subtitulo/`.
