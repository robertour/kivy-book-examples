# File name: ammo.py
import kivy
kivy.require('1.7.0')

from kivy.uix.image import Image
from kivy.core.audio import SoundLoader


class Boom(Image):
    sound = SoundLoader.load('boom.wav')

    def __init__(self, **kwargs):
        self.__class__.sound.play()
        super(Boom, self).__init__(**kwargs)
