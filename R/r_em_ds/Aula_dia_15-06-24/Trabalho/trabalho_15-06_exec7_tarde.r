# Dados de quantidade de alunos matriculados de 1990 a 1996 em milhares de alunos
anos <- c(1990, 1991, 1992, 1993, 1994, 1995, 1996)
alunos_matriculados <- c(19720, 20567, 21473, 21887, 20598, 22473, 23564)

# Converter os anos para fatores para exibição no gráfico
anos <- as.factor(anos)

# Criar o gráfico de série temporal
plot(anos, alunos_matriculados, type = "o", col = "blue", xlab = "Ano", ylab = "Alunos Matriculados (em milhares)", main = "Quantidade de Alunos Matriculados no Ensino de 1º Grau no Brasil (1990-1996)")
