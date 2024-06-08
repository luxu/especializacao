temp_set <- c(91,92,93,93,87,84,80,78,75,73,81,76,77,71,71,78,67,76,68)

num_classes <- ceiling(log2(length(temp_set) + 1))

hist(temp_set, breaks = num_classes, col = "dark blue", main = "Histograma das Temperaturas de Setembro", xlab = "Temperatura", ylab = "Frequência", border = "black")
