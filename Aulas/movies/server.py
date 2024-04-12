from flask import Flask, request
from datetime import date
from pymongo import *
import re
import json


app = Flask(__name__)

@app.route('/apis/get-generos/')
def getGeneros():
    con = MongoClient(
        'localhost',
        27017
    )
    try:
        con.server_info()
        db = con["moviesdb"]
        collection = db["filmes"]
        # query = {}
        query = {"cast":re.compile(r"Hor")}
        # project={'_id':0, 'genres': 1}
        glist = [] 
        dados = collection.find(query)
        for movie in dados:
            glist += movie
        # gset = set(glist)
        # glist = list(gset)
        # glist.sort()
        con.close()
        print(glist)
        return glist
        
        # filtro: filmes de um determinado gêneroque possua uma
        # deterinada palavra-chave no título ou na sinopse (extract)
    except Exception as e:
        print(e)

@app.route('/apis/filmes/')
def filmes():
    # 'mongodb://localhost:27017/'
    password = 'VDccwIJFNiwB0AnW'
    host = f'mongodb+srv://zicadopv:{password}@cluster0.2czwqjr.mongodb.net/'
    con = MongoClient(host)
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
    print(glist)
    gset = set(glist)
    glist = sorted(gset)
    return json.dumps(glist)


app.run(
    host='localhost',
    port=8000,
    debug=True
)