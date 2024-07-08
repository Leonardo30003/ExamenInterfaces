from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import date
import reflex as rx

class Pregunta(rx.Model, table=True):
    id_pregunta: Optional[int] = Field(default=None, primary_key=True)
    descripcion: str
    fecha_inicio: date
    fecha_fin: date
