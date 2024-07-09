from sqlmodel import SQLModel, create_engine

def connect():
    usuario = "root"
    clave=""
    host="localhost"
    puerto="3306"
    engine= create_engine(f"mysql+pymysql://{usuario}:{clave}@localhost:3306/respaldo2")
    SQLModel.metadata.create_all(engine)
    return engine

