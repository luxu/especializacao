import json

from flask import Flask, render_template
# from flask_cors import CORS
from megasena import MegasenaClass

app = Flask(__name__, template_folder='../frontend/templates')


@app.route('/')
def home():
    template_name = 'index.html'
    return render_template(template_name)

@app.route('/ocorrencias')
def ocorrencias():
    template_name = 'index.html'
    megasena = MegasenaClass()
    ocorrencias = megasena.getOcorrencias()
    return render_template(template_name, len=len(ocorrencias), ocorrencias=ocorrencias)

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8000,
        debug=True
    )
