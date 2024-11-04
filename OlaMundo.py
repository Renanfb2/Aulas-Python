def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero"

def list():
    vantagens = [
        "Fácil aprendizado", 
        "Simplicidade", 
        "Ampla biblioteca", 
        "Portabilidade", 
        "Suporte a POO"
        ]
    print("As vantagens do Python são:")
    for k in vantagens:
        print(k)

def parametro1():
    return int(input("Parâmetro 1: "))

def parametro2():
    return int(input("Parâmetro 2: "))  
    
print("""
      Escolha uma função: 
      1 - Somar 
      2 - Subtrair 
      3 - Dividir 
      4 - Multiplicar
      5 - Listar vantagens do Python
      """)
i = int(input("Entre com o número escolhido: "))

if i == 1: #Somar
    a = parametro1()
    b = parametro2()
    print("Soma:", soma(a,b))
elif i == 2: #Subtrair
    a = parametro1()
    b = parametro2()
    print("Subtração:", sub(a, b))
elif i == 3: #Dividir
    a = parametro1()
    b = parametro2()
    print("Divisão:", div(a, b))
elif i == 4: #Multiplicar
    a = parametro1()
    b = parametro2()
    print("Multiplicação:", mult(a, b))
elif i == 5:
    list()
else:
    print("Numero Inválido")
