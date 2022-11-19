from rest_framework import serializers
from .models import *

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
class PerfilUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUser
        fields = '__all__'
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class HistorialBusquedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialBusqueda
        fields = '__all__'