from nicegui import ui,html


ui.add_head_html('''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer" />

<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
                 
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/brands.min.css" integrity="sha512-WxpJXPm/Is1a/dzEdhdaoajpgizHQimaLGL/QqUIAjIihlQqlPQb1V9vkGs9+VzXD7rgI6O+UsSKl4u5K36Ydw==" crossorigin="anonymous" referrerpolicy="no-referrer" />

<style>
  body {
    font-family: 'Roboto', sans-serif;
  }
</style>
''')


def show_footer():
    with ui.element("footer").style("background-color: navy;").classes("w-screen h-[250px]"):
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
        
        ui.element("div").classes("bg-white w-[1075px] h-[0.2px] mx-auto mb-3")

        with ui.element("div"):
            with ui.element("div"):
                    ui.link("English")
                    ui.link("French")
                    ui.link("Hindi")
        # with ui.element("div").classes("bg-red w-[200px] h-[30px]"):
        #     ui.html('<i class="fa-brands fa-square-facebook"></i>')
        #     ui.html('<i class="fa-brands fa-instagram"></i>')
        #     ui.html('<i class="fa-brands fa-x-twitter"></i>')

            
        # 
        #             # navlinks
        #             navlinks = [
        #                 {"title":"Home","path":"/"},
        #                 {"title":"Menu","path":"/"},
        #                 {"title":"About","path":"/"},
        #                 {"title":"Gallery","path":"/"},
        #                 {"title":"Blog","path":"/"},
        #                 {"title":"Contact","path":"/"}
        #             ]
        #             with ui.row():
        #                 for item in navlinks:
        #                     ui.link(item["title"], item["path"]).classes("no-underline uppercase text-black font-bold")
                    
        #             # socials fac
        #             with ui.row().classes():
        #                 ui.html('<i class="fa-brands fa-square-facebook"></i>')
        #                 ui.html('<i class="fa-brands fa-instagram"></i>')
        #                 ui.html('<i class="fa-brands fa-x-twitter"></i>')
        


