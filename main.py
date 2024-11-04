class funcionario():
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0 # Privada na classe
        self.__horas_trabalhadas = 0
            
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossível alterar salário diretamente, use a função calcula_salario().")
    
    def horas_trabalhadas(self):
        self.__horas_trabalhadas = int(input("Qtd horas trabalhadas: "))
        return self.__horas_trabalhadas

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
        return self.__salario

jose = funcionario('José', 'Professor', 50)
jose.horas_trabalhadas()
sal = jose.calcula_salario()
print("Nome: ", jose.nome)
print("Cargo: ", jose.cargo)
print("Salario: ", sal)


    
