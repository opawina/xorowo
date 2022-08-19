from kivy.uix.screenmanager import Screen

from utils.button_add import ButtonAdd
from utils.button_menu import ButtonMenu
from utils.storage import Storage


class BaseScreen(Screen):
    button_menu = ButtonMenu()
    button_add = ButtonAdd()

    storage = Storage()
