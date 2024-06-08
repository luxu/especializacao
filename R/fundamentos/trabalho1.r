dados=read.csv("universidade.csv", header = T, sep = ";")
dados
# histograma para variável altura

ggplot(data = dados) + geom_histogram(aes(x=Altura, fill='Altura'), color='red', fill='yellow') + labs(fill='Altura') + theme(legend.position = "top")

# gráfico de colunas para Estado Civil

ggplot(dados, aes(x=as.factor(EstCivil), fill=as.factor(EstCivil))) + geom_bar() + labs(fill='Estado Civil') + theme(legend.position = "top")

# gráfico de Dispersão para “Idade x Há quantos anos terminou a graduação”.

ggplot(dados, aes(x=as.factor(Idade),y=as.factor(Grad))) + geom_point()
