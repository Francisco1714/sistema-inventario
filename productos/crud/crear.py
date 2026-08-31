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

    while True:
        nombre = input("Nombre del producto: ").strip()

        if nombre:
            break

        print("El nombre no puede estar vacío.")

    while True:
        descripcion = input("Descripción del producto: ").strip()

        if descripcion:
            break

        print("La descripción no puede estar vacía.")

    while True:
        try:
            precio = float(
                input("Precio del producto en USD: ")
            )

            if precio > 0:
                break

            print("El precio debe ser mayor que 0.")

        except ValueError:
            print("El precio debe ser un número válido.")

    while True:
        try:
            stock = int(
                input("Stock del producto: ")
            )

            if stock >= 0:
                break

            print("El stock no puede ser negativo.")

        except ValueError:
            print("El stock debe ser un número entero.")

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
