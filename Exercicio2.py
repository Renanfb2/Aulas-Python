"""
Exercício: Crie um módulo onde seja possível imprimir um texto de tras para frente.
Oriente o usuário do seu uso
"""

# Este módulo imprime uma string informada pelo usuário

"""  ESTE FOI COMO EU RESOLVI
def invtxt(texto):
    inv = ''
    j = len(texto)-1
    for i in texto:
        inv += texto[j]
        j -=1
    
    return inv

"""

def invtxt(texto):     # este foi como o professor resolveu !!!!!!
    return texto[::-1]

# txt = input("Entre com o Texto: ")
# print(invtxt(txt))
print(invtxt(input("Digite o texto: ")))

