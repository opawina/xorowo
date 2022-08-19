from src.base_screen import BaseScreen
from utils.button_down import ButtonDown


class WriteScreen(BaseScreen):
    button_down = ButtonDown()
    def apply(self, screen_manager):
        text = self.text_input.text
        self.storage.put(text)
        # TODO 1 swithch to MainScreen
        screen_manager.current('main')
