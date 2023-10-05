import PySimpleGUI as sg


class ViewChatBot():
    def __init__(self, controlador, listaBots):
        self.__controlador = controlador
        self.__window = self.tela_menu()
        self.__container = None
        self.__listaBots = listaBots

    @property
    def controlador(self):
        return self.__controlador

    @property
    def window(self):
        return self.__window

    @property
    def container(self):
        return self.__container
    
    @property
    def listaBots(self):
        return self.__listaBots
    
    @property
    def listaBotsNome(self):
        nomes = []
        for i in range(len(self.listaBots)):
            nomes.append(self.listaBots[i].nome)
        return nomes

    @container.setter
    def container(self, container: list):
        self.__container = container

    def tela_menu(self):

        #linha0 = [sg.Im("img.png"), sg.InputText("", key="nome")]
        linha0 = [sg.Text("Bem vindo(a) ao Chat Bots")]
        linha1 = [sg.Text("Lista de Bots: "), sg.Listbox(self.listaBotsNome, size=(20, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='listaBots')]
        linha2 = [sg.Text("Selecione com qual bot deseja conversar: "), sg.InputText("", key = "selBot")]
        self.__container = [linha0, linha1, linha2]

        return sg.Window("Chat Bots", self.__container, font=("Helvetica", 14))

    def tela_bots(self):

        #linha0 = [sg.Im("img.png"), sg.InputText("", key="nome")]
        linha0 = [sg.Text("Conversa com o Bot")]
        linha1 = [sg.Text("Lista de Bots: "), sg.Listbox(self.listaBots, size=(20, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='listaBots')]
        linha2 = [sg.Text("Selecione com qual bot deseja conversar: "), sg.InputText("", key = "selBot")]
        self.__container = [linha0, linha1, linha2]

        return sg.Window("Chat Bots", self.__container, font=("Helvetica", 14))

    def mostra_resultado(self, resultado):
        self.__window.Element('resultado').Update(resultado)

    def mostra_listaBots(self, listaBots):
        listaBotsNomes= []
        for i in range(len(listaBots)):
            listaBotsNomes.append(listaBots[i].nome)
            
        self.__window.Element("listaBots").Update(listaBotsNomes)
        print(listaBotsNomes)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()