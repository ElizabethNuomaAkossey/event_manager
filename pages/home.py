from nicegui import ui,app
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
                    ui.image("https://images.pexels.com/photos/1047442/pexels-photo-1047442.jpeg").classes("rounded-lg")
                    ui.label("BestSelller Book Bootcamp -write, Market & Publish Your Book -Lucknow").classes("text-lg")
                    ui.label("Saturdat, March 18, 9.30PM").classes("text-purple-600 text-sm")
                    with ui.row().classes("text-gray-600 space-x-1 gap-0"):
                        ui.label("ONLINE EVENT - ")
                        ui.label("Attend anywhere")
        with ui.element("div").classes("flex items-center justify-center py-10"):
            ui.button("Load More...", on_click=lambda: ui.navigate.to('/loadmore')).props("flat dense no-caps").classes("bg-purple-600 text-white shadow hover:bg-purple-500 px-4 py-2")

    # Make your own events
    with ui.element("section").classes("w-full bg-transparent"):
        with ui.row().classes("w-full h-[90%] flex flex-row justify-around items-center").style("background-color: navy;"):
            ui.image("/assets/make_your_own_event.png").classes("max-w-[300px] h-[100%] object-contain")
            with ui.column().classes("text-white max-w-md gap-0"):
                ui.label("Make your own Event").classes("text-2xl font-bold")
                ui.label("Lorem ipsum dolor sit amet, consectetur adipiscing elit.") \
                    .classes("whitespace-pre-line text-sm")
                with ui.element("div").classes("py-3"):
                    ui.button("Create Events", on_click=lambda: ui.navigate.to('/create_event')) \
                        .props("flat dense no-caps") \
                        .classes("bg-purple-600 hover:bg-purple-500 text-white px-10 py-1 rounded-sm")

            

    # Join these brands
    with ui.element("section").classes("w-full bg-transparent py-3"):
        with ui.row().classes("w-full flex flex-col justify-between items-center"):
            with ui.row().classes("gap-0 space-x-2"):
                ui.label("Join these").classes("text-2xl font-bold text-black")
                ui.label("brands").classes("text-2xl font-bold text-purple-600")
            with ui.element("div").classes("font-medium"):
                ui.label("We've had the pleasure of working with industry-defining brands. \nThese are just some of them.").classes("whitespace-pre-line text-center")
        with ui.row().classes("justify-center w-full items-center flex-wrap gap-8 bg-gray-50 rounded px-6 py-4"):
            logos = [
                "https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg",
                "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/4/4f/Stripe_Logo%2C_revised_2016.svg",
                "https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png",
                "https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/e/e5/Medium_icon.svg",
                "https://upload.wikimedia.org/wikipedia/commons/7/75/Zoom_Communications_Logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png",
                "https://upload.wikimedia.org/wikipedia/commons/5/5e/Grab_logo.svg",
            ]

            for logo in logos:
                ui.image(logo).classes(
                    "max-h-12 max-w-[120px] object-contain"
                )


    # Trending colleges
    with ui.element("section").classes("w-full bg-transparent"):
        with ui.row().classes("w-full flex flex-row justify-between items-center px-20 py-10"):
            with ui.row().classes("gap-0 space-x-2"):
                ui.label("Trending").classes("text-2xl font-bold text-black")
                ui.label("Colleges").classes("text-2xl font-bold text-purple-600")
        with ui.grid(columns=3).classes("w-full px-20"):
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
        with ui.grid(columns=3).classes("w-full px-20"):
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

