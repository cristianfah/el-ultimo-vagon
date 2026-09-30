# Keyframes y assets: Nano Banana Pro y GPT Image 2.5

Fuentes: [guía de Google Cloud para Nano Banana](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana) y [guía de prompting de OpenAI](https://developers.openai.com/api/docs/guides/image-prompting).

## Keyframe (generación con referencias)
Se mantiene la plantilla de rodaje (`produccion/plantilla_prompt_rodaje.md`): FILM STILL, MOMENT, COMPOSITION, LENS, LIGHT, TEXTURE y FINISH. En la prueba v1 funcionó: Control de calidad aprobó los keyframes con ancla sin rehacer ninguno. Se agrega:
- **En MOMENT, el beat de actuación:** el estado físico del primer instante del plano, con la mirada, su destino y la tarea de las manos. El keyframe es el primer fotograma del video: tiene que contener el estado inicial exacto.
- **En COMPOSITION, el mapa:** qué hay detrás del sujeto, qué se ve por cada vidrio y dónde está cada persona que queda fuera de cuadro pero cerca.
- **Manos y props:** qué mano, en qué lado del cuadro y en qué estado.
- **Referencias con rol:** «Image 1 is Martina: match her face, hair and sweater exactly. Image 3 is the reverse shot: match its light.» Se dice cómo se combinan.
- **Positivo antes que negativo:** «empty aisle» antes que «no people».

## Edición (una variable a la vez)
Primero Nano Banana Pro, porque edita sobre el original. GPT Image 2.5 edit se usa para cambios locales muy finos.

```text
Edit the image: [one-line goal].

CHANGE: [the single thing that changes, described precisely].

PRESERVE EXACTLY:
- [face, hair, wardrobe, hands and props with their side]
- [positions, camera angle, framing limits]
- [every light source, shadows, colour grade, grain]

ONLY CHANGE: [the change, restated]. Everything else stays identical.
```

Si hay que reconstruir la imagen, no es una edición: se regenera.

## Otra vista de la misma locación (contraplano)
Se describe objeto por objeto dónde queda cada cosa en la vista nueva: «in the main view the door is at the far end, frame centre; in this reverse view the door is behind the camera, and the aisle recedes toward the tail with the amber lamps on the left». Sin eso, el modelo mezcla la geometría. Cuando se armen los assets definitivos, las vistas del set salen de la biblia del set.
