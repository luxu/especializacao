tipo_defeito <- c('Linha Ruidosa', 'Linha Aberta', 'Alarme', 'Não Responde', 'Não toca')
ocorrencias <- c(250, 110, 85, 45, 25)
porcentagem <- round(ocorrencias / sum(ocorrencias) * 100, 2)

dados <- data.frame(tipo_defeito, ocorrencias, porcentagem)
minhas_cores <- rainbow(length(tipo_defeito))
pie(dados$porcentagem, labels = paste(dados$tipo_defeito, " (", round(dados$porcentagem, 1), "%)"), col = minhas_cores, main = "Distribuição de Tipos de Defeito")
legend("topright", legend = dados$tipo_defeito, fill = minhas_cores, title = "Tipos de Defeito", cex = 0.8)
