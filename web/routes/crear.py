from flask import render_template, request, redirect, url_for, flash
from web import web_bp
from web.crud import crear_producto

@web_bp.route("/productos/crear", methods=["GET", "POST"])
def crear_producto_view():
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        errores = []
        if not nombre or not nombre.strip():
            errores.append("El nombre es obligatorio")
        try:
            precio_float = float(precio)
            if precio_float <= 0:
                errores.append("El precio debe ser mayor a 0")
        except ValueError:
            errores.append("El precio debe ser un número válido")
        try:
            stock_int = int(stock)
            if stock_int < 0:
                errores.append("El stock no puede ser negativo")
        except ValueError:
            errores.append("El stock debe ser un número entero")

        if errores:
            return render_template("crear_producto.html", errores=errores, nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)

        crear_producto(nombre, descripcion, precio_float, stock_int)
        flash("Producto creado exitosamente", "success")
        return redirect(url_for("web.inicio"))
    return render_template("crear_producto.html")