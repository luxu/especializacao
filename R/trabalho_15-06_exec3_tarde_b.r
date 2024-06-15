# Criando os vetores
tipo_de_defeito <- c('linha ruidosa', 'linha aberta', 'alarme', 'nao_responde', 'nao_toca')
ocorrencia <- c(250, 110, 85, 45, 25)

# Criando o gráfico de setores
pie(ocorrencia, labels = paste(tipo_de_defeito, " (", round(ocorrencia/sum(ocorrencia)*100), "%)", sep = ""), col = rainbow(length(tipo_de_defeito)))

# Adicionando legenda
legend("topright", legend = tipo_de_defeito, fill = rainbow(length(tipo_de_defeito)))

# Adicionando título
title("Gráfico de Setores - Tipos de Defeito")
