# Sistema de actuación para video con IA

Manual del Director para escribir `actuacion` y del Prompter para llevarla al prompt. Está adaptado de guías de actuación para Seedance 2.0 que trajo Cristian (2026-09-30); los principios sirven para cualquier motor.

**Axioma:** actuar es **conducta bajo presión**, no mostrar una emoción. El personaje quiere algo, algo se lo impide y actúa para conseguirlo. La emoción es consecuencia de esa lucha; nunca se escribe directo.

La regla anterior («quietud y mirada, sin emociones») evitaba la sobreactuación, pero dejaba al modelo sin objetivo: en la prueba v1, la mano solo tocaba el vidrio y Martina nunca miraba a Tomás. Sigue prohibido escribir emociones. Lo que cambia es que ahora se escribe **qué quiere el personaje y qué hace el cuerpo para conseguirlo**.

## 1. Los cinco pilares de cada plano

Todo personaje en cuadro los tiene. Si falta uno, la actuación se cae.

| Pilar | Qué es | Ejemplo (Martina en c01_p03) |
|---|---|---|
| **Objetivo** | Un verbo dirigido a otra persona, ahora | «Que Tomás no le vea la cara mientras miente» |
| **Obstáculo** | Qué lo impide, y qué pasa si falla | «Él la está mirando de frente; si la descubre, se acaba el viaje» |
| **Táctica** | El método concreto: presionar, esquivar, suplicar, provocar, ganar tiempo | «Esquiva: responde a la ventana, no a él» |
| **Beats** | Cada cambio de táctica. Tiene que verse: una pausa, un cambio de postura, de ritmo o de mirada | «0–1,5 s esquiva · 1,5 s él insiste · 2 s ella gira y le sostiene la mirada: miente de frente» |
| **Subtexto** | Lo que de verdad piensa. No se actúa: se escapa | «El "sí" sale demasiado rápido» |

Un plano de 2–4 s tiene uno o dos beats. Un bloque de 10–15 s, entre dos y cuatro.

## 2. Escuchar y reaccionar

- **La reacción empieza antes de que el otro termine de hablar.** Una cara neutra hasta el final de la frase del otro es actuación muerta.
- **Primero el pensamiento, después la palabra.** Antes de una respuesta difícil hay una micro pausa en la que se ve que decide qué decir.
- **Momento de evaluación:** después de algo importante (el mensaje, el golpe), el personaje necesita tiempo para procesarlo. Ese plano es el más valioso del montaje.

## 3. El cuerpo

- **Centro de gravedad:** alto (pecho, mentón: control, amenaza) o bajo (hombros caídos: cansancio, miedo).
- **Tempo:** los peligrosos se mueven poco; los nerviosos, mucho y a destiempo.
- **Respiración:** es lo más honesto. Quien corrió no habla con voz pareja.
- **Tarea física (business):** el personaje casi siempre está haciendo algo mientras habla o escucha: gira el celular, dobla el boleto, se aprieta la manga. La tarea mantiene las manos ocupadas con algo verdadero.
- **La interrupción es puntuación:** el golpe más fuerte es cuando el personaje **detiene** su tarea. Si Carmen deja de acomodar el bolso a mitad de un gesto, eso es un evento.
- **Distancia:** a menos de 0,5 m hay amor o violencia; entre 0,5 y 1,2 m, confianza; más lejos, recelo. Quién acorta o rompe la distancia cuenta la escena.
- **Estatus:** alto = cabeza quieta, movimientos lentos, pausas antes de responder. Bajo = se toca la cara o el pelo, pide permiso con los ojos. Lo más interesante es cuando se quiebra un segundo.

## 4. Los ojos (obligatorio en todo plano con cara)

Los ojos muertos son la marca número uno de la actuación hecha con IA.
- **La mirada tiene destino y tiempo:** a quién o a qué mira, desde qué segundo y hasta cuál. En planos de dos personas es obligatorio.
- **La mirada se mueve:** se va en un pensamiento, busca un detalle, vuelve. Nunca queda fija en un punto sin decidirlo.
- **El parpadeo depende del estado:** ráfagas bajo estrés, lento en control. La quietud es una decisión, no un congelamiento.
- **Los ojos llegan antes que la cabeza,** y el pensamiento se lee en los ojos antes que en la boca.
- **Brillo vivo:** los ojos se ven húmedos y con reflejo.

## 5. Estados, no transiciones

Los modelos fallan las transiciones y aciertan los estados. Se describe al personaje **ya dentro** de la acción y se encadenan estados por beat: no «mete la mano al bolsillo, saca el celular y lo mira», sino «0–1 s: el celular ya en la mano, pantalla hacia ella; 1–2 s: lo da vuelta sobre el muslo».

## 6. Grupo

- **Las reacciones del grupo viajan en ola, nunca a la vez:** uno reacciona primero, otro medio segundo después, otro no reacciona.
- **Ante la amenaza, todo se congela:** el contraste entre movimiento y quietud es la puntuación.
- **Nadie se mueve sin motivo:** hacia algo o lejos de algo.
- **Los extras no actúan:** están, con conducta mínima y sin reaccionar a la acción principal, salvo que el plano lo pida.

## 7. Plano cerrado = menos movimiento

Cuanto más cerrado el plano, menos se mueve la cara: solo los ojos y el pensamiento. En un primer plano, una ceja que se mueve es un grito.

## 8. Perfil de actuación de cada personaje

Cada personaje fijo tiene **un** perfil de actuación, que se escribe una vez y se adapta a cada plano. Va en `produccion/actuacion/perfiles.md`, está en inglés y se arma desde `biblia/personajes.md`, sin inventar historia.

Plantilla (150–220 palabras, un párrafo, solo conducta observable):

```
Character acting as [NAME]. [Age, build, posture: the body tells the biography]. [The inner engine in one clause]. Vocal behavior: [pitch, pace, how the voice shifts under pressure]. Habits and tics: [tic + its trigger; stress tic + its trigger; what they do to hide what they feel; the facial mask and the exact condition under which it cracks]. Eye life: [blink rate, gaze pattern, what the eyes do before the head moves]. Walk: [a named gait, with weight, rhythm and foot placement]. However, when [trigger], [how the posture, gait and face change]. [Optional: the one person or thing that genuinely softens the face].
```

Reglas:
- **Todo tic tiene un disparador:** no «se muerde el labio», sino «se muerde el labio cuando le preguntan por Diego».
- **Toda máscara tiene su grieta:** al menos una cláusula «However, when…».
- **Sin vestuario, cámara ni color:** el perfil tiene que sobrevivir a cualquier cambio de ropa o de plano.
- **La voz no se adapta.** La voz de cada personaje es fija y sale de ElevenLabs. El perfil describe cómo se comporta el habla en lo dramático, no el timbre.

**Adaptación a cada plano:** el perfil se **reescribe** para el plano, nunca se pega tal cual. Se mantiene el núcleo (tics, ojos, voz) y se adapta a la postura, la acción y el beat. Lo que no puede ocurrir se **transforma, no se borra**: si alguien inquieto está sentado, su energía pasa a las manos o a los pies.

## 9. Cómo se escribe en el guion técnico

El Director llena `actuacion` con esta estructura (ver `formato_guion_tecnico.md`):

```yaml
actuacion:
  objetivo: "Que Tomás no le vea la cara mientras miente."
  obstaculo: "Él la mira de frente; si la descubre, se acaba el viaje."
  tarea: "Tiene el celular boca abajo sobre el muslo izquierdo, la mano encima."
  beats:
    - { de: 0.0, a: 1.5, conducta: "Responde a la ventana, no a él. El pulgar aprieta el celular.", mirada: "La ventana lateral, a la izquierda del cuadro." }
    - { de: 1.5, a: 3.0, conducta: "Él insiste. Ella gira la cabeza, los ojos llegan antes. Le sostiene la mirada: miente de frente.", mirada: "Los ojos de Tomás." }
  ojos: "Parpadeo lento y controlado; una ráfaga corta al girar."
```

## 10. Revisión antes de entregar

- [ ] ¿Cada personaje en cuadro tiene objetivo (un verbo dirigido a alguien) y obstáculo?
- [ ] ¿Hay beats con tiempos, y cada cambio se ve en la conducta?
- [ ] ¿Cada mirada tiene destino y tiempo?
- [ ] ¿Hay una tarea física, y se usa su interrupción cuando corresponde?
- [ ] ¿Está escrito como estados, no como transiciones?
- [ ] ¿Las reacciones del grupo están escalonadas?
- [ ] ¿No hay ninguna palabra de emoción?
- [ ] En una escala de 0 (maniquí) a 5 (magnético), ¿llega a 4? Un 4 tiene conducta continua, tácticas que cambian, subtexto que se escapa y reacciones que empiezan antes de la frase del otro.
