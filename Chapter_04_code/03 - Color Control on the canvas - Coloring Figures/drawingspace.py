# File name: drawingspace.py
import kivy
kivy.require('1.7.0')
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace(RelativeLayout):
    def on_children(self, instance, value):
        self.status_bar.counter = len(self.children)
