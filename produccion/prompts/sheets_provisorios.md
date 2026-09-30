# Hojas provisorias para pruebas (no son el casting final)

Sirven para probar continuidad y referencias. El vestuario sale de los hechos del Continuista en `produccion/shotlists/cap01.yaml` (todos «propuesta»). Las caras son inventadas para la prueba.

Modelo: Nano Banana Pro (`fal-ai/nano-banana-pro`), 3:4, 1K. Piel seca y luz neutra, para que ese brillo no se arrastre a las tomas.

## Martina
```
Character reference photo for a film. Full body, standing, facing the camera, arms relaxed. A woman around 29, tied-back low ponytail, plain cream wool sweater with round neck and black trousers, dark flat shoes, no coat, no bag, no jewelry. Dry matte skin, natural expression, mouth closed. Plain neutral gray studio backdrop, soft even daylight, no shadows on the backdrop. Sharp focus, 50mm lens, photographic, no text.
```

## Tomás
```
Character reference photo for a film. Full body, standing, facing the camera, arms relaxed. A man around 31, short hair, olive green jacket over a dark gray t-shirt, dark jeans, plain boots, no rings. Dry matte skin, calm neutral expression, mouth closed. Plain neutral gray studio backdrop, soft even daylight, no shadows on the backdrop. Sharp focus, 50mm lens, photographic, no text.
```

## Diego
```
Character reference photo for a film. Full body, standing, facing the camera, arms relaxed. A man around 30, light gray canvas work jacket, dark t-shirt, dark trousers, plain boots. Dry matte skin, tired neutral expression, mouth closed. Plain neutral gray studio backdrop, soft even daylight, no shadows on the backdrop. Sharp focus, 50mm lens, photographic, no text.
```

## Placa: vagón de pasajeros, luz de viaje (ámbar)
```
Film still of an empty night-train passenger carriage interior, vertical framing, camera at seated eye height looking down the central aisle. Pairs of worn blue-gray seats on both sides all facing forward, small warm amber reading lamps above the seats, dark windows with rain streaks on the outside of the glass, luggage racks above. Only practical warm lamp light, deep shadows in the far end. No people, no text, photographic, 35mm lens, slight film grain.
```

## Tomás v2 (edición: chaqueta cerrada, hecho hc12)
Endpoint `openai/gpt-image-2.5/flare/edit` con la hoja v1 como `image_urls[0]`.
```
Edit Image 1. Keep the same man, face, hair, pose, backdrop and lighting exactly. Only change: his olive green cotton jacket is now zipped closed up to the chest, so the dark gray t-shirt shows only at the collar. Nothing else changes.
```

## Carmen (hc13)
```
Character reference photo for a film. Full body, standing, facing the camera, arms relaxed. A woman around 54, gray-streaked hair tied back, two-piece aqua green nurse scrubs (V-neck top and trousers) under an open dark gray wool coat that reaches the knees, the V-neck clearly visible, plain dark shoes, a brown handbag hanging from one hand. Dry matte skin, tired calm expression, mouth closed. Plain neutral gray studio backdrop, soft even daylight. Sharp focus, 50mm lens, photographic, no text, no logos.
```

## Iván (hc15)
```
Character reference photo for a film. Full body, standing, facing the camera, arms relaxed. A man around 45, very short hair, stubble, heavy brown canvas work jacket zipped up to the chest, dark work trousers, worn work boots. Dry matte skin, hard neutral expression, mouth closed. Plain neutral gray studio backdrop, soft even daylight. Sharp focus, 50mm lens, photographic, no text, no logos.
```

## Don Hugo (hc16, hc28)
```
Character reference photo for a film. Full body, standing, facing the camera, arms relaxed. A man around 62, gray mustache, train conductor uniform: dark gray jacket with plain smooth metal buttons, matching gray trousers, black leather belt, gray peaked cap. No badges, no emblems, no logos, no name tags. The jacket is buttoned and covers the belt. Dry matte skin, calm tired expression, mouth closed. Plain neutral gray studio backdrop, soft even daylight. Sharp focus, 50mm lens, photographic, no text.
```

## Placa: último vagón, luz de emergencia roja, hacia la puerta (hc01, hc22)
```
Film still of the empty interior of the last carriage of a night train, vertical framing, camera at standing eye height in the aisle, looking toward the closed connecting door at the end. The door has a single vertical rectangular glass window with a plain metal frame at adult head height; beyond the glass, only darkness. The carriage is lit only by low red emergency lights along the walls near the floor, deep red, plus one cold white fluorescent tube near the door, dim. Worn blue-gray seats, luggage racks, no people. Deep shadows, light haze. No text, no logos, photographic, 32mm lens, fine film grain.
```

## Prop: celular de Martina (hc25)
```
Product reference photo. A generic modern smartphone lying face up on a plain neutral gray surface, matte terracotta case, no brand, no logo, simple camera module without recognizable design, the screen off and black. Soft even light, top-down view, sharp focus, no text.
```

## Prop: revólver de Don Hugo (hc28)
```
Prop reference photo. An old generic revolver in a short brown leather belt holster, worn blued steel, short barrel, dark wooden grips, the cylinder and grip visible above the holster, no markings, no engravings, no logos. Lying on a plain neutral gray surface, soft even light, sharp focus, no text.
```

## Placa vagón ámbar v2 (edición: alertas del Director de fotografía en c01_p03 y c01_p08)
Endpoint `openai/gpt-image-2.5/flare/edit`. Image 1 = placa ámbar v1, Image 2 = placa del último vagón (para copiar la puerta).
```
Edit Image 1. Keep the carriage, seats, reading lamps, camera position and lighting exactly. Two changes only: 1) outside the windows it is a dark blue night with rain streaks on the glass, no warm city lights, no bokeh, no street lamps. 2) The connecting door at the far end of the aisle has the same single tall vertical rectangular glass window with a plain metal frame as the door in Image 2, at adult head height, dark behind the glass. Nothing else changes.
```
