# Formato del guion técnico

Un archivo YAML por capítulo: `produccion/shotlists/capNN.yaml`. Es la **única fuente de datos** de la producción: los agentes escriben sus campos y los motores (fal, Kling, Comfy, Weavy) leen de ahí.

**Regla de propiedad:** cada rol escribe solo sus campos. Si un rol ve un problema en un campo ajeno, lo anota en `alertas` con su nombre como prefijo («Director: …») y no lo corrige.

**Campos vacíos:** se omiten. Cada rol agrega su bloque al plano cuando hace su parte; la plantilla de abajo muestra todos los campos posibles.

## Estructura

```yaml
capitulo: 1
guion: guion/cap01/cap01_v3.md     # versión exacta desglosada
duracion_objetivo_s: 90
estado: desglose                    # desglose → aprobado → en_generacion → montado

assets:                             # Asistente de dirección
  personajes:
    martina: { estado: pendiente, hoja: null, element_kling: null, voz: null }
  locaciones:
    loc_ultimo_vagon: { estado: pendiente, ref: null }
  props:
    llave_vieja: { estado: pendiente, ref: null }

hechos_continuidad:                 # Continuista: lo que debe mantenerse entre planos
  - id: hc01
    hecho: "La manga derecha de Diego está oscura de sangre; la mano derecha también."
    desde: c01_p01
    hasta: null                     # null = hasta nuevo aviso

bloques:                            # Asistente de dirección: unidades de generación (ver investigacion_referencias.md)
  - id: c01_b01
    planos: [c01_p03, c01_p04, c01_p05]   # planos que cubre, en orden de montaje
    estrategia: A                   # A multi-beat · B plano suelto recortado · C encadenado
    motor: h3_max
    ruta: reference-to-video        # text-to-video / image-to-video / reference-to-video
    duracion_s: 8                   # 5–15 en H3 Max; incluye el tiempo de los planos y holgura
    beats: [{ plano: c01_p03, de: 0.0, a: 3.0 }, { plano: c01_p04, de: 3.0, a: 5.0 }]
    pila_referencias: ["Image 1 = martina", "Image 2 = tomas", "Image 3 = loc_vagon_pasajeros_ambar"]
    encadena_desde: null            # id del bloque cuyo último fotograma o video entra como referencia
    costo_estimado_usd: null
    estado: pendiente

planos:
  - id: c01_p01
    escena: cold_open
    tiempo: "0:00–0:02"
    duracion_s: 2

    # --- Director ---
    tipo_plano: PP                  # GPG / PG / PM / PMC / PP / PPP / inserto / POV / tarjeta
    accion: "Una línea: qué pasa en el plano."
    intencion: "Qué debe sentir el público."
    informacion: "Qué sabe el público al terminar el plano que no sabía antes."
    ironia: null                    # qué sabe el público que un personaje no sabe, si aplica
    actuacion: "Quietud y mirada, sin palabras de emoción."
    audio:
      dialogo: ["MARTINA (casi sin voz): «Diego…»"]   # PERSONAJE (acotación): «línea»
      sfx: ["dos golpes de palma contra el vidrio"]
      musica: null                  # texto libre o null
    texto_pantalla: null            # tarjeta sobreimpresa: «MARTINA, 29 · Vine a salvar mi relación.»
    personajes: [martina]           # elenco visible, aunque sea en parte (una mano cuenta)
    locacion: loc_ultimo_vagon
    corte: "Por qué se corta aquí y a qué plano."

    # --- Director de fotografía ---
    camara: { altura: null, posicion: null, movimiento: null }
    lente: { focal_mm: null, apertura: null, foco: null }
    luz: { dominante: null, fuentes: [], contraste: null }
    zona_segura_9x16: null          # dónde van los sujetos y qué queda libre para subtítulos, tarjeta e interfaz

    # --- Continuista ---
    continuidad:
      entrada: []                   # estado al empezar el plano
      salida: []                    # estado al terminar el plano
      eje: null                     # lado de la línea de 180° y dirección de miradas
      hechos: []                    # ids de hechos_continuidad que aplican
      alertas: []

    # --- Asistente de dirección ---
    referencias: []                 # ids de assets que entran como imagen de referencia
    bloque: c01_b01                 # bloque de generación al que pertenece
    motor_keyframe: nano_banana_pro # nano_banana_pro / ninguno (tarjeta o plano cubierto solo por bloque multi-beat)
    motor_video: h3_max             # h3_max / kling / ninguno (plano fijo o tarjeta)
    metodo_video: FF                # FF (primer fotograma) · FL (primer y último) · REF (referencias) · FF+E (Kling con elements)
    tomas_objetivo: 3
    costo_estimado_usd: null
    grupo_generacion: null          # planos que comparten locación y luz se generan juntos

    # --- Prompter ---  (estructura en produccion/compilador_prompts.md)
    prompts:
      keyframe: { motor: nano_banana_pro, params: {}, referencias: [], texto: "" }
      video: { motor: h3_max, params: {}, texto: "", negativo: null }

    # --- Pipeline ---
    tomas: []                       # { tipo: keyframe|video, motor, seed, url, archivo, fecha }
    elegida: { keyframe: null, video: null }
    estado: pendiente               # pendiente → prompt ok → keyframe ok → video ok → montado

    # --- Control de calidad ---
    revision: []                    # { toma, veredicto, problema, correccion_unica }
```

## Convenciones
- **Ids de plano:** `cNN_pNN`, en orden de montaje. Si se inserta un plano, se usa sufijo (`c01_p04b`); nunca se renumera.
- **Tipos de plano:** GPG (gran plano general), PG (plano general), PM (plano medio), PMC (plano medio corto), PP (primer plano), PPP (primerísimo primer plano), inserto, POV, tarjeta.
- **Tiempos:** los del guion. Si el desglose no calza con la duración objetivo, el Director lo anota en `alertas` del primer plano de la escena.
- **Un plano, un momento.** Si una línea de acción pide dos momentos, son dos planos.
- **Tarjetas de personaje:** van **sobreimpresas** en el plano donde se presenta el personaje (`texto_pantalla`), no son planos propios. Ese plano dura lo necesario para leer la frase: al menos 2 s.
- **Textos a pantalla completa** (la tarjeta de votación): son planos con `tipo_plano: tarjeta`, sin keyframe ni video; el texto va en `texto_pantalla` y se hacen en After Effects.
- **Saltos de tiempo por corte:** los saltos («20 minutos antes») no llevan sobreimpresión: los resuelve el corte del montaje, apoyado por la hora del celular y la luz. No es un plano.
- **`estado_motor: exploracion`:** el plano usa un motor todavía no oficial (Kling 4.0 Flash); no se da por final.
- **Plano ≠ bloque.** `duracion_s` de un plano es lo que dura en el montaje. El modelo genera **bloques** (H3 Max 5–15 s, Kling 3 s o más) que agrupan varios planos; el costo se calcula sobre el bloque completo.
- **`intencion` e `informacion` son obligatorios** en todo plano. `ironia` se omite cuando no hay.
- **Hechos de continuidad:** lo que manda es la lista `hechos` de cada plano; `desde` y `hasta` son orientativos (orden de montaje) y `hasta: null` se escribe explícito. Un hecho que el guion no define se marca «(propuesta)» hasta que Cristian lo aprueba, y los que los modelos suelen perder llevan `fragil: true`.
- **Extras sin nombre** (el pasajero del boleto, la esposa del hombre de camisa azul) se describen en `accion`; no van en `personajes`.
- **Comillas:** los textos libres van entre comillas dobles; los ids y valores fijos (`PP`, `pendiente`, `martina`) no las necesitan.
