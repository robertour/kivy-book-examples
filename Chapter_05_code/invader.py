# File name: invader.py
import kivy
kivy.require('1.7.0')
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.animation import Animation
from random import choice, randint
from ammo import Missile


class Invader(Image):
    pre_fix = ['in_', 'out_', 'in_out_']
    functions = ['back', 'bounce', 'circ', 'cubic', 'elastic',
                 'expo', 'quad', 'quart', 'quint', 'sine']
    formation = True

    def solo_attack(self):
        if self.formation:
            self.parent.unbind_invader()
            animation = self.trajectory()
            animation.bind(on_complete=self.to_dock)
            animation.start(self)

    def trajectory(self):
        fleet = self.parent.parent
        area = fleet.parent
        x = choice((-self.width, area.width+self.width))
        y = randint(round(area.y), round(fleet.y))
        t = choice(self.pre_fix) + choice(self.functions)
        return Animation(x=x, y=y, d=randint(2, 7), t=t)

    def to_dock(self, instance, value):
        self.y = Window.height
        self.center_x = Window.width/2
        animation = Animation(pos=self.parent.pos, d=2)
        animation.bind(on_complete=self.parent.bind_invader)
        animation.start(self)

    def drop_missile(self):
        missile = Missile()
        missile.center = (self.center_x, self.y)
        fleet = self.parent.parent
        fleet.invasion.add_widget(missile)
        missile.shoot(self.center_x, 0, fleet.shooter)

