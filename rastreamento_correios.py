import requests
import json
from sys import argv


def rastreamento_correios(cod_objeto):
    # Obter JSON [API Correios]
    req = requests.get(
        url="https://proxyapp.correios.com.br/v1/sro-rastro/"+cod_objeto)
    data = req.json()

    # Parseando o JSON
    objeto = data["objetos"][0]["codObjeto"]
    ultimo_status = data["objetos"][0]["eventos"][0]["descricao"]
    ultima_atualizacao = data["objetos"][0]["eventos"][0]["dtHrCriado"]

    # Output
    print("-"*50)
    print(f"Código do objeto: {objeto}")
    print(f"Status: {ultimo_status}")
    print(f"Data: {ultima_atualizacao[:10]}")
    print(f"Hora: {ultima_atualizacao[11:]}")

    return 0


if __name__ == "__main__":
    rastreamento_correios(argv[1])
