# Fichas de personajes — v2 (referencias generadas)

Base: `fichas_personajes_v1.md`. Las anclas, el vestuario y lo que hay que evitar siguen vigentes; esta versión registra las referencias generadas y las correcciones aplicadas.
**Estado:** revisadas por el revisor de casting y continuidad. **Pendientes de la aprobación de Cristian.**
Drive: `imagenes/03_para_aprobacion/personajes` ([enlace](https://drive.google.com/drive/folders/14lyjcAAE0JPnAqUGUhNvdLl9mWNCm1Jr)), con la fila del elenco `00_elenco.jpg`. Las candidatas descartadas están en `imagenes/02_candidatos_fal/personajes`.

## Método

1. Cara de Midjourney 8.2 (`cara_<nombre>_mj01`) más vestuario de Midjourney (`vest_<nombre>_mj01`), unidos en una sola pasada que ya incluye las correcciones de la revisión de casting. Los prompts están en `produccion/assets/prompts_fal/personajes/u_<nombre>.txt`.
2. La hoja de personaje (16:9) se genera desde la unión (`h_<nombre>.txt`).
3. Cada hoja admite como máximo una corrección de una sola variable (`c_*.txt`). Si la corrección no funciona, se mantiene la original y la falla queda anotada.

## Resultados

| Personaje | Referencia de cuerpo entero | Hoja | Correcciones aplicadas | Nota para Cristian |
|---|---|---|---|---|
| Martina | `REF_martina` (Flare) | `HOJA_martina` (NBP) | Pelo seco al hombro, lunar en el pómulo izquierdo. El vestuario se describió en texto, porque faltaba el de Midjourney | La hoja NBP es la más fiel a la cara de Midjourney. En rojo se lee oscura por el abrigo carbón; conviene el abrigo abierto o sin abrigo en los planos clave |
| Tomás | `REF_tomas` (Flare) | `HOJA_tomas` (NBP) | Anteojos de metal de marco completo y fino, expresión menos fría | Sale algo atlético. Si se ve más guapo que Diego, la variable que hay que tocar es la contextura («un poco blando»), no la cara |
| Diego | `REF_diego` (Flare + `c_diego_barba`) | `HOJA_diego` (+ `c_hoja_diego_ropa`) | Barba pareja de tres días en vez de bigote con chivita; chaqueta de lona color piedra clara | Es el más claro del elenco: la mancha de la manga se va a leer en la ventanita |
| Carmen | `REF_carmen` (Flare) | `HOJA_carmen` (+ `c_hoja_carmen_raices`) | Raíces canosas en vez de mechón, bolso en el hombro izquierdo, zuecos lisos | Las raíces no forman una franja perfecta, pero se leen como crecidas |
| Iván | `REF_ivan` (Flare) | `HOJA_ivan` (Flare) | Sin heridas frescas, sin etiqueta en el pecho, polvo solo en las rodillas y las puntas de las botas | En los primeros planos el cuello de la chaqueta parece cuero. La referencia de material es la lona del cuerpo entero; se corrige en el keyframe si el plano lo muestra |
| Don Hugo | `REF_hugo` (Flare) | `HOJA_hugo` (NBP) | Gorra con una rueda simple sin letras; chaqueta bajo la cadera que tapa el cinturón (para el inserto del revólver del 0:11) | La hoja NBP es la más fiel a la cara |
| Pareja extra | `REF_extra_pareja_camisa_azul` (Flare) | `HOJA_extra_pareja_camisa_azul` (Flare) | Camisa azul cobalto fuerte | Bajo luz roja la camisa se vuelve negra. Ver la pregunta abierta sobre el 0:19 |

## Pendientes

- Aprobación de Cristian de las siete referencias.
- Estado «Diego mojado y herido» (prompt en v1). Se genera desde `REF_diego` cuando se apruebe.
- Decidir si «South American» se cambia por «Chilean» en los prompts.
