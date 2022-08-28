from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppTrabajoFinal/inicio.html")

def persona(request):
    return render(request, "AppTrabajoFinal/persona.html")
    
def perro(request):
    return render(request, "AppTrabajoFinal/perro.html")

def gato(request):
    return render(request, "AppTrabajoFinal/gato.html")