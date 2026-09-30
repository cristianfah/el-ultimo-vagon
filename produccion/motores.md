# Motores de generación: qué se usa para qué

Todos los motores leen del mismo guion técnico (`produccion/shotlists/capNN.yaml`). Cambiar de motor en un plano es cambiar un campo, no rehacer el plano.

## Resumen

| Tarea | Motor | Por qué | Costo aproximado |
|---|---|---|---|
| Hojas de personaje, locaciones y props | **Weavy** (GPT Image 2.5 y Nano Banana Pro) | Es trabajo creativo, se itera a mano en el canvas | Plan de Weavy |
| Keyframe por plano | **fal.ai · Nano Banana Pro** (`fal-ai/nano-banana-pro/edit`) | Hasta 14 imágenes de referencia, 9:16 nativo, se automatiza | 0,15 USD por imagen (1K/2K) |
| Video de exploración y tomas alternativas | **fal.ai · MiniMax H3 Max** | Muy barato y rápido: permite generar varias tomas por plano | 0,05 USD/s a 480p · 0,08 USD/s a 768p |
| Video de planos clave (identidad, diálogo, acción difícil) | **Kling 4.0** por el MCP oficial | Elements de personaje y voz vinculada; usa la suscripción propia | Créditos de la suscripción |
| Upscale final a 1080×1920 y correcciones puntuales | **Comfy Cloud** | Grafo propio, y hay créditos disponibles | Créditos de Comfy |
| Modelos pagados dentro de un grafo (Kling, GPT Image…) | **Comfy Cloud · nodos de partners** | Se pagan con créditos de Comfy, no con la suscripción de Kling | Créditos de Comfy |

## fal.ai

**Conexión:** un solo `FAL_KEY` sirve para la API y para el MCP (`https://mcp.fal.ai/mcp`). La clave nunca va al repo: en Cursor va en la configuración del MCP; en agentes en la nube, en *Cloud Agents > Secrets*.

```json
{
  "mcpServers": {
    "fal-ai": {
      "url": "https://mcp.fal.ai/mcp",
      "headers": { "Authorization": "Bearer ${env:FAL_KEY}" }
    }
  }
}
```

### MiniMax H3 Max
- **Endpoints:** `minimax/h3-max/text-to-video`, `minimax/h3-max/image-to-video` (con `end_image_url` hace primer y último fotograma) y `minimax/h3-max/reference-to-video` (hasta 12 archivos).
- **Límites:** clips de 5 a 15 s, **solo 480p o 768p**, 24 fps. Siempre hay que escalar para entregar en 1080×1920.
- **Aspecto:** en image-to-video sale del keyframe. El keyframe tiene que ser 9:16.
- **Audio:** lo genera junto con la imagen. El diálogo va entre comillas.
- **`prompt_expansion_mode`:** reescribe el prompt antes de generar. Como nuestros prompts ya son órdenes de rodaje, hay que probar si conviene apagarlo.
- **Ciclo de trabajo:** explorar a 480p y 5 s. Cuando el plano está decidido, generar a 768p con la duración real. Usar `seed` fijo para comparar dos versiones de un mismo prompt.
- **Prompt de image-to-video:** describir el movimiento y **nombrar lo que no debe cambiar** del keyframe (encuadre, luz, cara, vestuario).

### Nano Banana Pro
- **Endpoint:** `fal-ai/nano-banana-pro/edit`, con `image_urls` para las referencias, `aspect_ratio: "9:16"` y `resolution: "2K"`.
- Mantiene hasta 5 personas consistentes. Con más personajes en cuadro, hay que dividir el plano o componer.
- Se escribe con la plantilla de rodaje (`produccion/plantilla_prompt_rodaje.md`).

## Kling (MCP oficial)

- **Servidor:** `https://kling.ai/mcp`. Se autentica con OAuth en el navegador, sin API key.
- **Créditos:** solo acepta **créditos pagados del workspace personal**. Los créditos de bonificación no sirven por MCP.
- **Modelos:** el servidor informa en tiempo real qué modelos hay. Antes de cada tanda, revisar que Kling 4.0 esté disponible.
- Reglas de prompt en `produccion/kling/kling_4_0_resumen.md`.

```json
{
  "mcpServers": {
    "kling": { "url": "https://kling.ai/mcp" }
  }
}
```

## Comfy Cloud

- **API:** requiere un plan pagado (Standard, Creator o Pro). Se manda el workflow en formato API, el JSON que da *Export Workflow (API)*.
- **Nodos de partners** (Kling, Nano Banana, GPT Image…): se pagan con créditos de Comfy. No aceptan la clave de Kling propia.
- **Workflows del proyecto:** van en `produccion/comfy/workflows/`, uno por tarea (`upscale_9x16.json`, `inpaint_mano.json`…). En cada workflow hay que anotar qué nodo recibe la imagen y qué nodo entrega el resultado.

## Weavy

Solo assets. Los assets aprobados se exportan con URL pública y se registran en el guion técnico (sección `assets`) para que los motores los usen como referencia. Ver `produccion/weavy/`.

## Validar en las primeras pruebas

- [ ] H3 Max: ¿mantiene la identidad desde un keyframe de Nano Banana Pro con luz roja de emergencia?
- [ ] H3 Max: ¿`prompt_expansion_mode` activo o apagado respeta mejor la orden de rodaje?
- [ ] H3 Max: el audio generado, ¿sirve como ambiente o se reemplaza entero en post?
- [ ] Kling MCP: ¿los créditos de la suscripción cuentan como «pagados del workspace personal»?
- [ ] Kling MCP: ¿expone Kling 4.0 con elements y primer fotograma en la misma generación?
- [ ] Comfy Cloud: ¿qué plan tiene la cuenta? Sin plan pagado no hay API.
- [ ] Comfy Cloud: ¿hay un nodo de partner para GPT Image 2.5?
