class produto():
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class carrinho_compras():
    def __init__(self, ):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f'{produto.nome}: R$ {produto.valor}')

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return f'R$ {total}'
    
carrinho = carrinho_compras()
p1 = produto('Boné', 50)
p2 = produto('Sapato', 200)
p3 = produto('Camisa', 120)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.listar_produtos()
print(carrinho.soma_total())