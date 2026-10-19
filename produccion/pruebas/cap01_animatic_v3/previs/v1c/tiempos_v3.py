#!/usr/bin/env python3
"""Genera ../../tiempos_montaje_v3.json: tiempos por plano para la previs v1c y el video v3.

Regla (revision_v1.md §5, Cristian 18-oct 22:45): se recorta solo el plano que dura más que su
acción + 0,5 s; nunca dentro de una línea; la duración final es la que resulte (sin relleno).
Voz: fin de línea medido con silencedetect −35 dB sobre las pistas (tiempo de llamada, con colchón 0,5 s).
"""
import json, pathlib
V3 = pathlib.Path(__file__).resolve().parents[2]
PAD = 0.5
# id, llamada, plano, dur v10 (previs v1), dur v1c, acción estimada (s), motivo
S = [
 ("b0_p1","c00a","0·P1",1.2,1.2,1.0,"ojos de un extremo al otro y vuelven"),
 ("b0_p2","c00a","0·P2",1.8,1.8,1.5,"empuja, se traba, termina con la bota"),
 ("b0_p3","c00b","0·P3",1.5,1.5,1.0,"él se remueve y ronca; ella se congela"),
 ("b0_p4","c00b","0·P4",1.5,1.5,1.0,"se aleja; el secreto queda quieto"),
 ("b1_p1","c01","1·P1",0.8,0.8,0.6,"se apoya, cierra los ojos, aprieta"),
 ("b1_f1","c01f","1·F1",0.7,0.7,0.5,"tira de la cinta"),
 ("b1_f2","c01f","1·F2",0.7,0.7,0.5,"le dejan el maletín"),
 ("b1_f3","F3","1·F3",0.8,0.8,0.8,"pantalla, lectura de «VAGÓN 2» (post)"),
 ("b1_p2","c01","1·P2",1.0,1.0,0.8,"abre los ojos, manga, empuja la puerta"),
 ("b2_p1","c02","2·P1",3.5,3.2,2.7,"«En el baño.» termina a 3,20 s de llamada = 2,70 s del plano → máx. 3,2"),
 ("b2_p2","c02","2·P2",1.0,1.0,0.8,"la marca se ve y la manga la tapa"),
 ("b2_p3","c02","2·P3",3.0,2.7,2.17,"«¿Tu papá sabe…?» entra 0,2 s y termina 2,17 s después del corte → máx. 2,67"),
 ("b2_p4","c02","2·P4",4.0,4.0,3.5,"«No… Esa era la idea.» termina 2,95 s; mano de Tomás ~0,6 s; corte 0,5 s después (guion)"),
 ("b3_p1","c03a","3·P1",1.3,1.3,0.8,"clic-clic y la tapa se levanta"),
 ("b3_p2","c03a","3·P2",1.5,1.5,1.2,"la niebla sube de los zapatos a las rodillas"),
 ("b3_p3","c03a","3·P3",2.2,2.2,1.7,"despierta tosiendo, mira abajo, mano al cuello"),
 ("b3_p4","c03b","3·P4",1.5,1.5,1.2,"ojos blancos, venas, deja de toser, gira"),
 ("b3_p5","c03b","3·P5",1.0,1.0,0.6,"se lanza; corte en el impacto"),
 ("b3_p6","c03b","3·P6",1.5,1.5,1.0,"la lectora se levanta y grita; ola"),
 ("b4_p1","c04a","4·P1",1.8,1.8,1.3,"ola de cabezas: pasajero → Iván → Carmen"),
 ("b4_p2","c04a","4·P2",1.5,1.5,1.0,"le agarra el brazo; él gira"),
 ("b4_p3","c04a","4·P3",1.2,1.2,1.2,"chasquido, 0,5 s de negro (post), rojo"),
 ("b4_p4","c04b","4·P4",1.5,1.5,1.0,"siluetas se estrellan; la puerta se sacude"),
 ("b4_p5","c04b","4·P5",2.5,3.0,2.56,"pitazo 0,1 s; «¡Al último vagón! ¡Rápido!» termina 2,56 s del plano → v10: 3,0 s (antes 2,5 cortaba dentro de «¡Rápido!»)"),
 ("b4_p6","c04b","4·P6",2.5,2.0,1.5,"estampida; v10: 2,0 s"),
 ("b5_p1","c05a","5·P1",1.3,1.3,1.0,"mete la llave, se traba, la fuerza"),
 ("b5_p2","c05a","5·P2",1.5,1.5,1.2,"Iván cierra y empuja; infectados en el vidrio"),
 ("b5_p3","c05a","5·P3",1.0,1.0,0.6,"el vidrio revienta y la agarra"),
 ("b5_p4","c05b","5·P4",1.5,1.5,1.0,"choca, apoya la palma, Iván la arranca"),
 ("b5_p5","c05i","5·P5",1.0,1.0,0.6,"inserto de la palma"),
 ("b5_p6","c05b","5·P6",1.5,1.5,1.2,"la llave gira, clac; la saca; hombro"),
 ("b5_p7","c05b","5·P7",1.2,1.2,1.0,"entran en tropel"),
 ("b5_p8","c06a","5·P8",1.3,1.3,1.0,"cierra con el cuerpo, aplasta la mano, gira la llave"),
 ("b5_p9","c06a","5·P9",1.0,1.0,0.5,"la cara se estrella"),
 ("b6_p1","c06a","6·P1",2.0,2.0,2.0,"golpes, retroceden, grito lejano, paran: silencio escrito"),
 ("b6_p2","c06b","6·P2",1.5,1.5,1.2,"se mira la palma, puño, la esconde, mira"),
 ("b6_p3","c06b","6·P3",2.0,2.0,1.5,"Tomás gira y la mira; ella mira el piso (silencio del bloque)"),
 ("b7_p1","c07a","7·P1",0.8,0.8,0.6,"tres golpes; levantan la cabeza"),
 ("b7_p2","c07a","7·P2",3.6,3.6,3.25,"«¡Martina, ábreme!» termina 2,65 s; mira atrás ~0,6 s → máx. 3,75"),
 ("b7_p3","c07a","7·P3",2.9,2.7,2.16,"«¡Te vi en el vagón 2!» termina 2,16 s del plano → máx. 2,66"),
 ("b7_p4","c07b","7·P4",2.7,2.5,2.02,"«¿No estabas en el baño?» termina 2,02 s del plano → máx. 2,52"),
 ("b7_p5","c07b","7·P5",1.2,1.2,0.8,"golpea y mira atrás"),
 ("b7_p6","c07b","7·P6",2.6,2.0,2.0,"Cristian: ~2 s, mira a Tomás y luego a la manija; corte justo al llegar a la manija, sin el segundo extra"),
]
TRACKS = {
 "c02":  {"pista": "pistas/c02_v2.mp3", "wav": "pistas/c02_v2.wav", "origen": "pistas/c02.wav",
          "edicion": "se quitan 0,30 s de silencio en 3,55–3,85 s y 0,30 s en 7,50–7,80 s (tiempo de llamada); ninguna línea se toca",
          "lineas_entran_s": {"Tomás 1C": 0.8, "Martina 2B": 2.5, "Tomás 3C": 4.9, "Martina 4D": 7.6}},
 "c04b": {"pista": "pistas/c04b.mp3", "edicion": "sin cambios", "lineas_entran_s": {"Hugo A": 2.63}, "pitazo_post_s": 2.1},
 "c07a": {"pista": "pistas/c07a_v2.mp3", "wav": "pistas/c07a_v2.wav", "origen": "pistas/c07a.wav",
          "edicion": "cola recortada de 8,3 a 8,1 s (silencio)", "lineas_entran_s": {"Diego 5C": 1.5, "Diego 6C": 5.0}},
 "c07b": {"pista": "pistas/c07b_v2.mp3", "wav": "pistas/c07b_v2.wav", "origen": "pistas/c07b.wav",
          "edicion": "cola recortada de 7,5 a 6,7 s (silencio)", "lineas_entran_s": {"Tomás 7B": 0.7}},
}
PEDIDA_PLAN = {"c01": 3.5, "c01f": 2.5}
RES = {c: ("768P" if c in TRACKS else "480P") for c in ["c00a","c00b","c01","c01f","c02","c03a","c03b","c04a","c04b","c05a","c05b","c05i","c06a","c06b","c07a","c07b"]}
t = 0.0; shots = []; calls = {}
for sid, call, pl, d0, d, acc, why in S:
    assert d <= acc + 0.5 + 0.05, (sid, d, acc)  # 0,05 s = redondeo a 0,1 s
    shots.append({"id": sid, "llamada": call, "plano": pl, "entra_montaje_s": round(t, 2), "dur_s": d,
                  "dur_previs_v1_s": d0, "accion_s": acc, "cambio": round(d - d0, 2), "motivo": why})
    if call != "F3":
        c = calls.setdefault(call, {"llamada": call, "planos": [], "montaje_s": 0.0})
        c["planos"].append(sid); c["montaje_s"] = round(c["montaje_s"] + d, 2)
    t += d
for c in calls.values():
    c["pedida_s"] = round(c["montaje_s"] + 2 * PAD, 2)
    if c["llamada"] in PEDIDA_PLAN:  # plan.md: c01 es una acción continua (el montaje usa inicio y final); c01f igual que el plan
        c["pedida_s"] = PEDIDA_PLAN[c["llamada"]]; c["nota"] = "duración pedida según plan.md, no montaje + colchón"
    c["resolucion"] = RES[c["llamada"]]
    if c["llamada"] in TRACKS: c["audio1"] = TRACKS[c["llamada"]]
    # cortes internos en tiempo de llamada (con colchón)
    x = PAD; cuts = []
    for sid in c["planos"]:
        dd = next(s["dur_s"] for s in shots if s["id"] == sid); cuts.append({"id": sid, "de_s": round(x, 2), "a_s": round(x + dd, 2)}); x += dd
    c["planos_en_llamada"] = cuts
out = {"version": "v1c / video v3", "fecha": "2026-10-18", "guion": "guion/cap01/cap01_v10.md (main 3af1c19)",
       "regla": "revision_v1.md §5: ningún plano dura más que su acción + 0,5 s; nunca se recorta dentro de una línea; sin relleno. Mismos tiempos en el video.",
       "colchon_llamada_s": PAD, "total_montaje_s": round(t, 2),
       "nota_c05": "c05b = P4, P6, P7; el inserto c05i (P5) va entre P4 y P6 en el montaje.",
       "nota_post": "b4_p3: 0,5 s de negro en post al inicio del plano; H3 parte ya en rojo. Encuesta «Si fueras Martina, ¿lo dejas entrar?» va después, en post, sobre negro.",
       "planos": shots, "llamadas": list(calls.values())}
(V3 / "tiempos_montaje_v3.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
print("total", round(t, 2), "s;", len(shots), "planos")
for c in calls.values(): print(c["llamada"], c["resolucion"], c["montaje_s"], c["pedida_s"])
