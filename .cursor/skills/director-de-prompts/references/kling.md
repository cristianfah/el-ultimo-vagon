# Kling 4.0: formato de prompt

Kling 4.0 es el motor final de la serie desde el 18-oct-2026 (salió el 16-oct-2026). Reglas del proyecto en `produccion/kling/kling_4_0_resumen.md`. **Plantilla y ejemplo completo en `produccion/prompting/guia_direccion_video.md` (secciones 7 y 8).** Fuentes: [anuncio de Kling 4.0](https://finance.yahoo.com/technology/ai/articles/kling-ai-launches-kling-4-161000016.html), [guía de Each Labs](https://www.eachlabs.ai/blog/kling-4-0-prompting-guide) y [Omni Reference de Kling](https://kling.ai/blog/kling-video-3-omni-reference-workflows-multi-element), que no son la guía oficial de 4.0.

- **Capacidades:** clips de 3 a 30 s; hasta 15 referencias (10 imágenes, 5 videos con 30 s en total, 7 elements); hasta 10 keyframes; videos de referencia para guiar actuación, movimiento y cámara; prompts de hasta 8.000 tokens.
- **Un bloque, una llamada:** todo el bloque del guion (8–20 s, varios planos) va en una sola generación. No se usan keyframes ni primer y último fotograma, salvo un inserto con encuadre exacto.
- **Estructura:** REFERENCES → LOOK → SHOTS (uno por plano, con su rango de tiempo) → SOUND → cierre fijo. Cada plano: encuadre y corte, cámara (tipo, amplitud, velocidad, motivo), bloqueo, beats de actuación con segundo, diálogo exacto con entrega física.
- **Referencias:** un rol por referencia, declarado al principio: `@Image1 is Martina: identity, face, hair and wardrobe only; ignore the sheet layout and background.` Kling no publicó una sintaxis oficial de @; lo importante es que cada referencia tenga un solo rol y nombre.
- **Diálogo:** entre comillas, en español, con el idioma y la entrega: `Martina says in neutral Latin American Spanish, quietly: "No."`. Si la voz está vinculada (audio de referencia), no se describe el timbre.
- **Negativo** (si la interfaz lo tiene): `push-in, zoom, dolly, warped hands, extra fingers, morphing faces, text, subtitles, captions, logos, music`. Todo lo demás va en positivo dentro del prompt.
- **Kling infla el volumen del torso:** indicar la contextura («average, slightly soft build»).
- **4.0 Flash** (720p, hasta 20 s, solo primer fotograma) queda para exploración.

```text
REFERENCES
@Image1 is [Character]: identity, face, hair and wardrobe only — [anchors]. Ignore the sheet layout and background.
@ImageN is [location] with its light: match layout and light exactly.

LOOK
Live-action, cinematic, 9:16 vertical. [Lens, practical light sources, film look.] [Train motion.] Held for the whole clip: [continuity].

SHOTS
Shot 1 (0.0–X.Xs) — [framing, where the frame cuts]. Camera: [type, amplitude, speed], [motive]. [Blocking]. [Beats with seconds; gaze targets; hands with side]. [Character] says in neutral Latin American Spanish, [delivery]: "[line]".
Shot 2 (X.X–Y.Ys) — The camera cuts to [...].

SOUND
[Ambience]. [Effects with their second]. Dialogue only as sound.

No music. No subtitles, no captions, no on-screen text.
```
