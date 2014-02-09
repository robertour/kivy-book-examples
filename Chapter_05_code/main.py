# File name: main.py
import kivy
kivy.require('1.7.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.clock import Clock
from fleet import Fleet
from shooter import Shooter

Builder.load_file('images.kv')


class Invasion(FloatLayout):

    def __init__(self, **kwargs):
        super(Invasion, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self.close, self)
        self._keyboard.bind(on_key_down=self.press)
        self.start_game()

    def close(self):
        self._keyboard.unbind(on_key_down=self.press)
        self._keyboard = None

    def press(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.shooter.center_x -= 30
        elif keycode[1] == 'right':
            self.shooter.center_x += 30
        return True

    def start_game(self):
        label = Label(text='Ready!')
        animation = Animation(font_size=72, d=2)
        animation.bind(on_complete=self.fleet.start_attack)
        self.add_widget(label)
        animation.start(label)

    def end_game(self, message):
        label = Label(markup=True, size_hint=(.2, .1),
                      pos=(0, self.parent.height/2), text=message)
        self.add_widget(label)
        self.composed_animation().start(label)

    def composed_animation(self):
        animation = Animation(center=self.parent.center)
        animation &= Animation(font_size=72, d=3)
        animation += Animation(font_size=24, y=0, d=2)
        return animation


class InvasionApp(App):
    def build(self):
        return Invasion()

if __name__ == "__main__":
    InvasionApp().run()

