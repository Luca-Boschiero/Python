class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def exibirdetalhes(self):
        print(f"o nome é {self.nome}, o preço é {self.preco}")
        
a1 = Produto("notebook", 30)

a1.exibirdetalhes()