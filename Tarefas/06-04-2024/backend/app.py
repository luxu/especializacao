import json

from flask import Flask, render_template, request, jsonify
from megasena import MegasenaClass

app = Flask(__name__, template_folder='../frontend/templates')


@app.route('/')
def home():
    template_name = 'index.html'
    return render_template(template_name)


@app.route('/ocorrencias')
def ocorrencias():
    template_name = 'ocorrencias.html'
    megasena = MegasenaClass()
    ocorrencias = megasena.getOcorrencias()
    return render_template(template_name, len=len(ocorrencias), ocorrencias=ocorrencias)


@app.route('/volante')
def volante():
    template_name = 'cartela.html'
    return render_template(template_name)


@app.route('/conferir', methods=['POST'])
def conferir():
    numbers = json.loads(request.data)['numbers']
    megasena = MegasenaClass()
    resultado = megasena.conferir(numbers)
    response_data = {
        'result': resultado,
        'status': 'success'
    }
    return jsonify(response_data), 200

@app.route('/sugerir')
def sugerir():
    template_name = 'sugerir.html'
    megasena = MegasenaClass()
    resultados = megasena.getOcorrencias()[:30]
    return render_template(template_name, resultados=resultados)

@app.route('/sugerir-jogo')
def sugerirJogo():
    megasena = MegasenaClass()
    # Carrego os 30 primeiros
    megasena.numerosMaisSorteados()
    oitoNumerosEscolhidosAleatorios = megasena.sugerirJogo()
    resultado = megasena.conferir(oitoNumerosEscolhidosAleatorios)
    print(resultado)
    response_data = {
        'result': resultado,
        'status': 'success'
    }
    return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(debug=True)
