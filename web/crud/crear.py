from web.crud.base import obtener_cursor

def crear_producto(nombre, descripcion, precio, stock):
    with obtener_cursor() as cursor:
        cursor.execute(
            "INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (?, ?, ?, ?)",
            (nombre, descripcion, precio, stock)
        )