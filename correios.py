#!/usr/bin/env python3

import requests
import json
from sys import argv
from typing import Dict


def main():
    if (len(argv) != 2):
        print(f"Utilização: python correios.py [código do objeto]")
    else:
        track_object(api_request(argv[1]))

    return


def api_request(object_code: str) -> Dict:
    req = requests.get(
        url="https://proxyapp.correios.com.br/v1/sro-rastro/"+object_code)
    r = req.json()

    return r


def track_object(json_response: Dict):
    data = json_response
    tracked_object = data["objetos"][0]["codObjeto"]
    ojbect_type = data["objetos"][0]["tipoPostal"]["categoria"]
    event = data["objetos"][0]["eventos"][0]

    print(f"Código do objeto: {tracked_object}")
    print(f"Tipo postal: {ojbect_type}")

    i = 0
    for each_event in event:
        try:
            event_status = data["objetos"][0]["eventos"][i]["descricao"]
            event_date = data["objetos"][0]["eventos"][i]["dtHrCriado"][:10]
            event_hour = data["objetos"][0]["eventos"][i]["dtHrCriado"][11:16]
            event_city = data["objetos"][0]["eventos"][i]["unidade"]["endereco"]["cidade"]
            event_state = data["objetos"][0]["eventos"][i]["unidade"]["endereco"]["uf"]

            print(f"")
            print(f"Status: {event_status}")
            print(f"Data: {event_date}")
            print(f"Hora: {event_hour}")
            print(f"Cidade/Estado: {event_city.rstrip()}/{event_state}")
            i += 1
        except:
            break

    return 0


if __name__ == "__main__":
    main()
