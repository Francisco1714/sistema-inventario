from flask import render_template, request, redirect, url_for

from web import web_bp
from web.productos import obtener_producto_por_id, obtener_productos, crear_producto, actualizar_producto

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

@web_bp.route("/productos/<int:id>/modificar", methods=["GET", "POST"])
def modificar_producto_view(id):
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        stock = request.form["stock"]       

        actualizar_producto(id, nombre, descripcion, float(precio), int(stock))

        return redirect(url_for("web.listar_productos"))

    producto = obtener_producto_por_id(id)
    return render_template("modificar_producto.html", producto=producto)