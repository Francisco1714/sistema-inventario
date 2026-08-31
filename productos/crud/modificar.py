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

    while True:
        try:
            id = int(input("ID del producto a modificar: "))

            cursor.execute(
                "SELECT * FROM productos WHERE id = ?",
                (id,)
            )

            producto = cursor.fetchone()

            if producto:
                break

            print("No existe un producto con ese ID.")

        except ValueError:
            print("El ID debe ser un número entero.")

    print()
    print("Producto actual:")
    print(f"ID: {producto[0]}")
    print(f"Nombre: {producto[1]}")
    print(f"Descripción: {producto[2]}")
    print(f"Precio: ${producto[3]:.2f} USD")
    print(f"Stock: {producto[4]}")
    print()

    while True:
        nombre = input("Nuevo nombre: ").strip()

        if nombre:
            break

        print("El nombre no puede estar vacío.")

    while True:
        descripcion = input("Nueva descripción: ").strip()

        if descripcion:
            break

        print("La descripción no puede estar vacía.")

    while True:
        try:
            precio = float(input("Nuevo precio (USD): "))

            if precio > 0:
                break

            print("El precio debe ser mayor que 0.")

        except ValueError:
            print("El precio debe ser un número válido.")

    while True:
        try:
            stock = int(input("Nuevo stock: "))

            if stock >= 0:
                break

            print("El stock no puede ser negativo.")

        except ValueError:
            print("El stock debe ser un número entero.")

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
