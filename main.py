from database.conexion import obtener_conexion
from database.tablas import crear_tabla_productos

conexion = obtener_conexion()

print("Conexión a SQLite establecida con éxito.")

conexion.close()

crear_tabla_productos()
print("Tabla de productos creada con éxito.")