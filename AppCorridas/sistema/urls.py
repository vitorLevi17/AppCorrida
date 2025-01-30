from django.urls import path
from .views import index,comparar

urlpatterns = [
    path('',index,name='index'),
    path('comparar/<str:lat_origem>/<str:lon_origem>/<str:lat_destino>/<str:lon_destino>/',comparar,name='comparar'),
]