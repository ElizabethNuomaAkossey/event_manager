from nicegui import ui,html



def show_footer():
    with ui.element("footer").style("background-color: navy;").classes("w-full"):
        with ui.element("div").classes("flex flex-col items-center"):
            with ui.element("div").classes("flex flex-row font-bold text-lg mt-4 mb-3"):
                ui.label("Event").classes("mr-2").classes("text-white")
                ui.label("Hive").classes("text-purple-600")
            with ui.element("div").classes("flex flex-row mb-8"):
                ui.input(placeholder="Enter your maill").props("borderless dense flat").classes("rounded-sm text-xs mr-2 w-[240px] bg-white placeholder:text-right h-[40px] px-2")
                ui.button(text="Subscribe").props("flat dense no-caps").classes("bg-purple-600 extended font-normal text-white w-[120px]")
             # navlinks
            navlinks = [
                    {"title":"Home","path":"/"},
                    {"title":"About","path":"/"},
                    {"title":"Services","path":"/"},
                    {"title":"Get in touch","path":"/"},
                    {"title":"FAQs","path":"/"}
                ]
            with ui.row().classes("gap-[31px] mb-8"):
                 for item in navlinks:
                     ui.link(item["title"], item["path"]).classes("no-underline text-white")
        
        ui.element("div").classes("bg-white item-center justify-center w-[89%] min-h-[0.2px] mx-20")

        with ui.row().classes("justify-between items-center justify-center px-20 text-white my-5"):
            with ui.element("div").classes("space-x-1"):
                    ui.button("English").props("dense flat no-caps").classes("bg-purple-600 text-white px-5")
                    ui.button("French").props("dense flat no-caps").classes("text-white")
                    ui.button("Hindi").props("dense flat no-caps").classes("text-white")  
            with ui.element("div").classes("w-[200px] h-[30px]"):
                ui.html('<i class="fa-brands fa-square-linkedin"></i>')
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-facebook"></i>') 
            ui.label("Non Copyrighted © 2023 Upload by EventHive")

            
       
      
        


