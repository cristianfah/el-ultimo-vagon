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
- **Indicaciones:** describen cómo se dice la línea, no lo que hace el cuerpo: `[whispers]`, `[softly]`, `[breathless]`, `[trembling voice]`, `[quickly]`, `[nervous]`, `[tired]`, `[shouting]`, `[pause]`, `[long pause]`. Una indicación vale hasta la siguiente.
- **Una pista por línea,** con un poco de aire al inicio y al final, para usarla como referencia de audio en Kling 4.0 (`@Audio1 is [Personaje]'s voice…`).
- **Archivos:** `renders/voces/capNN/<personaje>_<bloque>_<n>.mp3` (Drive), con el texto exacto y las indicaciones registradas al lado.

## Pendiente
- Voces de Carmen, Iván, Hugo y el infiltrado (hablan desde el capítulo 2).
