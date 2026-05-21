ListaProdutos = []

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def Detalhes(self):
        print(f"Nome do produto: {self.nome}, Preço do produto: {self.preco}")

def cadastrarprod():
    while True:

        nomeprod = input("Digite o nome do produto: ").strip().title()
    
        if nomeprod.replace(" ", "").isalpha():
            break
    
        else:
            print("\nDigite APENAS texto!")
    
    while True:
    
        try:
            precoprod = float(input("Digite o preco: ").strip())
    
            if precoprod < 1:
                print("\nDigite APENAS números maiores que 0!")
    
            else:
                break
    
        except ValueError:
            print("\nDigite APENAS números !!!")
    
    ListaProdutos.append(Produto(nomeprod, precoprod))
    

while True:
    print("BEM VINDO AO SISTEMA D ECOPRA E CADASTRO D EPRODUTOS")
    print("escolha uma opção a seguir:")
    while True:
        try:
            opcao  = int(input("1 - Cadastrar Produto"))
            opcao  = int(input("2 - Listar Produtos"))
            opcao  = int(input("3 - Comprar Produtos"))
            opcao  = int(input("4 - Sair"))
            
            if opcao > 4 or opcao < 1:
                print("!!! Digite APENAS valores entre 1 e 4 !!!")
            else:
                break
            
        except ValueError:
            print("!!! Digite APENAS numeros !!!")
    
    if opcao == 1:
        