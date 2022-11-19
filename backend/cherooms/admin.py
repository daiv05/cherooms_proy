from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(PerfilUser)
admin.site.register(PublicacionAlquiler)
admin.site.register(Foto)