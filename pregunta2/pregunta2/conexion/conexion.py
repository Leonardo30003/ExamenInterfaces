from sqlmodel import create_engine

def connect():
    usuario = "root"
    clave=""
    host="localhost"
    puerto="3306"
    engine= create_engine(f"mysql+pymysql://{usuario}:{clave}@localhost:3306/pregunta2")
    return engine

