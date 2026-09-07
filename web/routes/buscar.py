from flask import render_template, request, redirect, url_for
from web import web_bp
from web.crud import buscar_productos
from web.crud.base import get_db

@web_bp.route("/productos/buscar")
def buscar():
    termino = request.args.get("q", "").strip()

    if not termino:
        return redirect(url_for("web.inicio"))

    db = next(get_db())
    productos = buscar_productos(db, termino)
    return render_template("productos.html", productos=productos, termino=termino)