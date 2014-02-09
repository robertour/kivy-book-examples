# File name: layouts.py
import kivy
kivy.require('1.7.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    pass

class LayoutsApp(App):
    def build(self):
        return MyGridLayout()

if __name__=="__main__":
    LayoutsApp().run()
