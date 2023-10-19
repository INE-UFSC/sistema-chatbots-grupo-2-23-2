import PySimpleGUI as sg
from bots.Bot import Bot


class MenuView:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = None
        self.__bots = self.controlador.scb.bots
        self.__janela = None

        # gera-se a janela quando instanciado 
        self.gerar_janela()

    # getters e setters
    @property
    def controlador(self):
        return self.__controlador

    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, container):
        self.__container = container

    @property
    def bots(self):
        return self.__bots

    @property
    def janela(self):
        return self.__janela
    
    @janela.setter
    def janela(self, janela):
        self.__janela = janela

    # metodos
    def gerar_janela(self):

        self.__container = [
            [sg.Text("Bem vindo(a) ao Chat Bots")],
            [sg.Text("Selecione com qual bot deseja conversar: "), sg.Listbox(self.getListaBotsNome(), size=(
                20, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='listaBots')],
            [sg.Text("Bot selecionado: "), sg.Text(key="selBot")],
            [sg.Button('Conversar')]
        ]

        self.janela = sg.Window("Menu", self.__container, font=('Arial', 14))
        return self.janela

    def getListaBotsNome(self):
        nomes = []
        for i in range(len(self.bots)):
            nomes.append(self.bots[i].nome)
        return nomes

    def mostra_selBot(self, selBot):
        self.janela.Element('selBot').Update(selBot)

    def le_eventos(self):
        return self.janela.read()

    def fim(self):
        self.janela.close()
