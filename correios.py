import json
from sys import argv
from api_request import api_request


def rastreamento(cod_objeto):
    api_request(cod_objeto)

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
    rastreamento(argv[1])
