from donaclotilde.model import Model


from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color

from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.list import TwoLineAvatarListItem, OneLineListItem, MDList
from kivymd.uix.screen import Screen 




import csv



class Opcao(ScreenManager):
    def __init__(self, **kwargs):
        super(Opcao, self).__init__(**kwargs)
        

        self.mad = Model()
        
            
    def menu_carregar(self):
        self.transition.direction = 'right'
        self.current="menu"
    def busca_carregar(self):
        self.transition.direction = 'up'
        self.current="busca"
    def voltar_mapa(self):
        self.transition.direction = 'down'
        self.current="mapa"    




class Tela_canvas(Widget):
    def __init__(self, **kwargs):
        super(Tela_canvas, self).__init__(**kwargs)

        mad = Model()
        self.lista = mad.listar_cordenadas()

        with self.canvas:

            #padronizar para usar as coordenadas corretas em qualquer tela
            #desenhar asreas do varejão
            #Color(0,1,1,1 , mode='rgba')
            #self.rect = Rectangle(pos=(0,0),size=( 400 ,510))


            Color(0,0,1,0.5 , mode='rgba')
            for x in self.lista:    
                self.rect = Rectangle(pos = (10 if x[1] == None  else x[1] 
                    ,10 if x[2] == None else x[2] ), size=(10,10) )

    def on_touch_down(self, touch):
        
        print(int(touch.pos[0]))
        print(int(touch.pos[1]))

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
            preview=False,
        )
        self.mad=Model()

    

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
        if self.path == '':
            toast("selecione o arquivo csv")
        else:
            with open(self.path,'r', encoding="ISO-8859-1") as f:
                reader = csv.reader(f)

                
                lista=[''.join(x).split(';') for x in reader]
                n = 0
                print(len(lista))
                
                #terminar ainda não funciona

                for x in lista:
                    asd = self.mad.consulta(x[6],x[7],x[4])
                    if asd == []:
                        asd = ['nome_permissionario']
                    if asd[0] == x[14]:
                        pass
                    else:
                        n = n +1
                        print(asd[0])
                        print("lista "+str(x[14]))

            toast("total de atualizações: " + str(n))    
        
    
    pass 
class Menu(Screen):
    pass 






class Busca(Screen):
    def __init__(self, **kwargs):
        super(Busca, self).__init__(**kwargs)
        self.mad = Model()
    
    def carregar(self,root,busca):

        self.dados = self.mad.lista_empresas_filt(busca)
        
        for x in self.dados:
            root.add_widget(TwoLineAvatarListItem(text="Empresa: "+ "vago" if x[0] == None else x[0] ,
                secondary_text='Local: ' +str(x[1])+" - Banca: "+str(x[2])))
     







class Scroll_lista_empresas(ScrollView):
    
    pass





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

