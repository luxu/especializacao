if (!require(ggplot2)) install.packages("ggplot2")
library(ggplot2)
getwd()

dados <- read.csv('R/r_em_ds/Aula_dia_15-06-24/Prova/Nutricao.csv', sep = ";")
tabela_frequencias <- table(dados$Classificacao)
tabela_frequencias

# Converter a tabela de frequências em um data frame
frequencias <- as.data.frame(tabela_frequencias)
colnames(frequencias) <- c("Classificacao", "Frequencia")
frequencias

# Gráfico de Barras
ggplot(frequencias, aes(x = Classificacao, y = Frequencia, fill = Classificacao)) +
  geom_bar(stat = "identity") +
  labs(title = "Frequência das Classificações IMC dos Pacientes", 
       x = "Classificação", 
       y = "Frequência") +
  scale_fill_manual(values = c("#1f77b4", "#ff7f0e", "#2ca02c")) +
  theme_minimal() +
  theme(legend.title = element_blank())
