from kivy.uix.screenmanager import Screen

from utils.storage import Storage


class BaseScreen(Screen):
    storage = Storage()
