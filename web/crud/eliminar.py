from web.crud.base import obtener_cursor

def eliminar_producto(id):
    with obtener_cursor() as cursor:
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))