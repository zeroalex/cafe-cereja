from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem, MDList
from kivymd.uix.screen import Screen 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton



class Inicial(Screen):
    pass 
class Menu(Screen):
    pass 
class Opcao(ScreenManager):
    pass


class CafeCereja_App(MDApp):
    def __init__(self, *args):
        super(CafeCereja_App, self).__init__(*args)

        self.window = Opcao()
        


    def build(self):
        self.theme_cls.primary_palette = "Purple" #, "Red"
        self.theme_cls.primary_hue = "800"  # "500"
        
        self.window.add_widget(Menu())
        self.window.add_widget(Inicial())


        print(self.window)

        return self.window

    def proxima_fase(self):
        print("asd")
        self.window.current = 'inicial'
    def anterior_fase(self):
        print("asd")
        self.window.current = 'menu'
        


CafeCereja_App().run()

