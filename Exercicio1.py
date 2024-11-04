class animal():
    def __init__(self, tipo, raca, porte):
        self.tipo = tipo
        self.raca = raca
        self.porte = porte

class felinos(animal):
    def __init__(self, tipo, raca, porte, idade, peso):
        super().__init__(tipo, raca, porte)
        self.idade = idade
        self.peso = peso

gato = felinos('GATO', 'SIAMÊS', 'PQ', 8, 10.3)
leao = felinos('LEÃO', 'LEÃO', 'GD', 4, 56.2)

print("TIPO: ", gato.tipo, " - RAÇA: ", gato.raca, " - PORTE: ", gato.porte, " - IDADE: ", gato.idade, " - PESO: ", gato.peso)
print("TIPO: ", leao.tipo, " - RAÇA: ", leao.raca, " - PORTE: ", leao.porte, " - IDADE: ", leao.idade, " - PESO: ", leao.peso)