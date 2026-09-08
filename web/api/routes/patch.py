from flask import jsonify, request
from database.models import Producto
from database.conexion import get_db
from .. import api_bp

@api_bp.route('/productos/<int:id>', methods=['PATCH'])
def patch_producto(id):
    db = next(get_db())
    producto = db.query(Producto).filter(Producto.id == id).first()
    
    if not producto:
        return jsonify({"success": False, "error": "Producto no encontrado"}), 404
    
    data = request.get_json(force=True)
    
    if not data:
        return jsonify({"success": False, "error": "Datos no proporcionados"}), 400
    
    if 'nombre' in data:
        if not data['nombre']:
            return jsonify({"success": False, "error": "El nombre no puede estar vacío"}), 400
        producto.nombre = data['nombre']
    
    if 'descripcion' in data:
        producto.descripcion = data['descripcion']
    
    if 'precio' in data:
        if data['precio'] <= 0:
            return jsonify({"success": False, "error": "El precio debe ser mayor a 0"}), 400
        producto.precio = data['precio']
    
    if 'stock' in data:
        if data['stock'] < 0:
            return jsonify({"success": False, "error": "El stock no puede ser negativo"}), 400
        producto.stock = data['stock']
    
    db.commit()
    db.refresh(producto)
    
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

