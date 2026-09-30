# Plan de la prueba de montaje v2 (cold open y escena 1 del capítulo 1)

Es la misma porción que la v1 (c01_p01–c01_p10), con los assets nuevos y el flujo corregido después de la revisión de Cristian (`../cap01_montaje_v1/feedback_proceso.md`). **Objetivo: que cada bloque salga bien en una o dos tomas porque todo se definió antes.** Se genera a 480P, igual que la v1, para que la comparación sea justa.

Todo agente que trabaje en la v2 lee este plan antes de empezar.

## 1. Qué necesita la v2 de los assets (para el agente de assets)

Se registran en la sección `assets` de `produccion/shotlists/cap01.yaml`, con `estado: aprobado` y su URL. Ningún bloque se genera con un asset que no esté aprobado.

| Asset | Qué tiene que resolver | De dónde sale |
|---|---|---|
| Hojas de los seis personajes | Casting definitivo. Tomás con pantalón gris carbón que no sea mezclilla; nadie con nombre viste de azul (hc18) | `mejoras.md` #9 |
| Variante de Martina después de la carrera | Mechones sueltos y sudor en la frente, para el cold open (hc10), en vez de dejarlo al prompt | `mejoras.md` #12 |
| Placa del vagón de pasajeros, luz ámbar | Una vista hacia la cabeza del tren y otra **hacia la cola**, para p03–p08 | `mejoras.md` #10 |
| Placa del último vagón, luz roja | Vista hacia la puerta con su ventanita. La ventanita tiene que ser **igual** a la de la placa ámbar (hc22) | `mejoras.md` #11 |
| **Qué se ve por cada vidrio** | Una línea por vidrio en la nota de cada placa. Ventanas laterales: noche, lluvia y exterior en movimiento. Ventanita de la puerta: el vestíbulo o el otro vagón, **quieto respecto del tren**. Es la versión mínima de la biblia del set, que se detalla después | Falla del fondo en p02 |
| Celular de Martina | Frente, dorso, pantalla apagada y encendida, sin marca ni muesca. Entra como referencia en todo plano donde se vea, aunque sea chico | Celular que se deforma en p06 |
| Revólver de Don Hugo | En su funda café, con el tambor cerrado, sin balas a la vista y con el cinturón negro vacío | Balas que aparecen en b06 |
| Boletos | Hoy está `pendiente` | p09 |

## 2. Flujo de la v2, en orden

Cada paso usa las reglas nuevas. Entre paréntesis va dónde está escrita cada una.

1. **Director:** reescribe `actuacion` de cada plano con objetivo, obstáculo, tarea, beats con tiempo, miradas con destino y ojos (`produccion/actuacion.md`). Escribe los perfiles de actuación de los personajes que aparecen (`produccion/actuacion/perfiles.md`) desde `biblia/personajes.md`.
2. **Productor de impacto:** revisa el desglose y propone gancho, caídas de atención y cámara. El Director acepta o descarta (`mejoras.md` #3).
3. **Director de fotografía:** escribe la `gramatica_escena` del cold open y de la escena 1. Da a cada plano un movimiento con tipo, amplitud, velocidad y motivo. Ningún plano queda fijo sin motivo escrito (`agentes/director_fotografia.md`).
4. **Continuista:** actualiza los hechos con los assets nuevos y agrega lo que se ve por cada vidrio en cada plano.
5. **Asistente de dirección:** vuelve a elegir el método de cada bloque con la regla de FL. Por defecto van referencias. b01, b04 y b06 pasan a REF o FF, salvo que sus dos fotogramas cumplan las dos condiciones (`agentes/asistente_direccion.md`). Máximo dos tomas por bloque. Probar el encadenado entre p09 y p10 (`mejoras.md` #14). Alargar el beat de p04 a 2 s para la tarjeta (#16).
6. **Cristian aprueba el guion técnico.**
7. **Prompter:** compila keyframes y bloques con la skill `director-de-prompts`, en el formato oficial de H3 (I2VA, FL2VA o Ref2VA). Los ajustes de prompt #4–#8 de `mejoras.md` ya están en los candados de la skill.
8. **Pipeline:** keyframes. **Control de calidad:** filtra. **Cristian elige.**
9. **Control de calidad:** hace la revisión previa de cada bloque (`revision_previa: lista`) antes de generar video.
10. **Pipeline:** como máximo dos tomas por bloque. **Control de calidad:** revisa el clip completo. **Cristian elige.**
11. **Montajista:** arma `cap01_prueba_montaje_v2.mp4` con un ambiente continuo de lluvia y tren debajo de la escena 1 (`mejoras.md` #15).

## 3. Cómo se compara con la v1

Se completa al terminar:

| Medida | v1 | v2 |
|---|---|---|
| Tomas de video generadas / bloques | 7 / 6 | |
| Bloques que salieron en la primera toma | | |
| Planos con cámara fija | 8 de 10 | |
| Palabras por prompt de video (promedio) | ~110 | |
| Errores de mundo (fondo, props, lo prohibido) | fondo en p02, celular en p06, balas en b06 | |
| Costo de video | 2,4 USD | |

Y la revisión de Cristian sobre el armado, con el mismo criterio que la v1: proceso, no contenido.
