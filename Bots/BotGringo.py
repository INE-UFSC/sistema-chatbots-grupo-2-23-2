from bots.Bot import Bot
from bots.comando import Comando

class BotGringo(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = [ Comando("Bom dia", "Bom dia for you too minha amigo! Lets buy coisas real is really barato"),
                           Comando('Quero conselho', 'Continuar morando em Brasil my friend!! Aqui is really good para viver you know, you have caipirinha, samba e futebol every day!'),
                           Comando('Por que gringo?', 'Eu vim para Brasil to visit the praias of Rio de Janeiro, like Copacabana and Lebron! Brasil has the most bonita capital of the mundo')
                         ]
    @property
    def comandos(self):
        return self.__comandos    

    def apresentacao(self):
        return f'Hello! My nome is {self.__nome()}. Im from America aka USA!!'
 
    def boas_vindas(self):
        return f'Welcome meu amigo! Qual é o boa de hoje? (Did i say that right ?)'

    def despedida(self):
        return f'Bye bye my friend! Eu estar indo embora too! Im going to the praia right now, see ya later!'

        