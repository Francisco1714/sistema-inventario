from sqlalchemy import Column, Integer, String, Text, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text)
    precio = Column(Numeric, nullable=False)
    stock = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio}, stock={self.stock})>"