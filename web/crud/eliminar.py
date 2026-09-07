from sqlalchemy.orm import Session
from database.models import Producto

def eliminar_producto(db: Session, id: int):
    producto = db.query(Producto).filter_by(id=id).first()
    if producto:
        db.delete(producto)
        db.commit()
        return True
    return False