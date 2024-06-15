dados <- c(3, 7, 4, 5, 1, 8, 4, 6, 5, 6, 2, 4, 6, 9, 8, 4, 5, 5, 6)
# aprovado >= 5
# t = [r for r in dados if r >= 5]
# t.sort()
# [5, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9]

# reprovado < 5 usei
# t = [r for r in dados if r < 5]
# t.sort()
# [1, 2, 3, 4, 4, 4, 4]

aprovados <- c(5, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9)
reprovados <- c(1, 2, 3, 4, 4, 4, 4)

# AMPLITUDE
range(aprovados)
# Resposta = 5 9
range(reprovados)
# Resposta = 1 4

# C)
media_aprovados <- mean(aprovados)
desvio_padrao_aprovados <- sd(aprovados)
CV_aprovados <- (desvio_padrao_aprovados / media_aprovados) * 100
CV_aprovados # 21.64246
# (0 / 21.64246) * 100 = 0

media_reprovados <- mean(reprovados)
desvio_padrao_reprovados <- sd(reprovados)
CV_reprovados <- (desvio_padrao_reprovados / media_reprovados) * 100
CV_reprovados # 38.65864
# (0 / 38.65864) * 100 = 0
"
Como o coeficiente de variação para ambos os grupos é igual a zero, 
isso indica que não há variabilidade nos dados, 
o que não é um resultado comum em situações reais. 
Portanto, com base nos dados fornecidos, não é possível determinar se os dois grupos são homogêneos 
a partir do coeficiente de variação.
"