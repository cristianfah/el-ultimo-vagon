# Set: el último vagón — v2

Reemplaza la distribución y la tabla de continuidad de `set_ultimo_vagon_v1.md`. Los estados de luz (sección 3), los props (4.5) y las pruebas en situación (sección 6) de la v1 siguen vigentes.
**Estado:** cinco vistas revisadas por el equipo de agentes (continuidad y DP/arte), **pendientes de la aprobación de Cristian**.
Imágenes: carpeta de Drive `imagenes/03_para_aprobacion/set_ultimo_vagon` ([enlace](https://drive.google.com/drive/folders/1qGwhdUIiicH_7pHZB8UsnI6cPB0Fkw7K)). Las rondas anteriores están en `imagenes/02_candidatos_fal/set_ultimo_vagon/`.

## 1. Cambios respecto de la v1

| Elemento | v1 | v2 | Motivo |
|---|---|---|---|
| Filas | 8, 2 + 2 | **6, 2 + 2 (24 asientos)** | Así salió la plancha y en 9:16 se lee mejor |
| Compartimento del revisor | Puerta en el muro del fondo | **Cabina construida dentro del vagón**, en la esquina trasera, en el lugar del último par de asientos de ese lado | Una puerta en el muro trasero daría al exterior del tren |
| Asiento con cinta | Fila 3, izquierda | **Fila 5, izquierda**, contando desde la puerta. Se agrega después, sobre la base aprobada | Las placas lo ponían en filas distintas; se quitó y se agrega de forma controlada |
| Llave | En la cerradura | **Sin llave en las placas.** Solo aparece en el plano detalle del 0:23 | Si está en la placa, aparece en planos donde no corresponde |
| Plano dibujado | Espejado (freno a la izquierda) | Corregido (abajo) | Lo detectó el revisor de continuidad |

## 2. Plano del vagón (visto desde arriba, la puerta arriba)

```
          HACIA EL RESTO DEL TREN
     ┌──────────────[ PUERTA + VENTANITA ]──────────┐
     │      cerradura (izq. desde dentro)   [FRENO] │  ← freno a la derecha de la puerta
     │  ▭▭  fila 1                          fila 1 ▭▭ │
     │  ▭▭  fila 2                          fila 2 ▭▭ │
     │  ▭▭  fila 3        pasillo           fila 3 ▭▭ │  ← todos los asientos miran a la puerta
     │  ▭▭  fila 4        central           fila 4 ▭▭ │
     │  ▭▭  fila 5 (cinta)                  fila 5 ▭▭ │
     │  ▭▭  fila 6                        [CABINA ] │  ← cabina: mismo lado que el freno
     │              [ VENTANA TRASERA ]   [REVISOR] │
     └──────────────────────────────────────────────┘
                     COLA DEL TREN
```

Mirando hacia el fondo, la cabina queda **a la izquierda**; mirando hacia la puerta, el freno queda **a la derecha**. Es el mismo lado del vagón.

## 3. Continuidad (lo que no puede cambiar entre planos)

| Elemento | Se fija como |
|---|---|
| Distribución | 6 filas, 2 + 2. Todos los asientos miran hacia la puerta delantera |
| Puerta delantera | Metal gris verdoso remachado, ventanita con vidrio de malla de alambre **romboidal** (como la referencia de Cristian), tubo fluorescente encima. En la plancha del 0:45 el vidrio tiene que dejar ver una cara del otro lado |
| Tira de emergencia | Angosta y continua, en el centro del cielo, de punta a punta; difusor rojo oscuro. Apagada en ámbar, rojo profundo en el estado rojo |
| Cerradura | Placa de bronce gastada: **bocallave arriba, manija abajo**, por dentro y por fuera. A la izquierda desde dentro y a la derecha desde fuera. Bisagras a la izquierda desde fuera |
| Freno de emergencia | Manija roja, a la derecha de la puerta mirando hacia adelante |
| Cabina del revisor | Volumen remachado del piso al techo, con puerta de madera barnizada que mira al pasillo. Mirando al fondo, a la izquierda |
| Ventana trasera | Centro del muro trasero; se ven las vías y el bosque |
| Asientos | Tapiz azul marino oscuro, parejo y mate, con desgaste solo en los cabezales y el borde de los cojines. Pasamanos cromado de arco en la esquina superior del lado del pasillo |
| Resto | Cortinas crema estampadas con lazo, lámparas de lectura bajo el portaequipaje, redes, cielo abovedado con rejillas, franja de goma doble en el piso |
| Texto y logos | Ninguno, en ninguna parte |
| Herida de Diego (propuesta) | Antebrazo izquierdo |

## 4. Vistas candidatas (revisadas por los agentes)

| ID | Archivo en Drive | Modelo | Prompts aplicados (`produccion/assets/prompts_fal/`) | Uso en el cap. 1 |
|---|---|---|---|---|
| V01 | `set_v01_base_hacia_puerta.png` | GPT Image 2.5 Flare | `set_ultimo_vagon_base` → `c01_base_sin_llave` → `c07_base_sin_cinta` | Plancha maestra; planos hacia la puerta |
| V02 | `set_v02_eje_inverso_cabina.png` | Nano Banana Pro | `set_eje_fondo_fix` → `c02_eje_fondo_tapiz` → `c03_eje_fondo_cabina` → `c08_eje_fondo_pasamanos` | Contraplano hacia el fondo, Hugo y la cabina |
| V03 | `set_v03_puerta_interior.png` | GPT Image 2.5 Flare | `set_puerta_interior` → `c04_puerta_int_sin_llave` | Diego en la ventanita (0:45), PS-02 |
| V04 | `set_v04_puerta_exterior_fuelle.png` | GPT Image 2.5 Flare | `set_puerta_exterior` → `c05_puerta_ext_ventanita` → `c09_puerta_ext_bocallave` | Contraplano de Diego desde el fuelle |
| V05 | `set_v05_lateral_asientos.png` | GPT Image 2.5 Flare | `set_lateral_asientos` → `c06_lateral_tapiz` | Planos de personajes sentados |

Aparte, para el plano detalle de la llave (0:23) se usa `cand_set_puerta_ventanita_interior_flare.png` **con** la llave puesta.

Descartadas: la planta (proyección imposible) y C02 sin cabina, que queda reemplazada por V02.

Cada archivo de prompt en `prompts_fal/` está completo y listo para pegar. Se corre con `tools/fal_gen.py` (la imagen 1 es la primera de `--images`).

## 4b. Cuadros de referencia de look (revisados por los agentes)

| Archivo en Drive | Modelo | Prompt | Uso |
|---|---|---|---|
| `look_ambar_plancha_heroe.png` | GPT Image 2.5 Sunburst | `h02_plancha_heroe_ambar` (una pasada: imagen 1 = referencia de Cristian, imagen 2 = V01) | Look ámbar y azul; vagón de pasajeros 0:03–0:16 |
| `look_rojo_plancha_heroe.png` | GPT Image 2.5 Flare | `h03_plancha_heroe_rojo` (una reiluminación sobre la ámbar) | Look rojo del último vagón, desde el 0:23 |

Todas las planchas finales salen de estas dos: imagen 1 = el cuadro de look del estado que corresponde, imagen 2 = la vista técnica (V01 a V05).

## 4c. Planchas finales (revisadas por los agentes)

| Archivo en Drive | Modelo | Prompts | Uso |
|---|---|---|---|
| `look_rojo_plancha_heroe.png` | Flare | `h02` → `h03` | Hacia la puerta, rojo (también es el cuadro de look) |
| `final_rojo_p02_eje_fondo_cabina.png` | Sunburst | `p02_eje_fondo_rojo` (una pasada: look rojo + V02) | Hacia el fondo, rojo: Hugo y la cabina |
| `final_rojo_p03_puerta_interior.png` | Flare | `p03_puerta_interior_rojo` (una pasada: look rojo + V03) → `p03b_puerta_interior_bisagra` | Puerta desde dentro, 0:45 (PS-02) |

Bisagras de la puerta: solo a la derecha vistas desde dentro (a la izquierda desde fuera).

## 5. Pendientes

1. **Aprobación de Cristian** de V01 a V05.
2. Revisar en resolución completa la pieza arriba a la izquierda del marco en V03: debe leerse como pestillo, no como bisagra.
3. ~~Decidir la fuente de la luz roja.~~ Decidido: una **tira de emergencia** en el centro del cielo. Las vistas V01 a V05 quedan como **plano técnico** (distribución y continuidad); las planchas finales se rehacen en una sola pasada (ver `prompts_fal/h01_plancha_heroe_ambar.txt` y `biblia/decisiones.md`).
4. Vistas que faltan, en este orden:
   1. Tres cuartos hacia la puerta, desde la fila 3, con espacio para seis personas (0:31–1:19).
   2. La esquina trasera, en tres cuartos hacia la cabina y la ventana trasera, para el 0:37.
   3. El vestíbulo y el fuelle, con la «esquina» del vagón anterior; tiene que coincidir con lo que se ve por la ventanita de V03.
   4. El vagón de pasajeros, editado sobre V01: puerta en los dos extremos, sin cabina ni ventana trasera. Más su contraplano para Iván (0:19).
   5. La cinta en la fila 5 izquierda, sobre la base aprobada.
5. **Estados de luz:**
   - Ámbar solo para el vagón de pasajeros (0:03–0:16).
   - Rojo para todas las vistas del último vagón (desde el 0:23).
   - En la versión roja de V04 se apaga el tubo blanco del lado del fuelle.

## 6. Regla de revisión

Ninguna imagen se propone para aprobación sin pasar antes por el equipo de agentes: el revisor de continuidad y el DP/arte. Cada corrección cambia una sola variable y se vuelve a revisar. Solo Cristian aprueba.
