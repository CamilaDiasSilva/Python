# --- Variáveis de entrada do jogo ---
vida = 0
vida_extra = True # O jogador possui um item de vida extra


# --- Lógica para verificar o Game Over ---


# O Game Over acontece SE:
# 1. A vida for igual a 0 E
# 2. Ele NÃO tiver uma vida extra (not vida_extra)


if vida == 0 and not vida_extra:
    # Se ambas as condições forem verdadeiras (sem vida E sem item extra)
    print("Game Over")
else:
    # Caso contrário (se ele tiver vida > 0 OU se tiver o item extra)
    print("Jogador usa item 'Vida Extra' e continua!")
