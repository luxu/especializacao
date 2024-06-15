dados <- c(67, 69, 102, 72, 83, 77, 69, 82, 74, 83)

# 1)
quantile(dados)

# 2)
# Calcular a média
media <- mean(dados)
media

# Calcular o desvio padrão
desvio_padrao <- sd(dados)
desvio_padrao

# Calcular o coeficiente de variação
coefficiente_variacao <- (desvio_padrao / media) * 100
coefficiente_variacao
