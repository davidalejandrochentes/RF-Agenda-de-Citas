import reflex as rx
from app.states.state import BarberState


def _nav_item(icon: str, href: str = "", on_click=None) -> rx.Component:
    """A reusable navigation item component."""
    if on_click:
        return rx.el.button(
            rx.icon(
                tag=icon,
                size=28,
                class_name="text-gray-500 group-hover:text-blue-600 transition-colors",
            ),
            on_click=on_click,
            class_name="flex items-center justify-center p-3 rounded-full hover:bg-gray-100 group",
        )
    return rx.link(
        rx.icon(
            tag=icon,
            size=28,
            class_name="text-gray-500 group-hover:text-blue-600 transition-colors",
        ),
        href=href,
        class_name="flex items-center justify-center p-3 rounded-full hover:bg-gray-100 group",
    )


def navbar() -> rx.Component:
    """The main navbar component for the application."""
    # This outer div is now just for positioning the bar.
    return rx.el.div(
        # This is the visible navbar element.
        rx.el.div(
            _nav_item(icon="calendar-days", href="/"),
            _nav_item(icon="search", on_click=BarberState.toggle_search_dialog),
            _nav_item(icon="info", href="/info"),
            # Styling for the bar itself: width, centering, background, etc.
            class_name=(
                "w-full max-w-md h-16 flex items-center justify-around "
                "bg-white/80 backdrop-blur-sm border border-gray-200 "
                "rounded-full shadow-lg"
            ),
        ),
        # Styling for the positioning container.
        class_name=(
            "fixed bottom-4 inset-x-4 z-50 flex justify-center "  # Mobile: at bottom with horizontal margin
            "md:top-4 md:bottom-auto md:inset-x-0"  # Desktop: reset to full-width for centering
        ),
    )
