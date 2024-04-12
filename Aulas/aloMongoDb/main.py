from pymongo import *
import re

con = MongoClient(
    'localhost',
    27017
)

try:
    con.server_info()
    db = con["moviesdb"]
    collection = db["movie"]
    genero = 'Action'
    palavra_chave_title = 'Dream'
    palavra_chave_extract = 'Dream'
    query = {
        "$and": [
            {"genres": genero},
            {"$or": [
                {"title": {"$regex": palavra_chave_title, "$options": "i"}},
                {"extract": {"$regex": palavra_chave_extract, "$options": "i"}}
            ]}
        ]
    }
    glist = []
    dados = collection.find(filter=query)
    for movie in dados:
        glist.append(movie['title'])
    gset = set(glist)
    glist = sorted(gset)
    print(glist)
    # filtro: filmes de um determinado gênero que possua uma
    # deterinada palavra-chave no título ou na sinopse (extract)
except Exception as e:
    print(e)
