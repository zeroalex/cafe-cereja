from donaclotilde.model import Model


from kivy.core.window import Window
from kivy.graphics import Rectangle, Line, Color

from kivy.lang import Builder

from kivy.properties import StringProperty


from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.list import TwoLineListItem, OneLineListItem, MDList, ImageLeftWidget
from kivymd.uix.screen import Screen 

import csv,math

#rodar como celular
# -m screen:onesv,portrait

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

        self.mad = Model()
        self.lista = self.mad.listar_cordenadas()
        self.dest_empresa = None
        self.dest_ilha_coluna = None
        self.dest_banca_numero = None

        self.edite = False

        self.carregar_mapa()
    def carregar_mapa(self):
        self.lista = self.mad.listar_cordenadas()
        self.canvas.clear()
        with self.canvas:

            Tela_Mapa.marcacao(self)
            
            Color(0,0,1,0.5 , mode='rgba')

            for x in self.lista:    
                Color(1,0,0,1 , mode='rgba') if x[0]==self.dest_empresa else Color(0,0,1,0.5 , mode='rgba')

                self.rect = Rectangle(pos = (10 if x[1] == None  else x[1] 
                    ,10 if x[2] == None else x[2] ), size=(10,10) )

    def on_touch_down(self, touch):
        
        
        #colocar função para consultar empresa com clique

        
        if self.edite:
            x = int(touch.pos[0])
            while x%10 != 0:
                x = x-1    

            
            y = int(touch.pos[1])
            while y%10 != 0:
                y = y-1

            
            condicao = [self.dest_ilha_coluna,self.dest_banca_numero,self.dest_empresa]
            print("editando "+str(self.dest_empresa))
            
            self.mad.update_cordenada(str(x),str(y),condicao)
            #passar parametro empresa
            self.carregar_mapa()
            self.dest_empresa = None
            self.dest_ilha_coluna = None
            self.dest_banca_numero = None

            self.edite = False

        else:

            
            x = int(touch.pos[0])
            while x%10 != 0:
                x = x-1    
            
            y = int(touch.pos[1])
            while y%10 != 0:
                y = y-1
            self.procura(x,y)

            


            #self.carregar_mapa()

            #colocar função para consultar empresa com clique
            #print("falha")
        self.carregar_mapa()

    
    def procura(self,x,y):
        data = self.mad.procura_cordenada(str(x),str(y))
        if data != []:
            self.dest_empresa = data[0][0]
            self.dest_ilha_coluna = data[0][1]
            self.dest_banca_numero = data[0][2]

            Tela_Mapa.muda_legenda(self,data[0][0]  )
        else:
            Tela_Mapa.muda_legenda(self,None  )

            

    pass
"""
class Tela_canvas2(Widget):
    def __init__(self, **kwargs):
        super(Tela_canvas, self).__init__(**kwargs)

        self.mad = Model()
        self.lista = self.mad.listar_cordenadas()
        self.dest_empresa = None
        self.dest_ilha_coluna = None
        self.dest_banca_numero = None

        self.edite = False

        with self.canvas:

            Tela_Mapa.marcacao(self)
            
            Color(0,0,1,0.5 , mode='rgba')

            for x in self.lista:    
                Color(1,0,0,1 , mode='rgba') if x[0]==self.dest_empresa else Color(0,0,1,0.5 , mode='rgba')

                self.rect = Rectangle(pos = (10 if x[1] == None  else x[1] 
                    ,10 if x[2] == None else x[2] ), size=(10,10) )

    def carregar_mapa(self):
        self.lista = self.mad.listar_cordenadas()
        self.dest_empresa = None
        self.dest_ilha_coluna = None
        self.dest_banca_numero = None

        self.edite = False
        self.canvas.clear()
        with self.canvas:

            Tela_Mapa.marcacao(self)
            
            Color(0,0,1,0.5 , mode='rgba')

            for x in self.lista:    
                Color(1,0,0,1 , mode='rgba') if x[0]==self.dest_empresa else Color(0,0,1,0.5 , mode='rgba')

                self.rect = Rectangle(pos = (10 if x[1] == None  else x[1] 
                    ,10 if x[2] == None else x[2] ), size=(10,10) )

    def on_touch_down(self, touch):
        
        
        #colocar função para consultar empresa com clique

        
        if self.edite:
            x = int(touch.pos[0])
            while x%10 != 0:
                x = x-1    

            
            y = int(touch.pos[1])
            while y%10 != 0:
                y = y-1

            
            condicao = [self.dest_ilha_coluna,self.dest_banca_numero,self.dest_empresa]

            self.mad.update_cordenada(str(x),str(y),condicao)
            #passar parametro empresa
            self.carregar_mapa()
            self.edite = False

        else:

            
            x = int(touch.pos[0])
            while x%10 != 0:
                x = x-1    
            
            y = int(touch.pos[1])
            while y%10 != 0:
                y = y-1
            self.procura(x,y)

            


            #self.carregar_mapa()

            #colocar função para consultar empresa com clique
            #print("falha")

    
    def procura(self,x,y):
        data = self.mad.procura_cordenada(str(x),str(y))
        if data != []:
            self.dest_empresa = data[0][0]
            self.dest_ilha_coluna = data[0][1]
            self.dest_banca_numero = data[0][2]

            Tela_Mapa.muda_legenda(self,data[0][0]  )
        else:
            Tela_Mapa.muda_legenda(self,None  )

            

    pass
"""
class Tela_Mapa(Screen):
    def __init__(self, **kwargs):
        super(Tela_Mapa, self).__init__(**kwargs)
        self.dest_empresa = None
        self.dest_ilha_coluna = None
        self.dest_banca_numero = None

    def muda_legenda(self,nome):
        print('chegeui')
        print(nome)
        if nome:
            self.parent.parent.ids.legenda.title=nome
        else:
            self.parent.parent.ids.legenda.title="-"

        pass

    def editar(self):
        
        self.ids.telamapa.edite = True
        
        print(self.dest_empresa)


    def marcacao(self):

        Color(.4,.4,.4,1 , mode='rgba')

        self.line = Line(points=(0,100,1600,100), size=(4))
        self.line = Line(points=(0,500,1600,500), size=(4))


        Color(0,0,1,0.1 , mode='rgba')
            
        self.rect = Rectangle(pos = (50,100), size=(150,400))
        Color(0,1,0,0.1 , mode='rgba')
            
        self.rect = Rectangle(pos = (200,100), size=(400,100))

        Color(1,0,0,0.1 , mode='rgba')
            
        self.rect = Rectangle(pos = (200,200), size=(400,100))

        Color(1,1,0,0.1 , mode='rgba')
            
        self.rect = Rectangle(pos = (200,300), size=(400,100))
        Color(0,1,1,0.1 , mode='rgba')
            
        self.rect = Rectangle(pos = (200,400), size=(400,100))


    def seleciona_empresa(self,item,root):
    
        self.dest_empresa = item.text
        area = item.secondary_text.replace('Banca','').replace("Local",'').split(":")

        self.dest_ilha_coluna = area[1].strip()
        self.dest_banca_numero = area[2].strip()
        """
        print(self.dest_banca_numero)
        print(self.dest_ilha_coluna)
        print(self.dest_empresa)
        """

        self.ids.legenda.title = self.dest_empresa
    
        
        root.current="mapa"
        
        #print(self.ids.telamapa.lista)
        self.ids.telamapa.canvas.clear()


        
            

        with self.ids.telamapa.canvas:
            self.marcacao()
            Color(1,0,0,1 , mode='rgba')
            
            for x in self.ids.telamapa.lista:
                Color(1,0,0,1 , mode='rgba') if x[0]==self.dest_empresa else Color(0,0,1,0.5 , mode='rgba')
                self.rect = Rectangle(pos = (10 if x[1] == None  else x[1] 
                    ,10 if x[2] == None else x[2] ), size=(10,10) )

    



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
        home = MDApp.get_running_app().user_data_dir+'/'
        #home = "./"
        self.file_manager.show(home)  # output manager to the screen
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
                lista.pop(0)
                alteracoes = []
                print(len(lista))
                
                #terminar ainda não funciona

                for x in lista:

                    asd = self.mad.consulta(x[6],x[7])
                    
                    if x[14] == '':
                        x[14] = None


                    if asd[0] == [x[14]]:
                        pass
                    else:

                        self.mad.update_consulta(x[14],[x[6],x[7],asd[0][0]])
                        
    
        
    
    pass 
class Menu(Screen):
    pass 



class Busca(Screen):
    def __init__(self, **kwargs):
        super(Busca, self).__init__(**kwargs)
        self.mad = Model()
    
    def carregar_inicio(self,root,busca):
        self.busca = busca
        self.contagem = self.mad.lista_empresas_filt_count(busca)
        self.limite= 7
        self.indice= 0
        self.mostrando = self.limite + self.indice if self.contagem[0][0] > self.limite + self.indice else self.contagem[0][0]


        root.clear_widgets()

        print(self.contagem)
        self.dados = self.mad.lista_empresas_filt_limite(busca,self.limite,self.indice)
        
        for x in self.dados:
            root.add_widget(TwoLineListItem(text="Empresa: "+ "vago" if x[0] == None else x[0] ,
                secondary_text='Local: ' +str(x[1])+" Banca: "+str(x[2]),on_release=lambda x: self.parent.get_screen('mapa').seleciona_empresa(x,self.parent) ))

        root.add_widget(Ultimo_item_lista(text="Exibindo: "+ str(self.mostrando)+" de total "+str(self.contagem[0][0]),
            secondary_text='Clique para carregar mais: '
            ))

    def carregar_final(self,root, remove):

        root.remove_widget(remove)
        self.indice +=self.limite
        self.dados = self.mad.lista_empresas_filt_limite(self.busca,self.limite,self.indice)
        self.mostrando = self.limite + self.indice if self.contagem[0][0] > self.limite + self.indice else self.contagem[0][0]

        for x in self.dados:
            root.add_widget(TwoLineListItem(text="Empresa: "+ "vago" if x[0] == None else x[0] ,
                secondary_text='Local: ' +str(x[1])+" Banca: "+str(x[2]),on_release=lambda x: self.parent.get_screen('mapa').seleciona_empresa(x,self.parent) ))

        root.add_widget(Ultimo_item_lista(text="Exibindo: " + str(self.mostrando)+" de total "+str(self.contagem[0][0]),
            secondary_text='Clique para carregar mais: '
            ))



        pass







class Scroll_lista_empresas(ScrollView):
    
    pass

class Ultimo_item_lista(TwoLineListItem):
    pass




class CafeCereja_App(MDApp):
    #lista_bancas = lista
    def __init__(self, *args):
        super(CafeCereja_App, self).__init__(*args)
        


    def build(self):
        self.theme_cls.primary_palette = "Purple" #, "Red"
        self.theme_cls.primary_hue = "800"  # "500"

        return Opcao()

       


CafeCereja_App().run()

