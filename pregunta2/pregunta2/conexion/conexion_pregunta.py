from ..model.pregunta_model import Pregunta 
from ..conexion.conexion import connect
from sqlmodel import Session, select

def select_all():
    engine = connect()
    with Session(engine) as session:
        query = select(Pregunta)
        return session.exec(query).all()
