# File name: ammo.py
import kivy
kivy.require('1.7.0')

from kivy.animation import Animation
from kivy.uix.image import Image
from boom import Boom


class Ammo(Image):
    def shoot(self, tx, ty, target):
        self.target = target
        self.animation = Animation(x=tx, top=ty)
        self.animation.bind(on_start=self.on_start)
        self.animation.bind(on_progress=self.on_progress)
        self.animation.bind(on_complete=self.on_stop)
        self.animation.start(self)

    def on_start(self, instance, value):
        self.boom = Boom()
        self.boom.center = self.center
        self.parent.add_widget(self.boom)

    def on_progress(self, instance, value, progression):
        if progression >= .1:
            self.parent.remove_widget(self.boom)
        if self.target.collide_ammo(self):
            self.animation.stop(self)

    def on_stop(self, instance, value):
        self.parent.remove_widget(self)


class Shot(Ammo):
    pass


class Missile(Ammo):
    pass

