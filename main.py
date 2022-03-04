from kivy import Config
from kivy.app import App
from kivy.graphics import Rectangle, Color
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout

Config.set("graphics", "width", "270")
Config.set("graphics", "height", "480")


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 10):
            label = Label(text='test', pos=(100, 200), size_hint=(1, None), height=dp(100))
            self.add_widget(label)



class MainWidget():
    pass



class ShoppingList(App):
    pass

if __name__ == "__main__":
    ShoppingList().run()

