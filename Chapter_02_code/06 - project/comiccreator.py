import kivy
kivy.require('1.7.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('toolbox.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('comicwidgets.kv')
Builder.load_file('generaloptions.kv')
Builder.load_file('statusbar.kv')

class ComicCreator(AnchorLayout):
    pass

class ComicCreatorApp(App):
    def build(self):
        return ComicCreator()

if __name__=="__main__":
    ComicCreatorApp().run()
