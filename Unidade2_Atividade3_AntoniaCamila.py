# O programa vai rodar continuamente até o usuário escolher a opção "Sair"
while True:

    # Mostra o menu de operações
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    # Lê a opção escolhida pelo usuário
    opcao = input("Escolha uma opção (1 a 5): ")

    # Se o usuário escolher sair, encerra o programa
    if opcao == "5":
        print("Programa encerrado. Obrigado por usar a calculadora!")
        break  # sai do loop while e finaliza o programa

    # Validação da opção escolhida
    if opcao not in ["1", "2", "3", "4"]:
        print("Erro: Escolha inválida. Selecione uma das opções de 1 a 5.")
        continue  # volta para o início do loop

    # Leitura do primeiro número inteiro
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
    except ValueError:
        print("Erro: você deve digitar um número inteiro válido.")
        continue

    # Leitura do segundo número inteiro
    try:
        num2 = int(input("Digite o segundo número inteiro: "))
    except ValueError:
        print("Erro: você deve digitar um número inteiro válido.")
        continue

    # Executa a operação escolhida
    if opcao == "1":
        # Soma
        resultado = num1 + num2
        print("O resultado é:", resultado)

    elif opcao == "2":
        # Subtração
        resultado = num1 - num2
        print("O resultado é:", resultado)

    elif opcao == "3":
        # Multiplicação
        resultado = num1 * num2
        print("O resultado é:", resultado)

    elif opcao == "4":
        # Divisão
        if num2 == 0:
            print("Erro: Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print("O resultado é:", resultado)
