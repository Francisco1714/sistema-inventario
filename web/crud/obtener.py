from web.crud.base import obtener_cursor
def obtener_producto_por_id(id):
    with obtener_cursor() as cursor:
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        return cursor.fetchone()