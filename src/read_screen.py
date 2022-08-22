from kivy.uix.label import Label

from src.base_screen import BaseScreen


class ReadField(Label):
    out = ''
    if BaseScreen.storage.get_random():
        out = BaseScreen.storage.get_random()['val']


class ReadScreen(BaseScreen):

    def get_one(self):
        self.ids.read_fld.text = self.storage.get_random()['val']
