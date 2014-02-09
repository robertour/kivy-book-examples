# File Name: gesturerecorder.py
import kivy
kivy.require('1.7.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line, Ellipse
from kivy.gesture import Gesture, GestureDatabase

class GestureRecorder(FloatLayout):

    def on_touch_down(self, touch):
        self.points = [touch.pos]
        with self.canvas:
            Ellipse(pos=(touch.x-5,touch.y-5),size=(10,10))
            self.line = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        self.points += [touch.pos]
        self.line.points += [touch.x, touch.y]

    def on_touch_up(self, touch):
        self.points += [touch.pos]
        gesture = Gesture()
        gesture.add_stroke(self.points)
        gesture.normalize()
        gdb = GestureDatabase()
        print "Gesture:", gdb.gesture_to_str(gesture)

class GestureRecorderApp(App):
    def build(self):
        return GestureRecorder()

if __name__=="__main__":
    GestureRecorderApp().run()
