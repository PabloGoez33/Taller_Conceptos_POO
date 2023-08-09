class Carta:

    PINTA_DIAMANTE = "DIAMANTE"
    PINTA_TREBOL = "TREBOL"
    PINTA_CORAZON = "CORAZON"
    PINTA_PICA = "PICA"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta