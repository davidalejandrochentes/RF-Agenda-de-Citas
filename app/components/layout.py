import reflex as rx
from app.components.navbar import navbar
from app.components.search_modal import search_dialog


def client_layout(page_content: rx.Component) -> rx.Component:
    """A layout for all client-facing pages.
    Includes the navbar and the search dialog.
    """
    return rx.el.div(
        navbar(),
        page_content,
        search_dialog(),
    )
