from src.base_screen import BaseScreen
from utils.button_add import ButtonAdd
from utils.button_main import ButtonMain
from utils.button_menu import ButtonMenu


class MainScreen(BaseScreen):
    button_menu = ButtonMenu()
    button_add = ButtonAdd()
    button_main = ButtonMain()