import PySimpleGUI as sg
from Bots.BotDAO import BotDAO
from Bots.Bot import Bot
from SistemaChatBot.ViewChatBot import ViewChatBot


class SistemaChatBot():
    def __init__(self, archive, listaBots):
        self.__listaBots = listaBots
        self.__telaBots = ViewChatBot(self, listaBots)
        self.__botsDAO = BotDAO(f'{archive}')


    @property
    def telaBots(self):
        return self.__telaBots
    
    @property
    def botsDAO(self):
        return self.__botsDAO
    
    @property
    def listaBots(self):
        return self.__listaBots

    def boas_vindas(self):
        pass

    def mostra_menu(self):
        print("Bots disponiveis no momento:")
        for i in range(len(self.__botsDAO)):
            print(f"{i+1}, Bot:",end=' ')
            
        print()

        # try:
        #     for i in len(self.botsDAO.comandos):
        #         comando = Comando().getAttr(msg) = "Qual seu nome ?"
    
    # def escolhe_bot(self):
    #     indice = int(input("Digite o numero do bot desejado: "))
    #     if indice == -1:
    #         return False
    #     self.__botsDAO = self.__lista_bots[indice - 1]
    #     print()
    #     return True
        
    def mostra_comandos_bot(self):
        self.__botsDAO.mostra_comandos()

    def le_envia_comando(self):
        while True:
            cmd = int(input('Escolha um numero:'))
            if cmd == -1:
                break
            self.__botsDAO.executa_comando(cmd)
            
    def inicio(self):
        self.boas_vindas()
        while True:
            self.mostra_menu()
            if not self.escolhe_bot():
                break  
            self.mostra_comandos_bot()
            self.le_envia_comando()
            ##ao sair mostrar a mensagem de despedida do bot

    def inicia(self):
        # Loop de eventos
        self.boas_vindas()
        rodando = True
        while rodando:
            event, values = self.__telaBots.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False
                self.telaBots.fim()
                break

            elif event == 'listaBots':
                try:
                    self.__telaBots.mostra_selBot(values['listaBots'][0])
                    
                except:
                    pass
                
            elif event == 'listaPerguntas':
                try:
                    self.__telaBots.mostra_selBot(str(values['ListaPerguntas']))
                    
                except:
                    pass

            # elif event == 'Consultar':
            #     if (values["nome"] == "") and (values["codigo"] == ""):
            #         resultado = "Preencha pelo menos uma caixinha"
            #     elif values["codigo"] != "":
            #         try:
            #             values["codigo"] = int(values["codigo"])
            #             resultado = self.busca_codigo(values["codigo"])
            #         except Exception:
            #             resultado = "Codigo deve ser um numero inteiro"
            #     else:
            #         resultado = self.busca_nome(values["nome"])
            
            # elif event == 'Remover':
            #     if (values["nome"] == "") and (values["codigo"] == ""):
            #         resultado = "Preencha pelo menos uma caixinha"
            #     elif values["codigo"] != "":
            #         try:
            #             values["codigo"] = int(values["codigo"])
            #             self.remover_codigo(values["codigo"])
            #             resultado = "Cliente removido"
                        
            #         except Exception:
            #             resultado = "Codigo deve ser um numero inteiro"
                        
            # elif event == 'Ver todos os clientes':
            #     resultado = ''
            #     for i in (self.__BotsDAO.get_all()):
            #         resultado += f'{i.__str__()}\n'
                    

            # retirar essa condicao????
            # if resultado != '':
            #     dados = str(resultado)
            #     self.telaBots.mostra_resultado(dados)

