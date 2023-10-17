from bots.BotZangado import BotZangado
from bots.BotTriste import BotTriste
from bots.BotFeliz import BotFeliz
from bots.BotGringo import BotGringo
from controle.controle import Controle

# lista de bots
bots = [BotZangado("Yoda"), BotTriste("Bolado"),
        BotFeliz("Smiley"), BotGringo("Kevin")]

# instanciacao do controle
controle = Controle(bots)
controle.inicio()
