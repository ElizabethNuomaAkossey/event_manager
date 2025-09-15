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
    with ui.element("section").classes("w-full h-screen bg-blue"):
        with ui.row().classes("w-full bg-transparent flex flex-row justify-between items-center px-10 py-10"):
            with ui.row():
                ui.label("Upcoming")
                ui.label("Events")
            with ui.row():

                ui.select(label["Monday","Tuesday","Wednesday","Thursday"])
                ui.select(value="Event Type", options=[1,2,3])
                ui.select(Value="Any Category", options=[1,2,3])

        



    show_footer()