from nicegui import ui


def show_home_page():
    with ui.element("div").classes(" flex justify-between items-center w-full"):
        with ui.element("div").classes("flex items-center space-x-2 ml-12"):
            ui.label("Event").classes("text-2xl font-bold text-black")
            ui.label("Hive").classes("text-2xl font-bold text-purple-600")
        
        with ui.element("div").classes("flex items-center mr-12"):
            ui.button("Login").props("flat dense no-caps").classes("text-black hover:bg-purple-200 shadow-none p-0 m-0 w-[80px] h-[10px]") \
            .on_click(lambda: ui.run_javascript("window.location.href = '/signin'"))
            ui.button("Signup").props("flat dense no-caps").classes("bg-purple-600 text-white shadow hover:bg-purple-500 w-[80px] h-[10px]") \
            .on_click(lambda: ui.run_javascript("window.location.href = '/signup'"))

    with ui.element("div").classes("relative w-full h-screen pl-5 pr-5 pt-1"):    
        ui.image(source ="https://images.pexels.com/photos/2774556/pexels-photo-2774556.jpeg").classes("w-full h-screen object-cover rounded-xl")
        
        with ui.element("div").classes("absolute inset-0 flex flex-col items-center justify-center text-white bottom-[30%]"):
            ui.label("MADE FOR THOSE").classes("text-6xl font-extrabold drop-shadow-lg")
            ui.label("WHO DO").classes("text-6xl font-extrabold drop-shadow-lg")
        
            # --- Search filter box ---
        with ui.element("div").classes(
            "absolute bottom-[-40px] left-1/2 transform -translate-x-1/2 flex space-x-4 "
            "bg-blue-900 p-6 rounded-2xl shadow-xl w-[500px]"):
            # Looking for
            with ui.element("div").classes("flex flex-col text-white"):
                ui.label("Looking for").classes("text-sm mb-1")
                ui.select(["Conference", "Workshop", "Meetup"], value="Conference").classes("bg-white text-black rounded-md h-10 w-48")

        #     # Location
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




ui.run()