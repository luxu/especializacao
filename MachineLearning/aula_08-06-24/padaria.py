import pandas as pd

cookies = 'R$ 3,50'
brownies = 'R$ 5,20'

# ler csv
df = pd.read_csv('padaria.csv')
print(df)

# Quantos cookies e brownies preciso vender para ter um faturamento
# bom

# F(x) = c * 