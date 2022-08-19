from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class ButtonMenu(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ButtonMenu, self).__init__(**kwargs)
        self.source = 'data/button_menu.jpg'

    # def on_press(self):
    #     self.source = 'data/button_down.jpg'
    #
    # def on_release(self):
    #     self.source = 'data/you_filthy_thing.jpg'