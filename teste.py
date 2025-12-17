# --- Definição das variáveis de entrada ---
# Você pode mudar True/False aqui para testar os diferentes cenários:


# Cenário de Teste 1 (Troque estes valores para testar):
tem_convite = True
tem_documento = True


# Cenário de Teste 2:
# tem_convite = False
# tem_documento = True


# Cenário de Teste 3:
# tem_convite = True
# tem_documento = False


# Cenário de Teste 4:
# tem_convite = False
# tem_documento = False




# --- Lógica de Verificação ---


if tem_convite and tem_documento:
    # Caso 1: Tem ambos
    mensagem = "Você pode entrar na festa, pois tem o convite e o documento"
elif not tem_convite and tem_documento:
    # Caso 2: Não tem convite, mas tem documento
    mensagem = "Você não pode entrar na festa, pois faltou o convite"
elif tem_convite and not tem_documento:
    # Caso 3: Tem convite, mas não tem documento
    mensagem = "Você não pode entrar na festa, pois faltou o documento"
else:
    # Caso 4: Não tem nenhum dos dois (usa o 'else' como fallback para o último caso possível)
    mensagem = "Você não pode entrar na festa, pois faltou o convite e o documento"


# --- Saída no Terminal ---
print(mensagem)
