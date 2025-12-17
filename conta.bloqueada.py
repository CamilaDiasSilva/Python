# 1. Crie uma variável: conta_bloqueada = True
conta_bloqueada = True


# 2. Usando o operador 'not', escreva uma estrutura if-else que verifique se o usuário pode fazer login.


# A condição 'not conta_bloqueada' será True apenas se 'conta_bloqueada' for False.
if not conta_bloqueada:
    # 3. Se a conta NÃO estiver bloqueada, imprima a mensagem de sucesso
    print("Login bem-sucedido.")
else:
    # 4. Caso contrário (se a conta estiver bloqueada), imprima a mensagem de erro
    print("Conta bloqueada. Entre em contato com o suporte.")


#Outra parte 
conta_bloqueada = False # Alterado para False


if not conta_bloqueada:
    print("Login bem-sucedido.") # Esta mensagem seria impressa
else:
    print("Conta bloqueada. Entre em contato com o suporte.")
