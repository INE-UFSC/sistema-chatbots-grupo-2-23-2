from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None

    def boas_vindas(self):
        print("🤖🤡🤖🤡Bem-vindo ao(by grupo 2)🤡🤖🤡🤖")
        print()

    def mostra_menu(self):
        print("Bots disponiveis no momento:")
        for i in range(len(self.__lista_bots)):
            print(f"{i+1}, Bot: {self.__lista_bots[i].apresentaco()}")
        print()
    
    def escolhe_bot(self):
        indice = int(input("Digite o numero do bot desejado: "))
        self.__bot = self.__lista_bots[indice - 1]
        print()

    def mostra_comandos_bot(self):
        pass
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        pass
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        pass
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
