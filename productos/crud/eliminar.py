from database.conexion import obtener_conexion

# --------------------------------------------------
# ELIMINAR PRODUCTO
# --------------------------------------------------

def eliminar_producto():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    print()
    print("================================")
    print("       ELIMINAR PRODUCTO")
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

    print("--------------------------------")

    id = input("ID del producto a eliminar: ")

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
    print("Producto seleccionado:")
    print(f"ID: {producto[0]}")
    print(f"Nombre: {producto[1]}")
    print(f"Descripción: {producto[2]}")
    print(f"Precio: ${producto[3]:.2f} USD")
    print(f"Stock: {producto[4]}")
    print()

    confirmacion = input(
        "¿Está seguro de eliminar este producto? (s/n): "
    )

    if confirmacion.lower() == "s":
        cursor.execute(
            """
            DELETE FROM productos
            WHERE id = ?
            """,
            (id,)
        )

        conexion.commit()

        print("Producto eliminado correctamente.")

    else:
        print("Operación cancelada.")

    conexion.close()

