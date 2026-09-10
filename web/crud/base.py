from database.conexion import get_session_local

def get_db():
    SessionFactory = get_session_local()
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()