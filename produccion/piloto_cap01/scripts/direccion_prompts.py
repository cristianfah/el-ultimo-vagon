#!/usr/bin/env python3
"""Agrega a los prompts de prueba de 4 s el bloque DIRECTION RULES (checklist de 6 reglas del 07
y marcas del guionista del 27-nov) y una línea AUDIO LOCK con las voces de produccion/voces.md.
Idempotente: si el bloque ya está, lo reemplaza. Uso: python3 -I direccion_prompts.py <carpeta pruebas4s>"""
import os, re, sys

LAYOUT = {
 "v2": "Carriage 2 never changes: two rows of paired blue seats with a central aisle; side windows on both walls; front door at one end, rear door at the other; the blue-shirt man's bench by the window wall, the briefcase under it at the aisle end; the woman reading across the aisle.",
 "v5": "Carriage 5 never changes: two rows of paired blue seats with a central aisle; side windows on both walls; the front door (where the infected come in) at one end; the rear door (Hugo's door, to the gangway) at the other; Martina's seat on the window side.",
 "fuelle": "The gangway never changes: a short narrow metal corridor with no windows; the carriage 5 door with its small window at one end, the last carriage's door with its key lock and handle at the other.",
 "ultimo": "The last carriage never changes: six rows of 2+2 seats facing the door; one single door with a small mesh window, the cold tube above it on the inside, the brass lock plate with keyhole above and handle below; the red emergency handle right of the door; at the far end the back wall with the black rear window and the conductor's cabin on its left. There is no second door.",
}
GAIT = {
 "Martina": "quick, small steps, head down",
 "Tomás": "long, careful strides",
 "Carmen": "short, heavy, steady steps",
 "Iván": "heavy, square, pushing forward",
 "Hugo": "stiff, slightly stooped",
}
VOICE = {
 "Tomás": "Chilean man, 31, soft Santiago accent; mid-low voice, calm and polite; when he doubts he lowers his voice and turns cold",
 "Martina": "Chilean woman, 29, soft Santiago accent; low, warm, tired, slightly husky voice, almost a whisper; answers too fast when she lies",
 "Hugo": "Chilean man, 62, soft Santiago accent; deep, worn, unhurried voice with a conductor's quiet authority; when he shouts his voice cracks but commands",
 "Diego": "Chilean man, 30, soft Santiago accent; warm, raspy voice; under pressure he speaks out of breath and his voice breaks at the end of phrases",
 "Carmen": "Chilean woman, 54, soft Santiago accent; warm but firm nurse's voice (no approved ElevenLabs voice yet)",
 "Iván": "Chilean man, 45, soft Santiago accent; deep, dry voice, short phrases (no approved ElevenLabs voice yet)",
}
TESTS = {
 "c00b": ("v2", "Warm amber reading lamps from above: one over the couple's row, one over the woman reading, one far back; the rest is dark. Half of each face in shadow.", [
   "CUT 1 (b0_p3): Martina's hand grips the seat back; her breath stops when the man stirs. The man's head slides down the window glass toward frame left.",
   "CUT 2 (b0_p4): the woman reading far back turns one page - the only movement in the background - and never looks at Martina. Sound before the cut: a low hum starts in the last 0.3s.",
 ]),
 "c03b": ("v2", "Warm amber reading lamps from above, one over the couple's row; the rest dark. Half of each face in shadow.", [
   "CUT 1 (b3_p4): the man's head turns toward frame right, toward his wife.",
   "CUT 2 (b3_p5): he lunges toward frame right; she stays on frame right.",
   "CUT 3 (b3_p6): the woman reading drops her book. Sound before the cut: a distant scream starts over the last 0.5s.",
 ]),
 "c04b": ("v5", "Red emergency strip on the ceiling, from above; amber lamps off; Hugo's doorway backed by the dark red gangway. Half of each face in shadow.", [
   "CUT 1 (end of b4_p5): Hugo keeps the key high in his right hand; the whistle has already blown (it was his breath).",
   "CUT 2 (b4_p6): Tomás drags Martina by the hand; each passenger dodges a different seat back; Martina on frame left, Tomás on frame right.",
 ]),
 "c05a": ("fuelle", "Red emergency strip on the gangway ceiling, from above; no white light. Half of each face in shadow.", [
   "CUT 1 (b5_p1): both of Hugo's hands force the key.",
   "CUT 2 (b5_p2): Iván slams the carriage 5 door and pushes the group on.",
   "CUT 3 (b5_p3): the arm comes through the glass; Carmen's reach goes toward the group, frame left.",
 ]),
 "c05b": ("ultimo", "Gangway: red strip from above. Last carriage: red emergency light from above plus the cold tube over the door on the inside, rimming heads and shoulders only. Half of each face in shadow.", [
   "CUT 1 (b5_p6): Hugo's two hands on the key; he keeps the key in his hand when it comes out.",
   "CUT 2 (b5_p7): the group stumbles in; Tomás drags Martina; Iván pushes Carmen. Carmen's whimper is heard before the cut.",
 ]),
 "c06a": ("ultimo", "Red emergency light from above; the cold tube above the door on the inside rims heads and shoulders only. Half of each face in shadow.", [
   "CUT 1 (b5_p8): Hugo crushes the hand with the door and turns the key. Sound before the cut: the clack of the lock lands over the cut.",
   "CUT 3 (start of b6_p1): a distant scream from carriage 5 is heard before the banging stops.",
 ]),
 "c07a": ("ultimo", "Red emergency light from above; the cold tube above the door, behind the camera, puts only a thin cold edge on heads and shoulders. Half of each face in shadow.", [
   "b7_p3: Martina on frame right, facing us, eyes just above the lens. She inhales once through the nose before Diego's second line. Her only new gesture after «¡Te vi en el vagón 2!» is one single blink, nothing else. Behind her the heads turn one by one.",
 ]),
}
MARK_OPEN, MARK_CLOSE = "DIRECTION RULES (27-nov)", "END DIRECTION RULES"

def present(text):
    return [n for n in ["Martina","Tomás","Carmen","Iván","Hugo","Diego"] if re.search(r"\b"+n+r"\b", text)]

def block(cid, people):
    lay, light, marks = TESTS[cid]
    g = "; ".join(f"{n}: {GAIT[n]}" for n in people if n in GAIT)
    lines = [MARK_OPEN,
      "LAYOUT: " + LAYOUT[lay],
      "LIGHT SOURCE: " + light,
      "AXIS: every screen direction in SIDES LOCK holds for the whole clip; nobody crosses the axis.",
      "BREATH: before any key line or key action, one directed breath or blink, never more.",
      "TIMING: the action is already under way in the first frame; no dead air after it ends.",
      ("GAIT: " + g + ".") if g else "",
      "MARKS:"] + ["- " + m for m in marks] + [MARK_CLOSE]
    return "\n".join(l for l in lines if l)

def audio_lock(people):
    return "AUDIO LOCK (produccion/voces.md, never Mexican, neutral or Spain Spanish): " + " | ".join(f"{n}: {VOICE[n]}" for n in people)

def main(root):
    n = 0
    for d in sorted(os.listdir(root)):
        cid = d.split("_")[0]
        if cid not in TESTS: continue
        for f in sorted(os.listdir(os.path.join(root, d))):
            if not (f.startswith("prompt_") and f.endswith(".md")): continue
            p = os.path.join(root, d, f); s = open(p, encoding="utf-8").read()
            s = re.sub(r"\n" + re.escape(MARK_OPEN) + r".*?" + re.escape(MARK_CLOSE) + r"\n", "\n", s, flags=re.S)
            s = re.sub(r"\nAUDIO LOCK \(produccion/voces\.md[^\n]*", "", s)
            people = present(s)
            i = s.index("\nAUDIO\n")
            s = s[:i] + "\n" + block(cid, people) + "\n" + s[i:]
            j = s.index("\nAUDIO\n") + 1
            k = s.index("\n\n", j)
            s = s[:k] + "\n" + audio_lock(people) + s[k:]
            open(p, "w", encoding="utf-8").write(s); n += 1
    print(n, "prompts actualizados")

if __name__ == "__main__":
    main(sys.argv[1])
