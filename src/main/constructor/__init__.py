from utilities.metatrader_service import MetaTraderService
from models.configs.bot_config import BotConfig
from controllers.bot_controller import BotController

class BotConstructor:
    def __init__(self):
        self.bot_config = BotConfig()
        self.metatrader_service = MetaTraderService(self.bot_config)
        self.bot_controller = BotController(self.metatrader_service)

    def initialize_bot(self):
        if self.metatrader_service.connect():
            print("Conexão com MetaTrader 5 estabelecida com sucesso.")
        else:
            print("Falha ao conectar com MetaTrader 5.")
            return False

        # Inicialize aqui outras configurações necessárias para o bot
        # Exemplo: Carregar estratégias, definir ativos, etc.

        print("Bot inicializado com sucesso.")
        return True

if __name__ == '__main__':
    constructor = BotConstructor()
    constructor.initialize_bot()