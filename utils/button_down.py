from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class ButtonDown(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ButtonDown, self).__init__(**kwargs)
        self.source = 'data/button_down.jpg'

    # def on_press(self):
    #     self.source = 'data/button_down.jpg'
    #
    # def on_release(self):
    #     self.source = 'data/you_filthy_thing.jpg'