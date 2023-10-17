from bots.Bot import Bot
from bots.comando import Comando


class BotFeliz(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = [Comando('Por que feliz?', "Estou feliz pq fui selecionado pelo processo seletivo da BRIDGE!!! YAAAYYY"),
                           Comando('O que você gosta de fazer nas horas vagas?',
                                   'Nas horas vagas, eu gosto de aprender coisas novas e ajudar as pessoas com suas dúvidas. É muito divertido!'),
                           Comando('Qual é o seu filme favorito?',
                                   'Não posso assistir filmes, mas se pudesse, talvez escolhesse um filme de ficção científica emocionante!')
                           ]

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return f"Oiee amigo!! Meu nome é {self.__nome}! Muito prazer em conhecê-lo"

    def boas_vindas(self):
        return f" OIIIIIIIEEEEE!!! Alguém já te falou que você está lindxs hoje 😁!!!"

    def despedida(self):
        return ": Tchau tchau!! Nos vemos em breve !! 😁😁😁"
