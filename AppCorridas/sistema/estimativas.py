import os
from datetime import datetime
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
    tempo_valor = round((elemento.get("duration").get("value")) / 60)


    #return distancia_texto, distancia_valor
    return distancia_valor,tempo,tempo_valor

def calculaUber(distancia,tempo):
    """
    Preço base: R$ 3,05
    Preço mínimo: R$ 6,06
    + por minuto :R$ 0,23
    + por quilômetro: R$ 1,34
    dinamico = Baseado no horario de maior quantidade de carros disponiveis
    """
    preco_km = distancia * 1.34
    preco_minuto = tempo * 0.23
    preco_base = 3.05
    preco_min = 6.06
    if datetime.now().hour > 20 or datetime.now().hour < 6:
        dinamico = 5
        print(dinamico)
    else:
        dinamico = 1.1
    total = preco_km + preco_base + preco_min + preco_minuto + dinamico
    return round(total,2)
def calculaPop(distancia,tempo):
    """
    + por km R$ 1, 14
    + por minuto R$ 0, 19
    tarifa base R$ 2, 38,
    preço mínimo R$ 5, 70
    dinamico = Baseado no horario de maior quantidade de carros disponiveis
    """
    preco_km = distancia * 1.14
    preco_minuto = tempo * 0.19
    preco_base = 2.38
    preco_min = 5.70
    if datetime.now().hour > 20 or datetime.now().hour < 6:
        dinamico = 7.5
        print(dinamico)
    else:
        dinamico = 1.5
    total = preco_km + preco_base + preco_min + preco_minuto + dinamico
    return round(total,2)