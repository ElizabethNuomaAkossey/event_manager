from nicegui import ui
from components.navbar import show_navbar

@ui.page("/create_event")
def show_create_event_page():
    show_navbar()
    with ui.element("section").classes("w-full"):
        with ui.card().classes("mx-[25%] flex flex-col items-center justify-center bg-gray-40"):
            ui.label("Create Event").classes("text-2xl font-bold py-2")
            with ui.element("div").classes("flex flex-col w-full py-2"):
                ui.label("Event Title").classes("text-xs text-left py-2")
                ui.input(placeholder="Enter the event title").props("flat outlined dense").classes("rounded-sm bg-white text-xs")
            with ui.element("div").classes("flex flex-col w-full"):
                ui.label("Event Venue").classes("text-xs text-left py-2") 
                ui.input(placeholder="Enter the event venue").props("flat dense no-caps outlined").classes("bg-white")
            with ui.element("div").classes("flex  w-full flex-row justify-between py-2"):
                with ui.element("div").classes("flex flex-col w-[48%]"):
                    ui.label("Start time").classes("text-xs") 
                    with ui.input().classes("bg-white").props("outlined") as time:
                        with ui.menu().props('no-parent-event') as menu:
                            with ui.time().bind_value(time):
                                with ui.row().classes('justify-end'):
                                    ui.button('Close', on_click=menu.close).props('flat')
                        with time.add_slot('append'):
                            ui.icon('access_time').on('click', menu.open).classes('cursor-pointer')
                with ui.element("div").classes("flex flex-col w-[50%]"):
                    ui.label("End time").classes("text-xs text-left") 
                    with ui.input().props("outlined") as time:
                        with ui.menu().props('no-parent-event') as menu:
                            with ui.time().bind_value(time):
                                with ui.row().classes('justify-end'):
                                    ui.button('Close', on_click=menu.close).props('flat')
                        with time.add_slot('append'):
                            ui.icon('access_time').on('click', menu.open).classes('cursor-pointer')
            with ui.element("div").classes("flex w-full flex-row justify-between"):
                with ui.element("div").classes("flex flex-col w-[48%]"):
                    ui.label("Start date").classes("text-xs py-2") 
                    with ui.input().props("outlined") as date:
                        with ui.menu().props('no-parent-event') as menu:
                            with ui.date().bind_value(date):
                                with ui.row().classes('justify-end'):
                                    ui.button('Close', on_click=menu.close).props('flat')
                        with date.add_slot('append'):
                            ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
                with ui.element("div").classes("flex flex-col w-[50%]"):
                    ui.label("End date").classes("text-xs text-left py-2") 
                    with ui.input().props('outlined') as date:
                        with ui.menu().props('no-parent-event') as menu:
                            with ui.date().bind_value(date):
                                with ui.row().classes('justify-end'):
                                    ui.button('Close', on_click=menu.close)
                        with date.add_slot('append'):
                            ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')  
    
    with ui.element("div").classes("w-full my-10"):
        with ui.card().classes("items-center justify-center flex flex-col mx-[25%]"):
            ui.label("Event Description").classes("text-2xl font-bold")
            with ui.column().classes("flex flex-col w-full"):
                ui.label("Event Image")
                ui.upload(multiple=True, label="Upload image").props("outlined").classes("w-full")
            with ui.column().classes("flex flex-col w-full"):
                ui.label("Event Description")
                ui.textarea(placeholder="Type here...").props("outlined").classes("w-full")
    
            ui.button("Create event").props("flat dense no-caps").classes("bg-purple-600 w-full text-white py-1")
                            