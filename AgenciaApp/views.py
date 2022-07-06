from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from AgenciaApp.forms import FormularioAuto
from .models import Auto
from django.template import loader

# Create your views here.


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
                modelo= informacion.get('modelo'))
            auto.save()
        return render(request, "crear_auto.html")
        
    else:
        formulario_auto=FormularioAuto()
    
    return render(request, "crear_auto.html", {'form': formulario_auto})

def busquedaAuto(request):
    
    return render(request, 'busquedaAuto.html')

# def buscar(request):
#     respuesta = f"Estoy buscando el auto: {request.GET['auto']}"
#     return HttpResponse(respuesta)
    
