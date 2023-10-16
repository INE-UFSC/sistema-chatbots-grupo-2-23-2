from Bots.Bot import Bot
from Bots.comando import Comando

class BotZangado(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = [Comando(1,'Bom dia','Bom dia pra QUEM? QUEM TA TENDO UM BOM DIA?\nQueria estar aqui nao po.')
                          ,Comando(2,'Quero conselho','Time que está ganhando não se mexe. Você estava ganhando antes de vir conversar comigo.')
                          ,Comando(3,'Por que zangado?','MEUS AMIGOS SÓ MARCAM O FUT AS 22H DA NOITE DESGRAÇA...COMO QUE EU SAIO DE CASA AS 22H NA CHUVA?????COMO????')
                          ]

    def apresentacao(self):
        print(f'{self.__nome}: Eu sou o {self.__nome}. Por favor... Vá embora... E nao me estresse.')
    
    def boas_vindas(self):
        return f'{self.__nome}: boas vindas é o CACETE. to muito PISTOLA. POR QUE VOCÊ VEM FALAR COMIGO??'

    def despedida(self):
        return f'Finalmente. Vai embora logo... Demorou demais já. TA OLHANDO O QUE AINDA VEI? VAI EMBORA.'