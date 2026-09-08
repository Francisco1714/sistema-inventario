from flask import jsonify
from database.models import Producto
from database.conexion import get_db
from .. import api_bp

@api_bp.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    db = next(get_db())
    producto = db.query(Producto).filter(Producto.id == id).first()
    
    if not producto:
        return jsonify({"success": False, "error": "Producto no encontrado"}), 404
    
    return jsonify({
        "success": True,
        "data": {
            "id": producto.id,
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio": float(producto.precio),
            "stock": producto.stock
        }
    })
