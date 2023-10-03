import random

class Comando:
    def __init__(self, id, msg, respostas = []):
        self.__id = id
        self.__msg = msg
        self.__respostas = respostas
        
    @property
    def id(self):
        return self.__id

    @property
    def mensagem(self):
        return self.__msg

    def getRandomResposta(self):
        return random.choice(self.__respostas)
    
    def addResposta(self, resposta):
        self.__respostas.append(resposta)

    def delResposta(self, resposta):
        if resposta in self.__respostas:
            del self.__respostas[resposta]