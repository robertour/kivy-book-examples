# File name: generaloptions.py
import kivy
kivy.require('1.7.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty

class GeneralOptions(BoxLayout):
    group_mode = False
    translation = ListProperty(None)

    def clear(self, instance):
        self.drawing_space.clear_widgets()

    def remove(self, instance):
        ds = self.drawing_space
        if len(ds.children) > 0:
            ds.remove_widget(ds.children[0])

    def group(self, instance, value):
        if value == 'down':
            self.group_mode = True
        else:
            self.group_mode = False
            self.unselect_all()

    def color(self, instance):
        pass

    def gestures(self, instance, value):
        pass

    def unselect_all(self):
        for child in self.drawing_space.children:
            child.unselect()

    def on_translation(self,instance,value):
        for child in self.drawing_space.children:
            if child.selected:
                child.translate(*self.translation)
