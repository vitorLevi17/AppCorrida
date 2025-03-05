import os
import googlemaps
import requests
from dotenv import load_dotenv
load_dotenv()

mapas = googlemaps.Client(key=os.getenv('MAPS'))
def calcularTempoDistancia(origem,destino,maps):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    params = {
        "origins": origem,
        "destinations": destino,
        "mode": "driving",
        "units": "metric",
        "avoidHighways": "false",
        "avoidTolls": "false",
        "key": maps,
    }

    response = requests.get(url,params)
    dados = response.json()

    elemento = dados.get("rows")[0].get("elements")[0]
    #distancia_texto = elemento.get("distance").get("text")
    distancia_valor = (elemento.get("distance").get("value")) / 1000
    tempo = elemento.get("duration").get("text")
    tempo_valor = elemento.get("duration").get("value")


    #return distancia_texto, distancia_valor
    return distancia_valor,tempo,tempo_valor


def calculaUber(request):
    # Preço base: R$ 3,05
    # Preço mínimo: R$ 6,06
    # + por minuto :R$ 0,23
    # + por quilômetro: R$ 1,34
    # Custo fixo: R$ 1,10
    pass
def calculaPop(request):
    # + por km R$ 1, 14
    # + por minuto R$ 0, 19
    # tarifa base R$ 2, 38,
    # preço mínimo R$ 5, 70
    pass