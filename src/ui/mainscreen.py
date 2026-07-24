from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty

class MainScreen(Screen):

    sum_cups = NumericProperty(-100000)
    add_cups = NumericProperty(0)
    json_file_manager:None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.json_file_manager = App.get_running_app().json_file_manager
        self.sum_cups = self.json_file_manager.read_today()

    def minus_on_release(self):
        self.add_cups -= 1

    def plus_on_release(self):
        self.add_cups += 1

    def confirm_on_release(self):
        self.json_file_manager.write(self.add_cups)
        print(f'add = {self.add_cups}, sum = {self.sum_cups}')
        self.sum_cups = self.json_file_manager.read_today()
        self.add_cups = 0
