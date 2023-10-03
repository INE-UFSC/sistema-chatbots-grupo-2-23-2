from Bots.Bot import Bot
from Bots.comando import Comando

class BotFeliz(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        
    def mostra_comandos(self):
        pass
        
    def qual_seu_nome(self):
        print(f'{self.__nome}: Meu nome é {self.__nome}!!!! Eu ADORO meu nome, ADORO ADORO ADORO!!')

    def apresentacao(self):
        print(f"{self.__nome}: Oiee amigo!! Meu nome é {self.__nome}! Muito prazer em conhecê-lo")
        
    def boas_vindas(self):
         print(f"{self.__nome}: OIIIIIIIEEEEE!!! Alguém já te falou que você está lindxs hoje 😁😁!!!")

    def despedida(self):
        print(f"{self.__nome}: Tchau tchau!! Nos vemos em breve !! 😁😁😁")

    def motivo_feliz(self):
        print(f"{self.__nome}: Estou feliz pq fui selecionado pelo processo seletivo da BRIDGE!!! YAAAYYY")

    def executa_comando(self,cmd):
        if cmd == 1:
            self.boas_vindas()
            
        elif cmd == 2:
            self.qual_seu_nome()
        
        elif cmd == 3:
            self.motivo_feliz()
            
        elif cmd == 4:
            self.despedida()
            
        else:
            print("Eu ainda não aprendi a responder isso! (1 a 4)")
            
