from nicegui import ui
from components.navbar import show_navbar

@ui.page("/create_event")
def show_create_event_page():
    show_navbar()
    with ui.element("section").classes("w-full"):
        with ui.element("div").classes("mx-[20%] flex flex-col items-center justify-center"):
            ui.label("Create Event").classes("text-3xl font-bold py-5")
            with ui.element("div").classes("flex flex-col w-full py-2"):
                ui.label("Event Title").classes("text-xs text-left py-2")
                ui.input(placeholder="Enter the event title").props("flat outlined dense").classes("rounded-sm bg-white text-xs")
            with ui.element("div").classes("flex flex-col w-full"):
                ui.label("Event Venue").classes("text-xs text-left py-2") 
                ui.input(placeholder="Enter the event venue").props("flat dense  no-caps outlined") 
            with ui.element("div").classes("flex  w-full flex-row justify-between py-2"):
                with ui.element("div").classes("flex flex-col w-[48%]"):
                    ui.label("Start time").classes("text-xs") 
                    ui.input(placeholder="Enter the starting time of the event").props("dense no-caps outlined")
                with ui.element("div").classes("flex flex-col w-[50%]"):
                    ui.label("End time").classes("text-xs text-left") 
                    ui.input(placeholder="Enter the ending time of the event").props("dense no-caps outlined") 
            with ui.element("div").classes("flex w-full flex-row justify-between"):
                with ui.element("div").classes("flex flex-col w-[48%]"):
                    ui.label("Start date").classes("text-xs py-2") 
                    with ui.input('Date') as date:
                        with ui.menu().props('no-parent-event') as menu:
                            with ui.date().bind_value(date):
                                with ui.row().classes('justify-end'):
                                    ui.button('Close', on_click=menu.close).props('flat')
                        with date.add_slot('append'):
                            ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
                with ui.element("div").classes("flex flex-col w-[50%]"):
                    ui.label("End date").classes("text-xs text-left py-2") 
                    with ui.input('Date') as date:
                        with ui.menu().props('no-parent-event') as menu:
                            with ui.date().bind_value(date):
                                with ui.row().classes('justify-end'):
                                    ui.button('Close', on_click=menu.close).props('flat')
                        with date.add_slot('append'):
                            ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')  
        
                            