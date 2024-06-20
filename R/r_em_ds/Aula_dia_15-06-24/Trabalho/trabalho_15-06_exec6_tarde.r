install.packages("clipr")
dia <- read.table(text = clipr::read_clip(), header = TRUE)
dia

acessos <- c(7, 8, 11, 10, 9, 12, 8)
volume <- c(14, 18, 19, 21, 18, 24, 17)

# Construa um diagrama de dispersão para esse par de variáveis
plot(acessos, volume, main = "Diagrama de Dispersão", xlab = "Acessos", ylab = "Volume", col = "blue", pch = 16)

cor(acessos, volume)
