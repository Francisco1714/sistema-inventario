from database.models import Producto
from web.crud import (
    crear_producto,
    obtener_producto_por_id,
    obtener_productos,
    obtener_productos_paginados,
    contar_productos,
    buscar_productos,
    actualizar_producto,
    eliminar_producto,
)


class TestCrearProducto:
    def test_crear_producto(self, db_session):
        producto = crear_producto(
            db_session,
            nombre="Mouse Gaming",
            descripcion="Mouse RGB",
            precio=49.99,
            stock=25
        )
        assert producto.id is not None
        assert producto.nombre == "Mouse Gaming"
        assert float(producto.precio) == 49.99
        assert producto.stock == 25

    def test_crear_producto_sin_descripcion(self, db_session):
        producto = crear_producto(
            db_session,
            nombre="Teclado",
            descripcion="",
            precio=29.99,
            stock=50
        )
        assert producto.descripcion == ""


class TestObtenerProducto:
    def test_obtener_por_id_existente(self, db_session, sample_product):
        resultado = obtener_producto_por_id(db_session, sample_product.id)
        assert resultado is not None
        assert resultado.nombre == "Laptop Test"

    def test_obtener_por_id_no_existente(self, db_session):
        resultado = obtener_producto_por_id(db_session, 999)
        assert resultado is None


class TestListarProductos:
    def test_listar_vacio(self, db_session):
        productos = obtener_productos(db_session)
        assert len(productos) == 0

    def test_listar_con_datos(self, db_session, sample_product):
        productos = obtener_productos(db_session)
        assert len(productos) == 1

    def test_contar_productos(self, db_session, sample_product):
        total = contar_productos(db_session)
        assert total == 1

    def test_paginacion(self, db_session):
        for i in range(15):
            crear_producto(db_session, f"Producto {i}", "", 10.0, 1)

        pagina1 = obtener_productos_paginados(db_session, page=1, per_page=12)
        pagina2 = obtener_productos_paginados(db_session, page=2, per_page=12)

        assert len(pagina1) == 12
        assert len(pagina2) == 3


class TestBuscarProductos:
    def test_buscar_por_nombre(self, db_session):
        crear_producto(db_session, "Laptop HP", "", 800.0, 5)
        crear_producto(db_session, "Mouse Logitech", "", 30.0, 20)

        resultados = buscar_productos(db_session, "Laptop")
        assert len(resultados) == 1
        assert resultados[0].nombre == "Laptop HP"

    def test_buscar_sin_resultados(self, db_session):
        crear_producto(db_session, "Laptop", "", 800.0, 5)
        resultados = buscar_productos(db_session, "XXXXX")
        assert len(resultados) == 0


class TestActualizarProducto:
    def test_actualizar_existente(self, db_session, sample_product):
        resultado = actualizar_producto(
            db_session,
            sample_product.id,
            "Laptop HP Actualizada",
            "Nueva descripcion",
            1299.99,
            15
        )
        assert resultado is not None
        assert resultado.nombre == "Laptop HP Actualizada"
        assert float(resultado.precio) == 1299.99

    def test_actualizar_no_existente(self, db_session):
        resultado = actualizar_producto(
            db_session, 999, "Test", "", 10.0, 1
        )
        assert resultado is None


class TestEliminarProducto:
    def test_eliminar_existente(self, db_session, sample_product):
        resultado = eliminar_producto(db_session, sample_product.id)
        assert resultado is True

        verificar = obtener_producto_por_id(db_session, sample_product.id)
        assert verificar is None

    def test_eliminar_no_existente(self, db_session):
        resultado = eliminar_producto(db_session, 999)
        assert resultado is False