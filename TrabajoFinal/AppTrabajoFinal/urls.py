from django.urls import path
from .views import *

urlpatterns=[
    path("", inicio),
    path("persona/", persona),
    path("perro/", perro),
    path("gato/", gato),





]
