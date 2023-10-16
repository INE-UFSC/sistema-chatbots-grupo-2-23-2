from Bots.Bot import Bot
from Bots.comando import Comando

class BotFeliz(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = [Comando(1,'Por que feliz?',"Estou feliz pq fui selecionado pelo processo seletivo da BRIDGE!!! YAAAYYY")]
        
    def apresentacao(self):
        return f"Oiee amigo!! Meu nome é {self.__nome}! Muito prazer em conhecê-lo"
        
    def boas_vindas(self):
        return f" OIIIIIIIEEEEE!!! Alguém já te falou que você está lindxs hoje 😁!!!"

    def despedida(self):
        return ": Tchau tchau!! Nos vemos em breve !! 😁😁😁"