from nicegui import ui,html
from nicegui.events import ValueChangeEventArguments
from pages.home import *
from pages.signin import *
from pages.signup import *
from pages.event import *
from pages.college import *
from pages.create_event import *
from pages.not_found import *



# Load font awesome for socials
ui.add_head_html('''
                 <link rel="stylesheet" href=<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/brands.min.css" integrity="sha512-WxpJXPm/Is1a/dzEdhdaoajpgizHQimaLGL/QqUIAjIihlQqlPQb1V9vkGs9+VzXD7rgI6O+UsSKl4u5K36Ydw==" crossorigin="anonymous" referrerpolicy="no-referrer"/>
                 ''')
# ui.add_head_html('''
# <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer"/>

# <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
                 
# <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/brands.min.css" integrity="sha512-WxpJXPm/Is1a/dzEdhdaoajpgizHQimaLGL/QqUIAjIihlQqlPQb1V9vkGs9+VzXD7rgI6O+UsSKl4u5K36Ydw==" crossorigin="anonymous" referrerpolicy="no-referrer"/>

# <style>
#   body {
#     font-family: 'Roboto', sans-serif;
#   }
# </style>
# ''')



# Exposing static files
app.add_static_files("/assets","assets")
  

ui.run()