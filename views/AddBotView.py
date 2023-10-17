import PySimpleGUI as sg
from bots.Bot import Bot


class AddBotView:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = None
        self.__window = self.adiciona_bot()

    #Decorators
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
    def window(self):
        return self.__window

    #Methods
    
    def adiciona_bot(self):
        self.__container = [
            [sg.Text('Nome do Bot'), sg.InputText("", key = 'nome_add')],
            [sg.Text('Apresentação do Bot'), sg.InputText("", key = 'apresentacao_add')],
            [sg.Text('Boas vindas'), sg.InputText("", key = 'boasVindas_add')],
            [sg.Text('Despedida'), sg.InputText("", key = 'despidada_add')],
            [sg.Button('Adicionar Bot'), sg.Button('Voltar')]
        ]
        return sg.Window(f"Adicionar Bot", self.__container, font=('Arial', 14))

    def le_eventos(self):
        return self.window.read()

    def fim(self):
        self.window.close()
