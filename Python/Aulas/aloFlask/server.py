from flask import Flask, request
from datetime import date

app = Flask(__name__)


@app.route('/apis/')
def Alo():
    return "Alô Flask"


@app.route('/apis/diga-data/<string:dma>/')
def data(dma):
    mens = "não entendi"
    if dma == 'dia':
        mens = date.today().day
    elif dma == 'mes':
        mens = date.today().month
    elif dma == 'ano':
        mens = date.today().year
    return str(mens)


@app.route('/apis/diga-dataq/')
def dataq():
    dma = request.args['dma']
    mens = "não entendi"
    if dma == 'dia':
        mens = date.today().day
    elif dma == 'mes':
        mens = date.today().month
    elif dma == 'ano':
        mens = date.today().year
    return str(mens)

@app.route('/apis/movies/')
def dataq():
    dma = request.args['dma']
    mens = "não entendi"
    if dma == 'dia':
        mens = date.today().day
    elif dma == 'mes':
        mens = date.today().month
    elif dma == 'ano':
        mens = date.today().year
    return str(mens)



app.run(
    host='localhost',
    port=8000,
    debug=True
)
