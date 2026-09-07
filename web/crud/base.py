from contextlib import contextmanager
import psycopg2.extras
from database.conexion import obtener_conexion

@contextmanager
def obtener_cursor():
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        yield cursor
        conexion.commit()
    finally:
        conexion.close()