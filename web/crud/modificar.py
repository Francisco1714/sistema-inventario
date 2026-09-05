from web.crud.base import obtener_cursor

def actualizar_producto(id, nombre, descripcion, precio, stock):
    with obtener_cursor() as cursor:
        cursor.execute(
            "UPDATE productos SET nombre = ?, descripcion = ?, precio = ?, stock = ? WHERE id = ?",
            (nombre, descripcion, precio, stock, id)
        )