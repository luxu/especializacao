fornecedor_A <- c(1.0, 1.2, 1.5, 1.8, 2.5)
fornecedor_B <- c(1.6, 2.5, 1.2, 2.3, 1.5)
fornecedor_A
fornecedor_B

# Calcule a média, mediana e desvio-padrão de cada conjunto.
media_a <- mean(fornecedor_A)
mediana_a <- median(fornecedor_A)
desvio_padrao_a <- sd(fornecedor_A)

media_b <- mean(fornecedor_B)
mediana_b <- median(fornecedor_B)
desvio_padrao_b <- sd(fornecedor_B)

media_a # 1.6
mediana_a # 1.5
desvio_padrao_a # 0.587367

media_b # 1.82
mediana_b # 1.6
desvio_padrao_b # 0.5540758
