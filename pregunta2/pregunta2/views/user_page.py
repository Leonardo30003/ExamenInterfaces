import reflex as rx
from ..conexion.conexion_usuarios import select_all
from ..servicios.usuarios_servicios import select_usuarios_by_nombre_servicios
from ..model.usuarios_model import Usuario

class UsuariosState(rx.State):
    users: list[Usuario] = []
    user_buscar: str = ""

    @rx.background
    async def get_all_users(self):
        async with self:
            self.users = await select_all()
    
    @rx.background
    async def get_usuarios_by_nombre(self):
        async with self:
            self.users = await select_usuarios_by_nombre_servicios(self.user_buscar)
    
    def buscar_on_change(self, value: str):
        self.user_buscar = value

@rx.page(route='/usuarios', title='Usuarios', on_load=UsuariosState.get_all_users)
def user_page() -> rx.Component:
    return rx.flex(
        rx.heading("Usuarios", align="center"),
        buscar_user_component(),
        tabla_usuarios(UsuariosState.users),
        justify='center',
        style={'margin-top': '30'}
    )

def tabla_usuarios(lista_usuarios: list[Usuario]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('Nombre'),
                rx.table.column_header_cell('Correo'),
                rx.table.column_header_cell('Contraseña'),
            )
        ),
        rx.table.body(
            rx.foreach(lista_usuarios, row_table)
        )
    )

def row_table(usuario: Usuario) -> rx.Component:
    return rx.table.row(
        rx.table.cell(usuario.nombre),
        rx.table.cell(usuario.correo),
        rx.table.cell(usuario.contrasenia),
        rx.table.cell(rx.hstack(
            rx.button('Eliminar')
        ))
    )

def buscar_user_component() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder='Ingrese el nombre', on_change=UsuariosState.buscar_on_change),
        rx.button('Buscar usuario', on_click=UsuariosState.get_usuarios_by_nombre),
        spacing=10  # Asegúrate de agregar un 'spacing' adecuado para mejor visualización.
    )
