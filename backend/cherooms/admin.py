from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(PerfilUser)
admin.site.register(PublicacionAlquiler)
admin.site.register(Foto)
admin.site.register(Pais)
admin.site.register(Preferencia)
admin.site.register(Departamento)
admin.site.register(VentaAlquiler)
admin.site.register(Hobbie)
