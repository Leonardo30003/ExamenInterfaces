from model.partido_model import Partido
from conexion.conexion_pregunta import select_all

def select_all_preguntas_servicios():
    partido = select_all()
    print(partido)
    return partido
