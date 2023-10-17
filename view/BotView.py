import PySimpleGUI as sg 
from bots.Bot import Bot

class BotView:
    def __init__(self, controlador, bot):
        self.__controlador = controlador
        self.__container = None
        self.__bot = bot
        self.__window = self.tela_bot()

    ## getters e setters
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
    def bot(self):
        return self.__bot
    @property
    def window(self):
        return self.__window

    ## metodos
    def tela_bot(self):

        self.__container = [
            [sg.Button('Voltar', size=(8, 1)) ,sg.Text(f'Pergunte alguma coisa para a {self.bot.nome}')],
            [sg.Multiline(size=(60, 5), key='resposta', autoscroll=True, disabled=True, pad=(5, 18),default_text="\n\n\n\n↓escolha uma alternativa↓")],
            [sg.Combo(self.bot.get_perguntas(), size=(48, 1), readonly=True, key="pergunta"), sg.Button('Enviar', size=(10, 1))]
        ]


        return sg.Window(f"Conversa com {self.bot.nome}", self.__container, font=("Helvetica", 16))

    def le_eventos(self):
        return self.window.read()

    def fim(self):
        self.window.close()
