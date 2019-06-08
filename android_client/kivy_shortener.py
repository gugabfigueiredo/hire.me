# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.base import runTouchApp

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.relativelayout import RelativeLayout


Builder.load_string('''
<ShortenerMain>:
    BoxLayout:
        orientation: 'vertical'
        ScreenManager:
            id: smanager
            ShortenerPage:
                name: 'shortener'
                TextInput:
                    size_hint: .80, .08
                    pos_hint: {'center_x': .5, 'center_y': .50}
            ShortenedPage:
                name: 'shortened'
        BoxLayout:
            size_hint_y: .10
            Button:
                text: 'Shortener'
                on_release: smanager.current = 'shortener'
            Button:
                text: 'Shortened'
                on_release: smanager.current = 'shortened'

<ShortenerPage@Screen>:

<ShortenedPage@Screen>:
    #displays the 10 most accessed urls
    GridLayout:
        rows: 10
        Button:
            size_hint_y: .10
        Button:
            size_hint_y: .10

''')


class ShortenerMain(RelativeLayout):
    pass


class ShortenerClient(App):

    def build(self):

        return ShortenerMain()

if __name__ == '__main__':
    runTouchApp(ShortenerMain())