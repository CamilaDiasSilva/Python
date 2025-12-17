# --- Variáveis de entrada ---
nova_senha = "python123"
confirmacao_senha = "python123"
# A variável tamanho_senha já é calculada automaticamente:
tamanho_senha = len(nova_senha)


# --- Lógica de Validação da Senha ---


# A senha é válida SE:
# 1. O tamanho da senha é maior que 8 E
# 2. A nova senha é idêntica à confirmação
if tamanho_senha > 8 and nova_senha == confirmacao_senha:
    # Se ambas as condições forem verdadeiras
    print("Senha criada com sucesso.")
else:
    # Caso contrário (se uma ou ambas as condições falharem)
    print("Erro: A senha deve ter mais de 8 caracteres e as duas devem ser idênticas.")
