from database.conexion import obtener_conexion

# --------------------------------------------------
# AGREGAR PRODUCTO
# --------------------------------------------------

def agregar_producto():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

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

# --------------------------------------------------
# LISTAR PRODUCTOS
# --------------------------------------------------

def listar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")

    productos = cursor.fetchall()

    if not productos:
        print("No hay productos registrados.")
    else:
        for id, nombre, descripcion, precio, stock in productos:
            print(f"ID: {id}")
            print(f"Nombre: {nombre}")
            print(f"Descripción: {descripcion}")
            print(f"Precio: ${precio:.2f} USD")
            print(f"Stock: {stock}")
            print()
    
    conexion.close()

# --------------------------------------------------
# MODIFICAR PRODUCTO
# --------------------------------------------------

def modificar_producto():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

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
        print(f"ID: {id}")
        print(f"Nombre: {nombre}")
        print(f"Descripción: {descripcion}")
        print(f"Precio: ${precio:.2f} USD")
        print(f"Stock: {stock}")
        print()

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

# --------------------------------------------------
# ELIMINAR PRODUCTO
# --------------------------------------------------

def eliminar_producto():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

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
        print(f"ID: {id}")
        print(f"Nombre: {nombre}")
        print(f"Descripción: {descripcion}")
        print(f"Precio: ${precio:.2f} USD")
        print(f"Stock: {stock}")
        print()

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