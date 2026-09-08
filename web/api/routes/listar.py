from flask import jsonify, request
from database.models import Producto
from database.conexion import get_db
from .. import api_bp


@api_bp.route('/productos', methods=['GET'])
def listar_productos():
    db = next(get_db())
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 12, type=int)
    
    productos = db.query(Producto).offset((page - 1) * per_page).limit(per_page).all()
    total = db.query(Producto).count()
    
    return jsonify({
        "success": True,
        "data": [
            {
                "id": p.id,
                "nombre": p.nombre,
                "descripcion": p.descripcion,
                "precio": float(p.precio),
                "stock": p.stock
            } for p in productos
        ],
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total": total,
            "pages": (total + per_page - 1) // per_page
        }
    })
