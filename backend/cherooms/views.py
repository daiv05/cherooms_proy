from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from decimal import Decimal

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

# -------------------------------------------------------------------------------------
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

# -------------------------------------------------------------------------------------
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
# ----------------------------VentaAlquiler & Hobbie-----------------------------------------------------
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
# ---------------------------------------------------------------------------------

class ListaFotosList(APIView):
    """
    List all ListaFotos, or create a new ListaFotos.
    """

    def get(self, request, format=None):
        listaFotos = ListaFotos.objects.all()
        serializer = ListaFotosSerializer(listaFotos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListaFotosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListaFotosDetail(APIView):
    """
    Retrieve, update or delete a ListaFotos instance.
    """

    def get_object(self, pk):
        try:
            return ListaFotos.objects.get(pk=pk)
        except ListaFotos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        listaFotos = self.get_object(pk)
        serializer = ListaFotosSerializer(listaFotos)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        listaFotos = self.get_object(pk)
        serializer = ListaFotosSerializer(listaFotos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        listaFotos = self.get_object(pk)
        listaFotos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
