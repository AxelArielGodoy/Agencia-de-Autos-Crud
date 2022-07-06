from django.urls import path
from AgenciaApp.views import index, crear_auto,busqueda_autos

urlpatterns = [
    path('', index, name='index'),
    path('crearauto/', crear_auto, name='crear_auto'),
    path('busquedaAuto/', busqueda_autos, name="busquedaAuto"),  
]