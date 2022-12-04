from django.shortcuts import render
from django.contrib.auth.models import User #es el modelo para realizar la autenticación 
from .models import *
from .serializers import *
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.http import Http404
from decimal import Decimal
# Para el Login
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache  import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
import base64, os


# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class UserToken(APIView):
    """
    Retrieve, update or delete a PerfilUser instance.
    """
    def get(self, request, format=None):
        elperfil = PerfilUser.objects.get(user=request.user.id)
        if elperfil.foto_perfil:
                foto = base64.b64encode(elperfil.foto_perfil.file.read())
                elperfil.foto64 = 'data:image/jpeg;base64,' + foto.decode('utf-8')
        serializer = PerfilUserSerializer(elperfil)
        return Response(serializer.data)


class PerfilUserList(APIView):
    """
    List all PerfilUser, or create a new PerfilUser.
    """
    def get(self, request, format=None):
        perfil = PerfilUser.objects.all()
        for p in perfil:
            if p.foto_perfil:
                foto = base64.b64encode(p.foto_perfil.file.read())
                p.foto64 = 'data:image/jpeg;base64,' + foto.decode('utf-8')
        serializer = PerfilUserSerializer(perfil, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PerfilUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerfilUserDetail(APIView):
    """
    Retrieve, update or delete a PerfilUser instance.
    """

    def get_object(self, pk):
        try:
            return PerfilUser.objects.get(pk=pk)
        except PerfilUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        perfil = self.get_object(pk)
        serializer = PerfilUserSerializer(perfil)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        perfil = self.get_object(pk)
        serializer = PerfilUserSerializer(perfil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        perfil = self.get_object(pk)
        perfil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class DepartamentoList(APIView):
    """
    List all Departamentos, or create a new Departamento.
    """

    def get(self, request, format=None):
        departamento = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamento, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartamentoDetail(APIView):
    """
    Retrieve, update or delete a PerfilUser instance.
    """

    def get_object(self, pk):
        try:
            return Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        perfil = self.get_object(pk)
        serializer = DepartamentoSerializer(perfil)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        perfil = self.get_object(pk)
        serializer = DepartamentoSerializer(perfil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        perfil = self.get_object(pk)
        perfil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------


class HistorialBusquedaList(APIView):
    """
    List all HistorialBusqueda, or create a new HistorialBusqueda.
    """

    def get(self, request, format=None):
        hisorialbusqueda = HistorialBusqueda.objects.all()
        serializer = HistorialBusquedaSerializer(hisorialbusqueda, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HistorialBusquedaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HistorialBusquedaDetail(APIView):
    """
    Retrieve, update or delete a PerfilUser instance.
    """

    def get_object(self, pk):
        try:
            return HistorialBusqueda.objects.get(pk=pk)
        except HistorialBusqueda.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        perfil = self.get_object(pk)
        serializer = HistorialBusquedaSerializer(perfil)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        perfil = self.get_object(pk)
        serializer = HistorialBusquedaSerializer(perfil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        perfil = self.get_object(pk)
        perfil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        user_id = Token.objects.get(key=request.data.get('token')).user_id
        user = User.objects.get(id=user_id)
        return Response({'token': user.id})


class PublicacionAlquilerList(APIView):
    """
    List all PublicacionAlquiler, or create a new PublicacionAlquiler.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        publicacionalquiler = PublicacionAlquiler.objects.all()
        serializer = PublicacionAlquilerSerializer(
            publicacionalquiler, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        elperfil = PerfilUser.objects.get(user=request.user.id)
        print(elperfil.genero)
        request.data['perfil'] = elperfil.perfil_id
        serializer = PublicacionAlquilerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublicacionAlquilerDetail(APIView):
    """
    Retrieve, update or delete a PublicacionAlquiler instance.
    """

    def get_object(self, pk):
        try:
            return PublicacionAlquiler.objects.get(pk=pk)
        except PublicacionAlquiler.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        publicacionalquiler = self.get_object(pk)
        serializer = PublicacionAlquilerSerializer(publicacionalquiler)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        publicacionalquiler = self.get_object(pk)
        serializer = PublicacionAlquilerSerializer(
            publicacionalquiler, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        publicacionalquiler = self.get_object(pk)
        publicacionalquiler.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class FotoList(APIView):
    """
    List all Foto, or create a new Foto.
    """

    def get(self, request, format=None):
        foto = Foto.objects.all()
        serializer = FotoSerializer(foto, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FotoDetail(APIView):
    """
    Retrieve, update or delete a Foto instance.
    """

    def get_object(self, pk):
        try:
            return Foto.objects.get(pk=pk)
        except Foto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        foto = self.get_object(pk)
        serializer = FotoSerializer(foto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        foto = self.get_object(pk)
        serializer = FotoSerializer(foto, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        foto = self.get_object(pk)
        foto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class CheroList(APIView):
    #permission_classes = (IsAuthenticated,)   
    #authentication_classes = (TokenAuthentication,)
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request, *args, **kwargs):
        id_usuario = request.user.id
        print(request.user)
        perfil = PerfilUser.objects.get(user = id_usuario)
        mis_cheros = Cheros.objects.filter(perfil_user = perfil.perfil_id)
        serializer = PerfilUserSerializer(self.obtener_perfil_cheros(mis_cheros) ,many = True)
        print(serializer.data)
        return Response(serializer.data)

    def obtener_perfil_cheros(self,mis_cheros):
        lista_perfil_cheros = []
        for chero in mis_cheros:
            lista_perfil_cheros.append(PerfilUser.objects.get(perfil_id = chero.favorito_user.perfil_id))
        return lista_perfil_cheros
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('chero-list')
    #metodo que 
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args,**kwargs):
        if request.user.is_authenticated:
            print(request.user.username)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)
    def form_valid(self, form):
        print(form)
        user = authenticate(username = form.cleaned_data["username"], password = form.cleaned_data["password"])
        #ahora hay que buscar el token asociado a este usuario
        token = Token.objects.get_or_create(user = user)
        if token:
            login(self.request,form.get_user())
            return super(Login,self).form_valid(form)
        return super().form_valid(form)

#vista para logiar y authenticar a los usuarios
class Logout(APIView):
    def get(self, request, format = None):
        tempToken = request.GET.get("token", "")
        if tempToken :
            print("Se recupero el token desde el frontend y es {}".format(tempToken))
            token = Token.objects.get(key = tempToken)
            token.delete()
            return Response(status=status.HTTP_200_OK)
        else :
            return Response( { "error" : "no se proporciono un token para cerrar sesión"},status = status.HTTP_404_NOT_FOUND)
        #request.user.auth_token.delete()
        #logout(request)

def index(request):
    return render(request,"index.html")

"""
class UserViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active = True)
    serializer_class = UserModelSerializer

    @action(detail=False, methods = ['post'])
    def login(self, request):
        "funcion para logearse"
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user' : UserModelSerializer(user).data,
            'acces_token' : token
        }
        return Response(data, status = status.HTTP_201_CREATED)
"""

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class PaisList(APIView):
    """
    List all Pais, or create a new Pais.
    """

    def get(self, request, format=None):
        pais = Pais.objects.all()
        serializer = PaisSerializer(pais, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaisDetail(APIView):
    """
    Retrieve, update or delete a Pais instance.
    """

    def get_object(self, pk):
        try:
            return Pais.objects.get(pk=pk)
        except Pais.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pais = self.get_object(pk)
        serializer = PaisSerializer(pais)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pais = self.get_object(pk)
        serializer = PaisSerializer(pais, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pais = self.get_object(pk)
        pais.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class PreferenciaList(APIView):
    """
    List all Preferencia, or create a new Pais.
    """

    def get(self, request, format=None):
        preferencia = Preferencia.objects.all()
        serializer = PreferenciaSerializer(preferencia, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PreferenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PreferenciaDetail(APIView):
    """
    Retrieve, update or delete a Preferencia instance.
    """

    def get_object(self, pk):
        try:
            return Preferencia.objects.get(pk=pk)
        except Preferencia.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        preferencia = self.get_object(pk)
        serializer = PreferenciaSerializer(preferencia)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        preferencia = self.get_object(pk)
        serializer = PreferenciaSerializer(preferencia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        preferencia = self.get_object(pk)
        preferencia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class VentaAlquilerList(APIView):
    """
    List all PerfilUser, or create a new PerfilUser.
    """

    def get(self, request, format=None):
        ventaAlquiler = VentaAlquiler.objects.all()
        serializer = VentaAlquilerSerializer(ventaAlquiler, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VentaAlquilerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VentaAlquilerDetail(APIView):
    """
    Retrieve, update or delete a VentaAlquiler instance.
    """

    def get_object(self, pk):
        try:
            return VentaAlquiler.objects.get(pk=pk)
        except VentaAlquiler.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ventaAlquiler = self.get_object(pk)
        serializer = VentaAlquilerSerializer(ventaAlquiler)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ventaAlquiler = self.get_object(pk)
        serializer = VentaAlquilerSerializer(ventaAlquiler, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ventaAlquiler = self.get_object(pk)
        ventaAlquiler.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class HobbieList(APIView):
    """
    List all PerfilUser, or create a new PerfilUser.
    """

    def get(self, request, format=None):
        hobbie = Hobbie.objects.all()
        serializer = HobbieSerializer(hobbie, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HobbieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HobbieDetail(APIView):
    """
    Retrieve, update or delete a VentaAlquiler instance.
    """

    def get_object(self, pk):
        try:
            return Hobbie.objects.get(pk=pk)
        except Hobbie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hobbie = self.get_object(pk)
        serializer = HobbieSerializer(hobbie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hobbie = self.get_object(pk)
        serializer = HobbieSerializer(hobbie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hobbie = self.get_object(pk)
        hobbie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------


class CiudadList(APIView):
    """
    List all Ciudad, or create a new Ciudad.
    """

    def get(self, request, format=None):
        ciudad = Ciudad.objects.all()
        serializer = CiudadSerializer(ciudad, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CiudadDetail(APIView):
    """
    Retrieve, update or delete a ciudad instance.
    """

    def get_object(self, pk):
        try:
            return Ciudad.objects.get(pk=pk)
        except Ciudad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ciudad = self.get_object(pk)
        serializer = CiudadSerializer(ciudad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ciudad = self.get_object(pk)
        serializer = CiudadSerializer(ciudad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ciudad = self.get_object(pk)
        ciudad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class ListaPreferenciaList(APIView):
    """
    List all listado de preferencias, or create a new Listado.
    """

    def get(self, request, format=None):
        listaPreferencia = ListaPreferencia.objects.all()
        serializer = ListaPreferenciaSerializer(listaPreferencia, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListaPreferenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListaPreferenciaDetail(APIView):
    """
    Retrieve, update or delete a listadePreferncia instance.
    """

    def get_object(self, pk):
        try:
            return ListaPreferencia.objects.get(pk=pk)
        except ListaPreferencia.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        listaPreferencia = self.get_object(pk)
        serializer = ListaPreferenciaSerializer(listaPreferencia)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        listaPreferencia = self.get_object(pk)
        serializer = ListaPreferenciaSerializer(
            listaPreferencia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        listaPreferencia = self.get_object(pk)
        listaPreferencia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class ListadoHobbiesList(APIView):
    """
    List all Hobbie, or create a new Hobbie.
    """

    def get(self, request, format=None):
        listahobbie = ListadoHobbies.objects.all()
        serializer = ListadoHobbiesSerializer(listahobbie, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListadoHobbiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListadoHobbiesDetail(APIView):
    """
    Retrieve, update or delete a ListaHobbie instance.
    """

    def get_object(self, pk):
        try:
            return ListadoHobbies.objects.get(pk=pk)
        except ListadoHobbies.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        listaHobbie = self.get_object(pk)
        serializer = ListadoHobbiesSerializer(listaHobbie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        listaHobbie= self.get_object(pk)
        serializer = ListadoHobbiesSerializer(listaHobbie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        listaHobbie = self.get_object(pk)
        listaHobbie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class AmenidadList(APIView):
    """
    List all Amenidad, or create a new Amenidad.
    """

    def get(self, request, format=None):
        amenidad = Amenidad.objects.all()
        serializer = AmenidadSerializer(amenidad, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AmenidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AmenidadDetail(APIView):
    """
    Retrieve, update or delete a Amenidad instance.
    """

    def get_object(self, pk):
        try:
            return Amenidad.objects.get(pk=pk)
        except Amenidad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        amenidad = self.get_object(pk)
        serializer = AmenidadSerializer(amenidad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        amenidad = self.get_object(pk)
        serializer = AmenidadSerializer(amenidad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        amenidad = self.get_object(pk)
        amenidad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class ListaAmenidadList(APIView):
    """
    List all ListaAmenidad, or create a new ListaAmenidad.
    """

    def get(self, request, format=None):
        listaAmenidad = ListaAmenidad.objects.all()
        serializer = ListaAmenidadSerializer(listaAmenidad, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListaAmenidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListaAmenidadDetail(APIView):
    """
    Retrieve, update or delete a ListaAmenidad instance.
    """

    def get_object(self, pk):
        try:
            return ListaAmenidad.objects.get(pk=pk)
        except ListaAmenidad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        listaAmenidad = self.get_object(pk)
        serializer = ListaAmenidadSerializer(listaAmenidad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        listaAmenidad = self.get_object(pk)
        serializer = ListaAmenidadSerializer(listaAmenidad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        listaAmenidad = self.get_object(pk)
        listaAmenidad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# clase para authenticar desde vue
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data = request.data,
            context = {'request' : request}
        )
        serializer.is_valid()
        print(serializer.errors)
        if serializer.is_valid():
            user = serializer.validated_data["user"] 
            token,created = Token.objects.get_or_create(user = user)
            user_serializer = UserTokenSerializer(user)
            if created:
                print(request.user)
                return Response({
                    'token': token.key,
                    'user': user_serializer.data,
                    'message' : "Inicio de sesión exitoso"
                }, status = status.HTTP_201_CREATED)
            else:
                token.delete()
                token = Token.objects.create(user = user)
                return Response({
                    'token': token.key,
                    'user': user_serializer.data,
                    'message' : "Inicio de sesión exitoso"
                }, status = status.HTTP_201_CREATED)
        else:
            return Response({'error':'Nombre de usuario o contraseña incorrecto'},
                            status = status.HTTP_400_BAD_REQUEST)
#class para logout desde vue
class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        datos_registro = RegisterSerializer(
            data = request.data,
            context = {'request' : request}
        )
        if datos_registro.is_valid():
            resultado = datos_registro.create()
            if resultado.get("error","")!= "":
                return Response({'error':resultado["error"]},status = status.HTTP_400_BAD_REQUEST)
            if resultado["user"] and resultado["perfil"]:
                return Response({"mensaje":"se creo el usuario y su perfil"}, status = status.HTTP_200_OK)
        else :
            return Response({"error" : "Los datos que envio no son validos"},status = status.HTTP_400_BAD_REQUEST)

def error_404(request, exception):
   context = {}
   return render(request,'404.html', context)