# Formato del guion técnico

Un archivo YAML por capítulo: `produccion/shotlists/capNN.yaml`. Es la **única fuente de datos** de la producción: los agentes escriben sus campos y los motores (fal, Kling, Comfy, Weavy) leen de ahí.

**Regla de propiedad:** cada rol escribe solo sus campos. Si un rol ve un problema en un campo ajeno, lo anota en `alertas` y no lo corrige.

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

planos:
  - id: c01_p01
    escena: cold_open
    tiempo: "0:00–0:02"
    duracion_s: 2

    # --- Director ---
    tipo_plano: PP                  # GPG / PG / PM / PMC / PP / PPP / inserto / POV
    accion: "Una línea: qué pasa en el plano."
    intencion: "Qué debe sentir el público."
    informacion: "Qué sabe el público al terminar el plano que no sabía antes."
    ironia: null                    # qué sabe el público que un personaje no sabe, si aplica
    actuacion: "Quietud y mirada, sin palabras de emoción."
    audio: { dialogo: [], sfx: [], musica: null }
    personajes: [martina]
    locacion: loc_ultimo_vagon
    corte: "Por qué se corta aquí y a qué plano."

    # --- Director de fotografía ---
    camara: { altura: null, posicion: null, movimiento: null }
    lente: { focal_mm: null, apertura: null, foco: null }
    luz: { dominante: null, fuentes: [], contraste: null }
    zona_segura_9x16: "Dónde van los sujetos y qué queda libre para subtítulos e interfaz."

    # --- Continuista ---
    continuidad:
      entrada: []                   # estado al empezar el plano
      salida: []                    # estado al terminar el plano
      eje: null                     # lado de la línea de 180° y dirección de miradas
      hechos: []                    # ids de hechos_continuidad que aplican
      alertas: []

    # --- Asistente de dirección ---
    referencias: []                 # ids de assets que entran como imagen de referencia
    motor_keyframe: nano_banana_pro
    motor_video: h3_max             # h3_max / kling / ninguno (plano fijo o tarjeta)
    metodo_video: FF                # FF (primer fotograma) · FL (primer y último) · REF (referencias) · FF+E (Kling con elements)
    tomas_objetivo: 3
    costo_estimado_usd: null
    grupo_generacion: null          # planos que comparten locación y luz se generan juntos

    # --- Prompter ---
    prompt_keyframe: null           # ruta: produccion/prompts/capNN/<id>.md
    prompt_video: null

    # --- Pipeline ---
    tomas: []                       # { tipo: keyframe|video, motor, seed, url, archivo, fecha }
    elegida: { keyframe: null, video: null }
    estado: pendiente               # pendiente → prompt ok → keyframe ok → video ok → montado

    # --- Control de calidad ---
    revision: []                    # { toma, veredicto, problema, correccion_unica }
```

## Convenciones
- **Ids de plano:** `cNN_pNN`, en orden de montaje. Si se inserta un plano, se usa sufijo (`c01_p04b`); nunca se renumera.
- **Tipos de plano:** GPG (gran plano general), PG (plano general), PM (plano medio), PMC (plano medio corto), PP (primer plano), PPP (primerísimo primer plano), inserto, POV.
- **Tiempos:** los del guion. Si el desglose no calza con la duración objetivo, el Director lo anota en `alertas` del primer plano de la escena.
- **Un plano, un momento.** Si una línea de acción pide dos momentos, son dos planos.
- **Tarjetas y textos** (nombres, «20 MINUTOS ANTES», votación) son planos con `motor_video: ninguno`; se hacen en After Effects.
