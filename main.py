from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.screen import Screen 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton

from kivy.graphics import Rectangle
from kivy.graphics import Color

import csv

with open('data/dados.csv','r', encoding="ISO-8859-1") as f:
    reader = csv.reader(f)

    
    lista=[''.join(x).split(';') for x in reader]
    
    


        
    
    #print(dado[4]+dado[6]+dado[7]+dado[11]+dado[14])
    

class Tela_canvas(Widget):
    def __init__(self, **kwargs):
        super(Tela_canvas, self).__init__(**kwargs)

        with self.canvas:
            for x in lista:
                
                if x[7]!='banca_numero':
                    
                    if x[11] == "Liberada":
                        Color(0,0,1,1 , mode='rgba')
                    else:
                        Color(1,0,0,1 , mode='rgba')
                    
                    self.rect = Rectangle(pos = (int(x[7]),int(x[7])), size=(10,10) )



    pass

class Inicial(Screen):
    
    pass 
class Menu(Screen):
    pass 
class Opcao(ScreenManager):
    pass
    
class Lista_empresas(MDList):
    def __init__(self, **kwargs):
        super(Lista_empresas, self).__init__(**kwargs)
        cont= 0 

        while cont < 10:
            
            self.add_widget(OneLineListItem(text=f"Empresa: {lista[cont][14]}"))
            cont = cont + 1


class CafeCereja_App(MDApp):
    lista_bancas = lista
    def __init__(self, *args):
        super(CafeCereja_App, self).__init__(*args)
        


    def build(self):
        self.theme_cls.primary_palette = "Purple" #, "Red"
        self.theme_cls.primary_hue = "800"  # "500"
        

        return Opcao()

    def carregar_lista_SGE(self):
        
        pass

    def anterior_fase(self):
        print("asd")
       


CafeCereja_App().run()

