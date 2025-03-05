import os
import googlemaps
import requests
from dotenv import load_dotenv
load_dotenv()

mapas = googlemaps.Client(key=os.getenv('MAPS'))
def calcularDistancia(origem,destino,maps):
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

    #Refatorar esse techo
    if "rows" in dados and dados["rows"] and "elements" in dados["rows"][0]:
        elemento = dados["rows"][0]["elements"][0]

        if "distance" in elemento:
            distancia_texto = elemento["distance"]["text"]
            distancia_valor = elemento["distance"]["value"]
        else:
            distancia_texto = " "
            distancia_valor = 0
    else:
        distancia_texto, distancia_valor = "Erro", 0

    return distancia_texto, distancia_valor
