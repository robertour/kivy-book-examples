# File name: toolbox.py
import kivy
kivy.require('1.7.0')
import math
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
from comicwidgets import StickMan, DraggableWidget

class ToolButton(ToggleButton):
    def on_touch_down(self, touch):
        ds = self.parent.drawing_space
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            (x,y) = ds.to_widget(touch.x, touch.y)
            self.draw(ds, x, y)
            return True
        return super(ToolButton, self).on_touch_down(touch)

    def draw(self, ds, x, y):
        pass

class ToolStickman(ToolButton):
    def draw(self, ds, x, y):
        sm = StickMan(width=48, height=48)
        sm.center = (x,y)
        ds.add_widget(sm)

class ToolFigure(ToolButton):
    def draw(self, ds, x, y):
        (self.ix, self.iy) = (x,y)
        with ds.canvas:
            self.figure=self.create_figure(x,y,x+1,y+1)
        ds.bind(on_touch_move=self.update_figure)
        ds.bind(on_touch_up=self.end_figure)

    def update_figure(self, ds, touch):
        if ds.collide_point(touch.x, touch.y):
            (x,y) = ds.to_widget(touch.x, touch.y)
            ds.canvas.remove(self.figure)
            with ds.canvas:
                self.figure = self.create_figure(self.ix, self.iy,x,y)

    def end_figure(self, ds, touch):
        ds.unbind(on_touch_move=self.update_figure)
        ds.unbind(on_touch_up=self.end_figure)
        ds.canvas.remove(self.figure)
        (fx,fy) = ds.to_widget(touch.x, touch.y)
        self.widgetize(ds,self.ix,self.iy,fx,fy)

    def widgetize(self,ds,ix,iy,fx,fy):
        widget = self.create_widget(ix,iy,fx,fy)
        (ix,iy) = widget.to_local(ix,iy,relative=True)
        (fx,fy) = widget.to_local(fx,fy,relative=True)
        widget.canvas.add(self.create_figure(ix,iy,fx,fy))
        ds.add_widget(widget)

    def create_figure(self,ix,iy,fx,fy):
        pass

    def create_widget(self,ix,iy,fx,fy):
        pass

class ToolLine(ToolFigure):
    def create_figure(self,ix,iy,fx,fy):
        return Line(points=[ix, iy, fx, fy])

    def create_widget(self,ix,iy,fx,fy):
        pos = (min(ix, fx), min(iy, fy)) 
        size = (abs(fx-ix), abs(fy-iy))
        return DraggableWidget(pos = pos, size = size)

class ToolCircle(ToolFigure):
    def create_figure(self,ix,iy,fx,fy):
        return Line(circle=[ix,iy,math.hypot(ix-fx,iy-fy)])

    def create_widget(self,ix,iy,fx,fy):
        r = math.hypot(ix-fx, iy-fy)
        pos = (ix-r, iy-r)
        size = (2*r, 2*r)
        return DraggableWidget(pos = pos, size = size)
