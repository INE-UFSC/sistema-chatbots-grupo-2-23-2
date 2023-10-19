import PySimpleGUI as sg
from bots.Bot import Bot


class BotView:
    def __init__(self, controlador, bot):
        self.__controlador = controlador
        self.__container = None
        self.__janela = None
        self.__bot = bot

        # gera-se a janela quando instanciado 
        self.gerar_janela(bot)

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
    def janela(self):
        return self.__janela
    
    @janela.setter
    def janela(self, janela):
        self.__janela = janela

    @property
    def bot(self):
        return self.__bot

    # gera e retorna a janela
    def gerar_janela(self, bot):
        self.__container = [
            [sg.Button('Voltar', size=(8, 1)), sg.Text(
                f'Pergunte alguma coisa para a {self.bot.nome}')],
            [sg.Multiline(size=(60, 5), key='resposta', autoscroll=True, disabled=True, pad=(
                5, 18), default_text="\n\n\n\n↓escolha uma alternativa↓")],
            [sg.Combo(self.bot.get_perguntas(), size=(48, 1), readonly=True,
                      key="pergunta"), sg.Button('Enviar', size=(10, 1))]
        ]

        self.janela = sg.Window(f"Conversa com {self.bot.nome}", self.__container, font=('Arial', 14))
        return self.janela

    # le eventos da janela 
    def le_eventos(self):
        return self.janela.read()

    def fim(self):
        self.janela.close()
