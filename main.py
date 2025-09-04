from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from pages.home import show_home_page
from pages.signin import show_signin_page
from pages.signup import show_signup_page
from pages.event import show_event_page
from pages.college import show_college_page
from pages.create_event import show_create_event_page

@ui.page("/")
def home_page():
    show_home_page()


@ui.page("/signup")
def signup_page():
    show_signup_page()


@ui.page("/signin")
def signin_page():
    show_signin_page()

@ui.page("/event")
def event_page():
    show_event_page()

@ui.page("/college")
def college_page():
    show_college_page()

@ui.page("/create_event")
def create_event_page():
    show_create_event_page()

  

ui.run()