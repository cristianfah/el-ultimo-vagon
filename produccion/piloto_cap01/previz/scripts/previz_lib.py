# -*- coding: utf-8 -*-
"""Utilidades comunes del previz (solo dentro de Blender): mallas de cajas, materiales, figuras, luz del set.

Convenciones del mundo:
  +Y = hacia la cabeza del tren (hacia la puerta delantera de cada vagon). +X = derecha mirando hacia adelante. +Z = arriba.
  Metros. Una figura con yaw 0 mira hacia +Y; yaw positivo gira hacia la izquierda (antihorario visto desde arriba).
"""
import math
import sys

import bpy
import bmesh
from mathutils import Matrix, Vector

# ----------------------------------------------------------------------------------------- argumentos


def args_script():
    argv = sys.argv
    return argv[argv.index("--") + 1:] if "--" in argv else []


# ----------------------------------------------------------------------------------------- colecciones

def coleccion(nombre, padre=None):
    col = bpy.data.collections.get(nombre)
    if col is None:
        col = bpy.data.collections.new(nombre)
        (padre or bpy.context.scene.collection).children.link(col)
    return col


# ----------------------------------------------------------------------------------------- materiales

# Grises del set (valor base, sin tinte). Se tinen con aplicar_luz().
GRISES_SET = {
    "SET_casco": 0.64,      # paredes, cielo
    "SET_piso": 0.50,
    "SET_asiento": 0.40,
    "SET_puerta": 0.46,
    "SET_detalle": 0.56,    # portaequipaje, rieles, costillas del fuelle
    "SET_cabina": 0.52,
}
# Tinte leve por estado de luz (multiplica los grises del set; no toca a los personajes).
LUCES = {
    "neutro":     {"tinte": (1.00, 1.00, 1.00), "nivel": 1.00, "tira": (0.45, 0.45, 0.45), "lampara": (0.95, 0.90, 0.80), "mundo": (0.03, 0.035, 0.05)},
    "ambar":      {"tinte": (1.00, 0.90, 0.72), "nivel": 1.00, "tira": (0.40, 0.36, 0.30), "lampara": (1.00, 0.86, 0.55), "mundo": (0.02, 0.025, 0.04)},
    "ambar_bajo": {"tinte": (1.00, 0.88, 0.68), "nivel": 0.86, "tira": (0.32, 0.28, 0.22), "lampara": (1.00, 0.86, 0.55), "mundo": (0.015, 0.02, 0.035)},
    "rojo":       {"tinte": (1.00, 0.80, 0.78), "nivel": 0.92, "tira": (0.70, 0.10, 0.08), "lampara": (0.36, 0.30, 0.29), "mundo": (0.03, 0.012, 0.012)},
}
# Mapa de colores del elenco (color plano y fijo por personaje).
COLORES = {
    "martina":      (0.86, 0.05, 0.05),   # rojo
    "tomas":        (0.07, 0.20, 0.88),   # azul
    "diego":        (0.96, 0.45, 0.04),   # naranja
    "carmen":       (0.97, 0.86, 0.06),   # amarillo
    "ivan":         (0.08, 0.60, 0.14),   # verde
    "hugo":         (0.50, 0.14, 0.72),   # morado
    "hombre_azul":  (0.04, 0.78, 0.88),   # cian (hombre de camisa azul)
    "esposa":       (0.97, 0.50, 0.72),   # rosado
    "infectado":    (0.12, 0.12, 0.13),   # gris oscuro
    "extra":        (0.12, 0.12, 0.13),   # gris oscuro
}
# Alturas en metros. SUPUESTAS: la biblia no las fija; ajustar aqui si las fichas dicen otra cosa.
ALTURAS = {
    "martina": 1.65, "tomas": 1.76, "diego": 1.80, "carmen": 1.58, "ivan": 1.84, "hugo": 1.70,
    "hombre_azul": 1.75, "esposa": 1.62, "infectado": 1.74, "extra": 1.70,
}
PROPS_COLOR = {
    "PROP_oscuro": (0.045, 0.045, 0.05),   # cuerpo del maletin
    "PROP_metal": (0.80, 0.80, 0.82),      # esquinas y cierres del maletin
    "PROP_hierro": (0.10, 0.10, 0.11),     # llave, manija
    "PROP_placa": (0.46, 0.34, 0.13),      # placa de la cerradura
    "PROP_negro": (0.01, 0.01, 0.01),      # bocallave
    "SET_vidrio": (0.55, 0.62, 0.66),      # vidrio de las ventanitas (alfa bajo)
    "SET_noche": (0.035, 0.04, 0.06),      # planos oscuros detras de las ventanas laterales
    "FX_esquirla": (0.82, 0.86, 0.88),
}


def material(nombre, rgb, alfa=1.0, es_set=False):
    mat = bpy.data.materials.get(nombre)
    if mat is None:
        mat = bpy.data.materials.new(nombre)
    mat.use_fake_user = True     # que no se pierda al guardar aunque todavia nadie lo use
    mat.diffuse_color = (rgb[0], rgb[1], rgb[2], alfa)
    mat.roughness = 1.0
    mat.metallic = 0.0
    mat["base_rgb"] = list(rgb)
    mat["es_set"] = bool(es_set)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = (rgb[0], rgb[1], rgb[2], 1.0)
        bsdf.inputs["Roughness"].default_value = 1.0
        if "Alpha" in bsdf.inputs:
            bsdf.inputs["Alpha"].default_value = alfa
    return mat


def crear_materiales_set():
    for nombre, v in GRISES_SET.items():
        material(nombre, (v, v, v), es_set=True)
    material("SET_tira", (0.45, 0.45, 0.45))
    material("SET_lampara_on", (1.0, 0.86, 0.55))
    for nombre, rgb in PROPS_COLOR.items():
        material(nombre, rgb, alfa=0.22 if nombre == "SET_vidrio" else 1.0)


def _poner_color(mat, rgb):
    a = mat.diffuse_color[3]
    mat.diffuse_color = (rgb[0], rgb[1], rgb[2], a)
    if mat.use_nodes:
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf is not None:
            bsdf.inputs["Base Color"].default_value = (rgb[0], rgb[1], rgb[2], 1.0)


def aplicar_luz(estado):
    """Tine los grises del set segun la luz de la locacion. Los personajes y props no cambian."""
    if estado not in LUCES:
        raise ValueError("set_light desconocido: %r (opciones: %s)" % (estado, ", ".join(LUCES)))
    luz = LUCES[estado]
    for mat in bpy.data.materials:
        if mat.get("es_set"):
            base = mat["base_rgb"]
            _poner_color(mat, [base[i] * luz["tinte"][i] * luz["nivel"] for i in range(3)])
    if bpy.data.materials.get("SET_tira"):
        _poner_color(bpy.data.materials["SET_tira"], luz["tira"])
    if bpy.data.materials.get("SET_lampara_on"):
        _poner_color(bpy.data.materials["SET_lampara_on"], luz["lampara"])
    mundo = bpy.context.scene.world
    if mundo is not None:
        mundo.color = luz["mundo"]
        if mundo.use_nodes and mundo.node_tree.nodes.get("Background"):
            mundo.node_tree.nodes["Background"].inputs[0].default_value = (*luz["mundo"], 1.0)


# ----------------------------------------------------------------------------------------- mallas

class Malla:
    """Acumula cajas y las convierte en un solo objeto (un objeto por grupo, no uno por caja)."""

    def __init__(self):
        self.v = []
        self.f = []

    def caja(self, x0, x1, y0, y1, z0, z1):
        if x1 < x0:
            x0, x1 = x1, x0
        if y1 < y0:
            y0, y1 = y1, y0
        if z1 < z0:
            z0, z1 = z1, z0
        b = len(self.v)
        self.v += [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0),
                   (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
        for q in ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)):
            self.f.append(tuple(b + i for i in q))
        return self

    def vacia(self):
        return not self.v

    def objeto(self, nombre, col, mat, origen=(0.0, 0.0, 0.0)):
        ox, oy, oz = origen
        me = bpy.data.meshes.new(nombre)
        me.from_pydata([(x - ox, y - oy, z - oz) for (x, y, z) in self.v], [], self.f)
        me.update()
        ob = bpy.data.objects.new(nombre, me)
        ob.location = origen
        if mat is not None:
            me.materials.append(mat if not isinstance(mat, str) else bpy.data.materials[mat])
        col.objects.link(ob)
        return ob


def objeto_bmesh(nombre, col, mat, bm, liso=False):
    me = bpy.data.meshes.new(nombre)
    bm.to_mesh(me)
    bm.free()
    if liso:
        for p in me.polygons:
            p.use_smooth = True
    ob = bpy.data.objects.new(nombre, me)
    if mat is not None:
        me.materials.append(mat if not isinstance(mat, str) else bpy.data.materials[mat])
    col.objects.link(ob)
    return ob


def esfera(nombre, col, mat, radio):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, radius=radio)
    return objeto_bmesh(nombre, col, mat, bm, liso=True)


def cilindro(nombre, col, mat, radio, largo, eje="Y", segmentos=12):
    """Cilindro que parte en el origen y se extiende `largo` a lo largo del eje dado."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segmentos, radius1=radio, radius2=radio, depth=largo)
    bmesh.ops.translate(bm, verts=bm.verts, vec=(0, 0, largo / 2.0))
    if eje == "Y":
        bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(-math.pi / 2, 3, "X"))
    elif eje == "X":
        bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(math.pi / 2, 3, "Y"))
    return objeto_bmesh(nombre, col, mat, bm, liso=True)


def vacio(nombre, col, pos, tam=0.1):
    ob = bpy.data.objects.new(nombre, None)
    ob.empty_display_size = tam
    ob.empty_display_type = "PLAIN_AXES"
    ob.location = pos
    ob.hide_render = True
    col.objects.link(ob)
    return ob


def emparentar(hijo, padre):
    """Emparenta conservando la posicion de mundo. Supone al padre sin rotacion ni padre propio."""
    hijo.parent = padre
    hijo.matrix_parent_inverse = Matrix.Translation(padre.location).inverted()


# ----------------------------------------------------------------------------------------- figuras

ALTURA_ASIENTO = 0.46   # debe calzar con build_set.DEF["asiento_z"]


def dims_figura(altura, ancho=None):
    """Proporciones de la figura de tres bloques a partir de la altura real."""
    a = float(altura)
    d = {
        "altura": a,
        "piernas_h": 0.50 * a,
        "torso_h": 0.345 * a,
        "cuello": 0.02 * a,
        "cabeza_r": 0.0675 * a,
        "ancho": ancho if ancho else 0.235 * a,   # hombros
        "fondo": 0.22,
        "brazo": 0.075,                            # seccion de la barra-brazo
    }
    d["piernas_ancho"] = d["ancho"] * 0.82
    # cadera (pivote del torso) por postura: (adelanto en Y local, altura)
    d["posturas"] = {
        "de_pie": (0.0, d["piernas_h"]),
        "sentado": (-0.05, ALTURA_ASIENTO),
        "agachado": (-0.06, 0.40),
    }
    return d


PARTES_POSTURA = {"de_pie": "piernas_pie", "sentado": "piernas_sentado", "agachado": "piernas_agachado"}


def crear_figura(nombre, altura, rgb, col, ancho=None, nariz=True):
    """Figura de tres bloques: cabeza (esfera lisa sin cara), torso (caja) y un bloque para las piernas.
    Sin brazos por defecto: las barras-brazo y la bota existen ocultas y solo se muestran si la ficha las pide.

    Jerarquia:  FIG_<n> (raiz en los pies) -> <n>_cadera (pivote del torso) -> <n>_cuello (pivote de la cabeza)
    """
    d = dims_figura(altura, ancho)
    mat = material("FIG_" + nombre, rgb)
    raiz = vacio("FIG_" + nombre, col, (0, 0, 0), 0.3)
    raiz.hide_render = False
    raiz["altura"] = d["altura"]
    raiz["ancho"] = d["ancho"]
    raiz["es_figura"] = True
    w2 = d["piernas_ancho"] / 2.0

    # un bloque de piernas por postura (se muestra uno solo)
    m = Malla().caja(-w2, w2, -0.11, 0.11, 0.0, d["piernas_h"])
    pie = m.objeto(nombre + "_piernas_pie", col, mat)
    m = Malla()
    m.caja(-w2, w2, -0.14, 0.46, ALTURA_ASIENTO, ALTURA_ASIENTO + 0.15)   # muslos sobre el cojin
    m.caja(-w2, w2, 0.32, 0.46, 0.0, ALTURA_ASIENTO)                      # canillas
    sen = m.objeto(nombre + "_piernas_sentado", col, mat)
    m = Malla().caja(-w2, w2, -0.18, 0.30, 0.0, 0.43)
    aga = m.objeto(nombre + "_piernas_agachado", col, mat)
    for ob in (pie, sen, aga):
        ob.parent = raiz

    cadera = vacio(nombre + "_cadera", col, (0, 0, d["piernas_h"]), 0.1)
    cadera.parent = raiz
    m = Malla().caja(-d["ancho"] / 2, d["ancho"] / 2, -d["fondo"] / 2, d["fondo"] / 2, 0.0, d["torso_h"])
    torso = m.objeto(nombre + "_torso", col, mat)
    torso.parent = cadera

    cuello = vacio(nombre + "_cuello", col, (0, 0, d["torso_h"]), 0.1)
    cuello.parent = cadera
    cab = esfera(nombre + "_cabeza", col, mat, d["cabeza_r"])
    cab.parent = cuello
    cab.location = (0, 0, d["cuello"] + d["cabeza_r"])
    partes = [pie, sen, aga, torso, cab]
    if nariz:
        r = d["cabeza_r"]
        me = bpy.data.meshes.new(nombre + "_nariz")
        s = 0.22 * r
        me.from_pydata([(-s, r * 0.93, s * 0.7), (s, r * 0.93, s * 0.7), (0, r * 0.93, -s * 1.5), (0, r * 1.26, -s * 0.9)],
                       [], [(0, 1, 3), (1, 2, 3), (2, 0, 3), (0, 2, 1)])
        me.update()
        me.materials.append(mat)
        nar = bpy.data.objects.new(nombre + "_nariz", me)
        col.objects.link(nar)
        nar.parent = cuello
        nar.location = (0, 0, d["cuello"] + d["cabeza_r"] - 0.12 * r)
        partes.append(nar)

    # barras: caja unitaria que parte en el origen y crece en +Z (se orienta y escala por cuadro)
    b = d["brazo"] / 2.0
    for lado in ("R", "L"):
        m = Malla().caja(-b, b, -b, b, 0.0, 1.0)
        br = m.objeto("%s_brazo_%s" % (nombre, lado), col, mat)
        br.rotation_mode = "QUATERNION"
        br.hide_render = True
        br.hide_viewport = True
    m = Malla().caja(-0.05, 0.05, -0.09, 0.19, 0.0, 0.10)    # bota: origen en el tobillo, punta hacia +Y local
    bota = m.objeto(nombre + "_bota", col, mat)
    m = Malla().caja(-0.05, 0.05, -0.05, 0.05, 0.0, 1.0)
    cana = m.objeto(nombre + "_cana", col, mat)
    cana.rotation_mode = "QUATERNION"
    for ob in (bota, cana):
        ob.hide_render = True
        ob.hide_viewport = True
    return raiz


def partes_figura(nombre):
    """Nombres de todos los objetos visibles posibles de una figura."""
    return ["%s_%s" % (nombre, p) for p in
            ("piernas_pie", "piernas_sentado", "piernas_agachado", "torso", "cabeza", "nariz",
             "brazo_R", "brazo_L", "bota", "cana")]


# ----------------------------------------------------------------------------------------- render

def preparar_escena(fps=24, res=(720, 1280)):
    sc = bpy.context.scene
    sc.render.fps = fps
    sc.render.fps_base = 1.0
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = 100
    sc.render.pixel_aspect_x = sc.render.pixel_aspect_y = 1.0
    sc.unit_settings.system = "METRIC"
    if sc.world is None:
        sc.world = bpy.data.worlds.new("MUNDO")
    sc.world.use_nodes = True
    return sc
