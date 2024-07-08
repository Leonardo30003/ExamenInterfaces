from sqlmodel import Field
from typing import Optional
import reflex as rx

class Partido(rx.Model, table=True):
    id_partido: Optional [int] = Field(default=None, primary_key=True)
    nombre: str       
    descripcion: str
 