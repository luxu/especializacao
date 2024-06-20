# install.packages('sampling')
library(dplyr)
library(sampling)
# dados <- read.table("Milsa.txt", header = T)
dados <- read.table("Aula_dia_15-06-24/Prova/Milsa.txt", header = T)
dados
tamanho_amostra <- 10

# Determinar o tamanho dos estratos
tamanho_estratos <- dados %>%
  group_by(instr) %>%
  summarise(Tamanho = n())

# Calcular a proporção de cada estrato
tamanho_estratos <- tamanho_estratos %>%
  mutate(Proporcao = Tamanho / sum(Tamanho))

# Determinar o número de funcionários amostrados em cada estrato
tamanho_estratos <- tamanho_estratos %>%
  mutate(Amostra = round(Proporcao * tamanho_amostra))

# Ajustar se o número total não for exatamente igual ao tamanho da amostra devido ao arredondamento
diferenca <- tamanho_amostra - sum(tamanho_estratos$Amostra)
diferenca

if (diferenca > 0) {
  indices <- order(tamanho_estratos$Proporcao - tamanho_estratos$Amostra / tamanho_amostra, decreasing = TRUE)
  tamanho_estratos$Amostra[indices[1:diferenca]] <- tamanho_estratos$Amostra[indices[1:diferenca]] + 1
} else if (diferenca < 0) {
  indices <- order(tamanho_estratos$Amostra / tamanho_estratos$Proporcao - tamanho_estratos$Proporcao, decreasing = TRUE)
  tamanho_estratos$Amostra[indices[1:abs(diferenca)]] <- tamanho_estratos$Amostra[indices[1:abs(diferenca)]] - 1
}

# Selecionar a amostra estratificada
set.seed(123) # Para reprodutibilidade
amostra <- NULL

for (i in 1:nrow(tamanho_estratos)) {
  estrato <- subset(dados, instr == tamanho_estratos$instr[i])
  amostra_estrato <- estrato[sample(1:nrow(estrato), tamanho_estratos$Amostra[i]), ]
  amostra <- rbind(amostra, amostra_estrato)
}

tamanho_estratos
# A tibble: 3 × 4
#   instr Tamanho Proporcao Amostra
# 1     1      13     0.325       3
# 2     2      19     0.475       5
# 3     3       8     0.2         2


amostra
   Func civil instr filhos salario ano mes regiao
3     3     2     1      2    5.25  36   5      2
40   40     2     1      3   24.00  52   6      3
18   18     2     1      2    9.80  39   7      3
35   35     2     2      2   19.40  48  11      2
22   22     1     2     NA   11.59  34   2      2
13   13     1     2     NA    8.74  37   5      3
11   11     2     2      2    8.12  33   6      1
28   28     2     2      0   14.69  29   8      1
36   36     2     3      3   23.30  42   2      1
19   19     1     3     NA   10.53  25   8      1
