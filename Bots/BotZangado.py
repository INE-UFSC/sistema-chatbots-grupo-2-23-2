from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f'{self.__nome}: Eu sou o {self.__nome}. Por favor... Vá embora... E nao me estresse.'
 
    def mostra_comandos(self):
        return '1. Bom dia\n2. Qual o seu nome?\n3. Quero um conselho.\n4. Por que você é zangado?\n5.Adeus.'
    
    def bom_dia(self):
        return f'{self.__nome}: Bom dia pra QUEM? QUEM TA TENDO UM BOM DIA?\nQueria estar aqui nao po.'
    
    def qual_seu_nome(self):
        return f'{self.__nome}:Meu nome é {self.__nome}, também conhecido como PutassoBot.\nTambém conhecido como quem não queria falar com você'
    
    def quero_conselho(self):
        return f'{self.__nome}: Time que está ganhando não se mexe.\nVocê estava ganhando antes de vir conversar comigo.'
    
    def por_que_zangado(self):
        return f'{self.__nome}: MEUS AMIGOS SÓ MARCAM O FUT AS 22H DA NOITE DESGRAÇA...\nCOMO QUE EU SAIO DE CASA AS 22H NA CHUVA?????\nCOMO????'
    
    def executa_comando(self,cmd):
        if cmd == 1:
            print(self.bom_dia())
        elif cmd == 2:
            print(self.qual_seu_nome())
        elif cmd == 3:
            print(self.quero_conselho())
        elif cmd == 4:
            print(self.por_que_zangado())
        elif cmd == 5:
            print(self.despedida())

    def boas_vindas(self):
        return f'{self.__nome}: boas vindas é o CACETE. to muito PISTOLA. POR QUE VOCÊ VEM FALAR COMIGO??'

    def despedida(self):
        return f'Finalmente. Vai embora logo... Demorou demais já. TA OLHANDO O QUE AINDA VEI? VAI EMBORA.'