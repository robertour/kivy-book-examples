# File name: floatlayout.py
import kivy
kivy.require('1.7.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class FloatLayoutApp(App):
    def build(self):
        return FloatLayout()

if __name__=="__main__":
    FloatLayoutApp().run()
