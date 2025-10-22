import reflex as rx
from app.components.appointment_form import appointment_form
from app.components.appointment_list import appointment_list
from app.components.layout import client_layout
from app.pages.login import login_page
from app.pages.admin import admin_page
from app.pages.info import info_page
from app.states.auth_state import AuthState
from app.states.state import BarberState
from app.states.db_service import init_db

init_db()


def index() -> rx.Component:
    return client_layout(
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.center(
                        rx.icon(
                            "scissors",
                            class_name="h-10 w-10 text-blue-600",
                        ),
                        rx.el.h1(
                            "Chente's Barber",
                            class_name="text-4xl font-extrabold tracking-tight text-gray-800",
                        ),
                        class_name="flex items-center",
                    ),
                    rx.el.p(
                        "Agenda tu cita de forma rápida y sencilla.",
                        class_name="text-lg text-gray-600 mt-2",
                    ),
                    class_name="text-center mb-10",
                ),
                appointment_form(),

                class_name="container mx-auto flex flex-col items-center p-4 md:p-8",
            ),
            # Add padding to prevent overlap with the fixed navbar
            class_name="min-h-screen bg-gray-50 font-['Inter'] pb-24 md:pt-20 md:pb-8",
            on_mount=BarberState.load_data,
        ),
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/", title="Chentes Barber")
app.add_page(
    login_page, route="/login", title="Admin Login"
)
app.add_page(
    admin_page,
    route="/admin",
    title="Panel de Administrador",
    on_load=[AuthState.check_login, BarberState.load_data],
)
app.add_page(info_page, route="/info", title="Información")