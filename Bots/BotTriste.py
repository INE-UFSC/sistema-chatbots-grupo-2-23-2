from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f'{self.__nome}: Eu sou o {self.__nome}. Por favor, não se incomode com a minha tristeza\nNão se incomode comigo na verdade.\nEu estou bem :c'
 
    def mostra_comandos(self):
        return '1. Bom dia\n2. Qual o seu nome?\n3. Quero um conselho.\n4. Por que você é triste?\n5.Adeus.'
    
    def bom_dia(self):
        return f'{self.__nome}: É, até que o dia está sendo bom... \nSó tenho 10 listas de cálculo pra fazer...\nNem chorei hoje ainda...'
    
    def qual_seu_nome(self):
        return f'{self.__nome}: Meu nome é {self.__nome}... Você pode me chamar de Tristonho se quiser...'
    
    def quero_conselho(self):
        return f'{self.__nome}: Se um dia você quiser marcar um fut com os amigos, marque antes das 22h...\nNum dia que não está chovendo também... '
    
    def por_que_triste(self):
        return f'{self.__nome}: Zerei a prova de calculo ontem, a morena me deixou semana passada e eu pisei num lego hoje de manhã... \nPior dia da minha vida'
    
    def executa_comando(self,cmd):
        if cmd == 1:
            return self.bom_dia()
        elif cmd == 2:
            return self.qual_seu_nome()
        elif cmd == 3:
            return self.quero_conselho()
        elif cmd == 4:
            return self.por_que_triste()
        elif cmd == 5:
            return self.despedida()


    def boas_vindas(self):
        return f'{self.__nome}: Boas vindas! \nVocê quer ser meu amigo? \nEu não tenho nenhum amigo por enquanto :c'

    def despedida(self):
        return f'{self.__nome}: Não... não me deixe aqui... Eu achei que você era meu amigo...'