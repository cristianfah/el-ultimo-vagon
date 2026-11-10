# -*- coding: utf-8 -*-
"""build_cast.py - elenco de figuras de tres bloques (cabeza esfera lisa, torso, un bloque de piernas).

  blender -b <set>/tren_blockout.blend -P build_cast.py -- --save [--infectados 6] [--extras 6] [--sin-nariz]

Agrega la coleccion ELENCO al .blend del set y lo guarda. Cada figura queda estacionada lejos del set y oculta:
shot_from_json.py las ubica, les da postura y decide que partes se ven en cada plano.
Sin brazos por defecto. Las barras-brazo (<n>_brazo_R / _L), la bota y su cana existen ocultas: solo se muestran
si la ficha del plano las pide (cuando la mano es la accion).
Colores y alturas: previz_lib.COLORES y previz_lib.ALTURAS (las alturas son supuestas; la biblia no las fija).
"""
import argparse
import os
import sys

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import previz_lib as L  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--save", action="store_true", help="guarda sobre el mismo .blend")
    ap.add_argument("--out", default=None, help="o guarda en otra ruta")
    ap.add_argument("--infectados", type=int, default=6)
    ap.add_argument("--extras", type=int, default=6)
    ap.add_argument("--sin-nariz", action="store_true", help="sin la cuna que marca hacia donde mira la cabeza")
    a = ap.parse_args(L.args_script())

    viejo = bpy.data.collections.get("ELENCO")
    if viejo is not None:                      # reconstruccion limpia
        for ob in list(viejo.objects):
            bpy.data.objects.remove(ob, do_unlink=True)
        bpy.data.collections.remove(viejo)
    col = L.coleccion("ELENCO")

    nombres = ["martina", "tomas", "diego", "carmen", "ivan", "hugo", "hombre_azul", "esposa"]
    nombres += ["infectado_%d" % i for i in range(1, a.infectados + 1)]
    nombres += ["extra_%d" % i for i in range(1, a.extras + 1)]
    for i, n in enumerate(nombres):
        base = n.rsplit("_", 1)[0] if n.startswith(("infectado_", "extra_")) else n
        raiz = L.crear_figura(n, L.ALTURAS[base], L.COLORES[base], col, nariz=not a.sin_nariz)
        raiz.location = (80.0 + i * 1.2, 0.0, 0.0)          # estacionadas fuera del tren
        for parte in L.partes_figura(n):
            ob = bpy.data.objects.get(parte)
            if ob is not None:
                ob.hide_render = True
        print("[build_cast] %-14s %.2f m  color %s" % (n, L.ALTURAS[base], L.COLORES[base]))

    if a.out:
        bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(a.out))
    elif a.save:
        bpy.ops.wm.save_mainfile()
    print("[build_cast] OK: %d figuras" % len(nombres))


if __name__ == "__main__":
    main()
