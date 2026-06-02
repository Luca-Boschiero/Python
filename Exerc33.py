soma = 0

for i in range(5):
    num = float(input("Digite um número: "))
    print("Número digitado:", num)

    soma = soma + num
    print("Soma parcial:", soma)

print("Soma:", soma)