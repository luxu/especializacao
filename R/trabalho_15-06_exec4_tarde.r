dias_de_nascido <- c(2, 4, 6, 8, 10)
peso <- c(42, 51, 59, 64, 76)

# Calculando o peso médio dos pintinhos em cada categoria
peso_medio <- tapply(peso, dias_de_nascido, mean)

# Criando o gráfico de barras horizontais
barplot(peso_medio, horiz=TRUE, col=c("blue", "pink", "yellow", "green", "red"), main="Peso Médio dos Pintinhos por Categoria de Dias de Nascido", xlab="Peso Médio", ylab="Dias de Nascido")

# Adicionando legenda
legend("topright", legend=names(peso_medio), fill=c("blue", "pink", "yellow", "green", "red"))
