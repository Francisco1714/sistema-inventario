from sqlalchemy.orm import Session
from database.models import Producto

def obtener_producto_por_id(db: Session, id: int):
    return db.query(Producto).filter_by(id=id).first()