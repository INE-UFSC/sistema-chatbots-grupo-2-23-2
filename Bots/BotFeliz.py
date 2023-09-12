from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        super().__init__(nome)


    def apresentacao(self):
        print(f"Oiee amigo!! Meu nome é {self.nome}! Muito prazer em conhecê-lo")
 
    @property
    def mostra_comandos(self):
        pass
    
    def executa_comando(self,cmd):
        while True:
            if cmd == 1:
                self.boas_vindas()
                
            elif cmd == 2:
                self.__nome
            
            elif cmd == 3:
                self.motivo_feliz()
                
            elif cmd == 4:
                self.despedida()
                
            else:
                print("Eu ainda não aprendi a responder isso! (1 a 4)")
                continue


    def boas_vindas(self):
         print("OIIIIIIIEEEEE!!! Alguém já te falou que você está lindxs hoje 😁😁!!!")

    def despedida(self):
        print("Tchau tchau!! Nos vemos em breve !! 😁😁😁")

    def motivo_feliz(self):
        print("Estou feliz pq fui selecionado pelo processo seletivo da BRIDGE!!! YAAAYYY")
