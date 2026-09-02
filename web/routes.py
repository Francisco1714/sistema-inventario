from flask import render_template, request, redirect, url_for

from web import web_bp
from web.productos import obtener_productos, crear_producto


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

@web_bp.route("/productos/crear", methods=["GET", "POST"])
def crear_producto_view():
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        crear_producto(nombre, descripcion, float(precio), int(stock))

        return redirect(url_for("web.listar_productos"))
    return render_template("crear_producto.html")