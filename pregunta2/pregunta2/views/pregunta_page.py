import asyncio
import reflex as rx
from ..conexion.conexion_pregunta import select_all
from ..model.pregunta_model import Pregunta

class PreguntasState(rx.State):
    preguntas: list[Pregunta] = []

    @rx.background
    async def get_all_preguntas(self):
        loop = asyncio.get_running_loop()
        preguntas_result = await loop.run_in_executor(None, select_all)
        async with self:
            self.preguntas = preguntas_result

@rx.page(route='/Preguntas', title='Preguntas', on_load=PreguntasState.get_all_preguntas)
def pregunta_page() -> rx.Component:
    return rx.flex(
        rx.heading("Preguntas", align="center"),
        tabla_preguntas(PreguntasState.preguntas),
    )

def tabla_preguntas(lista_preguntas: list[Pregunta]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('Descripción'),
                rx.table.column_header_cell('Fecha Inicio'),
                rx.table.column_header_cell('Fecha Fin'),
            )
        ),
        rx.table.body(
            rx.foreach(lista_preguntas, row_table)
        )
    )

def row_table(pregunta: Pregunta) -> rx.Component:
    return rx.table.row(
        rx.table.cell(pregunta.descripcion),
        rx.table.cell(str(pregunta.fecha_inicio)),
        rx.table.cell(str(pregunta.fecha_fin)),
        rx.table.cell(rx.hstack(
            rx.button('Editar'),
            rx.button('Eliminar')
        ))
    )
