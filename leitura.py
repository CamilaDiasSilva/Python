# --- Variáveis de entrada (Leituras do sistema) ---
uso_cpu = 92  # Porcentagem de uso da CPU
uso_memoria = 70 # Porcentagem de uso da memória RAM


# --- Lógica de Verificação de Sobrecarga ---


# O alerta é disparado se a CPU > 90% OU se a memória > 85%
if uso_cpu > 90 or uso_memoria > 85:
    # Se pelo menos uma das condições for verdadeira
    print("ALERTA: Sistema sobrecarregado.")
else:
    # Se ambas estiverem normais (nenhuma acima do limite)
    print("Status: Operando normalmente.")
