from django.urls import path
from .views import index,comparar

urlpatterns = [
    path('',index,name='index'),
    path('comparar/',comparar,name='comparar'),
]