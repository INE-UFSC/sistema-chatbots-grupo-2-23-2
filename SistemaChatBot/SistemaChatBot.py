from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        for bot in lista_bots:
            if not isinstance(bot, Bot):
                raise ValueError("A lista deve conter apenas Bots.")
        self.__lista_bots = lista_bots
        self.__bot = None

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

