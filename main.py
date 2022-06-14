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


from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

import csv


#trecho deve ser apagado ao implementar banco de dados
with open("data/dados.csv" ,'r', encoding="ISO-8859-1") as f:
    reader = csv.reader(f)

            
    lista=[''.join(x).split(';') for x in reader]


        
    
    #print(dado[4]+dado[6]+dado[7]+dado[11]+dado[14])
    

class Tela_canvas(Widget):
    def __init__(self, **kwargs):
        super(Tela_canvas, self).__init__(**kwargs)

        #introduzir banco de dados
        #self.lista = madruguinha.carregar_empresas()

        #apagar trecho abaixo
        self.lista = lista
        with self.canvas:
            for x in self.lista:
                
                if x[7]!='banca_numero':
                    
                    if x[11] == "Liberada":
                        Color(0,0,1,1 , mode='rgba')
                    else:
                        Color(1,0,0,1 , mode='rgba')
                    
                    self.rect = Rectangle(pos = (int(x[7]),int(x[7])), size=(10,10) )
    def buscar(self):
        print("asdasdasdasd")
        

    pass

class Tela_Mapa(Screen):


    pass 

class Carregar(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.path = ''
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )
    

    def file_manager_open(self):
        self.file_manager.show('../')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        self.path = path

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
    def atualizar(self):

        with open(self.path+"/dados.csv" ,'r', encoding="ISO-8859-1") as f:
            reader = csv.reader(f)

            
            lista=[''.join(x).split(';') for x in reader]
            
        #mudar para atualizar banco de dados
        print(lista)

    
    pass 
class Menu(Screen):
    pass 
class Busca(Screen):

    pass 
class Opcao(ScreenManager):
    def __init__(self, **kwargs):
        super(Opcao, self).__init__(**kwargs)
        self.dados = []
    
    def buscar(self, entrada):
        print('asdas')
        print(entrada)
        
    def menu_carregar(self):
        self.transition.direction = 'right'
        self.current="menu"
    def busca_carregar(self):
        self.transition.direction = 'up'
        self.current="busca"
    def voltar_mapa(self):
        self.transition.direction = 'down'
        self.current="mapa"

    
class Lista_empresas(MDList):
    def __init__(self, **kwargs):
        super(Lista_empresas, self).__init__(**kwargs)
        cont= 0 

        while cont < 10:
            
            self.add_widget(OneLineListItem(text=f"Empresa: {lista[cont][14]}"))
            cont = cont + 1


class CafeCereja_App(MDApp):
    #lista_bancas = lista
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

