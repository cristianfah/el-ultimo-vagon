# Revisión de assets v10 contra `revision_v1.md` sección 5

19-oct-2026. Dos tomas por asset. F1 no se generó: falta el fotograma P1 del tren como referencia de composición.

Costo real de esta tanda: **1,33 USD** (5 assets 1,03 + palma v2 0,30; tope de tanda 3 USD; tope del v3: 40 USD, techo).

| Ruta | Modelo | Costo USD | Sección 5 |
| --- | --- | ---: | --- |
| `assets/F08_v2_ambar_bajo.png` (toma 1) | Nano Banana Pro | 0,15 | sí |
| `assets/raw/F08_v2_ambar_bajo_nbp_0.png` | Nano Banana Pro | 0,15 | no |
| `assets/cuarto_rapto_martina_v2.png` (toma 0) | Nano Banana Pro | 0,15 | sí |
| `assets/raw/cuarto_rapto_martina_v2_nbp_1.png` | Nano Banana Pro | 0,15 | no |
| `assets/PANTALLA_tomas_anden.png` (toma 0) | GPT Image 2.5 Flare | 0,068 | sí |
| `assets/raw/PANTALLA_tomas_anden_flare_1.png` | GPT Image 2.5 Flare | 0,068 | sí |
| `assets/ESTADO_hombre_azul_infectado.png` (toma 0) | GPT Image 2.5 Flare | 0,068 | sí |
| `assets/raw/ESTADO_hombre_azul_infectado_flare_1.png` | GPT Image 2.5 Flare | 0,068 | no |
| `assets/ESTADO_carmen_palma.png` (toma 1) | GPT Image 2.5 Flare | 0,080 | sí |
| `assets/raw/ESTADO_carmen_palma_flare_0.png` | GPT Image 2.5 Flare | 0,080 | sí |
| `assets/ESTADO_carmen_palma_v2_palma.png` (toma 1) | Nano Banana Pro | 0,15 | sí |
| `assets/raw/ESTADO_carmen_palma_v2_palma_nbp_0.png` | Nano Banana Pro | 0,15 | no |

Las copias en `assets/*.png` son las tomas elegidas. Las que fallan quedan solo en `raw/`. `ESTADO_carmen_palma.png` no se toca: sigue como primer fotograma de c05i. La v2 es el estado de c06b.

## Qué se vigiló (sección 5 + notas del productor)

- **F08:** ventanita negra, sin cielo ni lluvia detrás de la puerta; ámbar bajo. La toma 0 se descarta porque deja ~6 lámparas. La toma 1 pasa, con la salvedad de 4 lámparas en vez de 3.
- **Rapto v2:** misma silla, sin cuerda, cinta gris, muñecas sobre los muslos. La toma 1 se descarta: un puente de cinta separa las muñecas.
- **Pantalla:** sin letras, números, hora ni logos. Las dos pasan; se elige la 0 por la franja oscura más limpia.
- **Hombre azul:** camisa de la hoja, venas hasta la mandíbula. La toma 1 se descarta porque las venas suben al pómulo.
- **Palma de Carmen (c05i):** mano **derecha**, corte fino, sin cielo ni lluvia al fondo. Las dos pasan; se elige la 1 porque el tajo se lee.
- **Palma v2 (c06b, prompt §6 exacto, dos tomas NBP sobre el asset de c05i):** la toma 0 es mano izquierda (se descarta). La toma 1 pasa: palma derecha hacia cámara, corte en el talón.
