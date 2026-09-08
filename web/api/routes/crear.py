from flask import jsonify, request
from database.models import Producto
from database.conexion import get_db
from .. import api_bp

@api_bp.route('/productos', methods=['POST'])
def crear_producto():
    db = next(get_db())
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
    
    producto = Producto(
        nombre=data['nombre'],
        descripcion=data.get('descripcion', ''),
        precio=data['precio'],
        stock=data.get('stock', 0)
    )
    db.add(producto)
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
    }), 201