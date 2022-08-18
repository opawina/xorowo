from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from src.base_screen import BaseScreen


class WriteScreen(BaseScreen):
    text_input = TextInput(text='TextInput')
    button_apply = Button(text="Хорошо!!!!")

    def apply(self):
        text = self.text_input.text
        self.storage.put(text)

