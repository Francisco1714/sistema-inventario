from contextlib import contextmanager
from database.conexion import obtener_conexion

@contextmanager
def obtener_cursor():
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        yield cursor
        conexion.commit()
    finally:
        conexion.close()