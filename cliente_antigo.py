# Definindo se a pessoa é cliente antigo ou não
cliente_antigo = True  # coloque False se não for cliente antigo


# Preço original do produto
preco_cheio = 100.0  # exemplo de preço
desconto = 0.2  # 20% de desconto


# Verificando se é cliente antigo
if cliente_antigo:
    preco_final = preco_cheio * (1 - desconto)
    print(f"Cliente antigo! Você ganhou desconto. Preço final: R${preco_final:.2f}")
else:
    preco_final = preco_cheio
    print(f"Preço cheio: R${preco_final:.2f}")
