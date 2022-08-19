import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from src.about_screen import AboutScreen
from src.hello_screen import HelloScreen
from src.main_screen import MainScreen
from src.read_screen import ReadScreen
from src.write_screen import WriteScreen
from utils.storage import Storage


kivy.require('2.1.0')


class XorowoApp(App):

    def build(self):
        sm = ScreenManager()
        storage = Storage()
        if not storage.get_all():
            sm.add_widget(HelloScreen())
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(WriteScreen(name='write'))
        sm.add_widget(ReadScreen(name='read'))
        sm.add_widget(AboutScreen(name='about'))

        return sm


if __name__ == '__main__':
    XorowoApp().run()
