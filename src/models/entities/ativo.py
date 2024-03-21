class Ativo:
    def __init__(self, simbolo, nome):
        self.simbolo = simbolo
        self.nome = nome

    def __str__(self):
        return f"Ativo: {self.nome} ({self.simbolo})"
