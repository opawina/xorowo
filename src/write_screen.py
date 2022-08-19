from src.base_screen import BaseScreen
from utils.button_down import ButtonDown


class WriteScreen(BaseScreen):
    button_down = ButtonDown()

    def apply(self):
        text = self.text_input.text
        self.storage.put(text)
        # TODO 1 switch to MainScreen
        # self.screen_manager.switch_to(MainScreen(name='main'))
