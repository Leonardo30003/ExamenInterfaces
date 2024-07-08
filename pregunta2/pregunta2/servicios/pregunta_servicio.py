from model.pregunta_model import Pregunta
from conexion.conexion_pregunta import select_all

def select_all_preguntas_servicios():
    preguntas = select_all()
    print(preguntas)
    return preguntas
