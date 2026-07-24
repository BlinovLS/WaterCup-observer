# docker run --rm -it -v "${PWD}:/home/user/hostcwd" kivy/buildozer android debug

import os.path

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

from ui.mainscreen import MainScreen
from file_manager.jsonmanager import JSONManager

class WaterCupObserverApp(App):

    json_file_manager:JSONManager

    def build(self):

        self.json_file_manager = JSONManager(self)

        main_screen_kv = os.path.join(os.path.dirname(__file__), 'ui', 'kv', 'main_screen.kv')
        Builder.load_file(main_screen_kv)

        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))

        return screen_manager


if __name__ == '__main__':
    WaterCupObserverApp().run()