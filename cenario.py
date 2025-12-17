# --- Variáveis de entrada (Cenário de Teste) ---
tipo_ingresso = "VIP"
idade = 16
acompanhado_por_responsavel = True


# --- Lógica de Verificação de Acesso VIP ---


# A regra é: (Tem ingresso VIP E (É maior de 18 OU Está acompanhado))
if tipo_ingresso == "VIP" and (idade >= 18 or acompanhado_por_responsavel):
    print("Acesso à área VIP liberado.")
else:
    print("Acesso negado.")
