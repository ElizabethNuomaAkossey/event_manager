from nicegui import ui
from components.footer import show_footer
from components.navbar import show_navbar




@ui.page("/")
def show_home_page():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    show_navbar()
    with ui.element("main").classes("w-full h-screen px-5"):
        with ui.element("div").classes("bg-[url('https://images.pexels.com/photos/2774556/pexels-photo-2774556.jpeg')] bg-cover bg-center w-full h-[80%] flex flex-col justify-center rounded-xl items-center relative"):
            with ui.column().classes("text-white text-7xl font-bold items-center"):
                ui.label("MADE FOR THOSE")
                ui.label("WHO DO")
                
            #     # --- Search filter box ---
            # with ui.element("div").classes(
            #     "absolute bottom-[-40px] left-1/2 transform -translate-x-1/2 flex space-x-4 "
            #     "bg-blue-900 p-6 rounded-2xl shadow-xl w-[500px]"):
            #     # Looking for
            #     with ui.element("div").classes("flex flex-col text-white"):
            #         ui.label("Looking for").classes("text-sm mb-1")
            #         ui.select(["Conference", "Workshop", "Meetup"], value="Conference").classes("bg-white text-black rounded-md h-10 w-48")

            # #     # Location
            #     with ui.element("div").classes("flex flex-col text-white"):
            #         ui.label("Location").classes("text-sm mb-1")
            #         ui.select(["New York", "London", "Berlin"], value="New York") \
            #             .classes("bg-white text-black rounded-md px-4 py-2 w-48")

            #     # When
            #     with ui.element("div").classes("flex flex-col text-white"):
            #         ui.label("When").classes("text-sm mb-1")
            #         ui.input("Choose date and time") \
            #             .classes("bg-white text-black rounded-md px-4 py-2 w-48")

            #     # Search button
            #     ui.button("").props("icon=search").classes(
            #         "bg-blue-500 text-white rounded-md p-4 hover:bg-blue-600"
            #     )
    # Upcoming Events
    with ui.element("section").classes("w-full bg-transparent"):
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
        with ui.grid(columns=3).classes("w-full px-20"):
            for i in range(6):
                with ui.card():
                    ui.image("https://images.pexels.com/photos/1047442/pexels-photo-1047442.jpeg")

        



    show_footer()