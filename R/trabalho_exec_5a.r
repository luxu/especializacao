tempm <- c(67,72,74,62,56,66,65,59,61,69,74,69,66,68,58,64,66,57,68,62,59,73,61,61,57,58,57,67,81,79,76)
temps <- c(91,92,93,93,87,84,80,78,75,73,81,76,77,71,71,78,67,76,68,82,64,71,81,69,63,70,77,75,76,68)

temps_celsius <- (temps - 32) / 1.8

hist(temps_celsius, freq = FALSE, breaks = 5, col = "dark blue", main = "Histograma da Frequência Relativa das Temperaturas de Maio em Graus Celsius", xlab = "Temperatura em Graus Celsius")
lines(density(temps_celsius), col = "dark blue", lwd = 2)