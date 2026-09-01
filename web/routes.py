from flask import render_template

from web import web_bp
from web.productos import obtener_productos


@web_bp.route("/")
def inicio():
    return render_template("inicio.html")


@web_bp.route("/productos")
def listar_productos():
    productos = obtener_productos()

    return render_template(
        "productos.html",
        productos=productos
    )