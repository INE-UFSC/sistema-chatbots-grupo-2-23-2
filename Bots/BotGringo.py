from Bots.Bot import Bot

class BotGringo(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__comandos = {}

    def apresentacao(self):
         print(f'{self.__nome}: Hello! My nome is {self.__nome}. Im from America aka USA!!')
 
    def mostra_comandos(self):
        print('1. Bom dia\n2. Qual o seu nome?\n3. Quero um conselho.\n4. Por que você veio ao Brasil?\n5.Adeus.')
    
    def bom_dia(self):
        print(f'{self.__nome}: Bom dia for you too minha amigo! Lets buy coisas real is really barato')
    
    def qual_seu_nome(self):
        print(f'{self.__nome}:My nome is {self.__nome}, and Im still aprendendo a sua língua. Spanish is really hard! ')
    
    def quero_conselho(self):
        print(f'{self.__nome}: Continuar morando em Brasil my friend!! Aqui is really good para viver you know, you have caipirinha, samba e futebol every day!')
    
    def por_que_gringo(self):
        print(f'{self.__nome}: Eu vim para Brasil to visit the praias of Rio de Janeiro, like Copacabana and Lebron! Brasil has the most bonita capital of the mundo!')
    
    def boas_vindas(self):
        print(f'{self.__nome}: Welcome meu amigo! Qual é o boa de hoje? (Did i say that right ?)')

    def despedida(self):
        print(f'Bye bye my friend! Eu estar indo embora too! Im going to the praia right now, see ya later!')
        
    def executa_comando(self,cmd):
        if cmd == 1:
            self.bom_dia()
        elif cmd == 2:
            self.qual_seu_nome()
        elif cmd == 3:
            self.quero_conselho()
        elif cmd == 4:
            self.por_que_gringo()
        elif cmd == 5:
            self.despedida()
