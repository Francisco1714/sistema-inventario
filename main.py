from database.conexion import obtener_conexion

conexion = obtener_conexion()

print("Conexión a SQLite establecida con éxito.")

conexion.close()