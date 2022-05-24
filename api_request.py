import requests
import json


def api_request(cod_objeto):
    req = requests.get(
        url="https://proxyapp.correios.com.br/v1/sro-rastro/"+cod_objeto)
    resposta = req.json()

    with open("search_output.json", "w", encoding="utf-8") as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)

    return 0
