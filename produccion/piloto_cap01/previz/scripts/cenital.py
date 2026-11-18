# -*- coding: utf-8 -*-
"""cenital.py - vista cenital (planta) de un plano, desde una llamada ya armada por shot_from_json.py.

  blender -b <trabajo>/render/<id>/<id>.blend -P cenital.py -- --plano b5_p7 --frame 90 \
      --region x0 y0 x1 y1 --px 900 --out <dir>/b5_p7_planta.png

Camara ortografica mirando hacia abajo, con +Y (cabeza del tren) hacia arriba de la imagen. Corta todo lo que esta
sobre 1,85 m (cielo, portaequipaje y lamparas) para que se vean los asientos y los cilindros. Muestra solo las marcas
de piso de ese plano (MARCA_<plano>_<personaje>_A/C). Workbench plano y rapido. Las flechas de camara y los
recorridos los dibuja storyboard.py encima, con la misma proyeccion (la region entra completa, sin margen extra).
"""
import argparse
import os
import sys

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import previz_lib as L  # noqa: E402

CORTE_Z = 1.85


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plano", required=True)
    ap.add_argument("--frame", type=int, required=True)
    ap.add_argument("--region", type=float, nargs=4, required=True, help="x0 y0 x1 y1 en metros de mundo")
    ap.add_argument("--px", type=int, default=900, help="ancho en pixeles")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(L.args_script())
    x0, y0, x1, y1 = a.region
    w, h = x1 - x0, y1 - y0
    sc = bpy.context.scene
    sc.frame_set(a.frame)
    cd = bpy.data.cameras.new("CAM_cenital")
    cd.type = "ORTHO"
    cd.sensor_fit = "HORIZONTAL"
    cd.ortho_scale = w
    alto_cam = 12.0
    cd.clip_start = alto_cam - CORTE_Z
    cd.clip_end = alto_cam + 1.0
    cam = bpy.data.objects.new("CAM_cenital", cd)
    sc.collection.objects.link(cam)
    cam.location = ((x0 + x1) / 2, (y0 + y1) / 2, alto_cam)
    cam.rotation_euler = (0, 0, 0)
    sc.camera = cam
    sc.timeline_markers.clear()                  # que los marcadores no cambien la camara
    sc.render.resolution_x = a.px
    sc.render.resolution_y = max(2, int(round(a.px * h / w)))
    sc.render.resolution_percentage = 100
    for ob in bpy.data.objects:
        if ob.name.startswith("MARCA_"):
            ob.hide_render = ob.get("plano") != a.plano
    sc.render.engine = "BLENDER_WORKBENCH"
    sh = sc.display.shading
    sh.light = "FLAT"
    sh.color_type = "MATERIAL"
    sh.show_shadows = False
    sh.show_cavity = False
    sh.show_object_outline = True
    sh.object_outline_color = (0.0, 0.0, 0.0)
    try:
        sh.background_type = "VIEWPORT"
        sh.background_color = (0.08, 0.08, 0.09)
    except Exception:
        pass
    sc.display.render_aa = "8"
    sc.view_settings.view_transform = "Standard"
    for mat in bpy.data.materials:                # planta en grises parejos, sin el tinte del estado de luz
        if mat.get("es_set"):
            L._poner_color(mat, mat["base_rgb"])
    sc.render.image_settings.file_format = "PNG"
    sc.render.filepath = os.path.abspath(a.out)
    os.makedirs(os.path.dirname(sc.render.filepath), exist_ok=True)
    bpy.ops.render.render(write_still=True)
    print("[cenital] %s cuadro %d -> %s (%dx%d)" % (a.plano, a.frame, a.out, sc.render.resolution_x, sc.render.resolution_y))


if __name__ == "__main__":
    main()
