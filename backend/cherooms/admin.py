from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(PerfilUser)
admin.site.register(PublicacionAlquiler)
admin.site.register(Foto)
admin.site.register(Cheros)
admin.site.register(Pais)
admin.site.register(Preferencia)
admin.site.register(Departamento)
admin.site.register(VentaAlquiler)
admin.site.register(Hobbie)
admin.site.register(Amenidad)
admin.site.register(ListadoHobbies)
admin.site.register(Ciudad)
admin.site.register(ListaAmenidad)
admin.site.register(HistorialBusqueda)
admin.site.register(ListaPreferencia)
admin.site.register(ListaFotos)