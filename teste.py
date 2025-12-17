# 1. Crie duas variáveis: valor_compra = 150 e assinante_prime = True
valor_compra = 150
assinante_prime = True


# 2. Usando o operador 'or', escreva uma estrutura if-else que verifique se o cliente receberá frete grátis.


# A condição verifica se o valor da compra é maior que R$ 200,00 OU se o cliente é assinante Prime
if valor_compra > 200 or assinante_prime:
    # 3. Se pelo menos uma das condições for verdadeira, imprima a mensagem de sucesso
    print("Parabéns! Você ganhou frete grátis.")
else:
    # 4. Caso contrário (se nenhuma for verdadeira), imprima a mensagem de negação
    print("Frete grátis não aplicável.")
