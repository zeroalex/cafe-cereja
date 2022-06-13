from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem, MDList
from kivymd.uix.screen import Screen 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton

from kivy.graphics import Rectangle
from kivy.graphics import Color

#from openpyxl import load_workbook

import csv

with open('data/dados.csv','r', encoding="ISO-8859-1") as f:
    reader = csv.reader(f)
    for x in reader:
        print(x[0])



class Inicial(Screen):
    
    pass 
class Menu(Screen):
    pass 
class Opcao(ScreenManager):
    pass


class CafeCereja_App(MDApp):
    def __init__(self, *args):
        super(CafeCereja_App, self).__init__(*args)



    def build(self):
        self.theme_cls.primary_palette = "Purple" #, "Red"
        self.theme_cls.primary_hue = "800"  # "500"
        
        """
        data_file= 'data/dados.csv'

        ws = load_workbook(data_file)

        all_rows = list(xs.rows)

        for x in all_rows:
            print(x.value)
        """



        return Opcao()

    def proxima_fase(self):
        print("asd")

    def anterior_fase(self):
        print("asd")
       


CafeCereja_App().run()

