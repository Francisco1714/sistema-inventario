from flask import render_template
from web import web_bp
from web.crud import obtener_productos

@web_bp.route("/")
def inicio():
    productos = obtener_productos()
    return render_template("productos.html", productos=productos)
