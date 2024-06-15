tempm=c(67,72,74,62,56,66,65,59,61,69,74,69,66,68,58,64,66,57,68,62,59,73,61,61,57,58,57,67,81,79,76)

celsius <- (tempm - 32) / 1.8
round(celsius,1)

# a)
# Criar o histograma com título, sombreamento de densidade e cor específica
hist(celsius, freq = FALSE, main = "Histograma de Frequência Relativa das Temperaturas em Celsius", breaks = 10, col = "dark blue", density = 25)


# b)
temps=c(91,92,93,93,87,84,80,78,75,73,81,76,77,71,71,78,67,76,68,82,64,71,81,69,63,70,77,75,76,68)

# Construir o histograma com 6 classes
hist(temps, breaks = 6, col = "lightblue", main = "Histograma de Temperaturas do Mês de Setembro", xlab = "Temperatura", ylab = "Frequência")
