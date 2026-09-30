# Mejoras propuestas después de la prueba de montaje v1 (2026-09-30)

Lista de trabajo para la próxima sesión. Las tres primeras son pedidos de Cristian; el resto son propuestas del equipo según lo que salió en la prueba. Se aplican de a una y se comprueba cada una con una tanda corta a 480P.

El feedback de Cristian sobre el proceso (cámara, actuación, set, FL y control de calidad de video) y las herramientas que propone para cada rol están en `feedback_proceso.md`.

## Pedidos de Cristian
1. **Prompts más dirigidos.** Hoy el Prompter compila bien los hechos, pero la dirección llega diluida: actuación genérica, sin ritmo interno del plano. Propuesta: que cada prompt de video tenga un «beat de actuación» con tiempos (qué hace el cuerpo en 0–1 s, 1–2 s…), una sola intención y el subtexto traducido a conducta visible.
2. **Más trabajo de cámara.** Casi todo salió fijo o con cámara en mano sutil. Propuesta: que el Director de fotografía defina por escena una «gramática de cámara» (qué se mueve, cuándo y por qué), con al menos un movimiento con motivo por escena. Hay que probar en H3 Max qué movimientos obedece: empuje, travelling lateral, grúa y seguimiento.
3. **Probar el Productor de impacto** (`agentes/impacto.md`) sobre el guion técnico del capítulo 1 y ver cuántas propuestas acepta el Director.

## Prompts
4. **Cierre contra marcas:** agregar «no notch, no dynamic island, no brand design» en todo plano con celular.
5. **Mano y lado siempre explícitos:** «LEFT hand (window side, frame right)». En p06 fallaron las tres tomas.
6. **Límite del encuadre en planos cerrados:** «framed from mid-chest up, hands out of frame». El PMC de p02 salió abierto.
7. **Tonos oscuros con valor:** «mid-dark grey, not black» (la gorra de Hugo).
8. **Lo prohibido, en positivo y en el último fotograma:** las balas de b06 aparecieron a mitad del clip. Probar a describir el cinturón como «plain black leather belt, empty» en vez de solo «no cartridges».

## Referencias y assets
9. **Hoja `tomas_v3`** con pantalón gris carbón que no sea mezclilla (hc18 prohíbe el azul).
10. **Placa ámbar mirando hacia la cola del tren,** para los planos p03–p08.
11. **Unificar la ventanita de la puerta** entre la placa roja y la ámbar (hc22).
12. **Variante de Martina después de la carrera** (mechones y sudor) para el cold open, en vez de dejarla al prompt.

## Generación y montaje
13. **Dos tomas por bloque** en la próxima pasada: esta vez se hizo una sola por bloque, para ahorrar.
14. **Probar encadenado** (último fotograma de un bloque como primero del siguiente) entre p09 y p10: hoy son dos bloques sueltos y el paso de la mano a la chaqueta no calza.
15. **Ambiente continuo de lluvia y tren** debajo de la escena 1 en el armado, para tapar los saltos de sonido entre clips.
16. **Tarjeta de Martina:** el plano p04 dura 1,64 s y la tarjeta necesita 2 s. Alargar el beat en b03 o pasarla a p06.
17. **Orquestador:** que `generar_desde_yaml.py` genere en paralelo todo lo que ya tiene sus entradas aprobadas, arme las hojas de contacto y escriba las elecciones en el YAML. Hoy eso se hizo a mano.
