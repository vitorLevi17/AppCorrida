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
    tempo_valor = round((elemento.get("duration").get("value")) / 60)


    #return distancia_texto, distancia_valor
    return distancia_valor,tempo,tempo_valor


#localização, horário e condições do trânsito.
def calculaUber(distancia,tempo):
    preco_km = distancia * 1.34
    preco_minuto = tempo * 0.23
    preco_base = 3.05
    preco_min = 6.06
    total = preco_km + preco_base + preco_min + preco_minuto
    # Preço base: R$ 3,05
    # Preço mínimo: R$ 6,06
    # + por minuto :R$ 0,23
    # + por quilômetro: R$ 1,34
    return round(total)
def calculaPop(distancia,tempo):
    preco_km = distancia * 1.14
    preco_minuto = tempo * 0.19
    preco_base = 2.38
    preco_min = 5.70
    total = preco_km + preco_base + preco_min + preco_minuto
    # + por km R$ 1, 14
    # + por minuto R$ 0, 19
    # tarifa base R$ 2, 38,
    # preço mínimo R$ 5, 70
    return round(total)