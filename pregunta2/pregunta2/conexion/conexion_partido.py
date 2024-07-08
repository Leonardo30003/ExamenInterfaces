from ..model.partido_model import Partido
from ..conexion.conexion import connect
from sqlmodel import Session, select

def select_all():
    engine = connect()
    with Session(engine) as session:
        query = select(Partido)
        return session.exec(query).all()
