import PySimpleGUI as sg
from bots.Bot import Bot


class MenuView:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = None
        self.__bots = self.controlador.scb.bots
        self.__window = self.tela_menu()

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
    def window(self):
        return self.__window

    # metodos
    def tela_menu(self):

        self.__container = [
            [sg.Text("Bem vindo(a) ao Chat Bots")],
            [sg.Text("Selecione com qual bot deseja conversar: "), sg.Listbox(self.getListaBotsNome(), size=(
                20, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='listaBots')],
            [sg.Text("Bot selecionado: "), sg.Text(key="selBot")],
            [sg.Button('Conversar')]
        ]

        return sg.Window("Menu", self.__container, font=("Helvetica", 16))

    def getListaBotsNome(self):
        nomes = []
        for i in range(len(self.bots)):
            nomes.append(self.bots[i].nome)
        return nomes

    def mostra_selBot(self, selBot):
        self.window.Element('selBot').Update(selBot)

    def le_eventos(self):
        return self.window.read()

    def fim(self):
        self.window.close()
