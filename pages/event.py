from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer


@ui.page("/event")
def show_event_page():
    show_navbar()
    ui.label("Welcome to Event.py")
    show_footer()
