class BotConfig:
    def __init__(self):
        # Exemplos de configurações. Estas podem ser expandidas conforme necessário.
        self.ativos = ['EURUSD', 'USDJPY']  # Ativos padrão para negociação
        self.timeframe = 'H1'  # Timeframe padrão para análise
        self.estrategia = 'EstrategiaPadrao'  # Nome da estratégia padrão a ser utilizada
        self.max_trades_abertos = 5  # Número máximo de trades abertos simultaneamente
        self.risk_management = True  # Ativar ou desativar gestão de risco
        self.stop_loss = 50  # Valor padrão do stop loss em pips
        self.take_profit = 100  # Valor padrão do take profit em pips

        # Adicione aqui outras configurações necessárias, como parâmetros para a conexão com o MetaTrader, etc.

    def load_from_file(self, config_file):
        # Método para carregar configurações a partir de um arquivo.
        # Implemente a lógica para ler um arquivo de configuração e atualizar as propriedades desta classe.
        pass

    def save_to_file(self, config_file):
        # Método para salvar as configurações atuais em um arquivo.
        # Útil para manter as configurações entre as sessões de negociação.
        pass
