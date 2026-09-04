from flask import redirect, url_for, flash
from web import web_bp
from web.productos import eliminar_producto

@web_bp.route("/productos/<int:id>/eliminar", methods=["POST"])
def eliminar_producto_view(id):
    eliminar_producto(id)
    flash("Producto eliminado exitosamente", "success")
    return redirect(url_for("web.inicio"))