from web.crud.base import obtener_cursor

def actualizar_producto(id, nombre, descripcion, precio, stock):
    with obtener_cursor() as cursor:
        cursor.execute(
            "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, stock = %s WHERE id = %s",
            (nombre, descripcion, precio, stock, id)
        )