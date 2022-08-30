from django.urls import path
from .views import *
from .forms import *
urlpatterns=[
    path("", inicio,name="inicio"),
    path("personas/", personas, name="personas"),
    path("perros/", perros,name="perros"),
    path("gatos/", gatos,name="gatos"),
    path("personasFormulario/", personaFormulario,name="personasFormulario" ),
    path("perrosFormulario/", perroFormulario,name="perrosFormulario" ),
    path("gatosFormulario/", gatoFormulario,name="gatosFormulario" ),
    path("busquedaNombre/", busquedaNombre , name="busquedaNombre"),
    
    path("buscar/", buscar , name="buscar"),

]
