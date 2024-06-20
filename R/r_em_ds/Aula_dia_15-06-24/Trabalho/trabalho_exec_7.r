anos <- c(1990:1996)
alunos <- c(19720, 20567, 21473, 21887, 20598, 22473, 23564)

# Criar o gráfico de série temporal
plot(anos, alunos, type = "o", col = "blue", xlab = "Ano", ylab = "Alunos", main = "Alunos Matriculados no Ensino de 1º Grau no Brasil de 1990 a 1996")
