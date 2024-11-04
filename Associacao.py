class escritor():
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class caneta():
    def __init__(self, marca):
        self.__marca = marca
    
    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print("Caneta está escrevendo...")

escr = escritor('José')
canet = caneta('BIC')

escr.ferramenta = canet
escr.ferramenta.escrever()