from django.shortcuts import render
from django.http import HttpResponse
from AgenciaApp.forms import BusquedaAuto, FormularioAuto
from .models import Auto


def index(request):
    return render(request, 'base.html')

def crear_auto(request):
    if request.method == 'POST':
        formulario_auto = FormularioAuto(request.POST)
        print(formulario_auto)
        
        if formulario_auto.is_valid:
            
            informacion = formulario_auto.cleaned_data
            auto = Auto(
                marca=informacion.get('marca'), 
                color =informacion.get('color'), 
                modelo= informacion.get('modelo')
                )
            auto.save()
        
        return render(request, "crear_auto.html", {'crear_auto': crear_auto})
        
    else:
        formulario_auto=FormularioAuto()
    return render(request, "crear_auto.html", {'form': formulario_auto})


# def busqueda_autos(request):
    
#     busqueda_autos = Auto.objects.all()
#     form = BusquedaAuto()
    
#     return render(request, "busquedaAuto.html", {'busqueda_autos': busqueda_autos, 'form': form})

def busqueda_autos(request):
    marca_de_busqueda = request.GET.get('marca')
    
    if marca_de_busqueda:
        busqueda_autos = Auto.objects.filter(marca__icontains=marca_de_busqueda)
    else:
        busqueda_autos = Auto.objects.all()
        
    form = BusquedaAuto()    
    return render(request, "busquedaAuto.html", {'busqueda_autos': busqueda_autos, 'form': form})