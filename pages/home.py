from nicegui import ui,app
from components.footer import show_footer
from components.navbar import show_navbar
from components.event_card import show_event_card

# for api
import requests
from utils.api import base_url



@ui.page("/")
def show_home_page():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    ui.query('#app').classes("m-0 p-o gap-0")
    show_navbar()
    with ui.element("main").classes("w-full h-screen"):
        with ui.element("div").classes("bg-[url('https://images.pexels.com/photos/2774556/pexels-photo-2774556.jpeg')] bg-cover bg-center w-full h-[80%] flex flex-col justify-center rounded-xl items-center relative"):
            with ui.column().classes("text-white md:text-7xl font-bold flex justify-center items-center"):
                ui.label("MADE FOR THOSE")
                ui.label("WHO DO")
                
                # --- Search filter box ---
            with ui.element("div").classes(
                "absolute bottom-[-12%] left-1/2 transform -translate-x-1/2 flex space-x-4 px-20 gap-8 flex justify-center py-6 rounded-2xl shadow-xl w-[93%]").style("background-color: navy;"):
                # Looking for
                with ui.element("div").classes("flex flex-col text-white"):
                    ui.label("Looking for").classes("text-sm mb-1")
                    ui.select(["Conference", "Workshop", "Meetup"], value="Conference").classes("bg-white text-black rounded-md px-4 w-72")

            #     # Location
                with ui.element("div").classes("flex flex-col text-white"):
                    ui.label("Location").classes("text-sm mb-1")
                    ui.select(["New York", "London", "Berlin"], value="New York") \
                        .classes("bg-white text-black rounded-md px-4 w-72")

                # When
                with ui.element("div").classes("flex flex-col text-white"):
                    ui.label("When").classes("text-sm mb-1")
                    ui.input("Choose date and time") \
                        .classes("bg-white text-black rounded-md px-4 w-72")

                # Search button
                ui.button("").props("icon=search dense flat no-caps").classes(
                    "bg-purple-600  bg:hover-purple-200 text-white  justify-center rounded-md hover:bg-purple-500 py-5 px-5 gap-0"
                )
    # Upcoming Events
    with ui.element("section").classes("w-full bg-transparent gap-0"):
        with ui.row().classes("w-full flex flex-row justify-between items-center px-20 py-10"):
            with ui.row().classes("gap-0 space-x-2"):
                ui.label("Upcoming").classes("text-2xl font-bold text-black")
                ui.label("Events").classes("text-2xl font-bold text-purple-600")
            with ui.row():
                weekdays = ["Weekdays","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sundays"]
                ui.select(label="", value="Weekdays", options=weekdays).props('dense outlined')
                event_type = ["Event type","Indoors","Outdoors"]
                ui.select(label="", value="Event type", options=event_type).props('dense outlined')
                any_category = ["Any category", "Any Category"]
                ui.select(label="", value="Any category", options=any_category).props('dense outlined')
        with ui.grid().classes("grid grid-cols-1 md:grid-cols-3 w-full md:px-20"):
            response = requests.get(f"{base_url}/events?limit=6")
            # print(response.status_code, response.content) -to check if there are any errors
            json_data = response.json()
            for e in json_data["data"]:
                show_event_card(e)
        with ui.element("div").classes("flex items-center justify-center py-10"):
            ui.button("Load More...", on_click=lambda: ui.navigate.to('/loadmore')).props("flat dense no-caps").classes("bg-purple-600 text-white shadow hover:bg-purple-500 px-4 py-2")

    # Make your own events
    with ui.column().classes("w-full mt-20").style("background-color: navy;"):
        with ui.grid(columns=2).classes("w-full h-full"):
            with ui.column().classes("relative"):
                ui.image("/assets/make_your_own_event.png").classes(" absolute bottom-0")

            with ui.column().classes("items-center mt-20"):
                ui.label("Make Your Own Event").classes("text-4xl font-bold text-white")
                ui.label("Create Your Own Experience").classes("text-xl text-white")
                ui.button("Create Event").props("flat dense no-caps").classes("bg-blue text-white text-bold")


            

    # Join these brands
    with ui.element("section").classes("w-full bg-transparent py-5"):
        with ui.row().classes("w-full flex flex-col justify-between items-center"):
            with ui.row().classes("gap-0 space-x-2"):
                ui.label("Join these").classes("text-2xl font-bold text-black")
                ui.label("brands").classes("text-2xl font-bold text-purple-600")
            with ui.element("div").classes("font-medium"):
                ui.label("We've had the pleasure of working with industry-defining brands. \nThese are just some of them.").classes("whitespace-pre-line text-center")
        with ui.row().classes("justify-center w-full items-center flex-wrap gap-9 bg-gray-50 rounded px-20 py-5"):
            logos = [
                "/assets/spotify.png",
                "/assets/Google.png",
                "/assets/stripe.png",
                "/assets/Youtube.png",
                "/assets/microsoft.png",
                "/assets/Medium.png",
                "/assets/zoom.png",
                "/assets/uber.png",
                "/assets/grab.png",
            ]

            for logo in logos:
                ui.image(logo).classes(
                    "max-h-14 max-w-[150px] object-contain"
                )


    # Trending colleges
    with ui.element("section").classes("w-full bg-transparent"):
        with ui.row().classes("w-full flex flex-row justify-between items-center px-20 py-10"):
            with ui.row().classes("gap-0 space-x-2"):
                ui.label("Trending").classes("text-2xl font-bold text-black")
                ui.label("Colleges").classes("text-2xl font-bold text-purple-600")
        with ui.grid().classes("grid grid-cols-1 md:grid-cols-3 w-full px-20"):
            for i in range(3):
                with ui.card().classes("m-0 p-0"):
                    ui.image("https://images.pexels.com/photos/207692/pexels-photo-207692.jpeg").classes("rounded-lg")
                    ui.label("Havard Univerity").classes("text-lg font-bold px-5")
                    with ui.row().classes("space-x-1 flex justify-between items-center text-xs font-medium py-2 px-5 w-full"):
                        ui.label("Cambridge, Massachusetts, UK")
                        ui.button("⋯", on_click=lambda: ui.navigate.to('/universities')).props("flat round dense no-caps") \
                            .classes("text-black bg-gray-200 hover:bg-gray-300")
        with ui.element("div").classes("flex items-center gap-0 justify-center py-10"):
            ui.button("Load More...", on_click=lambda: ui.navigate.to('/loadmore')).props("flat dense no-caps").classes("bg-purple-600 text-white shadow hover:bg-purple-500 px-4 py-2")
                            

    # blogs                     
    with ui.element("section").classes("w-full bg-transparent"):
        with ui.row().classes("w-full flex flex-row justify-between items-center px-20 py-10"):
            with ui.row().classes("gap-0 space-x-2"):
                ui.label("Our").classes("text-2xl font-bold text-black")
                ui.label("Blogs").classes("text-2xl font-bold text-purple-600")
        with ui.grid().classes("grid grid-cols-1 md:grid-cols-3 w-full px-20"):
            for i in range(3):
                with ui.card():
                    ui.image("https://images.pexels.com/photos/1587927/pexels-photo-1587927.jpeg").classes("rounded-lg")
                    ui.label("BestSelller Book Bootcamp -write, Market & Publish Your Book -Lucknow").classes("text-lg")
                    ui.label("Saturdat, March 18, 9.30PM").classes("text-purple-600 text-sm")
                    with ui.row().classes("text-gray-600 space-x-1 gap-0"):
                        ui.label("ONLINE EVENT - ")
                        ui.label("Attend anywhere")
        with ui.element("div").classes("flex items-center justify-center py-10"):
            ui.button("Load More...", on_click=lambda: ui.navigate.to('/loadmore')).props("flat dense no-caps").classes("bg-purple-600 text-white shadow hover:bg-purple-500 px-4 py-2")
        

    show_footer()

