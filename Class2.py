class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
a1 = Produto("notebook", 30)

print(f"o Nome do produto: {a1.nome}, e o Preço é {a1.preco}")