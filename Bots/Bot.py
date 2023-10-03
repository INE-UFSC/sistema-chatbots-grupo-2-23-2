##implemente as seguintes classes
from Bots.comando import Comando
from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    def __init__(self, nome):
        self._nome = nome
        self._comandos = []

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def mostra_comandos(self):
        string = f''
        for comando in self._comandos:
            string += f'Comando: {comando.id()} = {comando.msg()}\n'
        return string
    
    def executa_comando(self,cmd):
        for comando in self._comandos:
            if cmd == comando.id() or cmd == comando.msg():
                return comando.getRandomResposta()

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass