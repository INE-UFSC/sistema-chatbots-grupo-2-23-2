import PySimpleGUI as sg
from sistemaChatBot.SistemaChatBot import SistemaChatBot
from views.MenuView import MenuView
from views.BotView import BotView

# classe controladora
class Controle:
    def __init__(self):
        self.__scb = SistemaChatBot()
        self.__tela = None

    # getters e setters
    @property
    def scb(self):
        return self.__scb

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, tela):
        self.__tela = tela

    # metodo responsavel por iniciar
    def inicio(self):
        self.interface_menu()

    # loop da tela menu
    def interface_menu(self):
        self.tela = MenuView(self)

        # loop de eventos
        while True:
            evento, valores = self.tela.le_eventos()
            if evento == sg.WIN_CLOSED:
                self.tela.fim()
                break

            elif evento == 'listaBots':
                try:
                    self.tela.mostra_selBot(valores['listaBots'][0])
                except:
                    pass

            elif evento == 'Conversar':
                if len(valores['listaBots']) != 0:
                    bot_escolhido = None
                    for bot in self.scb.bots:
                        if bot.nome == valores['listaBots'][0]:
                            bot_escolhido = bot
                    self.tela.fim()
                    self.interface_bot(bot_escolhido)
                    break
                else:
                    self.tela.mostra_selBot("Nenhum bot selecionado")
                    sg.popup(
                        f"Selecione algum bot.", title=f"Erro",font=('Arial', 14))

    # loop tela conversa com bot
    def interface_bot(self, bot):
        self.tela = BotView(self, bot)

        #boas vindas do bot escolhido
        sg.popup(f"{bot.boas_vindas()}",title="Boas Vindas",font=('Arial', 14))

        # loop de eventos
        while True:
            evento, valores = self.tela.le_eventos()
            if evento == sg.WIN_CLOSED:
                self.tela.fim()
                break

            elif evento == 'Voltar':
                self.tela.fim()
                sg.popup(f"{bot.despedida()}",title="Despedida",font=('Arial', 14))
                self.interface_menu()
                break

            elif evento == "Enviar":
                if valores["pergunta"] == '':
                    sg.popup(
                        f"Escolha alguma pergunta.", title=f"Erro",font=('Arial', 14))

                else:
                    self.tela.janela['resposta'].update(bot.get_resposta(valores["pergunta"]))