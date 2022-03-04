from kivy.config import Config
from kivy.uix.gridlayout import GridLayout

Config.set("graphics", "width", "270")
Config.set("graphics", "height", "480")

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder


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

class AddItemToShoppingList(BoxLayout):
    def __init__(self):
        print("AddItemToShoppingList")

class MainWidget(GridLayout):
    scrolllist_items = ObjectProperty()
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)

    def open_add_item_screen(self):
        AddItemToShoppingList()

class ShoppingList(App):
    pass

if __name__ == "__main__":
    ShoppingList().run()
