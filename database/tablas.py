from database.conexion import obtener_conexion
import productos 

# --------------------------------------------------
# CREAR TABLA DE PRODUCTOS
# --------------------------------------------------

def crear_tabla_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # aqui ira el create table 
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        descripcion TEXT,
        precio REAL,
        stock INTEGER
    )
""")
    
    conexion.commit()
    conexion.close()

