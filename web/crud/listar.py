from web.crud.base import obtener_cursor

def obtener_productos():
    with obtener_cursor() as cursor:
        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()