from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        super().__init__(nome)

    @property
    def apresentacao(self):
        return f"Oiee amigo!! Meu nome é {self.nome}! Muito prazer em conhecê-lo"
 
    @property
    def mostra_comandos(self):
        pass
    
    def executa_comando(self,cmd):
        while True:
            if cmd == 1:
                return self.boas_vindas()
                
            elif cmd == 2:
                return self.__nome
            
            elif cmd == 3:
                return self.motivo_feliz()
                
            elif cmd == 4:
                return self.despedida()
                
            else:
                print("Eu ainda não aprendi a responder isso! (1 a 4)")
                continue


    def boas_vindas(self):
        return "OIIIIIIIEEEEE!!! Alguém já te falou que você está lindxs hoje 😁😁!!!"

    def despedida(self):
        return "Tchau tchau!! Nos vemos em breve !! 😁😁😁"

    def motivo_feliz(self):
        return "Estou feliz pq fui selecionado pelo processo seletivo da BRIDGE!!! YAAAYYY"
