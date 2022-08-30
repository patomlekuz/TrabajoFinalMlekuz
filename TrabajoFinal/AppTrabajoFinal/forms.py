from django import forms

class PersonasFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()

class PerrosFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    raza=forms.CharField(max_length=50)
    edad=forms.IntegerField()

class GatosFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    color=forms.CharField(max_length=50)
    edad=forms.IntegerField()