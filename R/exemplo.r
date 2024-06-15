install.packages("TeachingSampling")
library(TeachingSampling)

dados <- read.csv("amostra.csv", header = T, sep = ";")
set.seed(50) #Definição da semente a ser utilizada
amostra <- dados[runif(10, 1, nrow(dados)),] #Definição da amostra
amostra

N <- 200
n <- 10
k <- round(N/n)

set.seed(22222) #Definição da semente

n0 <- runif(1, min=1, max=k) #Definição do 1º elemento da amostra
n0

sequencia <- seq(n0, n0 + (n-1) * k, k) #Metodologia da amostragem
amostra2 <- dados[sequencia,]
amostra2

N<-nrow(dados)
n<-10
K<-round(N/n)
amostra<-S.SY(N,k)
amostra
NL = as.numeric(table(dados$Regiao))
n = 10
n1 = round((87/200) *n)
n2 = round((23/200) *n)
n3 = round((52/200) *n)
n4 = round((38/200) *n)
nL = c(4, 1, 3, 2)

amostra2 <- S.STSI(as.factor(dados$Regiao), NL, nL)