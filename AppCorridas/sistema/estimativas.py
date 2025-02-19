import os
import googlemaps
from dotenv import load_dotenv
load_dotenv()

mapas = googlemaps.Client(key=os.getenv('MAPS'))
def calcularDistancia(lat_origem,lon_origem,lat_destino,lon_destino):
    pass

def calcularTempo(lat_origem,lon_origem,lat_destino,lon_destino):
    pass