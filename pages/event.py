from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer
from components.event_card import show_event_card
import requests

# api
from utils.api import base_url


@ui.page("/event")
def show_event_page():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    show_navbar()
    event_id = ui.context.client.request.query_params.get("id")
    response = requests.get(f"{base_url}/events/{event_id}")
    # print(response.status_code,response.content)
    if response.status_code == 200:
        json_data = response.json()
        e = json_data["data"]
        # print(json_data)
        with ui.element("main").classes("w-full h-screen px-5"):
            with ui.element("div").classes(
                f"bg-[url({e['image']})] bg-cover bg-center w-full h-full rounded-xl"
            ):
                with ui.column().classes("py-10 px-5"):
                        ui.button(text="< Back",on_click=lambda:ui.navigate.back()).props("dense flat no-caps").classes("bg-purple-600 text-white px-3")
                with ui.column().classes("text-white px-5 w-1/2 h-full items-start"
                    # " w-full font-bold items-start justify-center h-full px-10"
                ):
                    with ui.element("div").classes("text-5xl font-bold"):
                        ui.label(text=e["title"])
                        # ui.label("Jakarta")
                    with ui.element("div").classes("text-2xl font-semi-bold"):
                        ui.label("IIIT Sonepat")
                    with ui.element("div"):
                        ui.label(text=e["description"]).classes("whitespace-pre-line")
                    with ui.element("div").classes("flex flex-row"):
                        ui.icon(name="location_on",color="white",size="sm")
                        ui.label("view map")
                
        
        # with ui.element("section"):
        #     with

        # other events
        with ui.element("section").classes("w-full bg-transparent"):
            with ui.row().classes("w-full flex items-center px-20 py-10"):
                ui.label("Other events you may like").classes("text-xl font-bold text-black")
            with ui.grid(columns=3).classes("w-full px-20"):
                for i in range(6):
                    with ui.card():
                        ui.image("https://images.pexels.com/photos/1587927/pexels-photo-1587927.jpeg").classes("rounded-lg")
                        ui.label("BestSelller Book Bootcamp -write, Market & Publish Your Book -Lucknow").classes("text-lg")
                        ui.label("Saturdat, March 18, 9.30PM").classes("text-purple-600 text-sm")
                        with ui.row().classes("text-gray-600 space-x-1 gap-0"):
                            ui.label("ONLINE EVENT - ")
                            ui.label("Attend anywhere")
            with ui.element("div").classes("flex items-center justify-center py-10"):
                ui.button("Load More...", on_click=lambda: ui.navigate.to('/loadmore')).props("flat dense no-caps").classes("bg-purple-600 text-white shadow hover:bg-purple-500 px-4 py-2")

    elif response.status_code == 422:
        ui.label(text="Not found")
    show_footer()
