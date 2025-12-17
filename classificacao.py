# Sistema simples de classificação de candidatos
# vamos descobrir o nível baseado nos anos de experiência


anos_de_experiencia = 3  # pode testar outros valores


if anos_de_experiencia > 5:
    print("Nível do candidato: Sênior")
elif anos_de_experiencia >= 2:
    print("Nível do candidato: Pleno")
else:
    print("Nível do candidato: Júnior")