from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from pages.home import show_home_page
from pages.signin import show_signin_page
from pages.signup import show_signup_page


@ui.page("/")
def home_page():
    show_home_page()


@ui.page("/signup")
def signup_page():
    show_signup_page()


@ui.page("/signin")
def signin_page():
    show_signin_page()
  

ui.run()