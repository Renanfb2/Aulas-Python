class veiculo():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class motocicleta(veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindrada = cilindrada

veic = veiculo('AUTOMÓVEL', '234AJ5784HJHHD30987', 'GM', 'CELTA', '2014')
# print(vars(veic))
print("Tipo: ", veic.tipo, "- Chassi: ", veic.chassi, " - Marca: ", veic.marca, " - Modelo: ", veic.modelo, " - Ano: ", veic.ano)
moto = motocicleta('MOTO', '43HHF342JH444554JJ2', 'HONDA', 'BIZ', '2021', 100)
# print(vars(moto))
print("Tipo: ", moto.tipo, "- Chassi: ", moto.chassi, " - Marca: ", moto.marca, " - Modelo: ", moto.modelo, " - Ano: ", moto.ano, " - Cilindrada: ", moto.cilindrada)
