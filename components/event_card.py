from nicegui import ui


def show_event_card(e):
    with ui.card().on(type="click", handler=lambda:ui.navigate.to(f"/event?id={e['id']}")).classes("cursor-pointer"):
        ui.image(source=e["image"]).classes("rounded-lg")
        ui.label(text=e["title"]).classes("text-lg")
        with ui.row():
            ui.label(text=e["start_date"]).classes("text-purple-600 text-sm")
            ui.label(text=e["start_time"]).classes("text-purple-600 text-sm")
        with ui.row().classes("text-gray-600 space-x-1 gap-0"):
            ui.label(text=e["venue"])
