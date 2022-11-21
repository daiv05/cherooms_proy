"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cherooms import views
from cherooms.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as views_token

#router = DefaultRouter()
#router.register(r'users', UserViewSet, basename='users')
app_name = "api"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    #---------------------------------------------------------------------------------
    # PERFIL
    path('perfil/', views.PerfilUserList.as_view(),name="perfil"),
    path('perfil/<int:pk>/', views.PerfilUserDetail.as_view()),
    #---------------------------------------------------------------------------------
    # DEPARTAMENTOS
    path('departamento/', views.DepartamentoList.as_view()),
    path('departamento/<int:pk>/', views.DepartamentoDetail.as_view()),
    #---------------------------------------------------------------------------------
    # HistorialBusqueda
    path('historial_busqueda', views.HistorialBusquedaList.as_view()),
    path('historial_busqueda/<int:pk>', views.HistorialBusquedaDetail.as_view()),
    #---------------------------------------------------------------------------------
    # PublicacionAlquiler
    path('publicacion_alquiler', views.PublicacionAlquilerList.as_view()),
    path('publicacion_alquiler/<int:pk>', views.PublicacionAlquilerDetail.as_view()),
    #---------------------------------------------------------------------------------
    # Foto
    path('foto', views.FotoList.as_view()),
    path('foto/<int:pk>', views.FotoDetail.as_view()),

    #login
    path('login/',Login.as_view(),name="login"),
    path('index/',index, name="index"),
    #path('',include(router.urls))
    path('api_generate_token/',views_token.obtain_auth_token),
    #lista de cheros por usuario
    path('chero_list/',views.CheroList.as_view(),name="chero-list"),
    path('logout/',views.Logout.as_view(),name="logout"),

]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)