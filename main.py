from database.conexion import obtener_conexion
from database.tablas import crear_tabla_productos
from productos.crud import agregar_producto, listar_productos, modificar_producto, eliminar_producto    

conexion = obtener_conexion()

eliminar_producto()