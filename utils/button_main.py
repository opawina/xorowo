from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class ButtonMain(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ButtonMain, self).__init__(**kwargs)
        self.source = 'data/button_main.png'

    # def on_press(self):
    #     self.source = 'data/button_down.jpg'
    #
    # def on_release(self):
    #     self.source = 'data/you_filthy_thing.jpg'