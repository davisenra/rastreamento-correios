import requests
import json
from sys import argv


def rastreamento_correios(cod_objeto):
    req = requests.get(
        url="https://proxyapp.correios.com.br/v1/sro-rastro/"+cod_objeto)
    resposta = req.json()

    with open("search_output.json", "w", encoding="utf-8") as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)

    output = open("search_output.json")
    data = json.load(output)

    objeto = data["objetos"][0]["codObjeto"]
    tipo_postal = data["objetos"][0]["tipoPostal"]["categoria"]

    print(f"Código do objeto: {objeto}")
    print(f"Tipo postal: {tipo_postal}")

    eventos = data["objetos"][0]["eventos"][0]
    i = 0
    for evento in eventos:
        status_evento = data["objetos"][0]["eventos"][i]["descricao"]
        data_evento = data["objetos"][0]["eventos"][i]["dtHrCriado"][:10]
        hora_evento = data["objetos"][0]["eventos"][i]["dtHrCriado"][11:16]

        print(f"")
        print(f"Status: {status_evento}")
        print(f"Data: {data_evento}")
        print(f"Hora: {hora_evento}")
        i += 1

    return 0


if __name__ == "__main__":
    rastreamento_correios(argv[1])
