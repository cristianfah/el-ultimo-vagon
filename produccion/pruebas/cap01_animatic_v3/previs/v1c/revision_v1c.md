# Previs v1c · corrida del 19-oct-2026

Montaje: `cap01_previs_v1c.mp4`, 70.5 s, 1692 fotogramas a 24 fps, 480×832, 43 planos y 44 segmentos (el de más es el negro de 0.5 s de `b4_p3`). Los cortes coinciden con `tiempos_montaje_v3.json`.

Costo de esta corrida, estimado, porque fal no devolvió monto: **8.29 USD**. El corredor dejó `gastado_usd` en 6.85 (las tarifas del lote de las llamadas V suman 6.40; los 0.45 restantes coinciden con el FIX de `b2_p4`). Sunburst, 25 llamadas, estimado 1.44. Detalle por llamada en `log_generaciones_v1c.json`. Decisiones en `log_decisiones_v1c.md`.

Regenerados en sunburst desde el PNG original (dos o más cambios, o una edición que no se podía seguir apilando): `b0_p2`, `b0_p3`, `b2_p4`, `b3_p1`, `b3_p6`, `b4_p6`, `b5_p6`, `b5_p8`, `b6_p1`, `b6_p2`, `b6_p3`, `b7_p1` a `b7_p6`. Editados y conservados (una variable, NBP o flare): `b0_p1`, `b0_p4`, `b1_f2`, `b2_p1`, `b2_p2`, `b2_p3`, `b3_p3`, `b3_p4`, `b3_p5`, `b4_p1`, `b5_p1`, `b5_p2`, `b5_p4`, `b5_p5`, `b5_p7`, `b5_p9`.

Marcados, el montaje usa el original: `b3_p2` (V04, maletín fuera del lado pasillo en las dos tomas). `b6_p1` se marcó en NBP y después entró por sunburst.

Fallas que quedaron en el corte: maletín de `b0_p2` y `b3_p1` al lado del asiento, no debajo; manga de Diego no solo en el brazo derecho; puño de Carmen sin entrar del todo al abrigo; uñas largas en `b5_p8`.

V36–V47 no se corrieron: el bloque 7 salió en un sunburst por plano.

---

# Previs v1c · Parte B + 7 arreglos de Cristian (cap. 1)

18-oct-2026, 22:55 (hora de Chile). Cristian aprobó la previs (22:45) y pidió la parte B (~5,75 USD) más siete arreglos. Después de esto la previs no vuelve a pasar por él, salvo que cambie la historia.

## Estado

- **Hecho, sin fal:** los tiempos (`../../tiempos_montaje_v3.json`), las pistas recortadas (`pistas/c02_v2`, `c07a_v2`, `c07b_v2`), `b1_f1` recortado (gratis), el negro de 0,5 s de `b4_p3` en el montaje (gratis), el lote completo de 47 ediciones (`lote_v1c.json` + `prompts/`), el corredor paso a paso (`run_lote_v1c.py`) y el montaje (`monta_previs_v1c.py`, stills a 480×832 sin barras).
- **Falta, con fal:** las 47 ediciones. Este box no tiene `FAL_KEY`. La parte A la corrió un Cursor Cloud Agent con `tools/fal_gen.py`, y el lote está listo para correrlo igual: `python3 run_lote_v1c.py --run V01`, revisar el PNG, `--accept V01 <png>`, y así en orden. Al terminar, `python3 monta_previs_v1c.py`.
- **Costo estimado:** 44 NBP × 0,15 + 3 flare × ~0,08 = **6,84 USD** sin reintentos. Tope del trabajo: 12 USD (el corredor para solo). Con lo gastado (5,56), quedaría en ~12,4 de 40.

## Tiempos (§5: acción + 0,5 s; nunca dentro de una línea; sin relleno)

Total **70,5 s** (antes 72,1). Las líneas siguen entrando 0,2 s después del corte (medido en el corte de prueba).

| Plano | Antes | Ahora | Motivo |
| --- | ---: | ---: | --- |
| b2_p1 | 3,5 | 3,2 | «En el baño.» termina a 2,70 s del plano |
| b2_p3 | 3,0 | 2,7 | «¿Tu papá sabe…?» termina a 2,17 s del plano |
| b4_p5 | 2,5 | 3,0 | v10: «¡Rápido!» termina a 2,56 s; con 2,5 s se cortaba dentro de la línea |
| b4_p6 | 2,5 | 2,0 | v10 |
| b7_p3 | 2,9 | 2,7 | «¡Te vi en el vagón 2!» termina a 2,16 s del plano |
| b7_p4 | 2,7 | 2,5 | «¿No estabas en el baño?» termina a 2,02 s del plano |
| b7_p6 | 2,6 | 2,0 | Cristian: dos miradas, corte justo al llegar a la manija |

- **c02:** para recortar P1 y P3 sin tocar ninguna línea, `c02_v2` quita 0,30 s de silencio en 3,55–3,85 s y 0,30 s en 7,50–7,80 s. La llamada pasa de 12,5 a 11,9 s.
- **c07a y c07b:** solo se recorta la cola de silencio (8,1 y 6,7 s).
- **c04b:** sin cambios (7,5 s).
- Duración pedida y resolución por llamada: en `tiempos_montaje_v3.json` (480P sin diálogo, 768P en c02, c04b, c07a y c07b).
- **Al guion (guionista):** v10 todavía dice «corte a negro un segundo después» en el bloque 7, P6. Cristian pidió cortar justo al llegar a la manija.

## Revisión de la regla de la ventana (vagón 5, bloques 2 y 4)

- **Falla:** solo `b2_p3`, con la ventana detrás de Tomás. Se rehace (V17).
- **Pasan:** b2_p1, b2_p2, b2_p4 y b4_p2, con la ventana del lado de Martina. Los generales b4_p1 y b4_p3 a b4_p6 muestran las dos filas de ventanas, como corresponde.

## Pelo de Tomás (hoja: corto, peinado con partidura)

- **Fallan** (pelo rizado o mechón en la frente): b2_p1 (V19), b2_p3 (V17), b4_p6 (V22), b5_p7 (V32) y b7_p4 (V45).
- **Pasan:** b6_p3 y b7_p3, donde se ve chico. En b4_p2 solo se ve la nuca desenfocada; para la previs se acepta.

## Otras cosas encontradas

- `b3_p1` (parte A) dejó el maletín en el pasillo. Se rehace desde el b0_p2 corregido, bajo el asiento (V03).
- `b7_p2`/`b7_p5`: Diego tiene manchas en toda la chaqueta. Pasan a quedar solo en la manga derecha (V39 y V41).
- `b5_p4`/`b5_p5`: la palma sale rojo vivo. Pasa a negro rojizo (V25 y V26).
- `b5_p3` (mano del infectado, vidrio que parece gotas) no tiene edición en el lote: se acepta para la previs y se resuelve en el prompt de video.
