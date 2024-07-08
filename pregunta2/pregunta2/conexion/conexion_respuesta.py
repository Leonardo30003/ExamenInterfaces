from ..model.respuesta_model import Respuesta
from ..conexion.conexion import connect
from sqlmodel import Session, select

def select_all():
    engine = connect()
    with Session(engine) as session:
        query = select(Respuesta)
        return session.exec(query).all()
