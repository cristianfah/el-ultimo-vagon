# Weavy (Figma Weave): armar flujos con JSON

El canvas de Weavy **copia y pega los nodos como JSON**. Se puede generar un flujo completo (nodos, conexiones y prompts) con un script o un agente, y pegarlo en el canvas con Cmd+V. Así se construyó el flujo «VAGÓN 7 — Assets base», con 52 nodos.

## Formato del portapapeles

```json
{ "workflowId": "<id del flow>", "nodes": [ ... ], "edges": [ ... ] }
```

Al pegar, Weavy reposiciona el grupo respecto de la vista, pero **mantiene las posiciones relativas** entre nodos.

## Tipos de nodo usados

| type | Qué es | Campos clave en `data` |
|---|---|---|
| `import` | Imagen de referencia | `files[0]` = `{type:"image", url, width, height, thumbnailUrl, publicId, id, name, insertionOrder:0}`; `output.file` = el mismo objeto; `selectedIndex:0`. **El nombre del archivo (`name`) es el título que muestra el nodo** |
| `promptV3` | Texto del prompt | `prompt`, `result.prompt` y `output.prompt` con el mismo texto; `output.type:"text"` |
| `custommodelV2` | Modelo (GPT Image 2.5, Nano Banana Pro…) | `name` (**es el título visible**; se puede renombrar, por ejemplo «soto_sheet · GPT 2.5»), `model`, `params`, `handles.input`, `handles.output` |
| `stickynote` | Nota | `result.note` = texto |

### Handles de entrada de los modelos
- **Nano Banana Pro:** `prompt` (order 0), `image_1` (order 1), `image_2` (order 2)…
- **GPT Image 2.5:** `prompt` (0), `image_1` (1), `mask` (2), `image_2` (3), `image_3` (4)…
- Cada handle nuevo: `{"description":"", "format":"uri", "id":"<uuid>", "label":"image_N", "order":N, "required":false, "type":"image"}`.

### Parámetros
- **Nano Banana Pro:** `aspect_ratio` (`9:16`, `4:5`, `2:3`, `16:9`…), `resolution` (`1K`, `2K`, `4K`).
- **GPT Image 2.5:** `image_size` (`portrait_16_9` = 9:16, `portrait_4_3`, `landscape_16_9`, `auto`), `model` (`Flare` o `Sunburst`), `quality`.

### Conexiones (edges)
```json
{
  "id": "<uuid>", "source": "<nodo origen>", "target": "<nodo destino>",
  "sourceHandle": "<nodo origen>-output-<file|prompt|result>",
  "targetHandle": "<nodo destino>-input-<prompt|image_N>",
  "type": "custom",
  "data": {"sourceColor": "...", "targetColor": "...", "sourceHandleType": "any|text|image", "targetHandleType": "text|image"}
}
```
- Salida de `import`: `file` (tipo `any`).
- Salida de `promptV3`: `prompt` (tipo `text`).
- Salida de un modelo: `result` (tipo `image`).

## Cómo obtener plantillas frescas de nodos
1. En Weavy, agrega a mano un nodo de cada tipo.
2. Selecciónalos y cópialos con Cmd+C.
3. Pega el portapapeles en `plantillas/` como JSON.

Un script puede clonar esas plantillas: se cambian los `id` (uuid nuevo), la posición, `name`, los prompts y los handles.

## Subir imágenes
- El nodo `import` acepta un link pegado: un evento de paste con la URL en el campo «Paste a file link» vuelve a subir la imagen a `media.weavy.ai`.
- **Alternativa:** la conexión de Figma Weave tiene un widget de subida que devuelve la URL en `media.weavy.ai`.

## Por construir (tarea para Cursor)
`tools/weavy_builder`: un script que lea un shot list (YAML o Markdown) y genere el JSON para pegar, con un nodo `import` por referencia, un `promptV3` por plano, un modelo por plano y sus conexiones.
