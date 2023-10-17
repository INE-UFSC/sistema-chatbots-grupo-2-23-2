import PySimpleGUI as sg
from sistemaChatBot.SistemaChatBot import SistemaChatBot
from views.MenuView import MenuView
from views.BotView import BotView


class Controle:
    def __init__(self, bots):
        self.__scb = SistemaChatBot(bots, 'bots.pkl')
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

    # metodos
    def inicio(self):
        self.interface_menu()

    # menu
    def interface_menu(self):
        self.__tela = MenuView(self)

        # loop de eventos
        rodando = True
        while rodando:
            event, values = self.tela.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False
                self.tela.fim()
                break

            elif event == 'listaBots':
                try:
                    self.tela.mostra_selBot(values['listaBots'][0])
                except:
                    pass

            elif event == 'Conversar':
                if len(values['listaBots']) != 0:
                    bot_escolhido = None
                    for bot in self.scb.bots:
                        if bot.nome == values['listaBots'][0]:
                            bot_escolhido = bot
                    self.tela.fim()
                    self.interface_bot(bot_escolhido)
                else:
                    self.tela.mostra_selBot("Nenhum bot selecionado")
                    sg.PopupError(
                        f"Selecione algum bot.", title=f"Erro",font=('Arial', 14))

    # conversa com o bot
    def interface_bot(self, bot):
        sg.popup(f"{bot.boas_vindas()}",title="Boas Vindas",font=('Arial', 14))

        self.tela = BotView(self, bot)

        # loop de eventos
        rodando = True
        while rodando:
            event, values = self.tela.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False
                self.tela.fim()
                break

            elif event == 'Voltar':
                self.tela.fim()
                sg.popup(f"{bot.despedida()}",title="Despedida",font=('Arial', 14))
                self.interface_menu()

            elif event == "Enviar":
                if values["pergunta"] == '':
                    sg.PopupError(
                        f"Escolha alguma pergunta.", title=f"Erro",font=('Arial', 14))

                else:
                    self.tela.window['resposta'].update(bot.get_resposta(values["pergunta"]))
