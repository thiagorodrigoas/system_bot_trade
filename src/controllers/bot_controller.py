from ..models.entities.estrategia import Estrategia
from ..models.entities.ativo import Ativo
from ..utilities.metatrader_service import MetaTraderService

class BotController:
    def __init__(self, metatrader_service: MetaTraderService):
        self.metatrader_service = metatrader_service
        self.ativos = []
        self.estrategias = []
        self.running = False

    def adicionar_ativo(self, simbolo_ativo):
        """Adiciona um ativo ao bot para monitoramento e operações."""
        ativo = Ativo(simbolo_ativo)
        self.ativos.append(ativo)

    def adicionar_estrategia(self, estrategia: Estrategia):
        """Adiciona uma estratégia ao bot para execução."""
        self.estrategias.append(estrategia)

    def iniciar(self):
        """Inicia o bot, estabelecendo a conexão com o MetaTrader e começando as operações de trading."""
        if not self.metatrader_service.connect():
            print("Não foi possível conectar ao MetaTrader 5.")
            return False
        self.running = True
        print("Bot iniciado com sucesso.")
        self.executar_estrategias()
        return True

    def parar(self):
        """Para o bot e desconecta do MetaTrader."""
        self.running = False
        self.metatrader_service.disconnect()
        print("Bot parado.")

    def executar_estrategias(self):
        """Executa todas as estratégias adicionadas ao bot."""
        if not self.running:
            print("Bot não está rodando. Por favor, inicie o bot antes de executar estratégias.")
            return

        for estrategia in self.estrategias:
            # Implemente aqui a lógica para executar cada estratégia.
            # Isso pode incluir a análise de mercado, tomada de decisão e execução de ordens.
            pass

    # Implemente aqui métodos adicionais conforme necessário, como monitoramento de posições abertas, etc.
