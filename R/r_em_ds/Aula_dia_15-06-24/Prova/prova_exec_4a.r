getwd()
head(dados)
dim(dados)
names(dados)
salarios <- length(dados$salario)
salarios

dados <- read.table("Aula_dia_15-06-24/Prova/Milsa.txt", header = T)
dados <- read.table("Milsa.txt", header = T)
vinte_por_cento_dos_dados <- ceiling(0.2 * salarios) # 8
set.seed(123)
amostra_indices <- sample(1:N, vinte_por_cento_dos_dados) # 15 19 14  3 10  2  6 11
amostra <- dados$salario[amostra_indices] # 9.13 10.53  8.95  5.25  7.44  4.56  6.66  8.12
desvio_padrao_amostra <- sd(amostra) # 2.024451
media_amostra <- mean(amostra) # 7.58
cv_amostra <- (desvio_padrao_amostra / media_amostra) * 100 # 26.70779
homogeneidade <- ifelse(cv_amostra < 20, "Homogêneos", "Não homogêneos") # "Não homogêneos"
