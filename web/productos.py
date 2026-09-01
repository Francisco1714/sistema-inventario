from database.conexion import obtener_conexion

def obtener_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")

    productos = cursor.fetchall()

    conexion.close()

    return productos