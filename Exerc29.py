try:
    idade = int(input("Digite sua idade: "))
    print("Idade:", idade)
except ValueError:
    print("Erro: digite apenas números.")