from django.urls import path
from .views import index,rota

urlpatterns = [
    path('',index,name='index'),
    path('rota/<str:lat_origem>/<str:lon_origem>/<str:lat_destino>/<str:lon_destino>/',rota,name='rota'),
]