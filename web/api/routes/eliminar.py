from flask import jsonify
from database.models import Producto
from database.conexion import get_db
from .. import api_bp

@api_bp.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    db = next(get_db())
    producto = db.query(Producto).filter(Producto.id == id).first()
    
    if not producto:
        return jsonify({"success": False, "error": "Producto no encontrado"}), 404
    
    db.delete(producto)
    db.commit()
    
    return jsonify({"success": True, "message": "Producto eliminado correctamente"})