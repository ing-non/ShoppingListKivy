from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy import Config

Config.set("graphics", "width", "270")
Config.set("graphics", "height", "480")

ROWS = ['Goc', 'COC', 'EEE', 'abs' , 'kju' , 'iop' , 'nmg', 'gty', 'jkio', 'dbkgcd' , 'udbcbjkb']

class Table(BoxLayout):
    def __init__(self, **kwargs):
        super(Table, self).__init__(**kwargs)
        for row in ROWS:
            self.add_widget(Row(row))



class Row(BoxLayout):
    txt = StringProperty()
    def __init__(self, row, **kwargs):
        super(Row, self).__init__(**kwargs)
        self.txt = row


class ScrollListItems(BoxLayout):
    pass

class ShoppingList(App):
    pass


if __name__ == "__main__":
    ShoppingList().run()

"""from kivy import Config
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


class List(BoxLayout):
    def __init__(self, **kwargs):
        super(List, self).__init__(**kwargs)
        for row in ROWS:
            self.add_widget(Row(row))

class Row(BoxLayout):
    txt = StringProperty()
    def __init__(self, row, **kwargs):
        super(Row, self).__init__(**kwargs)
        self.txt = row


class MainWidget():
    pass



class ShoppingList(App):
    pass

if __name__ == "__main__":
    ShoppingList().run()"""