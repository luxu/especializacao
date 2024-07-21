# cap2.3/appETL.py

import pandas as pd

# ETL Cliente
from a_extract.extCliente import executeExtract as cliExecuteExtract
from b_transform.transCliente import executeTransform as cliExecuteTransform
from c_load.loadCliente import executeLoad as cliExecuteLoad

# ETL Vendedor
# from a_extract.extVendedor import executeExtract as vendExecuteExtract
# from b_transform.transVendedor import executeTransform as vendExecuteTransform
# from c_load.loadVendedor import executeLoad as vendExecuteLoad

# ETL Produto
# from a_extract.extProduto import executeExtract as prodExecuteExtract
# from b_transform.transProduto import executeTransform as prodExecuteTransform
# from c_load.loadProduto  import executeLoad as prodExecuteLoad

# ETL Tempo
# from c_load.loadTempo  import executeLoad as tempoExecuteLoad

# ETL Pedido
# from a_extract.extPedido import executeExtract as pedExecuteExtract
# from b_transform.transPedido import executeTransform as pedExecuteTransform
# from c_load.loadPedido  import executeLoad as pedExecuteLoad

#******** ETL CLIENTE *******
# Chama a função para EXTRAIR os dados

print("++++++++++")
df_cliResults = cliExecuteExtract()

# Mostra os dados do DataFrame. Essa parte não é obrigatório. Apenas para Visulização. Defe ser retira na versão de produção
if df_cliResults is None:
    print("[appETLpy] Falha a executar a extração de CLIENTES")
    quit()
# else:    
    # print(f"Valor do DF após extração: {df_cliResults}")


# Chama a função para TRANSFORMAR os dados
df_cliResults = cliExecuteTransform(df_cliResults)

# Mostra os dados do DataFrame. Essa parte não é obrigatório. Apenas para Visulização. Defe ser retira na versão de produção
if df_cliResults is None:
    print("[appETLpy] Falha a executar a transformação de CLIENTES")
    quit()
# else:
#     print(f"Valor do DF após transformação: {df_cliResults}")


# Chama a função para CARREGAR os dados bo banco de dados
df_cliResults = cliExecuteLoad(df_cliResults)

# Mostra os dados do DataFrame. Essa parte não é obrigatório. Apenas para Visulização. Deve ser retira na versão de produção
if df_cliResults is None:
    print("[appETLpy] Falha a executar o carregamento para o banco de dados de CLIENTES")
    quit()
# else:    
#     print (f"Valor do DF após carregamento no banco de dados: ")