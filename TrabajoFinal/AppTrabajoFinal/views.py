from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppTrabajoFinal.forms import *



def inicio(request):
    return render(request, "AppTrabajoFinal/inicio.html")

def personas(request):
    return render(request, "AppTrabajoFinal/personas.html")
    
def perros(request):
    return render(request, "AppTrabajoFinal/perros.html")

def gatos(request):
    return render(request, "AppTrabajoFinal/gatos.html")



def personaFormulario(request):
    if request.method=="POST":
        miformulario=PersonasFormulario(request.POST)
        if miformulario.is_valid():
            info=miformulario.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            edad=info["edad"]
            persona=Personas(nombre=nombre, apellido=apellido, edad=edad)
            persona.save()
            return render(request, "AppTrabajoFinal/personas.html", {"mensaje":"Persona Creada"})
        else:
            return render(request, "AppTrabajoFinal/personas.html", {"mensaje":"Error"})
    else:
        miformulario=PersonasFormulario()
        return render(request, "AppTrabajoFinal/personasFormulario.html", {"formulario":miformulario})


def perroFormulario(request):
    if request.method=="POST":
        miformulario=PerrosFormulario(request.POST)
        if miformulario.is_valid():
            info=miformulario.cleaned_data
            nombre=info["nombre"]
            raza=info["raza"]
            edad=info["edad"]
            perro=Perros(nombre=nombre, raza=raza, edad=edad)
            perro.save()
            return render(request, "AppTrabajoFinal/perros.html", {"mensaje":"Perro creado"})
        else:
            return render(request, "AppTrabajoFinal/perros.html", {"mensaje":"Error"})
    else:
        miformulario=PerrosFormulario()
        return render(request, "AppTrabajoFinal/perrosFormulario.html", {"formulario":miformulario})

def gatoFormulario(request):
    if request.method=="POST":
        miformulario=GatosFormulario(request.POST)
        if miformulario.is_valid():
            info=miformulario.cleaned_data
            nombre=info["nombre"]
            color=info["color"]
            edad=info["edad"]
            gato=Gatos(nombre=nombre, color=color, edad=edad)
            gato.save()
            return render(request, "AppTrabajoFinal/gatos.html", {"mensaje":"Gato Creado"})
        else:
            return render(request, "AppTrabajoFinal/gatos.html", {"mensaje":"Error"})
    else:
        miformulario=GatosFormulario()
        return render(request, "AppTrabajoFinal/gatosFormulario.html", {"formulario":miformulario})



def busquedaNombre(request):
    return render(request, "AppTrabajoFinal/busquedaNombre.html")

def buscar(request):
    if request.GET["nombre"]:
        nom=request.GET["nombre"]
        persona=Personas.objects.filter(nombre=nom)
        if len(persona)!=0:

            return render(request, "AppTrabajoFinal/resultadosBusqueda.html", {"persona":persona})
        else:
            return render(request, "AppTrabajoFinal/resultadosBusqueda.html", {"mensaje": "No hay personas con ese nombre"}) 
    else:
        return render(request, "AppTrabajoFinal/busquedaNombre.html", {"mensaje": "No ingresaste ningun dato!"})