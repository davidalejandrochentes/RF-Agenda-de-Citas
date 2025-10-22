import reflex as rx
from app.states.state import BarberState


def _found_appointment_card() -> rx.Component:
    """Displays the details of the found appointment."""
    return rx.el.div(
        rx.el.h4(
            "Detalles de tu Cita",
            class_name="text-lg font-semibold text-gray-800",
        ),
        rx.el.div(class_name="my-4 border-t border-gray-200"),
        # Basic Details
        rx.el.div(
            rx.el.p(
                rx.el.span("Nombre: ", class_name="font-medium"),
                f"{BarberState.found_appointment['name']} {BarberState.found_appointment['last_name']}",
            ),
            rx.el.p(
                rx.el.span("Fecha: ", class_name="font-medium"),
                BarberState.found_appointment["date"],
            ),
            rx.el.p(
                rx.el.span("Hora: ", class_name="font-medium"),
                rx.moment(
                    BarberState.found_appointment["time"],
                    format="hh:mm A",
                    parse="HH:mm",
                ),
            ),
            rx.el.p(
                rx.el.span("Barbero: ", class_name="font-medium"),
                BarberState.found_appointment["barber"],
            ),
            class_name="flex flex-col gap-2 text-gray-700",
        ),
        # Services and Price Breakdown
        rx.el.div(
            rx.el.h4(
                "Servicios Seleccionados",
                class_name="font-semibold text-gray-800 mb-2 mt-4",
            ),
            rx.foreach(
                BarberState.found_appointment_services_details,
                lambda service: rx.el.div(
                    rx.el.p(service["name"]),
                    rx.el.p(f"${service['price']}"),
                    class_name="flex justify-between text-sm text-gray-600",
                ),
            ),
            rx.el.div(class_name="my-2 border-t border-gray-200"),
            rx.el.div(
                rx.el.p("Total a Pagar", class_name="font-bold"),
                rx.el.p(
                    f"${BarberState.found_appointment_total_price}",
                    class_name="font-bold",
                ),
                class_name="flex justify-between text-base text-gray-900 mt-2",
            ),
            class_name="p-4 bg-gray-50 rounded-lg mt-4",
        ),
        # Cancel Button
        rx.el.button(
            "Cancelar Cita",
            on_click=BarberState.cancel_found_appointment,
            class_name="w-full mt-6 py-2 bg-red-600 text-white rounded-lg font-semibold hover:bg-red-700 transition-all",
            type="button",
        ),
        class_name="mt-6 w-full",
    )


def _cancel_confirmation_dialog() -> rx.Component:
    """Alert dialog to confirm appointment cancellation."""
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("Confirmar Cancelación"),
            rx.alert_dialog.description(
                "¿Estás seguro de que quieres cancelar tu cita? Esta acción no se puede deshacer."
            ),
            rx.el.div(
                rx.alert_dialog.cancel(
                    rx.el.button(
                        "Volver",
                        class_name="px-4 py-2 bg-gray-200 rounded-lg",
                    )
                ),
                rx.alert_dialog.action(
                    rx.el.button(
                        "Sí, Cancelar Cita",
                        on_click=BarberState.confirm_cancellation,
                        class_name="px-4 py-2 bg-red-600 text-white rounded-lg",
                    )
                ),
                class_name="flex gap-3 mt-4 justify-end",
            ),
        ),
        open=BarberState.show_cancel_alert,
        on_open_change=BarberState.toggle_cancel_alert,
    )


def search_dialog() -> rx.Component:
    """The modal dialog for searching an appointment by booking code."""
    return rx.cond(
        BarberState.show_search_dialog,
        rx.el.div(
            _cancel_confirmation_dialog(),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Consultar mi Cita",
                            class_name="text-xl font-semibold text-gray-900",
                        ),
                        rx.el.button(
                            rx.icon("x", class_name="w-5 h-5"),
                            on_click=BarberState.close_search_dialog,
                            class_name="text-gray-400 hover:text-gray-600 p-1 rounded-full",
                        ),
                        class_name="flex justify-between items-center",
                    ),
                    rx.el.p(
                        "Ingrese su código de 4 dígitos para ver los detalles de su cita.",
                        class_name="text-sm text-gray-500 mt-1",
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.input(
                                name="booking_code",
                                placeholder="1234",
                                max_length=4,
                                class_name="flex-grow px-4 py-2 rounded-lg sm:rounded-r-none border border-gray-300 focus:ring-2 focus:ring-blue-500",
                            ),
                            rx.el.button(
                                "Buscar",
                                type="submit",
                                class_name="px-6 py-2 bg-blue-600 text-white rounded-lg sm:rounded-l-none font-medium hover:bg-blue-700",
                            ),
                            class_name="flex flex-col sm:flex-row gap-2 sm:gap-0 mt-4",
                        ),
                        on_submit=BarberState.find_appointment,
                        reset_on_submit=True,
                    ),
                    # Display search result or error
                    rx.cond(
                        BarberState.found_appointment,
                        _found_appointment_card(),
                        rx.cond(
                            BarberState.search_error_message != "",
                            rx.el.p(
                                BarberState.search_error_message,
                                class_name="text-red-500 text-sm mt-2 text-center",
                            ),
                        ),
                    ),
                    class_name="bg-white p-8 rounded-2xl shadow-2xl max-w-md w-full m-4 transition-all duration-300 animate-fade-in-up",
                ),
                class_name="fixed inset-0 z-50 flex items-center justify-center p-4",
            ),
            rx.el.div(
                on_click=BarberState.close_search_dialog,
                class_name="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm transition-opacity duration-300",
            ),
        ),
    )
