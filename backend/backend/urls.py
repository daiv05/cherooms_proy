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

router = DefaultRouter()
#router.register(r'users', UserViewSet, basename='users')
app_name = "api"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # ---------------------------------------------------------------------------------
    # PERFIL
    path('perfil/', views.PerfilUserList.as_view(),name="perfil"),
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

    #---------------------------------------------------------------------------------
    # LISTADODEHOBBIES
    path('listadodehobbies/', views.ListadoHobbiesList.as_view()),
    path('listadodehobbies/<int:pk>/', views.ListadoHobbiesDetail.as_view()),
    #---------------------------------------------------------------------------------
    # AMENIDADES
    path('amenidades/', views.AmenidadList.as_view()),
    path('amenidades/<int:pk>/', views.AmenidadDetail.as_view()),    #---------------------------------------------------------------------------------
    # ListaAmenidad
    path('lista_amenidad/', views.ListaAmenidadList.as_view()),
    path('lista_amenidad/<int:pk>/', views.ListaAmenidadDetail.as_view()),
    #---------------------------------------------------------------------------------

    #login
    path('login/',Login.as_view(),name="login"),
    path('index/',index, name="index"),
    #path('',include(router.urls))
    path('api_generate_token/',views_token.obtain_auth_token),
    #lista de cheros por usuario
    path('chero_list/',views.CheroList.as_view(),name="chero-list"),
    path('logout/',views.Logout.as_view(),name="logout"),
    #paths para el login y authenticacion con vue y dajngo
    path('login-api/',views.CustomAuthToken.as_view()),
    #url para el registro de un usuario
    path('register/',views.UserRegisterView.as_view()),
    #url para vista usuario
    path('obtener_usuario/',views.VistaUsuarioLogueado.as_view()),


    #Para obtener el user asocido a un token
    path('user_token/',views.UserToken.as_view()),

    #Para obtener el user asocido a un token
    path('user_token_admin/',views.CustomObtainAuthToken.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns,False)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
