##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    def __init__(self, nome):
        self._nome = nome
        self._comandos = {}

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @abstractmethod
    def mostra_comandos(self):
        pass
    
    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass