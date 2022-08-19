from kivy.uix.label import Label

from src.base_screen import BaseScreen
from utils.button_down import ButtonDown


class ReadField(Label):
    # TODO 0 broken
    # TODO 1 does not update new msg on "One more" button

    text_output = BaseScreen.storage.get_random()
    # TODO 1 instansiation class during import
    read_field = Label(text='EMPTY')
    if text_output:
        read_field = Label(text=text_output['val'])
        # print('FIELD:' + read_field.text)

    def get(self):
        text_output = BaseScreen.storage.get_random()
        # TODO 1 instansiation class during import
        # read_field = Label(text='EMPTY')
        if text_output:
            return Label(text=text_output['val'])
            print('FIELD:' + read_field.text)


class ReadScreen(BaseScreen):
    read_field = ReadField()
    button_down = ButtonDown()

