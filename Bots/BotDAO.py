from bots.DAO import DAO
from bots.Bot import Bot


class BotDAO(DAO):
    def __init__(self, source=""):
        super().__init__(source)
        
    
    def add(self, bot: Bot):
        if ((bot is not None) and (isinstance(bot.nome, str)) and isinstance(bot, Bot) and isinstance(bot.comandos, list)):
            # super().add(bot.codigo, bot)
            pass

    def get(self, codigo: int):
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, codigo: int):
        if isinstance(codigo, int):
            super().remove(codigo)
