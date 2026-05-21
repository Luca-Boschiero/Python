# Lista onde todos os alunos serão armazenados
alunos = []


# Função responsável por registrar os alunos
def registrar_aluno():

    # Exibe título da seção
    print("\nRegistro do aluno:")

    # Loop para validar o nome
    while True:

        # Pede o nome do aluno
        nome = input("Digite o nome do aluno: ").strip().title()

        # Verifica se contém apenas letras e espaços
        if nome.replace(" ", "").isalpha():

            # Sai do loop se estiver correto
            break

        else:
            # Mensagem de erro
            print("\nDigite APENAS texto!")

    # Loop para validar idade
    while True:

        try:
            # Recebe idade e converte para inteiro
            idade = int(input("Digite a idade: ").strip())

            # Verifica se é menor que 1
            if idade <1:

                # Exibe erro
                print("\nDigite APENAS números maiores que 0!")

            else:
                # Sai do loop se estiver correto
                break

        # Caso usuário digite algo inválido
        except ValueError:

            # Exibe erro
            print("\nDigite APENAS números inteiros!")

    # Loop para validar nota
    while True:

        try:
            # Recebe a nota e converte para float
            nota = float(input("Digite a nota: ").strip().replace(",", "."))

            # Verifica se a nota está fora do limite permitido
            if nota > 10 or nota < 0:

                # Exibe erro
                print("\nDigite APENAS números de 0 a 10!")

            else:
                # Sai do loop se estiver correto
                break

        # Caso digite algo inválido
        except ValueError:

            # Exibe erro
            print("\nDigite APENAS números!")

    # Verifica se aluno foi aprovado
    if nota >= 7:

        # Define status aprovado
        stats = "aprovado"

    # Verifica se ficou de recuperação
    elif nota >= 5:

        # Define status recuperação
        stats = "recuperação"

    else:
        # Caso contrário, reprovado
        stats = "reprovado"

    # Cria dicionário contendo os dados do aluno
    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota,
        "status": stats
    }

    # Adiciona aluno na lista
    alunos.append(aluno)

    # Confirma cadastro
    print("\nAluno registrado!\n")


# Função para calcular média da sala
def media_sala():

    # Variável acumuladora
    soma = 0

    # Percorre todos os alunos
    for aluno in alunos:

        # Soma as notas
        soma += aluno['nota']

    # Retorna média
    return soma / len(alunos)


# Função responsável pelo relatório final
def relatorio():

    # Título
    print("\n--- RELATÓRIO ---\n")

    # Subtítulo
    print("ALUNOS:")

    # Percorre todos os alunos cadastrados
    for aluno in alunos:

        # Exibe os dados formatados
        print(f"Nome: {aluno['nome']} || Idade: {aluno['idade']} || Nota: {aluno['nota']} || Situação: {aluno['status']}")

    # Lista auxiliar de notas
    notas = []

    # Percorre alunos
    for aluno in alunos:

        # Adiciona nota na lista
        notas.append(aluno['nota'])

    # Define inicialmente o primeiro aluno como maior nota
    aluno_maior_nota = alunos[0]

    # Define inicialmente o primeiro aluno como menor nota
    aluno_menor_nota = alunos[0]

    # Contador de aprovados
    qtd_aprovados = 0

    # Contador de recuperação
    qtd_recuperacao = 0

    # Contador de reprovados
    qtd_reprovados = 0

    # Percorre todos os alunos
    for aluno in alunos:

        # Verifica maior nota
        if aluno['nota'] > aluno_maior_nota['nota']:

            # Atualiza maior nota
            aluno_maior_nota = aluno

        # Verifica menor nota
        if aluno['nota'] < aluno_menor_nota['nota']:

            # Atualiza menor nota
            aluno_menor_nota = aluno

        # Conta aprovados
        if aluno['status'] == "aprovado":

             qtd_aprovados += 1

        # Conta recuperação
        elif aluno['status'] == "recuperação":

            qtd_recuperacao += 1

        else:
            # Conta reprovados
            qtd_reprovados += 1

    # Exibe seção de notas
    print("\nNOTAS: ")

    # Mostra média da sala
    print(f"Média da sala: {media_sala():.2f}")

    # Exibe seção situação
    print("\nSITUAÇÃO DA SALA:")

    # Mostra quantidade de aprovados
    print(f"Aprovados: {qtd_aprovados}")

    # Mostra quantidade de recuperação
    print(f"Recuperação: {qtd_recuperacao}")

    # Mostra quantidade de reprovados
    print(f"Reprovados: {qtd_reprovados}")

    # Exibe aluno com maior nota
    print(f"\nAluno com a maior nota: {aluno_maior_nota['nome']} || Nota: {aluno_maior_nota['nota']}")

    # Exibe aluno com menor nota
    print(f"Aluno com a menor nota: {aluno_menor_nota['nome']} || Nota: {aluno_menor_nota['nota']}")


# Mensagem inicial do sistema
print("BEM-VINDO AO SISTEMA DE REGISTRAR ALUNOS")

# Linha decorativa
print("--------------------------------------------------------------")


# Loop principal do programa
while True:

    # Chama função para registrar aluno
    registrar_aluno()

    # Loop para validar resposta do usuário
    while True:

        # Pergunta se deseja continuar
        continuar = input("Deseja adicionar outro aluno? (s/n): ").lower()

        # Se usuário digitar s
        if continuar == "s":

            # Continua o programa
            break

        # Se usuário digitar n
        elif continuar == "n":

            # Sai do loop
            break

        else:
            # Caso resposta inválida
            print("\nDigite apenas 's' ou 'n'!")

    # Se usuário não quiser continuar
    if continuar == "n":

        # Encerra cadastro
        break
    


# Chama função do relatório final
relatorio()