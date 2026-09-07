from flask import redirect, url_for, flash
from web import web_bp
from web.crud import eliminar_producto
from web.crud.base import get_db

@web_bp.route("/productos/<int:id>/eliminar", methods=["POST"])
def eliminar_producto_view(id):
    db = next(get_db())
    eliminar_producto(db, id)
    flash("Producto eliminado exitosamente", "success")
    return redirect(url_for("web.inicio"))