# -*- coding: utf-8 -*-
"""render_shot.py - renderiza los cuadros de una llamada ya armada por shot_from_json.py.

  blender -b <trabajo>/render/c05a/c05a.blend -P render_shot.py -- --out <trabajo>/render/c05a/frame_ \
      [--engine BLENDER_WORKBENCH|BLENDER_EEVEE_NEXT] [--res 720 1280] [--fps 24] [--frames 0 119] [--still 84]

Salida: <out>0000.png ... (cuadro k = archivo k). Luz plana: Workbench con luz de estudio, color por material,
sin sombras proyectadas, con cavidad y contorno para que los bloques se separen. Vista "Standard": los colores
de los personajes salen tal cual. Los cortes los hacen los marcadores de camara de la linea de tiempo.
"""
import argparse
import os
import sys
import time

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import previz_lib as L  # noqa: E402


def configurar_workbench(sc):
    sc.render.engine = "BLENDER_WORKBENCH"
    sh = sc.display.shading
    sh.light = "STUDIO"
    sh.color_type = "MATERIAL"
    sh.show_shadows = False
    sh.show_cavity = True
    sh.cavity_type = "BOTH"
    sh.cavity_ridge_factor = 0.6
    sh.cavity_valley_factor = 1.0
    sh.curvature_ridge_factor = 0.6
    sh.curvature_valley_factor = 0.8
    sh.show_object_outline = True
    sh.object_outline_color = (0.0, 0.0, 0.0)
    sh.show_specular_highlight = False
    sh.show_backface_culling = False
    sh.show_xray = False
    try:
        sh.background_type = "WORLD"
    except Exception:
        pass
    sc.display.render_aa = "8"


def configurar_eevee(sc):
    """EEVEE con luz plana: mundo parejo + un sol suave. Solo si el plano depende de la luz."""
    motores = [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items]
    sc.render.engine = "BLENDER_EEVEE_NEXT" if "BLENDER_EEVEE_NEXT" in motores else "BLENDER_EEVEE"
    w = sc.world
    w.use_nodes = True
    bg = w.node_tree.nodes.get("Background")
    if bg is not None:
        bg.inputs[0].default_value = (0.8, 0.8, 0.8, 1.0)
        bg.inputs[1].default_value = 0.45
    if bpy.data.objects.get("LUZ_plana") is None:
        ld = bpy.data.lights.new("LUZ_plana", "SUN")
        ld.energy = 0.8
        ld.use_shadow = False
        lo = bpy.data.objects.new("LUZ_plana", ld)
        lo.rotation_euler = (0.6, 0.2, 0.4)
        sc.collection.objects.link(lo)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="prefijo de salida, p. ej. <dir>/frame_")
    ap.add_argument("--engine", default="BLENDER_WORKBENCH")
    ap.add_argument("--res", type=int, nargs=2, default=None)
    ap.add_argument("--fps", type=int, default=None)
    ap.add_argument("--frames", type=int, nargs=2, default=None, help="rango de cuadros (por defecto, toda la llamada)")
    ap.add_argument("--still", type=int, nargs="*", default=None, help="renderiza solo estos cuadros")
    a = ap.parse_args(L.args_script())

    sc = bpy.context.scene
    if a.res:
        sc.render.resolution_x, sc.render.resolution_y = a.res
    if a.fps:
        sc.render.fps = a.fps
    sc.render.resolution_percentage = 100
    sc.render.film_transparent = False
    sc.render.use_motion_blur = False
    sc.view_settings.view_transform = "Standard"
    sc.view_settings.look = "None"
    sc.view_settings.exposure = 0.0
    sc.view_settings.gamma = 1.0
    sc.render.image_settings.file_format = "PNG"
    sc.render.image_settings.color_mode = "RGB"
    sc.render.image_settings.compression = 30
    sc.render.use_file_extension = True
    sc.render.use_overwrite = True
    if a.engine.upper().startswith("BLENDER_EEVEE"):
        configurar_eevee(sc)
    else:
        configurar_workbench(sc)

    prefijo = os.path.abspath(a.out)
    os.makedirs(os.path.dirname(prefijo), exist_ok=True)
    t0 = time.time()
    if a.still is not None and len(a.still) > 0:
        for f in a.still:
            sc.frame_set(f)                       # los marcadores eligen la camara del plano
            sc.render.filepath = "%s%04d.png" % (prefijo, f)
            bpy.ops.render.render(write_still=True)
        n = len(a.still)
    else:
        if a.frames:
            sc.frame_start, sc.frame_end = a.frames
        sc.render.filepath = prefijo + "####"
        bpy.ops.render.render(animation=True)
        n = sc.frame_end - sc.frame_start + 1
    dt = time.time() - t0
    print("[render_shot] %d cuadros en %.1f s (%.2f s/cuadro), motor %s, %dx%d a %d fps" %
          (n, dt, dt / max(1, n), sc.render.engine, sc.render.resolution_x, sc.render.resolution_y, sc.render.fps))


if __name__ == "__main__":
    main()
