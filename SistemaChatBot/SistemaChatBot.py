import PySimpleGUI as sg
from Bots.Bot import Bot
from ViewChatBot import ViewChatBot
from Bots.BotDAO import BotDAO

class SistemaChatBot():
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__telaBots = ViewChatBot()
        self.__BotsDAO = BotDAO()
        for bot in lista_bots:
            if not isinstance(bot, Bot):
                raise ValueError("A lista deve conter apenas Bots.")
        self.__lista_bots = lista_bots
        self.__bot = None

    @property
    def telaBots(self):
        return self.__telaBots
    
    @property
    def botsDAO(self):
        return self.__BotsDAO

    def boas_vindas(self):
        print(f"🤖🤖🤖Bem-vindo a {self.__empresa}🤖🤖🤖")
        print()

    def mostra_menu(self):
        print("Bots disponiveis no momento:")
        for i in range(len(self.__lista_bots)):
            print(f"{i+1}, Bot:",end=' ')
            self.__lista_bots[i].apresentacao()
        print()
    
    def escolhe_bot(self):
        indice = int(input("Digite o numero do bot desejado: "))
        if indice == -1:
            return False
        self.__bot = self.__lista_bots[indice - 1]
        print()
        return True
        
    def mostra_comandos_bot(self):
        self.__bot.mostra_comandos()

    def le_envia_comando(self):
        while True:
            cmd = int(input('Escolha um numero:'))
            if cmd == -1:
                break
            self.__bot.executa_comando(cmd)
            
    def inicio(self):
        self.boas_vindas()
        while True:
            self.mostra_menu()
            if not self.escolhe_bot():
                break  
            self.__bot.boas_vindas()
            self.mostra_comandos_bot()
            self.le_envia_comando()
            self.__bot.despedida()
            ##ao sair mostrar a mensagem de despedida do bot

    def inicia(self):
        # Loop de eventos
        self.boas_vindas()
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False
                self.telaCliente.fim()
                break

            elif event == 'Comando 1':
                try:
                    values["codigo"] = int(values["codigo"])
                    if values["nome"] != "":
                        resultado = self.adiciona_cliente(
                            values["codigo"], values["nome"])
                    else:
                        resultado = "Preencha o nome"
                except:
                    resultado = "Digite um número int no codigo"

            elif event == 'Consultar':
                if (values["nome"] == "") and (values["codigo"] == ""):
                    resultado = "Preencha pelo menos uma caixinha"
                elif values["codigo"] != "":
                    try:
                        values["codigo"] = int(values["codigo"])
                        resultado = self.busca_codigo(values["codigo"])
                    except Exception:
                        resultado = "Codigo deve ser um numero inteiro"
                else:
                    resultado = self.busca_nome(values["nome"])
            
            elif event == 'Remover':
                if (values["nome"] == "") and (values["codigo"] == ""):
                    resultado = "Preencha pelo menos uma caixinha"
                elif values["codigo"] != "":
                    try:
                        values["codigo"] = int(values["codigo"])
                        self.remover_codigo(values["codigo"])
                        resultado = "Cliente removido"
                        
                    except Exception:
                        resultado = "Codigo deve ser um numero inteiro"
                        
            elif event == 'Ver todos os clientes':
                resultado = ''
                for i in (self.__BotsDAO.get_all()):
                    resultado += f'{i.__str__()}\n'
                    

            # retirar essa condicao????
            if resultado != '':
                dados = str(resultado)
                self.telaBots.mostra_resultado(dados)

