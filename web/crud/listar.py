from web.crud.base import obtener_cursor

def obtener_productos():
    with obtener_cursor() as cursor:
        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()

def obtener_productos_paginados(page, per_page=12):
    offset = (page - 1) * per_page
    with obtener_cursor() as cursor:
        cursor.execute("SELECT * FROM productos LIMIT ? OFFSET ?", (per_page, offset))
        return cursor.fetchall()
    
def contar_productos():
    with obtener_cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM productos")
        return cursor.fetchone()[0]
    