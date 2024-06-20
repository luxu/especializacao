install.packages('dplyr')
library(dplyr)
dados <- read.table("Milsa.txt", header = T)
dados$instr <- factor(dados$instr, label=c("1º Grau", "2º Grau", "Superior"), lev = 1:3, ord=T)
dados$regiao <- factor(dados$regiao, label=c("capital", "interior", "outro"), lev = c(2, 1, 3))
dados$idade <- dados$ano + dados$mes/12
head(dados)
tabela = matrix(c(prop.table(table(dados$instr)), prop.table(table(dados$regiao))*100), nrow = 2, ncol = 3)
tabela
colnames(tabela) <- c("freq.absoluta", "freq.relativa", "freq.percentual")
tabela
rownames(tabela) <- c("solteiro", "casado")
tabela
prof <- c(1751, 1186, 947, 29)
names(prof) <- c("privada", "estadual", "municipal", "federal")
barplot(prof, main="Distribuição de professores do ensino fundamental em Niterói, 2009")
alunosprof <- matrix(c(1751,1186,947,29,25280,21328,18432,280), nrow = 4, ncol = 2)
