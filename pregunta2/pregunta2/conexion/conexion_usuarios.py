from ..model.usuarios_model import Usuario
from ..conexion.conexion import connect
from sqlmodel import Session, select

def select_all():
    engine = connect()
    with Session(engine) as session:
        query = select(Usuario)
        return session.exec(query).all()
    
def select_usuarios_by_nombre(nombre:str):
    engine = connect()
    with Session(engine) as session:
        query = select(Usuario).where(Usuario.nombre == nombre)
        return session.exec(query).all()