from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/foto_<id>/<filename>
    return 'foto/{0}'.format(filename)
def perfil_directory_path(instance,filename):
    return 'perfil/{0}'.format(filename)

class Amenidad(models.Model):
    amenidad_id = models.AutoField(primary_key=True)
    nombre_amenidad = models.CharField(max_length=1024)

    class Meta:
        db_table = 'amenidad'
    
    def __str__(self) :
        return self.nombre_amenidad


class Cheros(models.Model):
    cheros_id = models.AutoField(primary_key=True)
    perfil_user = models.ForeignKey('PerfilUser', on_delete=models.CASCADE, related_name='perfil')
    favorito_user = models.ForeignKey('PerfilUser', on_delete=models.CASCADE, related_name='favorito')
    
    class Meta:
        db_table = 'cheros'
    
    def __str__(self) :
        return "{} es amigo de {}".format(self.perfil_user,self.favorito_user)


class Ciudad(models.Model):
    ciudad_id = models.AutoField(primary_key=True)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE, db_column='departamento_id')
    nombre_ciudad = models.CharField(max_length=100)

    class Meta:
        db_table = 'ciudad'
    
    def __str__(self) :
        return self.nombre_ciudad


class Departamento(models.Model):
    departamento_id = models.AutoField(primary_key=True)
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE, db_column='pais_id')
    nombre_depa = models.CharField(max_length=1024)

    class Meta:
        db_table = 'departamento'
    
    def __str__(self) :
        return self.nombre_depa


class Foto(models.Model):
    foto_id = models.AutoField(primary_key=True)
    foto_lugar = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    publi_alquiler = models.ForeignKey('PublicacionAlquiler', on_delete=models.CASCADE, db_column='publicacion_id', blank=True, null=True)
    foto64 = models.CharField(max_length=1000000, blank=True, null=True)

    class Meta:
        db_table = 'foto'

class HistorialBusqueda(models.Model):
    busqueda_id = models.AutoField(primary_key=True)
    perfil = models.ForeignKey('PerfilUser', on_delete=models.CASCADE, db_column='perfil_id')
    busqueda = models.CharField(max_length=1024)
    fecha_busqueda = models.DateTimeField()

    class Meta:
        db_table = 'historial_busqueda'

    def __str__(self) :
        return self.busqueda + " " + self.fecha_busqueda.__str__()

class Hobbie(models.Model):
    hobbie_id = models.AutoField(primary_key=True)
    nombre_hobbie = models.CharField(max_length=1024)

    class Meta:
        db_table = 'hobbie'

    def __str__(self) :
        return self.nombre_hobbie

class ListaAmenidad(models.Model):
    listamenidad_id = models.AutoField(primary_key=True)
    publicacion = models.ForeignKey('PublicacionAlquiler', on_delete=models.CASCADE, db_column='publicacion_id')
    amenidad = models.ForeignKey('Amenidad', on_delete=models.CASCADE, db_column='amenidad_id')

    class Meta:
        db_table = 'lista_amenidad'

    def __str__(self) :
        return self.amenidad.__str__()

class ListaPreferencia(models.Model):
    listapref_id = models.AutoField(primary_key=True)
    perfil = models.ForeignKey('PerfilUser', on_delete=models.CASCADE, db_column='perfil_id')
    preferencia = models.ForeignKey('Preferencia', on_delete=models.CASCADE, db_column='preferencia_id')

    class Meta:
        db_table = 'lista_preferencia'

    def __str__(self) :
        return self.perfil.__str__() + " " + self.preferencia.__str__()

class ListadoHobbies(models.Model):
    listhobbies_id = models.AutoField(primary_key=True)
    perfil = models.ForeignKey('PerfilUser', on_delete=models.CASCADE, db_column='perfil_id')
    hobbie = models.ForeignKey('Hobbie', on_delete=models.CASCADE, db_column='hobbie_id')

    class Meta:
        db_table = 'listadohobbies'

    def __str__(self) :
        return self.perfil.__str__() + " " + self.hobbie.__str__()

class Pais(models.Model):
    pais_id = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=1024)

    class Meta:
        db_table = 'pais'

    def __str__(self) :
        return self.nombre_pais
    
"""
class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombre_user,apellidos_user,password = None,genero='Masculino'):
        if not email:
            raise("Necesita un correo electronico para registrarse")
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombre_user = nombre_user,
            apellidos_user = apellidos_user,
            genero = genero
            )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,email,username,nombre_user,apellidos_user,password,genero='Masculino'):
        usuario = self.create_user(
            email,
            username,
            nombre_user,
            apellidos_user,
            genero,
            password
        )
        usuario.usuario_administrador = True
        usuario.admin = True
        usuario.staff = True
        usuario.save()
        return usuario

"""

class PerfilUser(models.Model):
    perfil_id = models.AutoField(primary_key=True)
    ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE, db_column='ciudad_id',blank= True, null=True)
    email = models.CharField(max_length=1024, unique= True)
    nombre_user = models.CharField(max_length=1024)
    apellidos_user = models.CharField(max_length=1024)
    edad = models.IntegerField(blank=True, null=True)
    biografia = models.CharField(max_length=1024, blank=True, null=True)
    telefono = models.CharField(max_length=1024, blank=True, null=True)
    username = models.CharField(max_length=1024,unique= True)
    user_facebook = models.CharField(max_length=1024, blank=True, null=True)
    user_insta = models.CharField(max_length=1024, blank=True, null=True)
    user_twitter = models.CharField(max_length=1024, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to=perfil_directory_path, blank = True, null = True)
    genero = models.CharField(max_length=1024)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    necesita_cuarto = models.BooleanField(default = False)    
    foto64 = models.CharField(max_length=1000000, blank=True, null=True, default="")

    #staff = models.BooleanField(default=False)
    #admin = models.BooleanField(default=False)
    #usuario_administrador = models.BooleanField(default=False)
    #objects = UsuarioManager()
    #USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['email','nombre_user','apellidos_user','genero']

    class Meta:
        db_table = 'perfil_user'
    
    def __str__(self):
        return self.nombre_user + " " + self.apellidos_user
    """
    #para los permisos de poder ver el admin
    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.usuario_administrador
    """
    



class Preferencia(models.Model):
    preferencia_id = models.AutoField(primary_key=True)
    nombre_preferencia = models.CharField(max_length=1024)

    class Meta:
        db_table = 'preferencia'

    def __str__(self) :
        return self.nombre_preferencia

class PublicacionAlquiler(models.Model):
    publicacion_id = models.AutoField(primary_key=True)
    perfil = models.ForeignKey('PerfilUser', on_delete=models.CASCADE, db_column='perfil_id')
    titulo = models.CharField(max_length=1024)
    descrip_lugar = models.CharField(max_length=1024)
    coordenadas = models.CharField(max_length=1024)
    num_ocupantes = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    tiempo_contrato = models.CharField(max_length=1024)
    fecha_publi = models.DateField()
    p_activa = models.BooleanField()

    class Meta:
        db_table = 'publicacion_alquiler'

    def __str__(self) :
        return self.titulo + " " + self.perfil.__str__()

class VentaAlquiler(models.Model):
    venta_id = models.AutoField(primary_key=True)
    perfil = models.ForeignKey('PerfilUser', on_delete=models.CASCADE, db_column='perfil_id')
    publicacion = models.ForeignKey('PublicacionAlquiler', on_delete=models.CASCADE, db_column='publicacion_id')
    fecha_venta = models.DateField()
    comision = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'venta_alquiler'

    def __str__(self) :
        return self.perfil.__str__() + " " + self.publicacion.__str__()
