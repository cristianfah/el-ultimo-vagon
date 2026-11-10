# -*- coding: utf-8 -*-
"""build_set.py - blockout gris del tren para el previz (headless).

  blender -b -P build_set.py -- --out <dir>/tren_blockout.blend [--info <dir>/set_info.json] [--filas 20]

Construye, en bloques grises mate y sin textos:
  SET_ultimo_vagon  (6 filas 2+2, UNA sola puerta adelante, ventana trasera, cabina del revisor atras a la derecha)
  SET_fuelle        (pasillo corto y estrecho sin ventanas entre el ultimo vagon y el vagon 5)
  SET_vagon5        (modulo de pasajeros)
  SET_vagon2        (el mismo modulo, tres vagones mas adelante)
  PROPS             (maletin, llave) y ANCLAS (vacios con nombre para ubicar planos desde las fichas JSON)

Ejes: +Y hacia la cabeza del tren, +X derecha mirando hacia adelante, +Z arriba. Origen del mundo: piso del fuelle,
al centro, en la cara exterior de la pared del ultimo vagon (ANC_fuelle).
"""
import argparse
import json
import math
import os
import sys

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import previz_lib as L  # noqa: E402

# Medidas de partida (metros). No copian un tren real; se ajustan aqui y se reconstruye.
DEF = {
    "ancho": 2.80, "alto": 2.30, "pasillo": 0.60, "paso_fila": 0.90, "pared": 0.08,
    "puerta_w": 0.80, "puerta_h": 2.00, "hoja_esp": 0.05,
    "vent_w": 0.42, "vent_h": 0.55, "vent_z": 1.50,            # ventanita: ancho, alto, altura del centro (cara)
    "asiento_z": L.ALTURA_ASIENTO, "cojin_esp": 0.10, "cojin_fondo": 0.48, "cojin_ancho": 0.52,
    "respaldo_z": 1.15, "respaldo_esp": 0.10, "asiento_atras": 0.10,   # el asiento va 10 cm atras del centro de la fila
    "rack_z": 1.90, "rack_fondo": 0.42,
    "ventana_largo": 0.62, "ventana_z0": 0.85, "ventana_z1": 1.60,
    "margen_del": 1.00, "margen_tras": 1.00,                   # vestibulos del modulo de pasajeros
    "ultimo_filas": 6, "ultimo_margen_del": 1.20, "ultimo_margen_tras": 0.60,
    "fuelle_largo": 3.00, "fuelle_ancho": 1.25, "fuelle_alto": 2.10,
    "cerradura_x": 0.32, "bocallave_z": 1.10, "manija_z": 0.95,  # placa: bocallave arriba, manija abajo
    "riel_alto": 0.025,
}


def construir_puerta(nombre, col, anclas, bisagra_x, lado_libre, y_c, P, signo, con_cerradura=False):
    """Hoja de puerta con ventanita. Origen del objeto en la bisagra (gira en Z). lado_libre = +1 / -1 (hacia +X / -X)."""
    w, h, e = P["puerta_w"], P["puerta_h"], P["hoja_esp"]
    x_a, x_b = bisagra_x, bisagra_x + lado_libre * w
    xc = (x_a + x_b) / 2.0
    vw, vh, vz = P["vent_w"], P["vent_h"], P["vent_z"]
    y0, y1 = y_c - e / 2, y_c + e / 2
    m = L.Malla()
    m.caja(x_a, x_b, y0, y1, 0.0, vz - vh / 2)                    # panel bajo
    m.caja(x_a, x_b, y0, y1, vz + vh / 2, h)                      # panel alto
    m.caja(min(x_a, x_b), xc - vw / 2, y0, y1, vz - vh / 2, vz + vh / 2)
    m.caja(xc + vw / 2, max(x_a, x_b), y0, y1, vz - vh / 2, vz + vh / 2)
    hoja = m.objeto("PUERTA_" + nombre, col, "SET_puerta", origen=(bisagra_x, y_c, 0.0))
    hoja["bisagra_x"] = bisagra_x
    hoja["signo"] = signo            # rotation_z = signo * radianes(open_deg) abre la puerta
    hoja["es_puerta"] = True
    vid = L.Malla().caja(xc - vw / 2, xc + vw / 2, y_c - 0.005, y_c + 0.005, vz - vh / 2, vz + vh / 2) \
        .objeto("VIDRIO_" + nombre, col, "SET_vidrio")
    vid["ancho"], vid["alto"] = vw, vh
    L.emparentar(vid, hoja)
    cx = bisagra_x + lado_libre * (w - (0.40 - P["cerradura_x"]))   # a 8 cm del canto libre
    for cara, ys in (("ext", +1), ("int", -1)):
        # "ext"/"int" solo tienen sentido en la puerta del ultimo vagon: ext = lado del fuelle (+Y), int = dentro
        yf = y_c + ys * e / 2
        if con_cerradura:
            pl = L.Malla().caja(cx - 0.035, cx + 0.035, yf, yf + ys * 0.012, P["manija_z"] - 0.07, P["bocallave_z"] + 0.07) \
                .objeto("CERRADURA_%s_%s_placa" % (nombre, cara), col, "PROP_placa")
            bo = L.Malla().caja(cx - 0.008, cx + 0.008, yf + ys * 0.012, yf + ys * 0.014,
                                P["bocallave_z"] - 0.022, P["bocallave_z"] + 0.012) \
                .objeto("CERRADURA_%s_%s_bocallave" % (nombre, cara), col, "PROP_negro")
            L.emparentar(pl, hoja)
            L.emparentar(bo, hoja)
            a1 = L.vacio("ANC_bocallave_%s" % cara, anclas, (cx, yf + ys * 0.014, P["bocallave_z"]), 0.05)
            a2 = L.vacio("ANC_manija_%s" % cara, anclas, (cx - lado_libre * 0.07, yf + ys * 0.05, P["manija_z"]), 0.05)
            L.emparentar(a1, hoja)
            L.emparentar(a2, hoja)
        # manija: palanca horizontal que apunta hacia el centro de la hoja
        mm = L.Malla()
        mm.caja(cx - 0.012, cx + 0.012, yf, yf + ys * 0.05, P["manija_z"] - 0.012, P["manija_z"] + 0.012)
        mm.caja(cx, cx - lado_libre * 0.13, yf + ys * 0.035, yf + ys * 0.055, P["manija_z"] - 0.011, P["manija_z"] + 0.011)
        ma = mm.objeto("MANIJA_%s_%s" % (nombre, cara), col, "PROP_hierro")
        L.emparentar(ma, hoja)
    return hoja


def pared_extremo(m, y0, y1, P, con_puerta=True, ventana=None):
    """Pared de extremo del vagon entre y0 e y1. con_puerta deja el vano. ventana=(ancho, z0, z1) deja un hueco centrado."""
    W2 = P["ancho"] / 2 + P["pared"]
    H = P["alto"]
    if con_puerta:
        pw, ph = P["puerta_w"] / 2, P["puerta_h"]
        m.caja(-W2, -pw, y0, y1, 0, H)
        m.caja(pw, W2, y0, y1, 0, H)
        m.caja(-pw, pw, y0, y1, ph, H)
    elif ventana:
        vw, z0, z1 = ventana
        m.caja(-W2, -vw / 2, y0, y1, 0, H)
        m.caja(vw / 2, W2, y0, y1, 0, H)
        m.caja(-vw / 2, vw / 2, y0, y1, 0, z0)
        m.caja(-vw / 2, vw / 2, y0, y1, z1, H)
    else:
        m.caja(-W2, W2, y0, y1, 0, H)


def construir_vagon(nombre, y0, filas, P, anclas, tipo="pasajeros", lamparas_on=()):
    """Modulo parametrico de vagon. y0 = Y de mundo de la cara interior de la pared trasera.
    Filas numeradas desde la puerta delantera (fila 1 = la mas cercana a la puerta). Todos los asientos miran a +Y."""
    col = L.coleccion("SET_" + nombre, L.coleccion("SET"))
    ultimo = tipo == "ultimo"
    mt = P["ultimo_margen_tras"] if ultimo else P["margen_tras"]
    md = P["ultimo_margen_del"] if ultimo else P["margen_del"]
    largo = mt + filas * P["paso_fila"] + md
    W, H, p = P["ancho"], P["alto"], P["pared"]
    W2 = W / 2
    Y = lambda y: y0 + y   # noqa: E731  local -> mundo

    casco, piso, asientos, detalle, noche, tira, lamp_on, cabina = (L.Malla() for _ in range(8))
    piso.caja(-W2 - p, W2 + p, Y(-p), Y(largo + p), -0.10, 0.0)
    casco.caja(-W2 - p, W2 + p, Y(-p), Y(largo + p), H, H + p)
    tira.caja(-0.06, 0.06, Y(0.3), Y(largo - 0.3), H - 0.03, H)             # tira de emergencia, centro del cielo

    def y_fila(k):
        return largo - md - P["paso_fila"] * (k - 0.5)

    # paredes laterales con huecos de ventana (uno por fila) y un plano oscuro detras
    vl, z0, z1 = P["ventana_largo"], P["ventana_z0"], P["ventana_z1"]
    for s in (-1, 1):
        xa, xb = s * W2, s * (W2 + p)
        casco.caja(xa, xb, Y(0), Y(largo), 0, z0)
        casco.caja(xa, xb, Y(0), Y(largo), z1, H)
        cortes = sorted((y_fila(k) - vl / 2, y_fila(k) + vl / 2) for k in range(1, filas + 1))
        ya = 0.0
        for (a, b) in cortes:
            casco.caja(xa, xb, Y(ya), Y(a), z0, z1)
            ya = b
        casco.caja(xa, xb, Y(ya), Y(largo), z0, z1)
        noche.caja(s * (W2 + p * 0.6), s * (W2 + p), Y(0), Y(largo), z0, z1)
        # portaequipaje y riel de piso del lado del pasillo
        detalle.caja(s * (W2 - P["rack_fondo"]), s * W2, Y(mt - 0.2), Y(largo - md + 0.2), P["rack_z"], P["rack_z"] + 0.04)
        detalle.caja(s * (P["pasillo"] / 2), s * (P["pasillo"] / 2 + 0.04), Y(mt - 0.1), Y(largo - md + 0.1), 0, P["riel_alto"])

    # paredes de los extremos
    pared_extremo(casco, Y(largo), Y(largo + p), P, con_puerta=True)
    if ultimo:
        pared_extremo(casco, Y(-p), Y(0), P, con_puerta=False, ventana=(0.80, 1.00, 1.60))   # ventana trasera
        noche.caja(-0.40, 0.40, Y(-p), Y(-p * 0.6), 1.00, 1.60)
    else:
        pared_extremo(casco, Y(-p), Y(0), P, con_puerta=True)

    # asientos: pares a cada lado, caja asiento + caja respaldo, pedestal central
    info_filas = {}
    cz, ce, cf, cw = P["asiento_z"], P["cojin_esp"], P["cojin_fondo"], P["cojin_ancho"]
    x_pas = P["pasillo"] / 2
    x_asientos = (x_pas + cw / 2, W2 - 0.02 - cw / 2)        # centro del asiento de pasillo y del de ventana
    cab_fila = filas if ultimo else None                      # la cabina reemplaza el ultimo par del lado derecho
    for k in range(1, filas + 1):
        yc = y_fila(k)
        ys = yc - P["asiento_atras"]
        info_filas[k] = Y(ys)
        L.vacio("ANC_%s_fila_%02d" % (nombre, k), anclas, (0, Y(ys), 0), 0.15)
        for s in (-1, 1):
            if ultimo and k == cab_fila and s == 1:
                continue
            for xc in x_asientos:
                asientos.caja(s * (xc - cw / 2), s * (xc + cw / 2), Y(ys - cf / 2), Y(ys + cf / 2), cz - ce, cz)
                asientos.caja(s * (xc - cw / 2), s * (xc + cw / 2), Y(ys - cf / 2 - 0.08), Y(ys - cf / 2 + 0.02), cz, P["respaldo_z"])
            xm = (x_asientos[0] + x_asientos[1]) / 2
            detalle.caja(s * (xm - 0.04), s * (xm + 0.04), Y(ys - 0.20), Y(ys + 0.10), 0, cz - ce)       # pedestal
            detalle.caja(s * x_pas, s * (x_pas + 0.035), Y(ys - 0.22), Y(ys + 0.20), cz + 0.17, cz + 0.21)  # apoyabrazos
            detalle.caja(s * x_pas, s * (x_pas + 0.035), Y(ys - 0.22), Y(ys - 0.18), cz, cz + 0.17)
            # lampara de lectura bajo el portaequipaje
            lado = "izq" if s < 0 else "der"
            destino = lamp_on if (k, lado) in lamparas_on else detalle
            destino.caja(s * (W2 - 0.40), s * (W2 - 0.30), Y(ys - 0.05), Y(ys + 0.05), P["rack_z"] - 0.035, P["rack_z"])

    if ultimo:
        y_cab = mt + P["paso_fila"]
        cabina.caja(x_pas, W2, Y(0), Y(y_cab), 0, H)                                   # volumen del piso al cielo
        detalle.caja(x_pas - 0.03, x_pas, Y(0.25), Y(0.95), 0, 1.95)                   # su puerta mira al pasillo
        detalle.caja(0.56, 0.66, Y(largo - 0.05), Y(largo), 1.45, 1.70)                # freno, a la derecha de la puerta

    for malla, nom, mat in ((casco, "casco", "SET_casco"), (piso, "piso", "SET_piso"), (asientos, "asientos", "SET_asiento"),
                            (detalle, "detalle", "SET_detalle"), (noche, "ventanas", "SET_noche"), (tira, "tira", "SET_tira"),
                            (lamp_on, "lamparas_on", "SET_lampara_on"), (cabina, "cabina", "SET_cabina")):
        if not malla.vacia():
            malla.objeto("%s_%s" % (nombre, nom), col, mat)

    # puertas (hoja centrada en el espesor de la pared)
    if ultimo:
        # bisagras a la derecha vistas desde dentro (+X); cerradura a la izquierda desde dentro / derecha desde el fuelle
        construir_puerta(nombre, col, anclas, +P["puerta_w"] / 2, -1, Y(largo + p / 2), P, signo=+1, con_cerradura=True)
    else:
        construir_puerta(nombre + "_del", col, anclas, -P["puerta_w"] / 2, +1, Y(largo + p / 2), P, signo=-1)
        construir_puerta(nombre + "_tras", col, anclas, -P["puerta_w"] / 2, +1, Y(-p / 2), P, signo=+1)

    L.vacio("ANC_" + nombre, anclas, (0, Y(0), 0), 0.3)
    L.vacio("ANC_%s_puerta_del" % nombre, anclas, (0, Y(largo), 0), 0.2)
    if not ultimo:
        L.vacio("ANC_%s_puerta_tras" % nombre, anclas, (0, Y(0), 0), 0.2)
    return {"nombre": nombre, "tipo": tipo, "y0_mundo": y0, "largo_interior": round(largo, 3), "filas": filas,
            "y_asiento_fila_mundo": {str(k): round(v, 3) for k, v in info_filas.items()},
            "x_asiento_pasillo": round(x_asientos[0], 3), "x_asiento_ventana": round(x_asientos[1], 3)}


def construir_fuelle(P, anclas):
    """Fuelle: pasillo corto y estrecho sin ventanas. Cada pared lateral es un objeto aparte (fuelle_pared_izq / _der)
    para poder ocultarla en un plano ("pared movil", como en un set de rodaje) con "hide_set" en la ficha."""
    col = L.coleccion("SET_fuelle", L.coleccion("SET"))
    G, w2, H = P["fuelle_largo"], P["fuelle_ancho"] / 2, P["fuelle_alto"]
    piso, cielo, tira = L.Malla(), L.Malla(), L.Malla()
    piso.caja(-w2 - 0.05, w2 + 0.05, 0, G, -0.10, 0)
    cielo.caja(-w2 - 0.05, w2 + 0.05, 0, G, H, H + 0.05)
    for s, lado in ((-1, "izq"), (1, "der")):
        pared, costillas = L.Malla(), L.Malla()
        pared.caja(s * w2, s * (w2 + 0.05), 0, G, 0, H)
        n = int(G / 0.20)
        for i in range(n):                                   # costillas del fuelle: dan paralaje a la camara en mano
            y = 0.10 + i * (G - 0.20) / max(1, n - 1)
            costillas.caja(s * (w2 - 0.03), s * w2, y - 0.03, y + 0.03, 0, H)
        pared.objeto("fuelle_pared_" + lado, col, "SET_casco")
        costillas.objeto("fuelle_costillas_" + lado, col, "SET_detalle")
    tira.caja(-0.05, 0.05, 0.15, G - 0.15, H - 0.03, H)
    cielo.objeto("fuelle_cielo", col, "SET_casco")
    piso.objeto("fuelle_piso", col, "SET_piso")
    tira.objeto("fuelle_tira", col, "SET_tira")
    L.vacio("ANC_fuelle", anclas, (0, 0, 0), 0.3)
    L.vacio("ANC_fuelle_centro", anclas, (0, G / 2, 0), 0.2)


def construir_props(anclas):
    col = L.coleccion("PROPS")
    # maletin: 44 x 30 x 11 cm, parado sobre su canto largo. Origen en la base, al centro. El largo va en X local.
    lx, ly, lz = 0.44, 0.11, 0.30
    mal = L.Malla().caja(-lx / 2, lx / 2, -ly / 2, ly / 2, 0, lz).objeto("PROP_maletin", col, "PROP_oscuro")
    mm = L.Malla()
    e = 0.035
    for sx in (-1, 1):
        for sz in (0, 1):                                      # esquinas metalicas
            xa, xb = (lx / 2 - e, lx / 2 + 0.004) if sx > 0 else (-lx / 2 - 0.004, -lx / 2 + e)
            za, zb = (lz - e, lz + 0.004) if sz else (0.0, e)
            mm.caja(xa, xb, -ly / 2 - 0.004, ly / 2 + 0.004, za, zb)
    for sx in (-1, 1):
        mm.caja(sx * 0.11 - 0.02, sx * 0.11 + 0.02, -ly / 2 - 0.004, ly / 2 + 0.004, lz - 0.03, lz + 0.004)  # dos cierres
    met = mm.objeto("PROP_maletin_metal", col, "PROP_metal")
    met.parent = mal
    asa = L.Malla().caja(-0.07, 0.07, -0.012, 0.012, lz, lz + 0.03).objeto("PROP_maletin_asa", col, "PROP_oscuro")
    asa.parent = mal
    mal["es_prop"] = True
    mal.location = (60, 0, 0)

    # llave antigua de hierro, ~13 cm. Origen en la bocallave; el cano sale hacia +Y local; el paleton cuelga en -Z.
    llave = L.cilindro("PROP_llave", col, "PROP_hierro", 0.006, 0.085, eje="Y")
    mm = L.Malla()
    mm.caja(-0.004, 0.004, 0.080, 0.090, -0.024, 0.024)       # ojo de la llave (anillo de cuatro barras)
    mm.caja(-0.004, 0.004, 0.122, 0.132, -0.024, 0.024)
    mm.caja(-0.004, 0.004, 0.080, 0.132, 0.016, 0.026)
    mm.caja(-0.004, 0.004, 0.080, 0.132, -0.026, -0.016)
    mm.caja(-0.003, 0.003, -0.030, -0.008, -0.022, 0.0)       # paleton (queda dentro de la puerta)
    ojo = mm.objeto("PROP_llave_ojo", col, "PROP_hierro")
    ojo.parent = llave
    llave["es_prop"] = True
    llave.location = (61, 0, 0)
    for ob in (mal, met, asa, llave, ojo):
        ob.hide_render = True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="ruta del .blend de salida")
    ap.add_argument("--info", default=None, help="ruta del set_info.json (por defecto, junto al .blend)")
    ap.add_argument("--filas", type=int, default=20, help="filas del modulo de pasajeros (20 filas ~ 20 m)")
    a = ap.parse_args(L.args_script())

    bpy.ops.wm.read_factory_settings(use_empty=True)
    L.preparar_escena()
    L.crear_materiales_set()
    anclas = L.coleccion("ANCLAS")
    P = dict(DEF)
    p, G = P["pared"], P["fuelle_largo"]

    largo_u = P["ultimo_margen_tras"] + P["ultimo_filas"] * P["paso_fila"] + P["ultimo_margen_del"]
    largo_p = P["margen_tras"] + a.filas * P["paso_fila"] + P["margen_del"]
    paso_vagon = largo_p + 2 * p + G
    info = {"medidas": P, "ejes": "+Y cabeza del tren, +X derecha mirando adelante, +Z arriba; metros",
            "vagones": []}
    info["vagones"].append(construir_vagon("ultimo", -(largo_u + p), P["ultimo_filas"], P, anclas, tipo="ultimo"))
    construir_fuelle(P, anclas)
    info["vagones"].append(construir_vagon("vagon5", G + p, a.filas, P, anclas,
                                           lamparas_on=((4, "izq"), (11, "der"), (17, "izq"))))
    info["vagones"].append(construir_vagon("vagon2", G + p + 3 * paso_vagon, a.filas, P, anclas,
                                           lamparas_on=((5, "izq"), (12, "der"), (17, "der"))))
    construir_props(anclas)
    L.aplicar_luz("neutro")
    bpy.context.view_layer.update()

    info["anclas"] = {ob.name: [round(c, 4) for c in ob.matrix_world.translation] for ob in anclas.objects}
    info["fuelle"] = {"largo": G, "ancho": P["fuelle_ancho"], "alto": P["fuelle_alto"],
                      "nota": "y=0 pared del ultimo vagon (cara del fuelle); y=largo pared del vagon 5"}
    info["puertas"] = {ob.name: {"bisagra_x": ob["bisagra_x"], "signo": ob["signo"],
                                 "y_mundo": round(ob.location.y, 4)} for ob in bpy.data.objects if ob.get("es_puerta")}
    out = os.path.abspath(a.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=out)
    ruta_info = os.path.abspath(a.info) if a.info else os.path.join(os.path.dirname(out), "set_info.json")
    with open(ruta_info, "w", encoding="utf-8") as fh:
        json.dump(info, fh, ensure_ascii=False, indent=1)
    print("[build_set] OK ->", out)
    print("[build_set] info ->", ruta_info)


if __name__ == "__main__":
    main()
