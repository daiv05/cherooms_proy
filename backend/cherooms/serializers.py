from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
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
        #response['ciudad_id'] = CiudadSerializer(instance.ciudad_id).data
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
        #response['pais_id'] = PaisSerializer(instance.pais_id).data
        return response

class HistorialBusquedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialBusqueda
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['perfil_id'] = PerfilUserSerializer(instance.perfil_id).data
        return response

class PublicacionAlquilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionAlquiler
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['perfil_id'] = PerfilUserSerializer(instance.perfil_id).data
        return response

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = '__all__'

class CherosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cheros
        fields = '__all__'

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
class PerfilUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUser
        fields = "__all__"

class UserLoginSerializer(serializers.Serializer):
    #campos requeridos para hacer le login
    username = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    #validacion de los datos
    def validate(self,data):
        user = authenticate(username = data['username'] , password = data["password"])
        if not user:
            raise serializers.ValidationError("Las credenciales no estan registradas")
        
        self.context["user"] = user
        return data
    def create(self, data):
        #crear el token o generarlo
        token, created = Token.objects.get_or_create(user = self.context["user"])
        return self.context["user"], token.key