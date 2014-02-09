# File name: color.py
import kivy
kivy.require('1.7.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string("""
<GridLayout>:
    cols:2
    Label:
        color: 1,0,0,1
        canvas:
            Line:
                points: self.x, self.y, self.x + self.width, self.y + self.height
    Widget:
        canvas:
            Line:
                points: self.x, self.y, self.x +self.width, self.y + self.height
""")

class LabelApp(App):
    def build(self):
        return GridLayout()

if __name__=="__main__":
    LabelApp().run()
