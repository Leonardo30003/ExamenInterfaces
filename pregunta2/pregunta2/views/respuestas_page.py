import asyncio
import reflex as rx
from ..conexion.conexion_respuesta import select_all
from ..model.respuesta_model import Respuesta

class RespuestasState(rx.State):
    respuestas: list[Respuesta] = []

    @rx.background
    async def get_all_respuestas(self):
        loop = asyncio.get_running_loop()
        respuestas_result = await loop.run_in_executor(None, select_all)
        async with self:
            self.respuestas = respuestas_result

@rx.page(route='/Respuestas', title='Respuestas', on_load=RespuestasState.get_all_respuestas)
def respuesta_page() -> rx.Component:
    return rx.flex(
        rx.heading("Respuestas", align="center"),
        tabla_respuestas(RespuestasState.respuestas),
    )

def tabla_respuestas(lista_respuestas: list[Respuesta]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('ID Respuesta'),
                rx.table.column_header_cell('ID Pregunta'),
                rx.table.column_header_cell('Descripción'),
            )
        ),
        rx.table.body(
            rx.foreach(lista_respuestas, fila_respuesta)
        )
    )

def fila_respuesta(respuesta: Respuesta) -> rx.Component:
    return rx.table.row(
        rx.table.cell(str(respuesta.id_respuesta)),
        rx.table.cell(str(respuesta.id_pregunta)),
        rx.table.cell(respuesta.descripcion),
        rx.table.cell(rx.hstack(
            rx.button('Editar'),  # Implementar funcionalidad para editar
            rx.button('Eliminar')  # Implementar funcionalidad para eliminar
        ))
    )
