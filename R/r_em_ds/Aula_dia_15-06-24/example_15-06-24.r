dados <- read.csv("amostra.csv", header = TRUE, sep = ";")
# Função Quartis, ou seja, 25%
dados
quantile(dados$AnosServico)

summary(dados)
cor(dados$Renda, dados$Idade)
dados <- read.csv("DadosPIB.csv", header = TRUE, sep = ";", dec = ",")
modelo <- lm(formula = CULTIVO~PIBAGRO, data = dados)
abline(modelo, col = "blue")

amostra<-read.csv("amostra.csv", header=T, sep=";")
table(amostra$EstCivil,amostra$Escolaridade)
prop.table(table(amostra$EstCivil,amostra$Escolaridade))*100

chisq.test(table(amostra$EstCivil,amostra$Escolaridade))

tabela<-matrix(c(80,55,70,65,85,45), nrow=2, ncol=3, byrow=T)
rownames(tabela)<-c("Masculino","Feminino")
colnames(tabela)<-c("CS", "CH", "CE")
chisq.test(tabela)
barplot(tabela, beside=T, legend=T, col=c("blue", "pink"))
