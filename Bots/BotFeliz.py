from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        super().__init__(nome)

    @property
    def apresentacao_feliz(self):
        return f"Oiee amigo!! Meu nome é {self.nome}! Muito prazer em conhecê-lo"
 
    @property
    def mostra_comandos(self):
        pass
    
    def executa_comando(self,cmd):
        while True:
            if cmd == 1:
                self.boas_vindas()
                break
            elif cmd == 2:
                self.nome
                break
            elif cmd == 3:
                self.motivo_feliz
                break
            elif cmd == 4:
                self.despedida_feliz
                break
            else:
                print("Eu ainda não aprendi a responder isso! (1 a 4)")
                continue


    def boas_vindas_feliz(self):
        return "OIIIIIIIEEEEE!!! Alguém já te falou que você está lindxs hoje 😁😁!!!"

    def despedida_feliz(self):
        return "Tchau tchau!! Nos vemos em breve !! 😁😁😁"

    def motivo_feliz(self):
        return "Estou feliz pq fui selecionado pelo processo seletivo da BRIDGE!!! YAAAYYY"
