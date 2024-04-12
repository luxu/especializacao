import os
from funcoes import (
    carregarCidades,
    criarHtml
)

if __name__ == "__main__":
    cidades = carregarCidades()
    criarHtml(cidades)
    os.system('cidades.html')
