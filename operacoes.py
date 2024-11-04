"""
Este módulo oferece funções matemáticas basicas, tipo:
Somar, subtrair, dividir, multiplicar, potencializar e imprimir um dado qualquer.
"""


def somar(a, b):
    return (a + b)

def subtrair(a, b):
    return (a - b)

def dividir(a, b):
    if b == 0:
        print("Erro: divisão por zero")
    else:
        return (a / b)
    
def multiplicar(a, b):
    return (a * b)

def potencia(a, b):
    return (a ** b)

def imprimir(dado):
    print(dado)