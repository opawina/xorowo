from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

from src.base_screen import BaseScreen


class AboutScreen(Screen):
    text="""Хорошо!
    Открытый код. Репа: http://github.com/opawina/qqq
    - Не требует подключения к интернету
    - Требует доступ к хранилищу
    """