import reflex as rx
from app.states.state import BarberState
from app.components.scheduler import scheduler


def _form_field(
    label: str,
    name: str,
    placeholder: str,
    field_type: str = "text",
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            html_for=name,
            class_name="block text-sm font-medium text-gray-700 mb-1",
        ),
        rx.el.input(
            id=name,
            name=name,
            type=field_type,
            placeholder=placeholder,
            required=True,
            class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors",
        ),
        class_name="w-full",
    )


def _service_selection_field() -> rx.Component:
    """Creates a field for selecting multiple services using interactive cards."""
    return rx.el.div(
        rx.el.label(
            "Servicios",
            class_name="block text-sm font-medium text-gray-700 mb-2",
        ),
        rx.el.div(
            rx.foreach(
                BarberState.services,
                lambda service: rx.el.button(
                    rx.el.div(
                        rx.el.p(
                            service["name"],
                            class_name="font-semibold",
                        ),
                        rx.el.p(
                            f"${service['price']}",
                            class_name="text-sm",
                        ),
                        class_name="flex flex-col items-center",
                    ),
                    on_click=lambda: BarberState.toggle_service(
                        service["name"]
                    ),
                    class_name=rx.cond(
                        BarberState.selected_services.contains(
                            service["name"]
                        ),
                        "w-full p-4 rounded-lg text-center transition-all bg-blue-600 text-white border-blue-700 shadow-md",
                        "w-full p-4 rounded-lg text-center transition-all bg-white hover:bg-gray-50 border-gray-200",
                    ),
                    type="button",
                ),
            ),
            class_name="grid grid-cols-2 sm:grid-cols-3 gap-3 mt-1",
        ),
        class_name="w-full",
    )


def confirmation_dialog() -> rx.Component:
    return rx.cond(
        BarberState.show_confirm_dialog,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Confirmar Cita",
                        class_name="text-xl font-semibold text-gray-900",
                    ),
                    rx.el.p(
                        "Por favor, revise los detalles de su cita antes de confirmar.",
                        class_name="text-sm text-gray-500 mt-1",
                    ),
                    rx.el.div(
                        class_name="my-4 border-t border-gray-200"
                    ),
                    # Booking Code Display
                    rx.el.div(
                        rx.el.h4(
                            "Guarde su Código de Reserva",
                            class_name="font-semibold text-gray-800 mb-2",
                        ),
                        rx.el.div(
                            rx.icon("info", class_name="w-5 h-5 text-blue-500"),
                            rx.el.p(
                                "Use este código para consultar o gestionar su cita más tarde. Por favor, guárdelo en un lugar seguro.",
                                class_name="text-sm text-gray-600",
                            ),
                            class_name="flex items-center gap-2 p-3 bg-blue-50 rounded-lg",
                        ),
                        rx.el.p(
                            BarberState.pending_booking_code,
                            class_name="text-4xl font-bold tracking-widest text-center text-blue-600 my-4 p-3 bg-gray-100 rounded-lg",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.p(
                            rx.el.span(
                                "Nombre: ",
                                class_name="font-semibold",
                            ),
                            BarberState.pending_appointment_data.get(
                                "name", ""
                            ),
                            " ",
                            BarberState.pending_appointment_data.get(
                                "last_name", ""
                            ),
                        ),
                        rx.el.p(
                            rx.el.span(
                                "Teléfono: ",
                                class_name="font-semibold",
                            ),
                            BarberState.pending_appointment_data.get(
                                "phone", ""
                            ),
                        ),
                        rx.el.p(
                            rx.el.span(
                                "Barbero: ",
                                class_name="font-semibold",
                            ),
                            BarberState.selected_barber,
                        ),
                        rx.el.p(
                            rx.el.span(
                                "Fecha: ",
                                class_name="font-semibold",
                            ),
                            BarberState.selected_date,
                        ),
                        rx.el.p(
                            rx.el.span(
                                "Hora: ",
                                class_name="font-semibold",
                            ),
                            rx.moment(
                                BarberState.selected_time,
                                format="hh:mm A",
                                parse="HH:mm",
                            ),
                        ),
                        class_name="flex flex-col gap-2 my-4 text-base text-gray-700",
                    ),
                    # Services and Price Breakdown
                    rx.el.div(
                        rx.el.h4(
                            "Servicios Seleccionados",
                            class_name="font-semibold text-gray-800 mb-2",
                        ),
                        rx.foreach(
                            BarberState.selected_services_details,
                            lambda service: rx.el.div(
                                rx.el.p(service["name"]),
                                rx.el.p(f"${service['price']}"),
                                class_name="flex justify-between text-sm text-gray-600",
                            ),
                        ),
                        rx.el.div(
                            class_name="my-2 border-t border-gray-200"
                        ),
                        rx.el.div(
                            rx.el.p("Total a Pagar", class_name="font-bold"),
                            rx.el.p(
                                f"${BarberState.total_price}",
                                class_name="font-bold",
                            ),
                            class_name="flex justify-between text-base text-gray-900 mt-2",
                        ),
                        class_name="p-4 bg-gray-50 rounded-lg",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Cancelar",
                            on_click=BarberState.cancel_confirmation,
                            class_name="w-full sm:w-auto px-6 py-2 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 font-medium transition-all duration-300 transform hover:-translate-y-1",
                            type="button",
                        ),
                        rx.el.button(
                            "Confirmar Cita",
                            on_click=BarberState.confirm_appointment,
                            class_name="w-full sm:w-auto px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium transition-all duration-300 transform hover:-translate-y-1",
                            type="button",
                        ),
                        class_name="flex flex-col sm:flex-row justify-end gap-3 mt-6",
                    ),
                    class_name="bg-white p-8 rounded-2xl shadow-2xl max-w-md w-full m-4 transition-all duration-300 animate-fade-in-up",
                ),
                class_name="fixed inset-0 z-50 flex items-center justify-center p-4",
            ),
            rx.el.div(
                on_click=BarberState.cancel_confirmation,
                class_name="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm transition-opacity duration-300",
            ),
        ),
    )


def appointment_form() -> rx.Component:
    return rx.el.div(
        confirmation_dialog(),
        rx.el.h2(
            "Agendar Nueva Cita",
            class_name="text-2xl font-bold text-gray-800 mb-6 text-center",
        ),
        rx.el.form(
            rx.el.div(
                scheduler(),
                rx.cond(
                    BarberState.selected_time != "",
                    rx.el.div(
                        rx.el.div(
                            class_name="w-full border-t border-gray-200 my-6"
                        ),
                        _form_field(
                            "Nombre",
                            "name",
                            "Ej: Juan",
                        ),
                        _form_field(
                            "Apellido",
                            "last_name",
                            "Ej: Pérez",
                        ),
                        _form_field(
                            "Número de Teléfono",
                            "phone",
                            "Ej: 55 1234 5678",
                            field_type="tel",
                        ),
                        _service_selection_field(),
                        rx.el.button(
                            "Agendar Cita",
                            type="submit",
                            class_name="w-full mt-4 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition-all duration-200 shadow-md hover:shadow-lg transform hover:-translate-y-1",
                        ),
                        class_name="flex flex-col items-center gap-4 w-full",
                    ),
                    rx.el.div(),
                ),
                class_name="flex flex-col items-center gap-4",
            ),
            on_submit=BarberState.prepare_appointment,
            reset_on_submit=False,
            class_name="w-full",
        ),
        class_name="bg-white p-8 rounded-2xl shadow-lg border border-gray-100 w-full max-w-lg transition-shadow duration-300 hover:shadow-2xl animate-fade-in-up",
    )
