from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager, NoTransition

from utils.button_add import ButtonAdd
from utils.button_down import ButtonDown
from utils.button_main import ButtonMain
from utils.button_menu import ButtonMenu

from utils.storage import Storage


class BaseScreen(Screen):
    sm = ScreenManager(transition=NoTransition())
    storage = Storage()
