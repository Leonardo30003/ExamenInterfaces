from sqlmodel import Field
from typing import Optional
import reflex as rx

class Respuesta(rx.Model, table=True):
    id_respuesta : Optional [int] = Field(default=None, primary_key=True)
    id_pregunta : int = Field(foreign_key="pregunta.id")      
    descripcion : str       
 