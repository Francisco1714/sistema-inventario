from database.conexion import obtener_conexion

# --------------------------------------------------
# LISTAR PRODUCTOS
# --------------------------------------------------

def listar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    print()
    print("================================")
    print("          INVENTARIO")
    print("================================")
    print()

    cursor.execute("SELECT * FROM productos")

    productos = cursor.fetchall()

    if not productos:
        print("No hay productos registrados.")
    else:
        for id, nombre, descripcion, precio, stock in productos:
            print("--------------------------------")
            print(f"ID: {id}")
            print(f"Nombre: {nombre}")
            print(f"Descripción: {descripcion}")
            print(f"Precio: ${precio:.2f} USD")
            print(f"Stock: {stock}")

        print("--------------------------------")
        print(f"Total de productos: {len(productos)}")
    conexion.close()
