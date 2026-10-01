# Set: el último vagón — v2

Reemplaza la distribución y la tabla de continuidad de `set_ultimo_vagon_v1.md`. Los estados de luz (sección 3), los props (4.5) y las pruebas en situación (sección 6) de la v1 siguen vigentes.
**Estado:** las vistas técnicas (V01 a V05), los dos cuadros de look y las once planchas finales (F01 a F11) pasaron la revisión de continuidad del equipo de agentes. **Están pendientes de la aprobación de Cristian.**
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

Carpeta de Drive: `imagenes/03_para_aprobacion/set_ultimo_vagon/finales` ([enlace](https://drive.google.com/drive/folders/1ryV_s6_TSgVIUrEWwPDLpdNFTFo_6EcB)), con la hoja de contactos `00_hoja_contactos_set.jpg`. Las candidatas descartadas están en `imagenes/02_candidatos_fal/set_ultimo_vagon/planchas_finales_rojo`.

| Archivo | Modelo | Prompts (`prompts_fal/`) | Lente | Uso en el cap. 1 |
|---|---|---|---|---|
| `F01_rojo_ultimo_vagon_hacia_puerta` | Flare | `h02` → `h03` | 24 mm | Plano general hacia la puerta, 0:23–1:19 |
| `F02_rojo_ultimo_vagon_hacia_fondo_cabina` | Sunburst | `p02_eje_fondo_rojo` | 24 mm | Contraplano hacia el fondo, Hugo y la cabina |
| `F03_rojo_puerta_desde_dentro_0-45` | Flare | `p03_puerta_interior_rojo` → `p03b_puerta_interior_bisagra` | 35 mm T2.8 | Diego en la ventanita, 0:45 (PS-02), Carmen en el 0:58 |
| `F04_rojo_puerta_desde_fuelle` | NBP | `p04_puerta_exterior_rojo` → `p04b_puerta_ext_ventanita_rojo` | 35 mm T2.8 | Contraplano de Diego desde fuera |
| `F05_rojo_tres_cuartos_hacia_puerta` | NBP | `p05_tres_cuartos_puerta_rojo` → `p05b_tres_cuartos_artefacto` | 35 mm T2.8 | Grupo frente a la puerta, 0:31–1:19 |
| `F06_rojo_esquina_trasera_0-37` | Sunburst | `p06_esquina_trasera_rojo` | 50 mm T2 | Inserto de Hugo y el revólver, 0:37 |
| `F07_rojo_fuelle_vestibulo` | Sunburst | `p07_fuelle_vestibulo_rojo` | 35 mm T2.8 | Lo que se ve por la ventanita, 0:28, 0:45 y 1:08 (la esquina por donde aparecen los infectados) |
| `F08_ambar_pasajeros_hacia_puerta` | Flare | `p08_vagon_pasajeros_ambar` | 32 mm T4 | Vagón de pasajeros, 0:03–0:11 |
| `F09_ambar_asiento_pareja` | Sunburst | `p09_asiento_pareja_ambar` | 50 mm T2 | Martina y Tomás, 0:03 (PS-01) |
| `F10_rojo_pasajeros_hacia_puerta` | Flare | `p08` → `p11_vagon_pasajeros_rojo` | 32 mm T4 | Cambio de luz del 0:16 y el hombre de camisa azul del 0:19 |
| `F11_rojo_pasajeros_hacia_atras` | Sunburst | `p10b_vagon_pasajeros_fondo_rojo` | 32 mm T2.8 | Contraplano de Iván (0:19) y la huida hacia el último vagón (0:23) |
| `F12_rojo_detalle_llave_0-23` | Flare | `p12_detalle_llave_rojo` (imagen 1 = F03) | 75 mm T2.8 | Hugo gira la llave, 0:23; Martina con la llave, 1:10–1:19 |

### Props (carpeta `imagenes/03_para_aprobacion/props`, [enlace](https://drive.google.com/drive/folders/1aft6jqtrHR-Xm2NPCJItu552niCaSSSf))

| Archivo | Modelo | Prompt | Nota |
|---|---|---|---|
| `PROP_llave_y_cerradura` | Flare | `prop_llave` (imagen 1 = F03) | La misma llave de F12 y la placa de F03 |
| `PROP_freno_emergencia` | Flare | `prop_freno_emergencia` (imagen 1 = F03) | La palanca roja hacia arriba, como en F01, F03 y F05 |
| `PROP_revolver_dos_balas` | NBP | `prop_revolver` | Dos vainas y cuatro recámaras vacías, sin marcas |
| `PROP_celular_martina` | NBP | `prop_celular_martina_v3` | Teléfono económico genérico. Las v1 y v2 se descartaron porque la cámara recordaba modelos de marca |

Reglas de rodaje que siguen todas las planchas:
- Cada plancha sale de una pasada limpia (imagen 1 = el look aprobado, imagen 2 = la distribución) y tiene como máximo una corrección.
- Lente, diafragma, foco y altura de cámara van definidos en cada plano.
- Contención: sin niebla densa, sin resplandores, sin destellos de lente y sin saturación exagerada.

Bisagras de la puerta: solo a la derecha vistas desde dentro (a la izquierda desde fuera). En el vagón de pasajeros, los asientos miran hacia su puerta delantera, igual que en el último vagón.

## 4d. Keyframes de prueba del reel (revisados por los agentes)

Carpeta de Drive: `imagenes/03_para_aprobacion/frames` ([enlace](https://drive.google.com/drive/folders/1XaAcHvDPOYH_Hzya-PEeecQ3vRBAamS3)). Las candidatas están en `imagenes/02_candidatos_fal/frames`. Cada keyframe sale de una pasada limpia, sin correcciones, usando las hojas de personaje y las planchas finales como referencia.

| Archivo | Modelo | Prompt (`prompts_fal/frames/`) | Referencias | Lente | Nota de revisión |
|---|---|---|---|---|---|
| `KF01_0-03_pareja_ambar` | Flare | `kf01_0-03_pareja_ambar` | Hojas de Martina y Tomás, F09 | 50 mm T2 | Aprobado. Hay que confirmar el lunar de Martina en el plano final, y el pelo de Tomás sale más revuelto que en la hoja |
| `KF02_0-45_diego_ventanita` | Flare | `kf02_0-45_diego_ventanita` | Estado de Diego, F03 | 35 mm T2.8 | Aprobado con nota: tiene la boca algo abierta, en el límite de la sobreactuación |
| `KF03_1-19_martina_llave` | Flare | `kf03_1-19_martina_llave` | Hojas de Martina, Tomás y Hugo, estado de Diego, F05 | 40 mm T2 | Es la única con el freno a la derecha de la puerta. Sunburst lo puso a la izquierda y NBP cambió el color de la puerta y el pelo de Martina. Hugo queda en segundo término, no de nuca en primer plano |

Nota para el 1:10: pedir la placa de bronce colgando de la llave (prop aprobado), que no aparece en KF03.

## 5. Pendientes

1. ~~Aprobación de Cristian de F01 a F12, de los cuatro props y de los keyframes KF01 a KF03.~~ **Aprobados el 2026-10-01.** Los archivos se movieron a `imagenes/04_aprobados` (las URLs no cambian); el registro está en `produccion/assets/aprobados_v1.md`. Las rutas `03_para_aprobacion` de este documento son anteriores a la aprobación.
2. ~~Decidir la fuente de la luz roja.~~ Decidido: una **tira de emergencia** en el centro del cielo.
3. La cinta de la fila 5 izquierda todavía no está en ninguna plancha. Se agrega cuando haya un plano que la muestre.
4. El último vagón no tiene estado ámbar en el capítulo 1. `look_ambar_plancha_heroe` sirve solo como referencia de look.

## 6. Regla de revisión

Ninguna imagen se propone para aprobación sin pasar antes por el equipo de agentes: el revisor de continuidad y el DP/arte. Cada corrección cambia una sola variable y se vuelve a revisar. Solo Cristian aprueba.
