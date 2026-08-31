from database.conexion import obtener_conexion

# --------------------------------------------------
# MODIFICAR PRODUCTO
# --------------------------------------------------

def modificar_producto():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    print()
    print("================================")
    print("      MODIFICAR PRODUCTO")
    print("================================")
    print()

    productos = cursor.execute(
        "SELECT * FROM productos"
    ).fetchall()

    if not productos:
        print("No hay productos registrados.")
        conexion.close()
        return

    print()
    print("Productos registrados:")
    print()

    for id, nombre, descripcion, precio, stock in productos:
        print("--------------------------------")
        print(f"ID: {id}")
        print(f"Nombre: {nombre}")
        print(f"Descripción: {descripcion}")
        print(f"Precio: ${precio:.2f} USD")
        print(f"Stock: {stock}")
        print()

    print("--------------------------------")

    id = input("ID del producto a modificar: ")

    cursor.execute(
        "SELECT * FROM productos WHERE id = ?",
        (id,)
    )

    producto = cursor.fetchone()

    if not producto:
        print("No existe un producto con ese ID.")
        conexion.close()
        return

    print()
    print("Producto actual:")
    print(f"ID: {producto[0]}")
    print(f"Nombre: {producto[1]}")
    print(f"Descripción: {producto[2]}")
    print(f"Precio: ${producto[3]:.2f} USD")
    print(f"Stock: {producto[4]}")
    print()

    nombre = input("Nuevo nombre: ")
    descripcion = input("Nueva descripción: ")
    precio = float(input("Nuevo precio (USD): "))
    stock = int(input("Nuevo stock: "))

    print()
    print("Nuevos datos:")
    print(f"Nombre: {nombre}")
    print(f"Descripción: {descripcion}")
    print(f"Precio: ${precio:.2f} USD")
    print(f"Stock: {stock}")
    print()

    cursor.execute(
        """
        UPDATE productos
        SET nombre = ?, descripcion = ?, precio = ?, stock = ?
        WHERE id = ?
        """,
        (nombre, descripcion, precio, stock, id)
    )

    conexion.commit()
    conexion.close()

    print("Producto modificado correctamente.")
