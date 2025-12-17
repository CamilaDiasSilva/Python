#1. Crie duas variáveis: usuario_logado = True e nivel_acesso = "usuario"
usuario_logado = True
nivel_acesso = "usuario"


# 2. Usando o operador 'and', escreva uma estrutura if-else que verifique se o usuário deve ter acesso ao painel.


# A condição verifica se o usuário está logado E se o nível de acesso é exatamente "admin"
if usuario_logado and nivel_acesso == "admin":
    # 3. Se ambas as condições forem verdadeiras, imprima a mensagem de sucesso
    print("Acesso ao painel de Admin concedido.")
else:
    # 4. Caso contrário (se uma ou ambas as condições forem falsas), imprima a mensagem de negação
    print("Acesso negado. Você não tem permissão de administrador")
 