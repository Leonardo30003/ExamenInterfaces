from ..model.usuarios_model import Usuario
from pregunta2.conexion.conexion_usuarios import select_all, select_usuarios_by_nombre

def select_all_usuarios_servicios():
    usuarios = select_all()
    print(usuarios)
    return usuarios

def select_usuarios_by_nombre_servicios(nombre:str):
    if(len(nombre) !=0):
        return select_usuarios_by_nombre(nombre)
    else:
        return select_all()