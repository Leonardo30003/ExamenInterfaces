from model.voto_model import Voto
from pregunta2.conexion.conexion_usuarios import select_all

def select_all_usuarios_servicios():
    votos = select_all()
    print(votos)
    return votos
