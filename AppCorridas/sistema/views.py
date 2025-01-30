from django.shortcuts import render,redirect
from .forms import Corrida
import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()
mapas = googlemaps.Client(key=os.getenv('MAPS'))
def index(request):
    maps = os.getenv('MAPS')
    form = Corrida()
    if request.method == 'POST':
        form = Corrida(request.POST)
        if form.is_valid():
            origem = form["origem"].value()
            destino = form["destino"].value()

            origem_data = mapas.geocode(origem)
            destino_data = mapas.geocode(destino)

            lat_origem = round(origem_data[0]['geometry']['location']['lat'],6)
            lon_origem = round(origem_data[0]['geometry']['location']['lng'],6)

            lat_destino = round(destino_data[0]['geometry']['location']['lat'], 6)
            lon_destino = round(destino_data[0]['geometry']['location']['lng'], 6)

            return redirect(f'comparar',lat_origem = lat_origem, lon_origem = lon_origem, lat_destino = lat_destino, lon_destino = lon_destino)
    return render(request,'index.html',{"form":form,"MAPS":maps})

def comparar(request,lat_origem,lon_origem,lat_destino,lon_destino):
    print(lat_origem, lon_origem, lat_destino, lon_destino)
    return render(request,'comparar.html')