from database.conexion import obtener_conexion

# --------------------------------------------------
# AGREGAR PRODUCTO
# --------------------------------------------------

def agregar_producto():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    print()
    print("================================")
    print("       AGREGAR PRODUCTO")
    print("================================")
    print()

    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    precio = float(input("Precio del producto en USD: "))
    stock = int(input("Stock del producto: "))

    cursor.execute(
        """
        INSERT INTO productos (nombre, descripcion, precio, stock)
        VALUES (?, ?, ?, ?)
        """,
        (nombre, descripcion, precio, stock)
    )

    conexion.commit()
    conexion.close()

    print("Producto agregado con éxito.")
