# Plan de la prueba del cold open (capítulo 1)

**Objetivo:** prueba de calidad + lipsync del cold open en unos 8,5 s (4 planos). El plano 4 (c01_p02b) es el bloque de lipsync.

**Guion base:** `guion/cap01/cap01_v8.md` (cold open = momento de las 0:45, luz roja de emergencia).

## Qué quiere cada uno

- **Diego** (afuera, solo la mano): entrar, y que sea ella quien le abra. No ataca: ruega.
- **Martina**: que Diego no esté ahí, delante de Tomás. Miedo, culpa y, debajo, alivio de que esté vivo. Casi no habla: todo en la cara.
- **Tomás** (desenfocado, un paso detrás a su derecha): todavía no entiende. Solo reacciona al nombre.

## Regla de cámara

Cero push-in ni dolly in. Planos de la mano: cámara fija, 65 mm. Planos de Martina: cámara en mano muy leve (respiración), sin avanzar. El único movimiento de cámara del capítulo se guarda para cuando aparece la cara de Diego (escena 4).

## Los 4 planos

| ID | Tiempo | Encuadre | Lente | Cámara | Acción | Intención |
|---|---|---|---|---|---|---|
| c01_p01a | 0:00–0:01,5 | Desde adentro, la ventanita | 65 mm | Fija | El primer cuadro YA es el impacto: la palma ensangrentada golpea el vidrio de golpe. Detrás, el pasillo rojo vacío y quieto. El vidrio vibra | Susto limpio, legible en el celular sin sonido |
| c01_p01b | 0:01,5–0:03 | Contraplano, Martina, plano medio corto, ~3 m de la puerta | — | En mano leve | Martina salta con el golpe y se queda congelada. No se acerca. Tomás desenfocado detrás, a la derecha | Miedo puro, todavía no sabe quién es |
| c01_p02a | 0:03–0:05 | Inserto POV de Martina, la ventanita | 65 mm | Fija | La mano deja de golpear: se abre y se apoya plana y quieta, casi suave. Se ve el puño gris claro empapado | El cambio de golpe a palma calmada le dice «soy yo». Giro del plano |
| c01_p02b | 0:05–0:08,5 | Primer plano de Martina | — | En mano leve | Miedo → reconocimiento. Susurra «Diego…». Los ojos se van hacia Tomás (culpa). Tomás desenfocado gira la cabeza. Corte a negro en la respiración | **Bloque de lipsync.** La actuación importante es antes y después de la palabra |

**Tarjeta:** «20 MINUTOS ANTES» (ya está en la v8; se decide pieza por pieza en edición).

## Criterios de aprobación

1. Que se entienda en el celular sin sonido (el primer cuadro es el impacto de la mano).
2. Que no haya movimiento de fondo inmotivado (el pasillo rojo detrás del vidrio está quieto).
3. Que no haya push-in ni dolly in en ningún plano.
4. Que Martina tenga expresión (miedo → reconocimiento → culpa).
5. Que el lipsync de «Diego…» se vea natural (labios que apenas se separan, casi sin voz).
6. Continuidad: mano y herida de Diego en el brazo DERECHO; palma con el pulgar hacia la derecha del cuadro visto desde adentro.

## Lista técnica (modelo, lente, luz, movimiento, prompts)

**Archivo completo:** [`lista_tecnica.md`](lista_tecnica.md) (390 líneas, 3-oct-2026).

### Resumen

| Campo | Valor |
|---|---|
| Duración | 8,5 s con 4 planos, más tarjeta «20 MINUTOS ANTES» |
| Motor de video | **MiniMax H3 Max, solo 1080P** (`minimax/h3-max/image-to-video`). Kling queda fuera: su Preview es 720p |
| Keyframes | Nano Banana Pro 2K (4 nuevos: KF1, KF2, KF4, KF4b). Alternativa: GPT Image 2.5 high |
| Lipsync | Voz primero (ElevenLabs), pista de 5 s con `target_audio_url`. Respaldo: sync-3 |
| Cámara | P1 y P3 fijos en trípode. P2 y P4 en mano leve. **Cero push-in, zoom o dolly** |
| Costo | ~3,70 USD base, ~5,65 con respaldos (promo 0,096 USD/s hasta 15-oct) |
| Tiempo | ~2 h (1 h generación, 1 h post) |

### Bloques de generación

| Bloque | Planos | Duración | Descripción |
|---|---|---|---|
| B1 | P1 (0,0–1,5 s) + P3 (3,0–5,0 s) | 5 s | Un solo clip con la mano; P2 va en medio |
| B2 | P2 | 3 s | Martina salta y se congela, Tomás desenfocado |
| B3 | P4 | 5 s | Primer plano de Martina, lipsync de «Diego…» |

Los prompts completos de keyframes y video están en `lista_tecnica.md` §2.

## Decidido (Cristián)

1. **Segundo golpe fuera de campo en P2: SÍ.** (3-oct-2026, 10:33) Un segundo golpe **solo en audio**, fuera de campo, a los 0,3 s de P2. Martina salta en cámara con ese golpe. P1 sigue siendo «golpe seco, después silencio» durante 1,5 s.

2. **Ventanita con malla de alambre (F03): SÍ.** (3-oct-2026, 10:52) Se mantiene F03 y se corrigió hc22. La ventanita es un rectángulo vertical de esquinas redondeadas con marco metálico remachado, vidrio de seguridad con malla de alambre fina en rombo, a la altura de la cabeza de un adulto. Misma forma, tamaño y malla en todos los planos y desde ambos lados.

3. **Tomás SÍ va en P4, con giro de cabeza.** (3-oct-2026, 10:57) Tomás desenfocado, de tres cuartos de espalda (se le ve sobre todo la nuca y el perfil perdido), boca cerrada y apretada, nunca la abre. Gira la cabeza hacia Martina **después** de que ella termina de decir «Diego…». Solo Martina habla. KF4b (sin Tomás) queda como **plan B** si H3 le mueve la boca a él.

**Contradicción conocida (no se resuelve en este PR):** el YAML c01_b02 dice «door window off-screen left», pero la geografía de la v8 pone la ventanita a la derecha del cuadro. Cuando Cristián apruebe los planos, hay que corregir c01_b02.

## Notas

- Los ids de plano usan sufijos (c01_p01a, c01_p01b, c01_p02a, c01_p02b) para no romper las referencias del resto del YAML, que sigue desglosando la v3→v7. El cold open de la v8 tiene 4 planos; el de la v7 tenía 2.
- Martina en el cold open: pelo con mechones sueltos y sudor, suéter crema, luz roja (ya está en los hechos del YAML).
- P1 (c01_p01a): no usar el par de keyframes «mano separada → palma apoyada» si genera el acercamiento; mejor empezar en el impacto o cortar a mitad del movimiento.
- P4 (c01_p02b) es el bloque de lipsync. La actuación importante es antes y después de la palabra, no en la palabra.
