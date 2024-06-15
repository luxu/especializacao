dados <- read.table("Milsa.txt", header = T)
dados
# Tabela de frequências da variável Instrução
freq_instrucao <- table(dados$instr)
# > freq_instrucao
#  1  2  3 
# 13 19  8 

freq_instrucao_rel <- prop.table(freq_instrucao)
# > freq_instrucao_rel
#     1     2     3 
# 0.325 0.475 0.200 

# Tabela de frequências da variável Região
freq_regiao <- table(dados$regiao)
#freq_regiao
#  1  2  3 
# 13 13 14 

freq_regiao_rel <- prop.table(freq_regiao)
# > freq_regiao_rel
#     1     2     3 
# 0.325 0.325 0.350 
