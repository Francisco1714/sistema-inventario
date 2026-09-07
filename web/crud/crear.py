from sqlalchemy.orm import Session
from database.models import Producto

def crear_producto(db: Session, nombre: str, descripcion: str, precio: float, stock: int):
    nuevo = Producto(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo