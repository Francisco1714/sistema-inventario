from sqlalchemy.orm import Session
from database.models import Producto

def actualizar_producto(db: Session, id: int, nombre: str, descripcion: str, precio: float, stock: int):
    producto = db.query(Producto).filter_by(id=id).first()
    if producto:
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.stock = stock
        db.commit()
        db.refresh(producto)
    return producto