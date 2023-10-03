from Bots.Bot import Bot
from Bots.comando import Comando

class BotZangado(Bot):
    def __init__(self, nome):
        super().__init__(nome)

    def apresentacao(self):
        print(f'{self.__nome}: Eu sou o {self.__nome}. Por favor... Vá embora... E nao me estresse.')
 
    def mostra_comandos(self):
        print('1. Bom dia\n2. Qual o seu nome?\n3. Quero um conselho.\n4. Por que você é zangado?\n5.Adeus.')
    
    def bom_dia(self):
        print(f'{self.__nome}: Bom dia pra QUEM? QUEM TA TENDO UM BOM DIA?\nQueria estar aqui nao po.')
    
    def qual_seu_nome(self):
        print(f'{self.__nome}:Meu nome é {self.__nome}, também conhecido como PutassoBot.\nTambém conhecido como quem não queria falar com você')
    
    def quero_conselho(self):
        print(f'{self.__nome}: Time que está ganhando não se mexe.\nVocê estava ganhando antes de vir conversar comigo.')
    
    def por_que(self):
        print(f'{self.__nome}: MEUS AMIGOS SÓ MARCAM O FUT AS 22H DA NOITE DESGRAÇA...\nCOMO QUE EU SAIO DE CASA AS 22H NA CHUVA?????\nCOMO????')
    
    def boas_vindas(self):
        return f'{self.__nome}: boas vindas é o CACETE. to muito PISTOLA. POR QUE VOCÊ VEM FALAR COMIGO??'

    def despedida(self):
        return f'Finalmente. Vai embora logo... Demorou demais já. TA OLHANDO O QUE AINDA VEI? VAI EMBORA.'
    
    def executa_comando(self,cmd):
        if cmd == 1:
            self.bom_dia()
        elif cmd == 2:
            self.qual_seu_nome()
        elif cmd == 3:
            self.quero_conselho()
        elif cmd == 4:
            self.por_que()
        elif cmd == 5:
            self.despedida()