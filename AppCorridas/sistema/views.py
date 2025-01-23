from django.shortcuts import render
from .forms import Corrida

def index(request):
    form = Corrida()
    if request.method == 'POST':
        form = Corrida(request.POST)
        if form.is_valid():
            origem = form["origem"].value()
            destino = form["destino"].value()
            print(origem,destino)


    return render(request,'index.html',{"form":form})
