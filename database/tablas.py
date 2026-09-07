from database.conexion import obtener_conexion
import psycopg2.extras

# --------------------------------------------------
# CREAR TABLA DE PRODUCTOS
# --------------------------------------------------

def crear_tabla_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS productos (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(255),
        descripcion TEXT,
        precio NUMERIC,
        stock INTEGER
    )
""")
    
    conexion.commit()
    conexion.close()

