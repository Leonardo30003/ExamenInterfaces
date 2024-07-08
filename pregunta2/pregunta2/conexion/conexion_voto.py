from ..model.voto_model import Voto
from ..conexion.conexion import connect
from sqlmodel import Session, select

def select_all():
    engine = connect()
    with Session(engine) as session:
        query = select(Voto)
        return session.exec(query).all()