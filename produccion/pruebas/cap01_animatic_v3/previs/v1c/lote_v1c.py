#!/usr/bin/env python3
"""Lote de retomas previs v1c: Parte B + los 7 arreglos de Cristian (18-oct-2026, 22:45).

Solo escribe archivos (prompts/*.txt y lote_v1c.json); no llama a fal. Lo corre run_lote_v1c.py.
Una variable por paso. Base "frame:<id>" = el último aceptado de ese plano (v1c/frames/<id>.png si
existe, si no previs/frames/<id>.png). "ref:<clave>" = asset de produccion/assets/fal_urls_v1.json.
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
P = HERE / "prompts"; P.mkdir(exist_ok=True)

KEEP = ("- camera position, lens, framing and 9:16 aspect (unless the change says otherwise)\n"
        "- every person's face, hair, wardrobe, pose and eyeline not named in the change\n"
        "- every light source, shadow, colour grade and film grain not named in the change\n"
        "- natural hands with five separate fingers")
def txt(one, change, keep_extra=""):
    k = KEEP + (("\n" + keep_extra) if keep_extra else "")
    return (f"Edit the image: {one}\n\nCHANGE: {change}\n\nPRESERVE EXACTLY:\n{k}\n\n"
            f"ONLY CHANGE: {one} Everything else stays identical. No text.")

LUZ2 = ("lower the carriage light to the LOW amber of Image 2.",
        "Of the reading lamps under the luggage racks only two or three stay lit (the ones nearest the action in this shot); every other lamp and every ceiling fixture is dark. "
        "Short warm cones (~2800K) with real darkness between them; passengers away from the lit lamps fall into deep shade, almost silhouettes. Side windows stay black night with rain only on the outside of the glass.")
LUZR = ("make the red emergency light hard and from above, with no white fill on any face.",
        "The narrow red ceiling strip (#B3001B) is the only red source and lights from above: every face is half in shadow, real black zones, no white or grey fill light on skin, no pink or magenta. "
        "Keep the one cold white tube above the door only where it already is and only on heads and shoulders near it. Shorten any long glowing red neon lines to the single narrow ceiling strip.")
PARED = ("replace the far door at the back of the shot with the rear wall of this last carriage, as in Image 2.",
         "Behind the people there is no door, no small door window and no cold tube: only the rear end wall of the last carriage in red light, the rear window at its centre (black, nothing visible through it), "
         "the conductor's cabin door at frame LEFT, and the last seats in deep shade. This is the opposite end of the carriage from the front door; the cold white tube is behind the camera, above the real door.")
TOMAS = ("give Tomás the exact hair of Image 2.",
         "Tomás's hair becomes short dark brown hair, neatly combed with a side parting, tidy, short on the sides, as in Image 2: no curls, no fringe falling on the forehead, no messy waves. Same face, same thin metal-frame glasses.")
VENTANITA_R = "Behind the door window only the dark gangway in faint red, black glass: no sky, no rain, no water drops, no lit corridor."

S = []
def step(sid, frame, model, base, refs, one, change, check, keep="", cost=0.15, depends=None, prompt=None):
    name = f"{sid}_{frame}.txt"
    (P / name).write_text(prompt or txt(one, change, keep))
    S.append({"paso": sid, "plano": frame, "modelo": model, "base": base, "refs": refs, "prompt": f"prompts/{name}",
              "depende_de": depends or [], "costo_est_usd": cost, "revisar": check})

# ---------------- Vagón 2 (bloques 0, 1 y 3): primero la luz, después la historia ----------------
step("V01","b0_p2","nbp","frame:b0_p2",["ref:set/F08_v2_ambar_bajo.png"],*LUZ2,"2–3 lámparas; sigue el maletín bajo el asiento, lado pasillo; dedos")
step("V02","b0_p2","nbp","frame:b0_p2",[],"the oat sweater cuff covers her knuckles.",
     "The oat knit sweater cuff extends past her wrist out of the charcoal coat sleeve and covers her knuckles up to the first finger joints; only her fingertips show on top of the briefcase. Real knit texture; the hand is separate from the cuff; five separate fingers.",
     "Decisión de Cristian: manga gris + puño avena sobre los nudillos · dedos sin artefacto", depends=["V01"])
step("V03","b3_p1","nbp","frame:b0_p2",[],"the same floor-level shot without her hand, sleeve and boot; the briefcase has sprung open by itself.",
     "Her hand, sleeve and boot are gone; nobody is in the aisle. The briefcase stays EXACTLY where it is: half under the sleeping man's window seat, on its AISLE side, its back edge on the seat's metal rail, NOT out in the aisle. Both latches have just sprung open and the lid is lifted a finger's width; a thin thread of white mist seeps from the gap. His dark shoes behind it stay still: he is seated.",
     "Extra 1: maletín BAJO el asiento, lado pasillo, no en el pasillo · mismo encuadre que b0_p2 · nadie de pie", depends=["V02"])
step("V04","b3_p2","flare","frame:b3_p1",["ref:personajes/HOJA_extra_pareja_camisa_azul.png","ref:props/PROP_maletin_v2.png","ref:set/F08_v2_ambar_bajo.png"],None,None,
     "Extra 1: hombre SENTADO y dormido, nunca de pie · maletín bajo su asiento lado pasillo · niebla entre los zapatos · borde superior en las rodillas", cost=0.08, depends=["V03"],
     prompt=("FILM STILL, vertical 9:16. Image 1 is the previous shot (b3_p1): same carriage, same briefcase under the same seat, same low amber light. Image 2 is the blue-shirt man (identity and wardrobe only). Image 3 is the briefcase. Image 4 is carriage 2's LOW amber light (only two or three reading lamps lit). "
             "MOMENT: low shot at shin height, a little further back than Image 1. The blue-shirt man is SEATED in his window seat and ASLEEP: we only see his lower legs from the knees down, knees bent, both dark shoes flat on the floor in front of his seat, trouser hems; the TOP edge of the frame is at his knees. Nobody is standing. "
             "The briefcase is under his seat on the AISLE side exactly as in Image 1, lid open a finger's width; a thin, low white mist creeps out of the gap across the floor and rises between his shoes around his ankles and shins, not dense. "
             "CAMERA: at shin height, 35mm, f/2.8, ready to tilt up to the knees. LIGHT: one amber cone catches the mist and the metal corner; the rest falls to black. "
             "Shot on 35mm film, Kodak Vision3 500T grain, practical light only, blacks fall to black, no HDR, no glow halos. No text, no captions, no watermark."))
step("V05","b0_p3","nbp","frame:b0_p3",["ref:set/F08_v2_ambar_bajo.png"],*LUZ2,"2–3 lámparas; el hombre y la esposa siguen dormidos")
step("V06","b0_p3","nbp","frame:b0_p3",[],"Martina looks at the sleeping man.",
     "Martina, standing at the right edge with her hand on the seatback, has her head and eyes turned DOWN-LEFT toward the blue-shirt man who stirs in the window seat at frame left: her eyeline lands on his face, frozen, breath held. She does not look off frame or at the camera.",
     "Extra 3: mira al hombre que se remueve (eje hacia la izquierda), no fuera de cuadro", depends=["V05"])
step("V07","b0_p4","nbp","frame:b0_p4",["ref:set/F08_v2_ambar_bajo.png"],*LUZ2,"2–3 lámparas; la lectora sigue bajo SU lámpara encendida, misma cara")
step("V08","b3_p3","nbp","frame:b3_p3",["ref:set/F08_v2_ambar_bajo.png"],*LUZ2,"2–3 lámparas; él izq. tosiendo, mano derecha al cuello, esposa der.")
step("V09","b3_p5","nbp","frame:b3_p5",["ref:set/F08_v2_ambar_bajo.png"],*LUZ2,"2–3 lámparas · VIGILAR brazos fundidos (si siguen, marcar)")
step("V10","b3_p6","nbp","frame:b3_p6",["ref:set/F08_v2_ambar_bajo.png"],*LUZ2,"2–3 lámparas; la lámpara de la lectora encendida")
step("V11","b3_p6","nbp","frame:b3_p6",[],"the couple in the foreground left becomes a dark struggling tangle.",
     "Foreground left: the calm seated couple becomes a dark struggling tangle in shadow, the man lunging onto his wife, shapes only, motion blur, nothing graphic. They are not looking at the camera.",
     "Forcejeo en primer término izq., sin nada gráfico", depends=["V10"])
step("V12","b3_p6","nbp","frame:b3_p6",["file:v1c/refs/lectora_b0_p4.png"],"the screaming woman is the same reader as Image 2.",
     "The woman springing up and screaming at frame right is the same young woman as Image 2: same face, dark hair tied up in a bun, rust-red knitted scarf, dark top; no beige cardigan, no loose curly hair. Same pose, book falling, mouth open screaming.",
     "Lectora = la de b0_p4 (cara, moño, bufanda) · no se parece a la esposa", depends=["V11"])
step("V13","b3_p4","nbp","frame:b3_p4",[],"the moment just before the change: normal eyes and clean neck.",
     "His eyes are normal human eyes with dark irises, half-closed, and his neck and jaw skin is clean, with no veins and no marks: the instant just before the change. Same head angle turning toward frame right.",
     "Estado inicial de c03b; el final lo da ESTADO_hombre_azul_infectado como referencia")
step("V14","b0_p1","nbp","frame:b0_p1",[],"reframe tighter, to an extreme close-up of her eyes.",
     "Push in to an extreme close-up framed from just above her eyebrows to her upper lip: both eyes and the bridge of the nose fill the frame, her eyes darting toward frame left. Same lamp beam across her eyes, same shadow.",
     "PPP ceja–labio superior · mirada a la izq. · si NBP no lo logra, se acepta y se pide push-in en c00a")
step("V15","b1_f2","nbp","frame:b1_f2",[],"the two background masks are completely smooth and featureless.",
     "The two masked figures standing in the background wear completely smooth, featureless grey masks: no eyes, no eye holes, no nose, no mouth, no lines.",
     "Máscaras lisas · cinta y muñecas visibles, el maletín no las tapa")

# ---------------- Vagón 5 (bloques 2 y 4) ----------------
step("V16","b2_p2","nbp","frame:b2_p2",[],"the red mark on her right wrist is clearly visible before the sleeve covers it.",
     "Her sleeve has ridden up: across the inside of her RIGHT wrist, between the pushed-up oat cuff and her hand, a thin raw red line is clearly visible, like the mark a tight binding leaves (not a bracelet, not a thread, no jewellery). Her LEFT fingertips have just pinched the edge of the cuff to pull it down, but the mark is still fully uncovered.",
     "Extra 2: la marca roja se lee ANTES de que los dedos bajen la manga · es lo único que cuenta el plano")
step("V17","b2_p3","flare","frame:b2_p1",["ref:personajes/HOJA_tomas.png","ref:personajes/HOJA_martina.png","ref:set/F09_ambar_asiento_pareja.png"],None,None,
     "Extra 7 + 6: Tomás a la DERECHA mirando a la izquierda · hombro avena desenfocado en el borde izq. · detrás: pasillo y asientos del otro lado, SIN ventana · pelo de la hoja", cost=0.08,
     prompt=("FILM STILL, vertical 9:16. Image 1 is the two-shot of this scene (same carriage 5, same amber light, same wardrobe). Image 2 is Tomás: face, short neatly combed dark hair with a side parting, thin full metal-frame glasses, navy quilted jacket over a grey sweater (identity, hair and wardrobe only). Image 3 is Martina's oat knit sweater and charcoal coat (wardrobe only). Image 4 is carriage 5 and its amber light. "
             "MOMENT: close-up of Tomás from mid-chest up, positioned at frame RIGHT, turned and looking toward frame LEFT at Martina, who sits beside him at the window. A soft half smile: he has decided not to insist; lips parting on the first word of a gentle, sincere question. "
             "At the LEFT edge of frame, very close to camera and out of focus, Martina's shoulder in the oat knit sweater under the charcoal coat. Behind Tomás: the aisle and the seats on the other side of the carriage, with dozing passengers soft and dark. NO window anywhere behind him: the window is on Martina's side, out of frame left. "
             "His hair is exactly as Image 2: short, side-parted, tidy, no curls, no fringe. CAMERA: handheld, at seated eye height, 50mm, f/2, focus on his eyes behind the glasses. "
             "LIGHT: carriage 5 at night in warm amber from the reading lamps (~3000K), practical light only, deeper shade between lamps; a warm lamp catches the rim of his metal frames. "
             "Shot on 35mm film, Kodak Vision3 500T grain, blacks fall to black, real skin texture, no HDR, no glow halos. No text, no captions, no watermark."))
step("V18","b2_p4","nbp","frame:b2_p4",[],"remove Tomás's hand; her hands rest alone.",
     "Tomás's hand and navy cuff are gone from the bottom right; her LEFT hand rests alone on the armrest. She still stares straight ahead, never at him.",
     "Estado inicial de P4: la mano de Tomás entra después · ventana a su lado (izq.) ✓")
step("V19","b2_p1","nbp","frame:b2_p1",["ref:personajes/HOJA_tomas.png"],*TOMAS,"Extra 6: pelo corto con partidura · Tomás der. mira a la izq. · ventana del lado de Martina ✓")
step("V20","b4_p1","nbp","frame:b4_p1",[],"Iván is still seated and Carmen is still asleep.",
     "Iván, mid-carriage, is still sitting in his seat, only lifting his head toward the front door; Carmen, nearer camera, is still asleep, head down, glasses on the cord against her chest, bag on her LEFT shoulder. The passenger near the front door already stands staring at it.",
     "Estado inicial de c04a (la ola aún no llega a Iván y Carmen) · bolso hombro izq.")
step("V21","b4_p6","nbp","frame:b4_p6",[],"through the burst front door only a dark red gangway.",
     "Through the burst-open front door at the far end, behind the incoming infected silhouettes, there is only a dark gangway lit faint red: no blue light, no sky, no rain, no exterior.",
     "Fuelle rojo detrás de las siluetas · VIGILAR brazo de Martina saliendo de la chaqueta de Tomás")
step("V22","b4_p6","nbp","frame:b4_p6",["ref:personajes/HOJA_tomas.png"],*TOMAS,"Extra 6 · manos naturales (Tomás der. toma la izq. de Martina)", depends=["V21"])

# ---------------- Fuelle y último vagón (bloques 5, 6 y 7) ----------------
step("V23","b5_p1","nbp","frame:b5_p1",[],*LUZR,"Solo luz (encuadre ya pasa) · llave trabada, dos manos, dedos separados")
step("V24","b5_p2","nbp","frame:b5_p2",[],*LUZR,"Solo luz · Carmen última de espaldas a la puerta del vagón 5")
step("V25","b5_p4","nbp","frame:b5_p4",[],"the smear on her palm and on the glass is reddish black, not bright red.",
     "The smear on Carmen's RIGHT palm and on the broken glass under it is a dark reddish black, almost black, matte, not bright red, not glossy; one thin cut, no exposed flesh.",
     "Extra 5 · palma DERECHA")
step("V26","b5_p5","nbp","frame:b5_p5",[],"the smear on her palm and on the glass is reddish black, not bright red.",
     "The smear on Carmen's RIGHT palm and on the glass edge is a dark reddish black, almost black, matte, not bright red, not glossy; one thin clean cut; no exposed flesh.",
     "Extra 5 · mano derecha (corregida en parte A)")
step("V27","b5_p6","nbp","frame:b5_p6",["ref:props/PROP_llave_y_cerradura.png"],"the key is in the keyhole, mid-turn, held by Hugo's right hand.",
     "The antique key from Image 2 is in the keyhole of the bronze plate, mid-turn, held between the thumb and fingers of Hugo's RIGHT hand; his left shoulder presses the door, which is still closed. No key in any pocket. Fingers clearly separate from the key.",
     "Decisión llave: gira por fuera en P6 y se queda con ella en la mano (estado inicial: a mitad de giro)")
step("V28","b5_p6","nbp","frame:b5_p6",[],*LUZR,"Solo luz", depends=["V27"])
step("V29","b5_p8","nbp","frame:b5_p8",[],"make the door window dry and dark.",
     "The small wired-glass window of the door is dry and dark: no water drops at all, only a dark red gangway behind the mesh.", "Sin gotas en la ventanita (regla dura §5)")
step("V30","b5_p8","nbp","frame:b5_p8",[],"reframe to a tight shot at lock height.",
     "Tighter framing at the height of the lock: Hugo's shoulder and back pressing the door closed, the door edge crushing a grey infected hand jammed in the gap on the lock side, and his RIGHT hand turning the antique key in the keyhole from inside (the clac). The bronze plate, keyhole and key read clearly and large in frame.",
     "Decisión llave: plano cerrado a la altura de la cerradura; aplasta la mano y gira la llave por dentro", depends=["V29"])
step("V31","b5_p9","nbp","frame:b5_p9",[],"remove every water droplet from the door window.",
     "Every water droplet and rain streak on the small door window is gone; the glass is dry. Keep the infected face, the dark smear and the wire mesh.", "Sin gotas")
step("V32","b5_p7","nbp","frame:b5_p7",["ref:personajes/HOJA_tomas.png"],*TOMAS,"Extra 6")
step("V33","b6_p1","nbp","frame:b6_p1",[],"Iván stands with his back pressed against the door.",
     "Iván stands with his BACK pressed against the door, facing camera, arms braced against the door frame, head turned slightly; the small window full of palms and dark smears stays above his shoulder.",
     "Iván de espaldas a la puerta mirando a cámara · Hugo sin llave en la mano")
step("V34","b6_p2","flare","frame:b6_p2",["ref:personajes/HOJA_carmen.png","ref:personajes/ESTADO_carmen_palma_v2_palma.png","ref:set/F05_rojo_tres_cuartos_hacia_puerta.png"],None,None,
     "Extra 4 + 5: mira su palma cerca del pecho, la cierra en un puño y la mete en el abrigo · no la muestra a cámara · mancha negra rojiza · luz roja de arriba, media cara en sombra", cost=0.08,
     prompt=("FILM STILL, vertical 9:16. Image 1 is this shot as it is now (same Carmen, same last carriage, same red light). Image 2 is Carmen (face, grey roots, nurse uniform under a brown coat, bag on her LEFT shoulder, glasses on a cord; identity and wardrobe only). Image 3 is the state of her RIGHT palm (one thin cut and a dark reddish-black smear). Image 4 is the last carriage in red light. "
             "MOMENT: close-up of Carmen, chest up, locked off. Her chin is down: she looks at her own RIGHT palm, which she holds close to her chest, palm turned toward HER face, not toward the camera; we only glimpse the edge of the dark reddish-black smear (almost black, matte, not bright red). Her fingers are curling into a fist and the fist is already slipping inside the opening of her brown coat. Her eyes stay on the hand. "
             "CAMERA: locked off, 50mm, f/2. LIGHT: the narrow red ceiling strip (#B3001B) from above is the only light: half her face in shadow, real black zones, no white fill on her skin. Glasses on the cord, bag on her left shoulder. "
             "Shot on 35mm film, Kodak Vision3 500T grain, blacks fall to black, real skin texture, no HDR. No text, no captions, no watermark."))
step("V35","b6_p3","nbp","frame:b6_p3",["ref:set/F02_rojo_ultimo_vagon_hacia_fondo_cabina.png"],*PARED,"Geografía: pared trasera, sin segunda puerta · Tomás izq. mira der., Martina der. mira el piso")
step("V36","b7_p1","nbp","frame:b7_p1",[],"the door window shows only a dark gangway, with the dark smears on the glass.",
     f"{VENTANITA_R} On the wired glass, the same dark reddish-black smears and handprints left in the previous scene. The door stays closed.",
     "Manchas en el vidrio · fuelle oscuro, sin cara aún")
step("V37","b7_p2","nbp","frame:b7_p2",[],"wider framing: the door window fills about 60% of the frame width.",
     "Pull the camera back: the small wired-glass door window now fills about 60% of the frame width, with the riveted metal door around it visible on all sides, so there is room for a slow push-in. Diego's face stays behind the glass in the same place within the window.",
     "Reencuadre para el avance lento · VIGILAR dedos de Diego")
step("V38","b7_p2","nbp","frame:b7_p2",[],"the gangway behind Diego falls almost to black and half his face is in shadow.",
     "Behind Diego the gangway falls almost to black with only a faint red cast; the cold white tube above the door, on our side, is the only light on the glass and lights his face from above, half of it in shadow. No lit corridor, no doors behind him.",
     "Fondo casi negro, media cara en sombra (midjourney)", depends=["V37"])
step("V39","b7_p2","nbp","frame:b7_p2",["ref:personajes/ESTADO_diego_mojado_herido_v3.png"],"only Diego's right sleeve is stained, and the prints on the glass are dark.",
     "Diego's pale stone canvas jacket is soaked and clean except the RIGHT sleeve (frame LEFT), which is torn and stained dark reddish black, as in Image 2; no stains on the chest, the left sleeve or the hood. The handprints on the glass become dark, almost black, matte, not bright red.",
     "Extra 5: solo manga derecha, manos del vidrio oscuras", depends=["V38"])
step("V40","b7_p5","nbp","frame:b7_p5",[],"the gangway behind Diego falls almost to black and half his face is in shadow.",
     "Behind Diego the gangway falls almost to black with only a faint red cast; the cold white tube above the door, on our side, is the only light on the glass and lights his face from above, half of it in shadow.",
     "Fondo casi negro · golpea con la palma IZQUIERDA")
step("V41","b7_p5","nbp","frame:b7_p5",["ref:personajes/ESTADO_diego_mojado_herido_v3.png"],"only Diego's right sleeve is stained, and the prints on the glass are dark.",
     "Diego's pale stone canvas jacket is soaked and clean except the RIGHT sleeve, which is torn and stained dark reddish black, as in Image 2; no stains on the chest or the left sleeve. The handprints on the glass become dark, almost black, matte, not bright red.",
     "Extra 5", depends=["V40"])
step("V42","b7_p3","nbp","frame:b7_p3",["ref:set/F02_rojo_ultimo_vagon_hacia_fondo_cabina.png"],*PARED,"Geografía · Martina der. enfocada, Iván borde izq.")
step("V43","b7_p3","nbp","frame:b7_p3",[],*LUZR,"Luz roja sin relleno blanco", depends=["V42"])
step("V44","b7_p4","nbp","frame:b7_p4",["ref:set/F02_rojo_ultimo_vagon_hacia_fondo_cabina.png"],*PARED,"Geografía · Tomás izq. mira der.")
step("V45","b7_p4","nbp","frame:b7_p4",["ref:personajes/HOJA_tomas.png"],*TOMAS,"Extra 6", depends=["V44"])
step("V46","b7_p6","nbp","frame:b7_p6",["ref:set/F02_rojo_ultimo_vagon_hacia_fondo_cabina.png"],*PARED,"Geografía · mano de Hugo en la manija, sin llave, abajo a la der.")
step("V47","b7_p6","nbp","frame:b7_p6",[],*LUZR,"Sin relleno blanco en la cara de Martina", depends=["V46"])

lote = {"lote": "previs_v1c", "fecha": "2026-10-18", "tope_trabajo_usd": 12.0, "tope_v3_usd": 40.0, "gastado_antes_usd": 5.56,
        "regla": "una variable por paso; revisar cada salida contra «Estado del mundo» y §5; máximo un reintento por paso; si falla dos veces, se marca y se sigue",
        "pasos": S, "costo_est_total_usd": round(sum(s["costo_est_usd"] for s in S), 2)}
(HERE / "lote_v1c.json").write_text(json.dumps(lote, ensure_ascii=False, indent=1) + "\n")
print(len(S), "pasos;", lote["costo_est_total_usd"], "USD estimados sin reintentos")
