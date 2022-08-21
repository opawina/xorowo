from src.base_screen import BaseScreen


class WriteScreen(BaseScreen):
    def apply(self):
        text = self.text_input.text
        self.storage.put(text)
