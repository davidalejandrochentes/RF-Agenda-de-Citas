import reflex as rx
from app.components.layout import client_layout
from app.states.state import BarberState


def faq_item(question: str, answer: str) -> rx.Component:
    """A reusable FAQ item with an accordion-style disclosure."""
    return rx.el.details(
        rx.el.summary(
            question,
            class_name="flex justify-between items-center font-semibold cursor-pointer p-4 hover:bg-gray-100 rounded-lg",
        ),
        rx.el.p(
            answer,
            class_name="p-4 pt-0 text-gray-600",
        ),
        class_name="border-b border-gray-200",
    )


def info_page() -> rx.Component:
    """A page to display information about the barbershop."""
    return client_layout(
        rx.el.main(
            rx.el.div(
                # Header
                rx.el.div(
                    rx.center(
                        rx.icon(
                            "info",
                            class_name="h-10 w-10 text-blue-600",
                        ),
                        rx.el.h1(
                            "Información",
                            class_name="text-4xl font-extrabold tracking-tight text-gray-800",
                        ),
                        class_name="flex items-center gap-4",
                    ),
                    rx.el.p(
                        "Aquí encontrarás todo lo que necesitas saber sobre Chente's Barber.",
                        class_name="text-lg text-gray-600 mt-2",
                    ),
                    class_name="text-center mb-12",
                ),
                # Main content grid
                rx.el.div(
                    # Left Column: Contact, Hours, Social
                    rx.el.div(
                        # Contact & Hours Card
                        rx.el.div(
                            rx.el.h2(
                                "Contacto y Horarios",
                                class_name="text-2xl font-bold text-gray-800 mb-4",
                            ),
                            rx.el.div(
                                rx.icon("phone", class_name="w-5 h-5 text-blue-500"),
                                rx.el.p("Teléfono: ", rx.el.span("+53 54214040", class_name="font-semibold")),
                                class_name="flex items-center gap-3 text-gray-700",
                            ),
                            rx.el.div(
                                rx.icon("map-pin", class_name="w-5 h-5 text-blue-500"),
                                rx.el.p("Dirección: ", rx.el.span("Roberto Amaran #64. PR/PR/CU", class_name="font-semibold")),
                                class_name="flex items-center gap-3 text-gray-700 mt-2",
                            ),
                            rx.el.div(
                                rx.icon("clock", class_name="w-5 h-5 text-blue-500"),
                                rx.el.p("Horario: ", rx.el.span("Lunes a Sábado de 9:00 AM a 10:00 PM", class_name="font-semibold")),
                                class_name="flex items-center gap-3 text-gray-700 mt-2",
                            ),
                            class_name="bg-white p-6 rounded-xl shadow-md border border-gray-100",
                        ),
                        # Social Media Card
                        rx.el.div(
                            rx.el.h2(
                                "Síguenos",
                                class_name="text-2xl font-bold text-gray-800 mb-4",
                            ),
                            rx.el.div(
                                rx.link(rx.icon("facebook", class_name="w-6 h-6"), href="#", is_external=True, class_name="text-gray-500 hover:text-blue-600"),
                                rx.link(rx.icon("instagram", class_name="w-6 h-6"), href="#", is_external=True, class_name="text-gray-500 hover:text-pink-500"),
                                rx.link(rx.icon("message-circle", class_name="w-6 h-6"), href="#", is_external=True, class_name="text-gray-500 hover:text-green-500"),
                                class_name="flex justify-start gap-8",
                            ),
                            class_name="bg-white p-6 rounded-xl shadow-md border border-gray-100 mt-8",
                        ),
                        # Map Placeholder
                        rx.el.div(
                            rx.el.h2(
                                "Ubicación",
                                class_name="text-2xl font-bold text-gray-800 mb-4",
                            ),
                            rx.el.iframe(
                                src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d862.0579897451511!2d-83.69370828295528!3d22.418250092458592!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e1!3m2!1ses!2scu!4v1761143513573!5m2!1ses!2scu",
                                class_name="rounded-lg w-full h-80 border-0",
                                allow_fullscreen=True,
                                loading="lazy",
                                referrerpolicy="no-referrer-when-downgrade"
                            ),
                            class_name="bg-white p-6 rounded-xl shadow-md border border-gray-100 mt-8",
                        ),
                        class_name="flex flex-col",
                    ),
                    # Right Column: Services & Barbers
                    rx.el.div(
                        # Services Card
                        rx.el.div(
                            rx.el.h2(
                                "Nuestros Servicios",
                                class_name="text-2xl font-bold text-gray-800 mb-4",
                            ),
                            rx.cond(
                                BarberState.services.length() > 0,
                                rx.el.div(
                                    rx.foreach(
                                        BarberState.services,
                                        lambda service: rx.el.div(
                                            rx.el.p(
                                                service["name"],
                                                class_name="font-semibold text-gray-700",
                                            ),
                                            rx.el.p(
                                                f"${service['price']}",
                                                class_name="font-bold text-blue-600",
                                            ),
                                            class_name="flex justify-between items-center p-4 bg-gray-50 rounded-lg",
                                        ),
                                    ),
                                    class_name="flex flex-col gap-3",
                                ),
                                rx.el.p("No hay servicios disponibles en este momento.", class_name="text-gray-500"),
                            ),
                            class_name="bg-white p-6 rounded-xl mt-8 shadow-md border border-gray-100",
                        ),
                    ),
                ),
                # FAQ Section
                rx.el.div(
                    rx.el.h2(
                        "Preguntas Frecuentes",
                        class_name="text-3xl font-bold text-gray-800 mb-6 text-center",
                    ),
                    rx.el.div(
                        faq_item(
                            "¿Cómo puedo reservar una cita?",
                            "Puedes reservar fácilmente a través de nuestra página web. Solo tienes que seleccionar el servicio, el barbero de tu preferencia, la fecha y la hora disponible que mejor te convenga."
                        ),
                        faq_item(
                            "¿Puedo cancelar o modificar mi cita?",
                            "Sí, por supuesto. Entendemos que los imprevistos suceden. Puedes cancelar o modificar tu cita directamente desde la Web"
                        ),
                        faq_item(
                            "¿Es obligatorio reservar o aceptan walk-ins (clientes sin cita)?",
                            "Aceptamos clientes sin cita según la disponibilidad de nuestros barberos, pero no podemos garantizarla. Para asegurarte un hueco y evitar esperas, la reserva online es siempre la opción más recomendable."
                        ),
                        faq_item(
                            "¿Ofrecen servicios a domicilio?",
                            "Por el momento, todos nuestros servicios se realizan exclusivamente en nuestra barbería para garantizar la máxima calidad y comodidad."
                        ),
                        faq_item(
                            "¿Qué pasa si llego tarde a mi cita?",
                            "Valoramos el tiempo de todos nuestros clientes. Si llegas con más de [ej: 10 minutos] de retraso, es posible que necesitemos acortar tu servicio o, en casos de mucha demanda, reprogramar tu cita para no afectar las reservas siguientes."
                        ),
                        faq_item(
                            "¿Tengo que dar propina?",
                            "La propina es un gesto opcional y siempre apreciado por nuestro equipo si estás satisfecho con el servicio. No es obligatoria en absoluto."
                        ),
                        faq_item(
                            "¿Qué métodos de pago aceptan?",
                            "Aceptamos efectivo y transferencias bancarias."
                        ),
                        faq_item(
                            "¿Necesito lavarme el pelo antes de venir?",
                            "No es necesario, pero llega con el cabello seco y preferiblemente sin productos (como geles o ceras) para que el barbero pueda evaluar mejor tu cabello natural y trabajar con él."
                        ),
                        faq_item(
                            "¿Ofrecen asesoramiento de estilo?",
                            "Por supuesto. Nuestros barberos están formados para asesorarte sobre el corte y estilo que mejor se adapte a la forma de tu cara, tipo de cabello y estilo de vida. ¡Solo tienes que pedirlo!"
                        ),
                        faq_item(
                            "¿Quién desarrolló esta aplicación y cómo puedo obtener una versión personalizada para mí?",
                            "Esta aplicación fue desarrollada por David Alejandro Chentes. Puedes obtener tu propia versión personalizada por tan solo 1000 CUP al mes. Para más información o para solicitar la tuya, puedes contactarlo directamente al +53 54214040."
                        ),
                        class_name="bg-white rounded-xl shadow-md border border-gray-100 overflow-hidden",
                    ),
                    class_name="w-full max-w-4xl mt-12",
                ),
                class_name="container mx-auto flex flex-col items-center p-4 md:p-8",
            ),
            class_name="min-h-screen bg-gray-50 font-['Inter'] pb-24 md:pt-20 md:pb-8",
            on_mount=BarberState.load_data,
        ),
    )
