from django.contrib import admin
from django.urls import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cherooms import views
from cherooms.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # ---------------------------------------------------------------------------------
    # PERFIL
    path('perfil/', views.PerfilUserList.as_view()),
    path('perfil/<int:pk>/', views.PerfilUserDetail.as_view()),
    # ---------------------------------------------------------------------------------
    # DEPARTAMENTOS
    path('departamento/', views.DepartamentoList.as_view()),
    path('departamento/<int:pk>/', views.DepartamentoDetail.as_view()),
    # ---------------------------------------------------------------------------------
    # HistorialBusqueda
    path('historial_busqueda/', views.HistorialBusquedaList.as_view()),
    path('historial_busqueda/<int:pk>/',
         views.HistorialBusquedaDetail.as_view()),
    # ---------------------------------------------------------------------------------
    # PublicacionAlquiler
    path('publicacion_alquiler/', views.PublicacionAlquilerList.as_view()),
    path('publicacion_alquiler/<int:pk>/',
         views.PublicacionAlquilerDetail.as_view()),
    # ---------------------------------------------------------------------------------
    # Foto
    path('foto/', views.FotoList.as_view()),
    path('foto/<int:pk>/', views.FotoDetail.as_view()),
    # ---------------------------------------------------------------------------------
    # PAIS
    path('pais/', views.PaisList.as_view()),
    path('pais/<int:pk>/', views.PaisDetail.as_view()),
    # ---------------------------------------------------------------------------------
    # PREFERENCIA
    path('preferencia/', views.PreferenciaList.as_view()),
    # ---------------------------------------------------------------------------------
    path('preferencia/<int:pk>/', views.PreferenciaDetail.as_view()),
    # VENTAALQUILER
    path('venta_alquiler/', views.VentaAlquilerList.as_view()),
    path('venta_alquiler/<int:pk>/', views.VentaAlquilerDetail.as_view()),
    # ---------------------------------------------------------------------------------
    # HOBBIE
    path('hobbie/', views.HobbieList.as_view()),
    path('hobbie/<int:pk>/', views.HobbieDetail.as_view()),
    # ---------------------------------------------------------------------------------
    # CIUDAD
    path('ciudad/', views.CiudadList.as_view()),
    path('ciudad/<int:pk>/', views.CiudadDetail.as_view()),
    # ---------------------------------------------------------------------------------
    # ListaPreferencia
    path('lista_preferencia/', views.ListaPreferenciaList.as_view()),
    path('lista_preferecia/<int:pk>/', views.ListaPreferenciaDetail.as_view()),
    # ---------------------------------------------------------------------------------


]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
