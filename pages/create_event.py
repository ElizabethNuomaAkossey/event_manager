from nicegui import ui
from components.navbar import show_navbar
from utils.api import base_url
import requests

# variable to store the image content
_event_image = None


# function to handle image upload
def _handle_image_upload(e):    # where e stands for event
    global _event_image
    _event_image = e.content


# function to handle the button "create event"
def _post_event(data, files):
    response = requests.post(f"{base_url}/events", data=data, files=files)
    print(response.status_code)
    json_data = response.json()
    print(json_data)



@ui.page("/create_event")
def show_create_event_page():
    show_navbar()
    with ui.element("section").classes("w-full"):
        with ui.card().classes("mx-[25%] flex flex-col items-center justify-center bg-gray-40"):
            ui.label("Create Event").classes("text-2xl font-bold py-2")

            with ui.element("div").classes("flex flex-col w-full py-2"):
                ui.label("Event Title").classes("text-xs text-left py-2")
                event_title = ui.input(placeholder="Enter the event title").props("flat outlined dense").classes("rounded-sm bg-white text-xs")
            
            with ui.element("div").classes("flex flex-col w-full"):
                ui.label("Event Venue").classes("text-xs text-left py-2") 
                event_venue = ui.input(placeholder="Enter the event venue").props("flat dense no-caps outlined").classes("bg-white")
            
            with ui.element("div").classes("flex  w-full flex-row justify-between py-2"):
                with ui.element("div").classes("flex flex-col w-[48%]"):
                    ui.label("Start time").classes("text-xs") 
                    event_start_time = ui.input().props("outlined type=time")
                    
                with ui.element("div").classes("flex flex-col w-[50%]"):
                    ui.label("End time").classes("text-xs text-left") 
                    event_end_time = ui.input().props("outlined type=time")
    
            with ui.element("div").classes("flex w-full flex-row justify-between"):
                with ui.element("div").classes("flex flex-col w-[48%]"):
                    ui.label("Start date").classes("text-xs py-2")
                    event_start_date = ui.input().props("outlined type=date") 
        
                with ui.element("div").classes("flex flex-col w-[50%]"):
                    ui.label("End date").classes("text-xs text-left py-2") 
                    event_end_date = ui.input().props("outlined type=date")
    
    with ui.element("div").classes("w-full my-10"):
        with ui.card().classes("items-center justify-center flex flex-col mx-[25%]"):
            ui.label("Event Description").classes("text-2xl font-bold")
            with ui.column().classes("flex flex-col w-full"):
                ui.label("Event Image")
                ui.upload(label="Upload image",auto_upload=True, on_upload=_handle_image_upload).props("outlined color=purple-600").classes("w-full")
            with ui.column().classes("flex flex-col w-full"):
                ui.label("Event Description")
                event_description = ui.textarea(placeholder="Type here...").props("outlined").classes("w-full")
    
            ui.button("Create event", on_click=lambda: _post_event(data={
                "title": event_title.value,
                "venue": event_venue.value,
                "start_time": event_start_time.value,
                "end_time": event_start_time,
                "start_date": event_start_date,
                "end_date": event_end_date},
                files={
                    "image":_event_image
                }
                )).props
            ("flat dense no-caps").classes("bg-purple-600 w-full text-white py-1")
                            