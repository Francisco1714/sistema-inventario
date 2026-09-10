from database.conexion import get_session_local as SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
