# ./cap2.1/appCsvXls.py
import pandas as pd

# Identificação dos arquivos
arquivoCSV = '01PedidoClienteProduto.csv'
arquivoXLSX = '01_primeiro_saida.xlsx'

## Extract
df = pd.read_csv(arquivoCSV, delimiter=',')

# Os prints são desnecessários. Apenas para visualizar o conteúdo das etapas.
print(f"*** Conteúdo do arquivo: {arquivoCSV} ***")
print(df)

print(f"*** Tipo de dados das colunas ***")
print(df.dtypes)

print(f"*** Informações estatísticas das colunas ***")
print(df.describe())

## Transformation
# Altera o nome das colunas
df = df.rename(columns={'num_pedido': 'numero_pedido'})

# Cria um campo para ser usado como ID e move ela para a 1ª posição
df['pedidoID'] = range(1, len(df) + 1)
cols = df.columns.tolist()
cols = ['pedidoID'] + [col for col in cols if col != 'pedidoID']
df = df[cols]
print(f"*** Conteúdo do arquivo após transformação: {arquivoCSV} ***")
print(df)

## Load into file or database
print(f"*** Salvando o arquivo: {arquivoXLSX} ***")
df.to_excel(arquivoXLSX, index=False)
