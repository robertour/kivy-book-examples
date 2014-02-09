# File name: drawingspace.py
import kivy
kivy.require('1.7.0')
from kivy.uix.stencilview import StencilView
from kivy.gesture import Gesture, GestureDatabase
from gestures import line45_str, circle_str, cross_str

class DrawingSpace(StencilView):

    def __init__(self, *args, **kwargs):
        super(DrawingSpace, self).__init__()
        self.gdb = GestureDatabase()
        self.line45 = self.gdb.str_to_gesture(line45_str)
        self.circle = self.gdb.str_to_gesture(circle_str)
        self.cross = self.gdb.str_to_gesture(cross_str)
        self.line135 = self.line45.rotate(90)
        self.line225 = self.line45.rotate(180)
        self.line315 = self.line45.rotate(270)
        self.gdb.add_gesture(self.line45)
        self.gdb.add_gesture(self.line135)
        self.gdb.add_gesture(self.line225)
        self.gdb.add_gesture(self.line315)
        self.gdb.add_gesture(self.circle)
        self.gdb.add_gesture(self.cross)

    def activate(self):
        self.bind(on_touch_down=self.down,
                  on_touch_move=self.move,
                  on_touch_up=self.up)

    def deactivate(self):
        self.unbind(on_touch_down=self.down,
                  on_touch_move=self.move,
                  on_touch_up=self.up)

    def down(self, ds, touch):
        if self.collide_point(*touch.pos):
            self.points = [touch.pos]
            self.ix = self.fx = touch.x
            self.iy = self.fy = touch.y
        return True

    def move(self, ds, touch):
        if self.collide_point(*touch.pos):
            self.points += [touch.pos]
            self.min_and_max(touch.x, touch.y)
        return True

    def up(self, ds, touch):
        if self.collide_point(*touch.pos):
            self.points += [touch.pos]
            self.min_and_max(touch.x, touch.y)
            gesture = self.gesturize()
            recognized = self.gdb.find(gesture, minscore=0.50)
            if recognized:
                self.discriminate(recognized)
        return True

    def gesturize(self):
        gesture = Gesture()
        gesture.add_stroke(self.points)
        gesture.normalize()
        return gesture

    def min_and_max(self, x, y):
        self.ix = min(self.ix, x)
        self.iy = min(self.iy, y)
        self.fx = max(self.fx, x)
        self.fy = max(self.fy, y)

    def discriminate(self, recognized):
        if recognized[1] == self.cross: 
            self.add_stickman()
        if recognized[1] == self.circle: 
            self.add_circle()
        if recognized[1] == self.line45:
            self.add_line(self.ix,self.iy,self.fx,self.fy)
        if recognized[1] == self.line135:
            self.add_line(self.ix,self.fy,self.fx,self.iy)
        if recognized[1] == self.line225:
            self.add_line(self.fx,self.fy,self.ix,self.iy)
        if recognized[1] == self.line315:
            self.add_line(self.fx,self.iy,self.ix,self.fy)

    def add_circle(self):
        cx = (self.ix + self.fx)/2.0
        cy = (self.iy + self.fy)/2.0
        self.tool_box.tool_circle.widgetize(self, cx, cy, self.fx, self.fy)

    def add_line(self,ix,iy,fx,fy):
        self.tool_box.tool_line.widgetize(self,ix,iy,fx,fy)

    def add_stickman(self):
        cx = (self.ix + self.fx)/2.0
        cy = (self.iy + self.fy)/2.0
        self.tool_box.tool_stickman.draw(self,cx,cy)

    def on_children(self, instance, value):
        self.status_bar.counter = len(self.children)
