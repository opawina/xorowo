from kivy.uix.label import Label

from src.base_screen import BaseScreen


class ReadField(Label):
    text_output = BaseScreen.storage.get_random()
    # TODO instansiation class during import
    read_field = Label(text='EMPTY')
    if text_output:
        read_field = Label(text=text_output['val'])
        print('FIELD:' + read_field.text)


class ReadScreen(BaseScreen):
    read_field = ReadField()
