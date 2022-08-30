from django.db import models

class Personas(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre + " "+ str(self.apellido)

class Perros(models.Model):
    nombre=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)
    edad=models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre + " "+ str(self.raza)

class Gatos(models.Model):
    nombre=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    edad=models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre