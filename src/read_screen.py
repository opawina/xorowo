from kivy.uix.screenmanager import Screen

from src.base_screen import BaseScreen
from utils.storage import Storage


class ReadScreen(Screen):
    storage = Storage()
    label_text = storage.get_random()
    print('1111111111111111111111111111111')
    print(label_text)
    print('1111111111111111111111111111111')
