from nicegui import ui



@ui.page("/signin")
def show_signin_page():
    with ui.element("div").classes("w-screen h-screen flex m-0 p-0 border rounded-2xl overflow-hidden"):
        with ui.element("div").classes("relative h-full w-[55%] bg-gray-100 m-0 p-0 flex items-center justify-center"):
                with ui.card().classes("w-[80%] h-[100%] bg-transparent flex flex-col items-center m-0 pt-8 shadow-none border-none"):
                    
                    # Top row: Event + Hive
                    with ui.element("div").classes("flex justify-center items-center space-x-2 mt-2"):
                        ui.label("Event").classes("text-s font-bold text-black")
                        ui.label("Hive").classes("text-s font-bold text-purple-500")

                    # Subtitle
                    ui.label("Sign In to Event Hive").classes("text-xl font-bold text-center m-0 p-0")

                    # Form section
                    with ui.element("div").classes("w-full flex flex-col space-y-3 px-1"):

                            # E-mail
                        with ui.element("div").classes("flex flex-col w-full"):
                            ui.label("YOUR EMAIL").classes("text-xs mb-1 text-left")
                            ui.input(
                                placeholder="Enter your mail"
                            ).props("flat borderless dense").classes("rounded-sm w-full bg-white mb-2 px-2 text-xs")


                        # Password
                        with ui.element("div").classes("flex flex-col w-full"):
                            # Label row (Password + Forgot link inline)
                            with ui.element("div").classes("flex justify-between items-center w-full mb-1"):
                                ui.label("PASSWORD").classes("text-xs text-left")
                                ui.link("Forgot your password?", target="/forgot-password").props("dense flat borderless").classes("text-xs text-ash-500 hover:underline")

                            # Input box below the label row
                            ui.input(
                                placeholder="Enter your password", 
                                password_toggle_button="yes"
                            ).props("flat dense password borderless").classes("rounded-sm w-full bg-white text-xs px-2 mb-2")

                                


                    # Signin button
                    ui.button("Sign in") \
                        .props("flat dense no-caps") \
                        .classes("bg-purple-500 text-white min-w-[200px] mt-5 self-center")

                    # "or" label
                    ui.label("or").classes("text-s text-gray-500 my-1 self-center")

                    # Signup with Google button
                    with ui.button().props("flat dense no-caps outlined").classes("bg-white text-black min-w-[300px] border-2 border-black rounded-md flex items-center justify-center space-x-2 self-center"):
                # Google logo (SVG)
                        ui.html("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" class="w-5 h-5">
                            <path fill="#4285F4" d="M24 9.5c3.5 0 6.2 1.5 7.6 2.8l5.5-5.5C33.4 3.8 28.9 2 24 2 14.8 2 7.2 7.8 4 16.2l6.7 5.2C12.4 14.5 17.7 9.5 24 9.5z"/>
                            <path fill="#34A853" d="M46.1 24.5c0-1.6-.1-2.7-.4-3.9H24v7.4h12.6c-.3 2.1-1.8 5.2-5 7.3l7.6 5.9c4.6-4.3 7.2-10.6 7.2-16.7z"/>
                            <path fill="#FBBC05" d="M10.7 28.3c-.5-1.5-.8-3.2-.8-5s.3-3.5.8-5L4 13c-1.2 2.4-2 5.2-2 8.3s.7 5.9 2 8.3l6.7-5.3z"/>
                            <path fill="#EA4335" d="M24 46c6.5 0 11.9-2.1 15.8-5.7l-7.6-5.9c-2 1.4-4.7 2.4-8.2 2.4-6.3 0-11.6-4.2-13.5-10.1l-6.7 5.2C7.2 40.2 14.8 46 24 46z"/>
                        </svg>""").classes("mr-2")
                        ui.label("Signup with Google").classes("text-sm font-medium")

        
        with ui.element("div").classes("relative bg-red-500 h-full w-[45%] m-0 p-0"):
                ui.image("https://images.pexels.com/photos/1387174/pexels-photo-1387174.jpeg").classes("h-full blur-sm")
                with ui.element("div").classes('absolute inset-0 flex flex-col items-center justify-center text-white'):
                    ui.label("Hello Friend").classes('text-4xl text-center font-bold mb-6')
                    ui.label("To keep connected with us provide us with your information").classes('text-s text-center max-w-md mb-6')
                    ui.button("Signup").props("flat dense no-caps").classes("bg-gray-400 text-white w-[100px] hover:bg-gray-300").on_click(lambda: ui.run_javascript("window.location.href = '/signup'"))
ui.run()