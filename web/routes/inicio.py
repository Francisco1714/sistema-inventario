from flask import render_template
from web import web_bp
from web.crud import obtener_productos_paginados, contar_productos

@web_bp.route("/")
@web_bp.route("/page/<int:page>")
def inicio(page=1):
    total = contar_productos()
    per_page = 12
    total_pages = (total + per_page - 1) // per_page 

    if page < 1:
        page = 1
    elif page > total_pages and total_pages > 0:
        page = total_pages

    productos = obtener_productos_paginados(page, per_page)
    return render_template("productos.html", productos=productos, page=page, total_pages=total_pages)
