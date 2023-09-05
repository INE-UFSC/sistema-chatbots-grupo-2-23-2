##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    
    @abstractmethod
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {}
    
    @property
    def nome(self):
        pass

    @nome.setter
    def nome(nome):
        pass

    @property
    def mostra_comandos(self):
        pass

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass
