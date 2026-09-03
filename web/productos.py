from database.conexion import obtener_conexion

def obtener_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")

    productos = cursor.fetchall()

    conexion.close()

    return productos

def crear_producto(nombre, descripcion, precio, stock):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (?, ?, ?, ?)",
        (nombre, descripcion, precio, stock)
    )

    conexion.commit()
    conexion.close()

def obtener_producto_por_id(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))

    producto = cursor.fetchone()

    conexion.close()

    return producto

def actualizar_producto(id, nombre, descripcion, precio, stock):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
    "UPDATE productos SET nombre = ?, descripcion = ?, precio = ?, stock = ? WHERE id = ?",
    (nombre, descripcion, precio, stock, id)
    )

    conexion.commit()
    conexion.close()

def eliminar_producto(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))

    conexion.commit()
    conexion.close()