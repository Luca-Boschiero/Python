nomes = ["Ana", "Bruno", "Carlos"]

i = int(input("Digite o índice: "))

if 0 <= i < len(nomes):
    print(nomes[i])
else:
    print("Índice inválido.")