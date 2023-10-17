#encoding: utf-8
from controle.controle import Controle
from bots.BotZangado import BotZangado
from bots.BotTriste import BotTriste
from bots.BotFeliz import BotFeliz
from bots.BotGringo import BotGringo 

controle = controle('botsDAO.pkl', [BotZangado("Yoda"), BotTriste("Bolado"), BotFeliz("Smiley"), BotGringo("Kevin")])
controle.inicio()
