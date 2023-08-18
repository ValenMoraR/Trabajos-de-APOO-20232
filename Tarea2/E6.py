class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

PINTA_CORAZON = "Corazón"
PINTA_DIAMANTE = "Diamante"
PINTA_TREBOL = "Trébol"
PINTA_ESPADA = "Espada"

carta1 = Carta(10, PINTA_CORAZON)
carta2 = Carta(4, PINTA_TREBOL)

print(f"Carta 1: Valor {carta1.valor}, Pinta {carta1.pinta}")
print(f"Carta 2: Valor {carta2.valor}, Pinta {carta2.pinta}")
