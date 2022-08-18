import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from src.about_screen import AboutScreen
from src.hello_screen import HelloScreen
from src.main_screen import MainScreen
from src.read_screen import ReadScreen


kivy.require('2.1.0')


class XorowoApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(HelloScreen())
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(ReadScreen(name='read'))
        return sm


if __name__ == '__main__':
    XorowoApp().run()