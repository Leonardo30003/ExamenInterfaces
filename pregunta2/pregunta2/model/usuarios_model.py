from sqlmodel import Field, SQLModel
from typing import Optional
import reflex as rx

class Usuario(SQLModel, table=True):
    id_usuario: Optional[int] = Field(default=None, primary_key=True)
    nombre: str       
    correo: str       
    contrasenia: str
