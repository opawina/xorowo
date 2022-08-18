from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

from src.base_screen import BaseScreen
from src.main_screen import MainScreen
from utils.storage import Storage

# class ButtonXorowo(Button):
#     def callback(self):
#         print('The button <%s> is being pressed' % self.text)
#         return MainScreen()

    # btn1 = Button(text='Hello world 1')
    # btn1.bind(on_press=callback)


class HelloScreen(Screen):
    if not Storage().get_all():
        print(5555555555555555555555)
