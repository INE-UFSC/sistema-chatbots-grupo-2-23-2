import pickle


class SistemaChatBot:
    def __init__(self, bots, arquivo):
        self.__bots = bots
        self.__arquivo = arquivo
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    @property
    def bots(self):
        return self.__bots
    
    @bots.setter
    def bots(self, bots):
        self.__bots = bots
    
    @property
    def arquivo(self):
        return self.__arquivo

    def __dump(self):
        f = open(self.__arquivo, 'wb')
        pickle.dump(self.bots, f)
        f.close()
        
    def __load(self):
        f = open(self.__arquivo, 'rb')
        self.bots = pickle.load(f)
        f.close()