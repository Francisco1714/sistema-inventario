from flask import jsonify, request
from database.models import Producto
from database.conexion import get_db
from .. import api_bp

@api_bp.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    db = next(get_db())
    producto = db.query(Producto).filter(Producto.id == id).first()
    
    if not producto:
        return jsonify({"success": False, "error": "Producto no encontrado"}), 404
    
    data = request.get_json(force=True)
    
    if not data:
        return jsonify({"success": False, "error": "Datos no proporcionados"}), 400
    
    errores = []
    if not data.get('nombre'):
        errores.append("El nombre es obligatorio")
    if not data.get('precio') or data['precio'] <= 0:
        errores.append("El precio debe ser mayor a 0")
    if 'stock' in data and data['stock'] < 0:
        errores.append("El stock no puede ser negativo")
    
    if errores:
        return jsonify({"success": False, "error": errores}), 400
    
    producto.nombre = data['nombre']
    producto.descripcion = data.get('descripcion', '')
    producto.precio = data['precio']
    producto.stock = data.get('stock', 0)
    
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