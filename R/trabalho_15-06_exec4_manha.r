dados <- read.csv("amostra.csv", header = TRUE, sep = ";")
dados
# Análise de Correlação entre as variáveis Renda e Idade,
correlacao <- cor(dados$Renda, dados$Idade)
correlacao
# Construir o diagrama de dispersão
plot(dados$Idade, dados$Renda, xlab = "Idade", ylab = "Renda", main = "Diagrama de Dispersão Renda x Idade")

# Realizar o teste de correlação de Pearson
resultado <- cor.test(dados$Renda, dados$Idade, method = "pearson")
print('==========================')
resultado

# Ajustar o modelo de regressão linear
modelo <- lm(Renda ~ Idade, data = dados)

# Exibir um resumo do modelo
summary(modelo)
