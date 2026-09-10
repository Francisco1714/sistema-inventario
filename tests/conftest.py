import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from app import app as flask_app
from database.models import Base
from database.conexion import get_db

@pytest.fixture(scope="session")
def app():
    flask_app.config["TESTING"] = True
    flask_app.config["DATABASE_URL"] = "sqlite:///:memory:"
    yield flask_app

@pytest.fixture(scope="function")
def db_session(app):
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    yield db

    db.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(app, db_session):
    import web.crud.base as crud_base
    import web.api.routes.listar as listar_mod
    import web.api.routes.obtener as obtener_mod
    import web.api.routes.crear as crear_mod
    import web.api.routes.put as put_mod
    import web.api.routes.patch as patch_mod
    import web.api.routes.eliminar as eliminar_mod

    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    mods = [crud_base, listar_mod, obtener_mod, crear_mod, put_mod, patch_mod, eliminar_mod]
    originals = [m.get_db for m in mods]

    for m in mods:
        m.get_db = override_get_db

    with app.test_client() as client:
        yield client

    for m, orig in zip(mods, originals):
        m.get_db = orig

@pytest.fixture(scope="function")
def sample_product(db_session):
    from database.models import Producto

    producto = Producto(
        nombre="Laptop Test",
        descripcion="Laptop de prueba",
        precio=999.9,
        stock=10
    )
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)
    return producto
