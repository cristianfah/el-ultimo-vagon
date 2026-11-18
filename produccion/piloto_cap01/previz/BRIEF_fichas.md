# Brief para armar las fichas del gris (cilindros) · 18-nov-2026

Encargo común de los agentes que arman las fichas `shots/<llamada>.json` del gris del cap. 1. Lo escribió el director del piloto a partir del 05 (`05_prompt_sesion_claude_2026-11-10.md`) y del 07 (`07_retomar_piloto_cap01_2026-11-17.md`, que reemplaza al 06). Sirve también para el cap. 2.

## Qué es el gris

El capítulo entero dirigido en Blender: cámara, lente, encuadre, blocking y tiempos. De cada plano salen **stills A/B/C** desde la cámara real (A = inicio, B = momento clave, C = final; nunca ángulos extra), una **planta** y una **página de storyboard** por bloque. El MP4 se exporta solo en las llamadas de blocking y geografía (`llamadas_tiempos.json`, campo `mp4_ref`). Cristian corrige cámara y dirección de arte sobre el gris (PARADA 1) antes de gastar.

## Personajes = cilindros con nariz (decisión de Cristian, 17-nov)

- Un cilindro por personaje, a su altura real, todos del mismo diámetro (0,32 m), con una nariz (cono) a la altura de los ojos que marca hacia dónde mira. **Nada más:** sin cara, sin brazos, sin inclinación, sin contextura.
- En la ficha valen: `pose` (`de_pie`, `sentado`, `agachado`), `pos`, `yaw` (giro del cuerpo), `head_yaw` y `head_pitch` (hacia dónde mira la nariz) y `dz` (sube o baja el cilindro, por ejemplo al agacharse). **`lean`, `side`, `head_roll`, `arms` y `boot` no se dibujan**: no los uses para contar la acción. La acción de manos (la llave, la palma en el vidrio, la mano en la manija) se escribe en `descripcion` y va al prompt.
- Los props sí se ven: `maletin` y `llave` (y las puertas y el vidrio que revienta, en `set_anim`).
- Colores fijos (no se eligen): Martina avena · Tomás azul marino · Diego piedra clara · Carmen celeste · Iván café oscuro · Hugo bronce · Hombre de camisa azul azul fuerte · Esposa beige rosado · Figura con máscara gris liso · Pasajeros gris oscuro (`extra_N`) · Infectados casi negro (`infectado_N`). Hay 6 `extra_*` y 6 `infectado_*`.

## Herramientas (no edites los scripts)

```bash
export PREVIZ_TRABAJO=/tmp/claude-0/-home-user-el-ultimo-vagon/d1f48229-f7ac-54de-96cb-5fb120f28a0c/scratchpad/trabajo/previz
export BLENDER=/opt/blender/blender-4.5.16-linux-x64/blender FFMPEG=/usr/bin/ffmpeg
cd /home/user/el-ultimo-vagon/produccion/piloto_cap01/previz/scripts
python3 storyboard.py armar   --json ../shots/<id>.json             # arma la llamada (.blend + datos por cuadro)
python3 storyboard.py stills  --json ../shots/<id>.json --rapido    # stills A/B/C + planta en Workbench (rápido, para iterar)
python3 storyboard.py revisar --json ../shots/<id>.json             # chequeo automático: tiene que dar 0 PROBLEMAS
python3 storyboard.py stills  --json ../shots/<id>.json --samples 12   # final, con luz real (EEVEE, ~6-10 s por cuadro)
```

- Los stills quedan en `$PREVIZ_TRABAJO/stills/<id>/` (`<id>_<plano>_A.png`, `_B`, `_C`, `_planta.png`). **Míralos** con la herramienta Read en cada vuelta: el chequeo no ve composición.
- **Nunca** corras `armar --set`, `build_set.py` ni `build_cast.py`: el set y el elenco son uno solo y los comparten todos. Si te falta algo del set, anótalo en tu informe.
- Formato de la ficha: `scripts/README.md` (sección «Ficha»). Ejemplo completo: `shots/c05a.json` (armado con las figuras de bloques del 10-nov; sus brazos ya no se dibujan).

## Campos nuevos de la ficha (los pide la página de storyboard)

Por plano, además de lo de siempre (`id`, `t0`, `t1`, `montaje`, `descripcion`, `motivo_camara`, `camera`, `actors`, `props`, `hide_set`):

- `titulo`: corto, con el número del guion. Ej.: `"P7 · Entran en tropel"`.
- `camera.tag`: tipo de cámara en mayúsculas para el nombre `CAM_<plano>_<TAG>`. Ej.: `HANDHELD_RETRO`, `FIJA_PISO`, `MANO_LEVE`, `PUSH_IN`, `BARRIDO`, `FIJA`.
- `camera.mira`: hacia dónde mira, en pocas palabras. Ej.: `"hacia la puerta del último vagón"`.
- `camera.mov`: el movimiento. Ej.: `"retrocede 0,6 m mientras entran"`, `"fija; solo vibra con el tren"`.
- `en_cuadro`: qué hay en cuadro y dónde (izquierda/derecha, primer término, fondo). Ej.: `"Tomás a la izquierda arrastrando a Martina; Iván detrás empuja a Carmen; al fondo, la puerta con el tubo frío encima."`
- `stills`: `{"A": {"t": 3.55, "desc": "…"}, "B": {"t": 4.1, "desc": "…", "lados": {"martina": "der", "tomas": "izq"}}, "C": {…}}`. `t` en segundos de la llamada, **dentro de la ventana de montaje** del plano. `desc` es una línea. `lados` es opcional y el chequeo lo verifica: úsalo en todo plano donde el guion fija un lado.

Por llamada: `set_light` o `light_keys` (ver luz), `fuente_tiempos` y `notes` (geografía en una línea).

## Tiempos (no se discuten)

`llamadas_tiempos.json` manda: `duration_s` entero de la llamada y, por plano, la ventana de montaje `de_s`–`a_s`. En la ficha: el primer plano parte en `t0 = 0` (el colchón de 0,5 s ya tiene la acción en marcha), cada plano siguiente parte en su `de_s`, cada plano termina en el `de_s` del siguiente, y el último termina en `duration_s` (se alarga con acción, nunca con quietud). `montaje.usar_desde_s`/`usar_hasta_s` = `de_s`/`a_s`. En las llamadas con pista, las líneas entran en los segundos de `pista.lineas` (quien no habla está con la boca cerrada; eso va al prompt).

## Reglas de dirección (05, 07, `01_propuesta.md` §1, guion v10)

- **Cámara con intención:** lente y distancia reales (24–28 mm vagón y pasillo; 35–40 mm plano medio y de dos; 50 mm diálogo; 85 mm ojos y manija). Altura con sentido (ras de piso para el maletín, ojos sentados en el diálogo, baja en la embestida, a la altura de la cerradura en la llave). Cada plano tiene un motivo escrito en `motivo_camara`; si no hay motivo, va fija con el vaivén del tren.
- **Energía:** bloques 0–2 fija o en mano muy suave; bloque 3 en mano que llega tarde al grito; bloques 4–5 dentro de la acción; bloque 6 fija a propósito; bloque 7 en mano leve y avance lento a la ventanita.
- **Movimiento con peso** (arranca y frena), temblor de operador (`handheld`), sacudidas 2 a 4 cuadros después del impacto (`shakes`). Push-in solo donde el guion lo pide (b2_p3 y b7_p2).
- **Primer término:** hombros, respaldos, el marco de la ventanita. El cuadro limpio y centrado delata la IA.
- **Nadie mira al lente.** El chequeo marca toda nariz a menos de 14° de la cámara dentro de la ventana de montaje. También vale para la gente que corre hacia la cámara: su mirada tiene un objetivo (Hugo, la puerta, hacia atrás por encima del hombro).
- **Cilindros que se tocan** = gente fundida: el chequeo avisa si dos cilindros se superponen; evítalo salvo contacto buscado (y entonces dilo en el informe).
- **Primer plano con cilindros:** encuadra la parte de arriba del cilindro con la nariz y aire sobre la cabeza; el cilindro no debe llenar el cuadro entero como una pared (eso no sirve de referencia).
- **Luz** (solo fuentes del set; ya está programada, solo eliges el estado): `set_light` = `ambar_bajo` (vagón 2), `ambar` (vagón 5), `rojo` (vagón 5 en emergencia, fuelle y último vagón; el tubo frío existe solo dentro del último vagón, sobre la puerta), `rapto` (cuarto del rapto). Para un cambio dentro de la llamada: `"light_keys": [{"t": 0, "estado": "ambar"}, {"t": 3.8, "estado": "rojo"}]`. Estados: `ambar`, `ambar_bajo`, `rojo`, `negro`, `rapto`.

## Mapa fijo del set (metros de mundo; +Y = hacia la cabeza del tren, +X = derecha mirando hacia adelante, Z arriba)

Las anclas `ANC_*` están en `$PREVIZ_TRABAJO/set/set_info.json`. Asientos: todos miran a +Y; asiento de pasillo en |x| = 0,56 y de ventana en |x| = 1,12; pasillo de 0,60 m al centro. `yaw` 0 = mira a +Y; positivo gira a la izquierda (hacia −X). `yaw` 180 = mira a −Y.

**Nombres fijos de muros y puertas (07):** en los vagones 2 y 5, «puerta delantera» = +Y (hacia la cabeza del tren) y «puerta trasera» = −Y (hacia el fuelle y el último vagón); «muro de la ventana» = la pared lateral del lado de Martina en su escena, «muro del pasillo» = la del otro lado. En el último vagón hay **una sola puerta**: «la puerta del último vagón (la del tubo frío)», en su extremo +Y; al fondo (−Y) va la pared trasera con la ventana trasera negra y la cabina del revisor a la derecha de quien mira hacia el fondo (lado +X).

**Vagón 2** (bloques 0, 1 y 3; luz `ambar_bajo`; lámparas encendidas: fila 12 der (sobre la pareja), fila 15 izq (la lectora) y fila 5 der). Fila 12 en y = 81,11; fila 15 en y = 78,41 (las filas bajan de número hacia +Y, 0,9 m entre filas). **La pareja va del lado derecho (+X)** (cambio del 18-nov respecto de la ficha c00a del 10-nov): el guion pide a la esposa a la **derecha del cuadro** en los planos frontales del bloque 3 (b3_p3, b3_p4, b3_p5), y eso solo pasa con la pareja en +X y la cámara mirándolos de frente (hacia −Y). Marcas fijas:
- Hombre de camisa azul: ventana derecha (1,12; 81,11), sentado, dormido con la cabeza contra la ventana. Esposa: pasillo derecho (0,56; 81,11), dormida en su hombro.
- Maletín: bajo el asiento del hombre, por el lado del pasillo; asoma la esquina metálica. El inserto a ras de piso (b0_p2 y b3_p1, «mismo lugar y mismo encuadre») mira hacia la cola (−Y), con el asiento a la izquierda del cuadro, como en la toma de Kling de c00a que quedó candidata.
- Lectora (`extra_5`): (−1,12; 78,41), bajo la lámpara encendida de la fila 15 izq: al otro lado del pasillo y más hacia la cola, para que en b0_p4 (mirando a la cola) quede «al fondo». Joven con audífonos (`extra_1`): (−0,56; 82,01). Dormidos: `extra_2` (1,12; 83,81), `extra_3` (−1,12; 83,81), `extra_4` (0,56; 85,61).
- Martina camina hacia la cola (−Y) por el pasillo. Puerta trasera del vagón 2 (donde se apoya en el bloque 1): `ANC_vagon2_puerta_tras` (0; 72,56).

**Vagón 5** (bloques 2 y 4; luz `ambar`, después `rojo`; lámparas encendidas: fila 4 izq, fila 11 der, fila 17 izq). Fila 11 en y = 12,53; fila 10 en y = 13,43.
- Martina: ventana derecha (1,12; 12,53), sentada. Tomás: pasillo derecho (0,56; 12,53), sentado. La lámpara de la fila 11 der está sobre ellos. Desde el asiento de enfrente (fila 10, mirando a −Y), Martina queda a la **izquierda** del cuadro (ventana) y Tomás a la **derecha** (pasillo). En el primer plano de Tomás, detrás de él va el pasillo y los asientos del otro lado, **nunca la ventana**.
- Iván y Carmen: sentados en el vagón 5, más adelante (+Y) que la pareja; los ubica el bloque 4 (Iván fila 7 izq pasillo, Carmen fila 8 izq ventana, salvo que el guion pida otra cosa).
- Puerta delantera (infectados): `ANC_vagon5_puerta_del` (0; 23,08). Puerta trasera (Hugo, hacia el fuelle): `ANC_vagon5_puerta_tras` (0; 3,08).

**Fuelle** (bloque 5; `rojo`, sin tubo): de y = 0 (puerta del último vagón) a y = 3,0 (puerta del vagón 5), 1,25 m de ancho. Cerradura del último vagón en x = −0,32 (bocallave por fuera `ANC_bocallave_ext`). Paredes ocultables con `hide_set`: `fuelle_pared_izq`, `fuelle_costillas_izq`, `fuelle_pared_der`, `fuelle_costillas_der`.

**Último vagón** (bloques 5 P7–P9, 6 y 7; `rojo` con el tubo frío sobre la puerta, por dentro). Puerta en y ≈ −0,04; por dentro, la cerradura queda a la **izquierda** de quien mira la puerta (x = −0,32; `ANC_bocallave_int`, `ANC_manija_int` (−0,25; −0,115; 0,95)). Vestíbulo libre entre la puerta y la fila 1 (y de −0,1 a −1,3, ancho completo). Marcas fijas del grupo **después de entrar** (bloques 6 y 7, mirando hacia la puerta; Martina a la izquierda de Tomás):
- Martina (−0,25; −1,55) · Tomás (0,25; −1,45) · Carmen (0,80; −1,85)
- Iván: espalda contra la puerta (0,10; −0,32) en 6·P1; «junto a la puerta» (0,50; −0,40) en el bloque 7
- Hugo: junto a la puerta, del lado de la cerradura (−0,62; −0,50). En b7_p6 su mano derecha está en la manija (va en el texto).
- Diego (bloque 7): afuera, en el fuelle, frente a la ventanita (0,0; 0,40), mirando hacia −Y. Ventanita centrada en x = 0, z = 1,5.
- Planos cerrados de los bloques 6 y 7 tomados **desde el lado de la puerta** (cámara cerca de y = −0,4, mirando a −Y): Martina a la **derecha** del cuadro y Tomás a la **izquierda**; al fondo, la pared trasera con la ventana negra y la cabina del revisor a la izquierda del cuadro.

**Cuarto del rapto** (bloque 1, flashes; luz `rapto`): `ANC_rapto` (40; 0; 0), silla metálica en `ANC_rapto_silla` mirando a +Y. Martina sentada en la silla; la figura con máscara es `enmascarado`.

## Qué entregas

1. Las fichas de tus llamadas en `previz/shots/` (y nada más del repo). Sin commits.
2. `revisar` en 0 PROBLEMAS; si queda un aviso, explícalo.
3. Stills finales con `--samples 12`.
4. Un informe corto (es tu respuesta final), en español neutro:
   - por llamada y plano: lente, altura, tag, qué resolviste del guion y qué no se puede mostrar con cilindros;
   - una **nota de layout** por bloque, en lenguaje simple (ej.: «Martina en el lado de la ventana, mirando hacia la puerta trasera»);
   - los **planos difíciles** (los que más probablemente rompa el modelo de video) y, para cada uno, los 4 s más complicados de la llamada (de qué segundo a qué segundo);
   - todo lo que contradiga el guion, la tabla del estado del mundo o el mapa fijo, y lo que te falte del set.

No llames a ningún servicio pagado (fal, Kling, Higgsfield, ElevenLabs, nada): hoy no se gasta. No edites el guion, los scripts, `bloques.json` ni el log.
