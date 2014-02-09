# File name: dock.py
import kivy
kivy.require('1.7.0')

from kivy.uix.widget import Widget
from invader import Invader


class Dock(Widget):

    def __init__(self, **kwargs):
        super(Dock, self).__init__(**kwargs)
        self.invader = Invader()
        self.add_widget(self.invader)
        self.bind_invader()

    def bind_invader(self, instance=None, value=None):
        self.invader.formation = True
        self.bind(pos=self.on_pos)

    def unbind_invader(self):
        self.invader.formation = False
        self.unbind(pos=self.on_pos)

    def on_pos(self, instance, value):
        self.invader.pos = self.pos

