import asyncio
import reflex as rx
from ..conexion.conexion_partido import select_all
from ..model.partido_model import Partido  # Asumiendo que este es el modelo de Partido

class PartidosState(rx.State):
    partidos: list[Partido] = []

    @rx.background
    async def get_all_partidos(self):
        loop = asyncio.get_running_loop()
        partidos_result = await loop.run_in_executor(None, select_all)
        async with self:  # Modificar el estado dentro de este contexto
            self.partidos = partidos_result

@rx.page(route='/Partidos', title='Partidos', on_load=PartidosState.get_all_partidos)
def partido_page() -> rx.Component:
    return rx.flex(
        rx.heading("Lista de Partidos", align="center"),
        tabla_partidos(PartidosState.partidos),
    )

def tabla_partidos(lista_partidos: list[Partido]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('Nombre'),
                rx.table.column_header_cell('Descripción'),
            )
        ),
        rx.table.body(
            rx.foreach(lista_partidos, row_partido)
        )
    )

def row_partido(partido: Partido) -> rx.Component:
    return rx.table.row(
        rx.table.cell(partido.nombre),
        rx.table.cell(partido.descripcion),
        rx.table.cell(rx.hstack(
            rx.button('Editar'),
            rx.button('Eliminar')
        ))
    )

