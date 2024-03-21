class Estrategia:
    def __init__(self, nome, descricao=""):
        self.nome = nome
        self.descricao = descricao
        self.indicadores = []  # Lista para armazenar os indicadores usados pela estratégia

    def adicionar_indicador(self, indicador):
        self.indicadores.append(indicador)

    def __str__(self):
        return f"Estratégia: {self.nome} - {self.descricao}"
