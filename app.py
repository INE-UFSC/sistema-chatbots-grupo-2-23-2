#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz
from Bots.BotGringo import BotGringo 

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Bolado"), BotFeliz("Smiley"), BotGringo("Kevin")]


sys = scb.SistemaChatBot('botsDAO.pkl')
sys.inicia()
