# Criando os vetores
tipo_de_defeito <- c('linha ruidosa', 'linha aberta', 'alarme', 'nao_responde', 'nao_toca')
ocorrencia <- c(250, 110, 85, 45, 25)

# Montando a matriz
matriz_defeito_ocorrencia <- matrix(c(tipo_de_defeito, ocorrencia), ncol = 2, byrow = FALSE)

# Nomeando as colunas
colnames(matriz_defeito_ocorrencia) <- c('Tipo de Defeito', 'Ocorrência')

matriz_defeito_ocorrencia
