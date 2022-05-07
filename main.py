import requests
import json


def main():
    # Obter JSON [API Correios]
    cod_busca = ""  # código do objeto
    req = requests.get(
        url="https://proxyapp.correios.com.br/v1/sro-rastro/"+cod_busca[0])
    data = req.json()

    # Parseando o JSON
    objeto = data["objetos"][0]["codObjeto"]
    ultimo_status = data["objetos"][0]["eventos"][0]["descricao"]
    data_ultima_atualizacao = data["objetos"][0]["eventos"][0]["dtHrCriado"]

    # Output
    print("-"*50)
    print(f"Código do objeto: {objeto}")
    print(f"Último status: {ultimo_status}")
    print(f"Data da última atualização: {data_ultima_atualizacao[:10]}")
    print(f"Hora da última atualziação: {data_ultima_atualizacao[11:]}")

    return 0


if __name__ == "__main__":
    main()
