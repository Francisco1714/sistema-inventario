from productos.crud import agregar_producto, listar_productos, modificar_producto, eliminar_producto    

# --------------------------------------------------
# MENÚ PRINCIPAL
# --------------------------------------------------

def menu():
    while True:

        print()
        print("================================")
        print("       SISTEMA DE INVENTARIO")
        print("================================")
        print()
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        print()

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":
                agregar_producto()

            case "2":
                listar_productos()

            case "3":
                modificar_producto()

            case "4":
                eliminar_producto()

            case "5":
                print("Saliendo del sistema...")
                break

            case _:
                print("Opción no válida.")