from kivy.uix.label import Label

from src.base_screen import BaseScreen


class ReadField(Label):
    out = BaseScreen.storage.get_random()['val']


# TODO 0    Add 1 item. -> Start reding and KeyError: '3'
# при чтении следующих сообщений можно попасть на
# добавленный только что элемент. Как будто контекст для сторажда не обновляется
class ReadScreen(BaseScreen):

    def get_one(self):
        self.ids.read_fld.text = self.storage.get_random()['val']
