from django.contrib import admin

from Appmensajes.models import Mensaje
from .models import *


admin.site.register(auto)

admin.site.register(sucursal)

admin.site.register(cliente)

admin.site.register(Mensaje)

# Register your models here.
