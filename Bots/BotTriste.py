from bots.Bot import Bot
from bots.comando import Comando

class BotTriste(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__comandos = [ Comando( 'Bom dia','É, até que o dia está sendo bom... Só tenho 10 listas de cálculo pra fazer...Nem chorei hoje ainda...'),
                           Comando('Quero conselho','Se um dia você quiser marcar um fut com os amigos, marque antes das 22h...Num dia que não está chovendo também... '),
                           Comando('Por que triste?','Zerei a prova de calculo ontem, a morena me deixou semana passada e eu pisei num lego hoje de manhã... Pior dia da minha vida')
                         ]
    @property
    def comandos(self):
        return self.__comandos 

    def apresentacao(self):
        return f'Eu sou o {self.__nome}. Por favor, não se incomode com a minha tristeza... Não se incomode comigo na verdade. Eu estou bem :c'
        
    def boas_vindas(self):
        return f'Boas vindas!!! Você quer ser meu amigo? Eu não tenho nenhum amigo por enquanto :c'

    def despedida(self):
        return f'Não... não me deixe aqui... Eu achei que você era meu amigo...'