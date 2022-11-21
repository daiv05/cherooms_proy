from django.shortcuts import render
from django.contrib.auth.models import User #es el modelo para realizar la autenticación 
from .models import *
from .serializers import *
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.http import *
from decimal import Decimal

#para el login
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

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
class PerfilUserList(APIView):
    """
    List all PerfilUser, or create a new PerfilUser.
    """

    def get(self, request, format=None):
        perfil = PerfilUser.objects.all()
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

# AMBAS CLASES CON TODOS ESOS METODOS POR CADA MODELO
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
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

# -------------------------------------------------------------------------------------
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

# -------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class PublicacionAlquilerList(APIView):
    """
    List all PublicacionAlquiler, or create a new PublicacionAlquiler.
    """

    def get(self, request, format=None):
        publicacionalquiler = PublicacionAlquiler.objects.all()
        serializer = PublicacionAlquilerSerializer(publicacionalquiler, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
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
        serializer = HistorialBusquedaSerializer(publicacionalquiler)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        publicacionalquiler = self.get_object(pk)
        serializer = HistorialBusquedaSerializer(publicacionalquiler, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        publicacionalquiler = self.get_object(pk)
        publicacionalquiler.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       

# -------------------------------------------------------------------------------------
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
        serializer = FotoSerializer(foto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        foto = self.get_object(pk)
        foto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CheroList(APIView):
    #permission_classes = (IsAuthenticated,)   
    #authentication_classes = (TokenAuthentication,)
    authentication_classes = [SessionAuthentication, BasicAuthentication]
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
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
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
