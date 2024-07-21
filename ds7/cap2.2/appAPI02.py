# ./cap2.2/appAPI02.py
import pandas as pd
import requests
import psycopg2

# Identificação das APIs
apiURLProdutosEstatisticas = "https://servicodados.ibge.gov.br/api/v1/produtos/estatisticas"

## Extract
response = requests.get(apiURLProdutosEstatisticas)

# Verifica se a requisição foi realizada com sucesso
if response.status_code == 200:
    data = response.json()
else:
    print(f"Falha em buscar a API. Código do status: {response.status_code}")

## Transform
# Criando um dataframe com os dados da API
df = pd.DataFrame(data)
print(f"Valor DF")
print(df)

## Load
# Parâmetros de conexão

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

try:
    # Conecta com o Postgres
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    # Cria tabela para persistir os dados
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS produtos_estatisticas (
        prodestatID BIGSERIAL PRIMARY KEY,
        id BIGINT,
        tipo VARCHAR,
        titulo VARCHAR,
        alias VARCHAR,
        sigla VARCHAR,
        catid bigint,
        catTitle VARCHAR,
        parentCatId BIGINT,
        parentCatTitle VARCHAR,
        path TEXT
    );
    '''
    cur.execute(create_table_query)
    conn.commit()
    # Insert para inserir os dados
    insert_query = '''
        INSERT INTO produtos_estatisticas (
            id,
            tipo,
            titulo,
            alias,
            sigla,
            catid,
            catTitle,
            parentCatId,
            parentCatTitle,
            path
        )
        VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    for _, row in df.iterrows():
        # Necessário para inserir somente IDs que ainda não estão no banco de dados.
        cur.execute("SELECT id FROM produtos_estatisticas where id = %s", (row['id'],))
        existing_id = cur.fetchone()
        if existing_id == None:
            cur.execute(insert_query, (row['id'],
            row['tipo'],
            row['titulo'],
            row['alias'],
            row['sigla'],
            row['catId'],
            row['catTitle'],
            row['parentCatId'],
            row['parentCatTitle'],
            row['path']
        ))
    conn.commit()
    cur.close()
    conn.close()
except psycopg2.OperationalError as e:
    print(e)