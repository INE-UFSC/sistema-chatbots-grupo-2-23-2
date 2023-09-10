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
        return 'BotZangado: Eu sou o BotZangado. Por favor... Vá embora... E nao me estresse.'
 
    def mostra_comandos(self):
        return '1. Bom dia\n2. Qual o seu nome?\n3. Quero um conselho.\n4. Por que você é zangado?\n4.Adeus.'
    
    def bom_dia(self):
        return 'bom dia pra quem? queria estar aqui nao po.'
    
    def qual_seu_nome(self):
        return 'Meu nome é BotZangado, também conhecido como BotPistola ou PutassoBot'
    
    def quero_conselho(self):
        return 
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        return 'BotZangado: boas vindas é o caralho porra. to muito puto desgraça. va toma no cu'

    def despedida(self):
        pass