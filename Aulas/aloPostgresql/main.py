import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres', 
    password='postgres123'
)

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

sql_select = "select * from cidade,estado where cidade.cod_estado=estado.cod_estado"
cur.execute(sql_select)
dados = cur.fetchall()
for info in dados:
    print(info['nom_cidade'],' ',info['nom_estado'])
