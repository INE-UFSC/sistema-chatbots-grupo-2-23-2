import PySimpleGUI as sg


class ViewChatBot():
    def __init__(self, controlador, listaBots):
        self.__controlador = controlador
        self.__listaBots = listaBots
        self.__container = None
        self.__window = self.tela_menu()

    @property
    def controlador(self):
        return self.__controlador
    
    @property
    def listaBots(self):
        return self.__listaBots  

    @property
    def window(self):
        return self.__window

    @property
    def container(self):
        return self.__container
    
    @container.setter
    def container(self, container: list):
        self.__container = container
    
    def getListaBotsNome(self):
        nomes = []
        for i in range(len(self.listaBots)):
            nomes.append(self.listaBots[i].nome)
        return nomes

    def tela_menu(self):

        #linha0 = [sg.Im("img.png"), sg.InputText("", key="nome")]
        linha0 = [sg.Text("Bem vindo(a) ao Chat Bots")]
        linha1 = [sg.Text("Selecione com qual bot deseja conversar: "), sg.Listbox(self.getListaBotsNome(), size = (20, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='listaBots')]
        linha2 = [sg.Text("Bot selecionado: "), sg.Text(key = "selBot")]
        self.__container = [linha0, linha1, linha2]

        return sg.Window("Chat Bots", self.__container, font=("Helvetica", 14))

    def tela_bots(self, mensagens):

        linha0 = [sg.Text("Conversa com o Bot")]
        linha1 = [sg.Text("Lista de perguntas: ")]
        linha2 = [sg.Listbox(mensagens, size=(20, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='ListaPerguntas', ), sg.Button('Perguntar', key='Perguntar')]
        linha3 = [sg.Text("Resposta do Bot: "), sg.Text(key = "RespBot"), sg.Button(key = "Conversar")]
        self.__container = [linha0, linha1, linha2, linha3]

        return sg.Window("", self.__container, font=("Helvetica", 14))

    def mostra_selBot(self, selBot):
        self.__window.Element('selBot').Update(selBot)
        
    def mostra_respBot(self, RespBot):
        self.__window.Element('RespBot').Update(RespBot)

    ##^^fazer funcao geral que atualiza qualquer elemento da tela, passando ele como parametro


    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()