# --- Variáveis de entrada do cliente ---
negativado = False
renda_mensal = 3500
cliente_premium = True


# --- Lógica de Pré-Aprovação do Empréstimo ---


# A regra é:
# O cliente NÃO está negativado E (tem renda > 4000 OU é cliente Premium)


if not negativado and (renda_mensal > 4000 or cliente_premium):
    print("Empréstimo pré-aprovado.")
else:
    print("Empréstimo negado.")
