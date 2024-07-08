import asyncio
import reflex as rx
from ..conexion.conexion_voto import select_all
from ..model.voto_model import Voto

class VotosState(rx.State):
    votos: list[Voto] = []

    @rx.background
    async def get_all_votos(self):
        loop = asyncio.get_running_loop()
        votos_result = await loop.run_in_executor(None, select_all)
        async with self:
            self.votos = votos_result

@rx.page(route='/Votos', title='Votos', on_load=VotosState.get_all_votos)
def voto_page() -> rx.Component:
    return rx.flex(
        rx.heading("Lista de Votos", align="center"),
        tabla_votos(VotosState.votos),
    )
def tabla_votos(lista_votos: list[Voto]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('ID Voto'),
                rx.table.column_header_cell('ID Usuario'),
                rx.table.column_header_cell('ID Respuesta'),
                rx.table.column_header_cell('Fecha'),
            )
        ),
        rx.table.body(
            rx.foreach(lista_votos, fila_voto)
        )
    )

def fila_voto(voto: Voto) -> rx.Component:
    return rx.table.row(
        rx.table.cell(str(voto.id_voto)),
        rx.table.cell(str(voto.id_usuario)),
        rx.table.cell(str(voto.id_respuesta)),
        rx.table.cell(str(voto.fecha)),
        rx.table.cell(rx.hstack(
            rx.button('Editar'),  # Implementar funcionalidad para editar
            rx.button('Eliminar')  # Implementar funcionalidad para eliminar
        ))
    )
