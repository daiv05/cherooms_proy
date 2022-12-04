from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import *
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *
from django import forms


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

class PerfilUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUser
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['ciudad'] = CiudadSerializer(instance.ciudad).data
        return response
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
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class HistorialBusquedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialBusqueda
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['perfil'] = PerfilUserSerializer(instance.perfil).data
        return response
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class PublicacionAlquilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionAlquiler
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['perfil'] = PerfilUserSerializer(instance.perfil).data
        return response
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = '__all__'
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class CherosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cheros
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['perfil_user'] = PerfilUserSerializer(instance.perfil_user).data
        response['favorito_user'] = PerfilUserSerializer(instance.favorito_user).data
        return response
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class UserLoginSerializer(serializers.Serializer):
    #campos requeridos para hacer le login
    username = serializers.CharField(min_length=8, max_length=64)
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
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class PreferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferencia
        fields = '__all__'
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class VentaAlquilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaAlquiler
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['perfil'] = PerfilUserSerializer(instance.perfil).data
        response['publicacion'] = PublicacionAlquilerSerializer(
            instance.publicacion).data
        return response
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class HobbieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbie
        fields = '__all__'
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['departamento'] = DepartamentoSerializer(instance.departamento).data
        return response
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class ListaPreferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaPreferencia
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['perfil'] = PerfilUserSerializer(instance.perfil).data
        response['preferencia'] = PreferenciaSerializer(instance.preferencia).data
        return response
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class ListadoHobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListadoHobbies
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['perfil'] = PerfilUserSerializer(instance.perfil).data
        response['hobbie'] = HobbieSerializer(instance.hobbie).data
        return response
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class AmenidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenidad
        fields = '__all__'
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class ListaAmenidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaAmenidad
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['publicacion'] = PublicacionAlquilerSerializer(instance.publicacion).data
        response['amenidad'] = AmenidadSerializer(instance.amenidad).data
        return response
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')
#-----------------Serializador para el registro del usuario
class RegisterSerializer(serializers.Serializer):
    #no hay class meta XD hay que inventar 
    username = serializers.CharField(max_length = 200)
    name = serializers.CharField(max_length = 200)
    lastName = serializers.CharField(max_length =200)
    sexo = serializers.CharField(max_length = 10)
    ciudad =serializers.IntegerField()
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 200)
    necesita_cuarto = serializers.BooleanField()

    def create (self):
        resultado = {}
        try:
            user = User(username = self.data["username"])
            user.set_password(self.data['password'])
            user.save()
            ciudad = Ciudad.objects.get(ciudad_id = self.data['ciudad'])
            try : 
                perfil = PerfilUser(
                    username = self.data["username"],
                    user = user,
                    nombre_user = self.data["name"],
                    genero = self.data["sexo"],
                    email = self.data["email"],
                    apellidos_user = self.data["lastName"],
                    necesita_cuarto = self.data["necesita_cuarto"],
                    ciudad = ciudad
                )
                perfil.save() 
                resultado["perfil"] = perfil
                resultado["user"] = user
                return resultado
            except IntegrityError as error:
                print("Ocurrio un error en la creacion del perfil de usuario  {}".format(error))
                print("Clase de error: {}".format(type(error).__name__))
                print(error.args)
                resultado["error"] = "Ya existe un perfil registrado con el correo {}".format(self.data["email"])
                return resultado
        except IntegrityError as error:
            print ("Ocurrio un error en la creacion del usuario : {} ".format(error))
            print("Clase de error : {}" .format(type(error).__name__))
            resultado["error"] = "Ya existe el usuario :{}. Intente con otro nombre de usuario".format(self.data["username"])
            return resultado

class FiltroSerializer(serializers.Serializer):
    departamento_id = serializers.CharField(max_length = 20, required = False)
    monto_renta = serializers.IntegerField(required = False)
    necesidad_perfil = serializers.BooleanField(required = False)
    param_ciudad = serializers.CharField(max_length = 1024, required = False)