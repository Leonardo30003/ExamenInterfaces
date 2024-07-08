from model.respuesta_model import Respuesta
from conexion.conexion_pregunta import select_all

def select_all_preguntas_servicios():
    respuestas = select_all()
    print(respuestas)
    return respuestas
