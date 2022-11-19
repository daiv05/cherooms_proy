from rest_framework import serializers
from .models import *

class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# --------------ESTE ES EL EJEMPLO, la funcion to_representation IGNORAR
# ------------------------LUEGO LA ESTARÉ AGREGANDO--------------------------------
# ---------------------------------------------------------------------------------
class PerfilUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUser
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        #response['ciudad'] = CiudadSerializer(instance.ciudad).data
        return response
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['pais'] = PaisSerializer(instance.pais).data
        return response

class HistorialBusquedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialBusqueda
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['perfil'] = PerfilUserSerializer(instance.perfil).data
        return response

class PublicacionAlquilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionAlquiler
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['perfil'] = PerfilUserSerializer(instance.perfil).data
        return response

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = '__all__'

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class PreferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferencia
        fields = '__all__'


# --------------VentaAlquiler & Hobbie-------------------------------------------------------------------
class VentaAlquilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaAlquiler
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['perfil'] = PerfilUserSerializer(instance.perfil).data
        response['publicacion'] = PublicacionAlquilerSerializer(instance.publicacion).data
        return response

class HobbieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbie
        fields = '__all__'
# ---------------------------------------------------------------------------------