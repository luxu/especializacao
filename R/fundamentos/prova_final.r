install.packages("clipr")
coluna_paciente <- read.table(text = clipr::read_clip(), header = TRUE)
coluna_sexo <- read.table(text = clipr::read_clip(), header = TRUE)
coluna_idade <- read.table(text = clipr::read_clip(), header = TRUE)
coluna_peso <- read.table(text = clipr::read_clip(), header = TRUE)
coluna_imc <- read.table(text = clipr::read_clip(), header = TRUE, dec = ",")
class(coluna_paciente)
df = data.frame(coluna_paciente,coluna_sexo,coluna_idade, coluna_peso, coluna_imc)
df
dados = df[, !(names(df) %in% "Paciente")]
dados
dados$"Dias na UTI" <- c(4, 10, 7, 12, 8, 5, 13)
dados
dados_filtrados <- dados[, c("Peso", "IMC")]
dados_filtrados
dados_ordenados <- dados[order(dados$Idade), ]
dados_ordenados
dados$Peso[5] <- 67
imc_acima_de_30 = dados[dados['IMC'] > 30]
imc_acima_de_30
media_imc = mean(dados$IMC)
media_peso = mean(dados$Peso)
media_idade = mean(dados$Idade)
media_imc
media_peso
media_idade

# Construir o gráfico de colunas
ggplot(coluna_sexo, aes(x = Sexo, fill = Sexo)) +
  geom_bar() +
  scale_fill_manual(values = c("blue", "pink")) +
  labs(x = "SEXO", y = "FREQUÊNCIA")


df2 <- data.frame(Peso = c(70, 65, 80, 75, 85),
                 IMC = c(25.3, 31.7, 29.8, 27.5, 32.2))

ggplot(df, aes(x = Peso, y = IMC)) +
  geom_point() +
  xlab("Peso") +
  ylab("IMC")

luz = c(9839, 10149, 10486, 10746, 11264, 11684, 12082, 12599, 13004, 13350, 13717, 14052)
luz.cons = diff(luz)
luz.cons
n.luz = length(luz)
media.luz = sum(luz)/n.luz
max.luz = max(luz)
min.luz = min(luz)
max.luz
min.luz
luz.range = c(min.luz, max.luz)
luz.range
luz = c(9839, 10149, 10486, 10746, 11264, 11684, 12082, 12599, 13004, 13350, 13717, 14052)
meses = c('Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez')
nome=function(numero){
    result = which(luz == numero);
    re = meses[result];
    return(re)
}
nome(min.luz)
nome(max.luz)


dados_consumo = data.frame(mes = meses, consumo = luz)
dados_consumo

ggplot(dados_consumo, aes(x = mes, y = consumo)) +
  geom_bar(stat = "identity", fill = "blue") +
  labs(title = "Consumo Mensal da Casa", x = "Mês", y = "Consumo")

texto <- readLines("prova.txt")
texto_completo <- paste(texto, collapse = " ")
texto_completo <- tolower(texto_completo)
palavras <- strsplit(texto_completo, "\\W+")
contador_palavras <- table(unlist(palavras))
palavras_ord <- sort(contador_palavras, decreasing = TRUE)
dados_grafico <- data.frame(palavra = names(palavras_ord)[1:6], frequencia = as.numeric(palavras_ord)[1:6])
ggplot(data = dados_grafico, aes(x = palavra, y = frequencia)) + 
  geom_bar(stat = "identity", fill = "skyblue") + 
  xlab("Palavra") + ylab("Frequência") + 
  ggtitle("Top 10 palavras mais frequentes")

palavras_freq <- head(sort(contador_palavras, decreasing = TRUE), 25)
wordcloud(words = names(palavras_freq), freq = palavras_freq, colors = brewer.pal(8, "Dark2"))
