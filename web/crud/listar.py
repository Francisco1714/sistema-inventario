from sqlalchemy.orm import Session
from database.models import Producto

def obtener_productos(db: Session):
    return db.query(Producto).all()

def obtener_productos_paginados(db: Session, page: int, per_page: int = 12):
    offset = (page - 1) * per_page
    return db.query(Producto).offset(offset).limit(per_page).all()

def contar_productos(db: Session):
    return db.query(Producto).count()

def buscar_productos(db: Session, termino: str):
    return db.query(Producto).filter(
        (Producto.nombre.ilike(f"%{termino}%")) | 
        (Producto.descripcion.ilike(f"%{termino}%"))
    ).all()