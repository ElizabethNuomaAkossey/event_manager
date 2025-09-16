from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer


@ui.page("/event")
def show_event_page():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    show_navbar()
    with ui.element("main").classes("w-full h-screen px-5"):
        with ui.element("div").classes(
            "bg-[url('https://images.pexels.com/photos/301987/pexels-photo-301987.jpeg')] "
            "bg-cover bg-center w-full h-full rounded-xl"
        ):
            with ui.column().classes("py-10 px-5"):
                    ui.button("< Back").props("dense flat no-caps").classes("bg-purple-600 text-white px-3")
            with ui.column().classes("text-white px-5 w-1/2 h-full items-start"
                # " w-full font-bold items-start justify-center h-full px-10"
            ):
                with ui.element("div").classes("text-5xl font-bold"):
                    ui.label("Dream world wide in")
                    ui.label("Jakarta")
                with ui.element("div").classes("text-2xl font-semi-bold"):
                    ui.label("IIIT Sonepat")
                with ui.element("div"):
                    ui.label("DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 \nPM. The workshop taught participants the magic of " \
                    "creating stunning 3D models \nand animations using Blender. It was suitable for both beginners and experienced \nusers. " \
                    "The event was followed by a blender-render competition, which added to the \nexcitement.").classes("whitespace-pre-line")
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

    show_footer()
