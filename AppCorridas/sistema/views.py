from django.shortcuts import render,redirect
from .forms import Corrida
import googlemaps
import os
from dotenv import load_dotenv

#Carregar variaveis de ambiente e a key secret do google maps
load_dotenv()
mapas = googlemaps.Client(key=os.getenv('MAPS'))
def index(request):
    maps = os.getenv('MAPS')
    form = Corrida()

    #Garantir que seja um POST
    if request.method == 'POST':
        form = Corrida(request.POST)

        #Verificar validade da resposta fornecida pelo usuario no formulário
        if form.is_valid():
            # receber valores do usuario
            origem = form["origem"].value()
            destino = form["destino"].value()

            #buscar endereço pelo maps
            origem_data = mapas.geocode(origem)
            destino_data = mapas.geocode(destino)

            #Pegar as cordenadas do endereço(latitude e longitude limitados a 6 caracteres) dos endereços fornecidos para calculo da rota
            lat_origem = round(origem_data[0]['geometry']['location']['lat'],6)
            lon_origem = round(origem_data[0]['geometry']['location']['lng'],6)

            lat_destino = round(destino_data[0]['geometry']['location']['lat'], 6)
            lon_destino = round(destino_data[0]['geometry']['location']['lng'], 6)

            #passar cordenadas para a view da rota atraves da url
            return redirect(f'rota',lat_origem = lat_origem, lon_origem = lon_origem, lat_destino = lat_destino, lon_destino = lon_destino)
    return render(request,'index.html',{"form":form,"MAPS":maps})

def rota(request,lat_origem,lon_origem,lat_destino,lon_destino):

    maps = os.getenv('MAPS')
    #passar cordenadas e secret key do google maps para o template por meio do dicionario
    context = {
        "MAPS": maps,
        "lat_origem": lat_origem,
        "lon_origem": lon_origem,
        "lat_destino": lat_destino,
        "lon_destino": lon_destino,
    }
    return render(request,'rota.html',context)