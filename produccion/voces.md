# Voces de la serie

Aprobadas por Cristian el 18-oct-2026. Están en la biblioteca de ElevenLabs de la cuenta (plan Creator). **Cada personaje usa siempre esta voz;** no se diseñan voces nuevas para un personaje existente.

| Personaje | Nombre en ElevenLabs | voice_id | Descripción |
| --- | --- | --- | --- |
| Tomás | UV · Tomás | `32TKm2yo0S1caJHTYiFJ` | Hombre chileno de 31 años, acento suave de Santiago. Voz media grave, tranquila y educada; cuando duda baja la voz y se vuelve frío |
| Martina | UV · Martina | `v4QCZzj0PB6WaqO3Sn6D` | Mujer chilena de 29 años, acento suave de Santiago. Voz baja, cálida, cansada y algo ronca; casi susurra; cuando miente responde demasiado rápido |
| Diego | UV · Diego | `qXAGWqslOQWtQyyko9NJ` | Hombre chileno de 30 años, acento suave de Santiago. Voz cálida y rasposa; bajo presión habla sin aire y se le quiebra al final de las frases |

## Cómo se generan las líneas

- **Acento:** chileno suave, latinoamericano. Nunca acento de España. (Cierra la pregunta abierta del acento.)
- **Modelo:** ElevenLabs **v4** (`eleven_v4`), que acepta indicaciones de entrega entre corchetes. El diseño de voz solo fija timbre y acento; la actuación se dirige línea por línea.
- **Indicaciones:** describen cómo se dice la línea, no lo que hace el cuerpo (`[softly]`, `[breathless]`, `[quickly]`, `[nervous]`, `[tired]`, `[shouting]`, `[pause]`…). Una indicación vale hasta la siguiente.
- **Menos es más (nota de Cristian, 18-oct-2026):** en v4 las indicaciones exageran la actuación. Máximo una o dos por línea; la voz diseñada ya trae el tono del personaje. Probar primero sin etiquetas, con la puntuación (`...`, `—`) y `[pause]`.
- **`[whispers]` no se usa:** da un susurro extremo. Para hablar bajo, `[quietly]` o `[softly]`.
- **Cada toma es una lectura distinta:** tres tomas por línea con intención diferente (p. ej. nerviosa / casual forzada / plana). Nunca varias tomas con las mismas indicaciones: salen casi iguales.
- **Una pista por línea,** con un poco de aire al inicio y al final, para usarla como referencia de audio en Kling 4.0 (`@Audio1 is [Personaje]'s voice…`).
- **Archivos:** `renders/voces/capNN/<personaje>_<bloque>_<n>.mp3` (Drive), con el texto exacto y las indicaciones registradas al lado.

## Capítulo 1: tomas elegidas (18-oct-2026)

Flujo de ElevenLabs `r6dpxC6EYTl7hcfMXoJw`. El `generation_id` identifica la toma. **Los MP3 para el animatic están en `produccion/pruebas/cap01_animatic/voces/`** con el nombre `<personaje>_<bloque>_<n>.mp3`.

| # | Bloque | Personaje | Línea | Indicaciones | generation_id |
| --- | --- | --- | --- | --- | --- |
| 1 | 2 | Tomás | ¿Dónde estabas? | `[curious][a little suspicious]` | `HvCQbsS9OiNL80lqZwOT` |
| 2 | 2 | Martina | En el baño. | `[casually][forced lightness]` | `4RrclPgpmeD4JrP6g5JA` |
| 3 | 2 | Tomás | ¿Tu papá sabe que vienes en este tren? | `[gently][sincere]` | `tmSKhQo2s9J0j7Ziz1BA` |
| 4 | 2 | Martina | No. … Esa era la idea. | `No. [pause] Esa era la idea.` (sin etiquetas) | `hnhzQySfP72ZEuoSGEq7` |
| 5 | 7 | Diego | ¡Martina! ¡Martina, ábreme! | `[breathless][pleading] … [voice breaking]` | `I8ao0FNiZPHDuv6QMAt1` |
| 6 | 7 | Diego | ¡Te vi en el vagón 2! (escrito «vagón dos») | `[out of breath][pleading][voice cracks]` | `vtgFQKEC0fz06AsPRAwC` |
| 7 | 7 | Tomás | ¿No estabas en el baño? | `[confused][slowly]` | `rRdo5vZ8f4jqVdeqSkLr` |

## Pendiente
- **Voz de Don Hugo:** habla desde el capítulo 1 en la v10 («¡Al último vagón! ¡Rápido!», toma de 1,6 s como máximo).
- Voces de Carmen, Iván y el infiltrado (hablan desde el capítulo 2).
