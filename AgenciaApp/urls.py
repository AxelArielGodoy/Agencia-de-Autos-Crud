from .views import busquedaAuto, index, crear_auto
from django.urls import path
from AgenciaApp.views import busquedaAuto, index, crear_auto

urlpatterns = [
    path('', index, name='index'),
    path('crearauto/', crear_auto, name='crear_auto'),
    path('busquedaAuto/', busquedaAuto, name="busqueda_auto"),
    # path('buscar/', buscar),
   
]