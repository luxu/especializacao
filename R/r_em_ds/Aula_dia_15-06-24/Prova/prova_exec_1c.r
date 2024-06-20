if (!require(ggplot2)) install.packages("ggplot2")
library(ggplot2)

# Calcular a correlação de Pearson
correlacao <- cor.test(dados$Peso, dados$Altura)
correlacao

# Ajustar um modelo de regressão linear
modelo <- lm(Peso ~ Altura, data = dados)

# Resumo do modelo de regressão
summary(modelo)

# Estimar o peso de uma pessoa com 1,80m de altura
altura_nova <- 1.80
peso_estimado <- predict(modelo, newdata = data.frame(Altura = altura_nova))
peso_estimado
