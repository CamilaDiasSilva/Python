# Calculadora simples com validação básica

# Ler o primeiro número inteiro
while True:
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Ler o segundo número inteiro
while True:
    try:
        num2 = int(input("Digite o segundo número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Mostrar as operações disponíveis
print("\nEscolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (×)")
print("4 - Divisão (÷)")
print("5 - Módulo (resto da divisão)")

# Ler a opção
while True:
    try:
        opcao = int(input("Digite o número da operação (1 a 5): "))
        if 1 <= opcao <= 5:
            break
        else:
            print("Opção inválida. Digite um número entre 1 e 5.")
    except ValueError:
        print("Opção inválida. Digite um número entre 1 e 5.")

# Fazer o cálculo
if opcao == 1:
    resultado = num1 + num2
elif opcao == 2:
    resultado = num1 - num2
elif opcao == 3:
    resultado = num1 * num2
elif opcao == 4:
    while num2 == 0:
        print("Erro: não é possível dividir por zero.")
        num2 = int(input("Digite outro número diferente de zero: "))
    resultado = num1 / num2
elif opcao == 5:
    while num2 == 0:
        print("Erro: não é possível dividir por zero.")
        num2 = int(input("Digite outro número diferente de zero: "))
    resultado = num1 % num2

# Mostrar o resultado
print(f"O resultado é: {resultado}")
