from database.tablas import crear_tabla_productos
from cli.menu import menu

# --------------------------------------------------
# INICIAR APLICACIÓN
# --------------------------------------------------

if __name__ == "__main__":
    crear_tabla_productos()
    menu()