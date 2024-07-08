from datetime import date
from sqlmodel import Field
from typing import Optional
import reflex as rx

class Voto(rx.Model, table=True):
    id_voto : Optional [int] = Field(default=None, primary_key=True)
    id_usuario : int = Field(foreign_key="usuario.id")      
    id_respuesta : int = Field(foreign_key="respuesta.id")
    fecha: date      
 