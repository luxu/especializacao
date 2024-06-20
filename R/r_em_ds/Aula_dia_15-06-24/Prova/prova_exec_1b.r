if (!require(ggplot2)) install.packages("ggplot2")
library(ggplot2)

# Gráfico Boxplot
ggplot(dados, aes(x = Situacao, y = Peso, fill = Situacao)) +
  geom_boxplot() +
  scale_fill_manual(values = c("Acamado" = "green", "Deambulando" = "blue")) +
  labs(title = "Boxplot do Peso em função da Situação", 
       x = "Situação", 
       y = "Peso") +
  theme_minimal() +
  theme(legend.title = element_blank())
