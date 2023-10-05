##implemente as seguintes classes
from Bots.comando import Comando
from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos
    
    def mostra_comandos(self):
        string = f''
        for comando in self.__comandos:
            string += f'Comando: {comando.id()} = {comando.msg()}\n'
        return string
    
    def executa_comando(self,cmd):
        for comando in self.__comandos:
            if cmd == comando.id() or cmd == comando.msg():
                return comando.getRandomResposta()

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass