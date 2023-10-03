from Bots.Bot import Bot
from Bots.comando import Comando

class BotGringo(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self._comandos = [  Comando(1,"Bom dia", "Bom dia for you too minha amigo! Lets buy coisas real is really barato"),
                            Comando(2, 'Quero conselho', 'Continuar morando em Brasil my friend!! Aqui is really good para viver you know, you have caipirinha, samba e futebol every day!'),
                            Comando(3, 'Por que gringo?', 'Eu vim para Brasil to visit the praias of Rio de Janeiro, like Copacabana and Lebron! Brasil has the most bonita capital of the mundo')
                            ]
        
    def apresentacao(self):
        return f': Hello! My nome is {self.__nome()}. Im from America aka USA!!'
 
    def boas_vindas(self):
        return f'Welcome meu amigo! Qual é o boa de hoje? (Did i say that right ?)'

    def despedida(self):
        return f'Bye bye my friend! Eu estar indo embora too! Im going to the praia right now, see ya later!'

        