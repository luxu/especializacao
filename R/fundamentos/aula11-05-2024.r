getwd()

install.packages("ggplot2")

library(ggplot2)
dados=read.csv("amostra.csv", header = T, sep = ";")
dados
ggplot(dados) + geom_point(mapping = aes(x=ID, y=Idade))

ggplot(data = dados, aes(x=Idade, y=Renda)) + geom_point()

ggplot(data = dados, aes(x=AnosServico, y=Idade)) + geom_point()

ggplot(data = dados, aes(x=Idade, y=Renda)) + geom_line()

ggplot(data = dados, aes(x=as.factor(EstCivil))) + geom_bar()

ggplot(data = dados) + geom_histogram(aes(x=Renda))

ggplot(data = dados,aes(x=Renda)) + geom_histogram(binwidth = 10, color='white')

ggplot(data = dados) + geom_boxplot(aes(x=EstCivil,y=Renda))

ggplot(dados, aes(x=as.factor(EstCivil))) + geom_bar(color='red', fill='red')

ggplot(dados, aes(x = as.factor(EstCivil), fill = as.factor(EstCivil))) + 
  geom_bar() +
  labs(fill = "Estado Civil")

Ou se quiser mudar a posição da legenda:
ggplot(dados, aes(x = as.factor(EstCivil), fill = as.factor(EstCivil))) + 
  geom_bar() +
  labs(fill = "Estado Civil") +
theme(legend.position="top")
