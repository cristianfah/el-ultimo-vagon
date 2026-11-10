# -*- coding: utf-8 -*-
"""Tiempos de una ficha de llamada -> cuadros. Python puro (lo usan Blender y los scripts de ffmpeg).

Regla unica de redondeo: cuadro = round(t * fps). El cuadro k se muestra en t = k / fps.
Un plano ocupa los cuadros [f0, f1) : f1 es el primer cuadro del plano siguiente (corte seco).
"""
import json


def cuadro(t, fps):
    return int(round(float(t) * fps))


def leer_ficha(ruta):
    with open(ruta, "r", encoding="utf-8") as fh:
        return json.load(fh)


def planos_en_cuadros(ficha):
    """Devuelve (n_cuadros, [ {id, f0, f1, t0, t1} ... ]) y valida que los planos cubran la llamada."""
    fps = int(ficha.get("fps", 24))
    dur = ficha["duration_s"]
    if abs(dur - round(dur)) > 1e-9:
        raise ValueError("duration_s debe ser un entero de segundos (es %r)" % dur)
    n = int(round(dur)) * fps
    planos = []
    for sh in ficha["shots"]:
        planos.append({"id": sh["id"], "f0": cuadro(sh["t0"], fps), "f1": cuadro(sh["t1"], fps),
                       "t0": sh["t0"], "t1": sh["t1"]})
    planos.sort(key=lambda p: p["f0"])
    if planos[0]["f0"] != 0:
        raise ValueError("El primer plano debe partir en t0 = 0 (la accion ya esta en marcha en el cuadro 0)")
    for a, b in zip(planos, planos[1:]):
        if a["f1"] != b["f0"]:
            raise ValueError("Hueco o traslape entre %s y %s" % (a["id"], b["id"]))
    if planos[-1]["f1"] != n:
        raise ValueError("El ultimo plano debe terminar en duration_s (%d cuadros), termina en %d" % (n, planos[-1]["f1"]))
    for p in planos:
        if p["f1"] <= p["f0"]:
            raise ValueError("Plano vacio: %s" % p["id"])
    return n, planos
