# Kling 4.0 y 4.0 Flash: formato de prompt

Reglas del proyecto en `produccion/kling/kling_4_0_resumen.md`. Fuentes: [blog de Kling](https://kling.ai/blog/kling-ai-prompt-guide) y la [guía de Morphic para 4.0](https://morphic.com/resources/how-to/kling-4-0-guide), que no es oficial. Cuando salga la versión completa (octubre de 2026), hay que revisar contra la guía oficial.

- **Largo:** acepta hasta 8.000 tokens. Lo que falta se rellena con un promedio, así que vale el mismo método de la skill: sin huecos.
- **Estructura:** una orden de rodaje con sujeto y acción, locación y luz, cámara, tiempos y sonido.
- **Beats con rangos de tiempo** (`0-3s: … 3-8s: …`), con una acción principal por rango. Se pide el mismo personaje y la misma luz en todos los planos.
- **Referencias:** un rol por referencia. `@Image1 is the first frame.` / `@Element1 is Martina.`
- **Videos de referencia** (solo en 4.0 completo): sirven para actuación, movimiento, cámara y ritmo. Es el camino para la referencia de actuación grabada con el celular.
- **Diálogo:** entre comillas, con el idioma y el acento: `Martina says in neutral Latin American Spanish, almost voiceless: "Diego…"`. No se describe el tono de una voz ya vinculada.
- **Negativo:** negaciones por eje, solo para lo que el plano no debe hacer (*no tilt, no orbit*). El resto va en positivo dentro del prompt.
- **Flash:** no tiene keyframes ni primer y último fotograma. Solo primer fotograma y referencias.

```text
@Image1 is the first frame. @Element1 is [character].
[Shot framing and first-frame blocking, with the background and whether it moves].
0-2s: [camera: type, amplitude, speed]. [Acting state with gaze target and hands].
2-5s: [...]. [Character] says in neutral Latin American Spanish, [delivery]: "[line]".
[Light kept steady; changes with their source]. [Physical behavior of cloth, props and contact].
Sound: [ambience], [effects with their second]. The frame contains no text of any kind. No music. No subtitles, no captions, no on-screen text.
```
