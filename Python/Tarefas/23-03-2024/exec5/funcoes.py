
def carregarCidades():
    with open('cidades.txt', "r") as _f:
        cidades = _f.read()
    return cidades

def criarHtml(cidades):
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
        <head>
            <title>Cidades do Estado de São Paulo</title>
        </head>
        <body>            
    """
    alfabeto = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    for letra in alfabeto:
        for cidade in cidades.split('\n'):
            if cidade.startswith(letra):
                html += f"""
            <h1>{letra}</h1>
                """
                break
        for cidade in cidades.split('\n'):
            if cidade.startswith(letra):
                html += f"""
            <p> {cidade} </p>
                """
    html += """
        </body>
    </html>
    """
    with open("cidades.html", "w") as _f:
        _f.write(html)
