import pickle


class SistemaChatBot:
    def __init__(self, bots, arquivo):
        self.__bots = bots
        self.__arquivo = arquivo

    @property
    def bots(self):
        return self.__bots
    
    @property
    def arquivo(self):
        return self.__arquivo

    def __dump(self):
        f = open(self.__arquivo, 'wb')
        pickle.dump(self.__lista_bots, f)
        f.close()
        
    def __load(self):
        f = open(self.__arquivo, 'rb')
        self.__lista_bots = pickle.load(f)
        f.close()