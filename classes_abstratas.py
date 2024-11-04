from abc import ABC, abstractmethod
class letras():
    @abstractmethod
    def MostrarTipo(self):
        print('Eu sou uma classe abstrata')

class A(letras):
    def __init__(self, descricao):
        self.descricao = descricao

    def imprimir(self):
        print('Aqui é um método diferente!')

letraA = A("Letra A")
letraA.MostrarTipo()
letraA.imprimir()
