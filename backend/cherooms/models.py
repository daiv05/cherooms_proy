from datetime import datetime
from django.db import models

def publicacion_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/foto_<id>/<filename>
    return 'foto_{0}/{1}'.format(instance.foto_id, filename)

def usuario_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/foto_<id>/<filename>
    return 'perfil_{0}/{1}'.format(instance.perfil_id, filename)

class Amenidad(models.Model):
    amenidad_id = models.AutoField(primary_key=True)
    nombre_amenidad = models.CharField(max_length=1024)

    class Meta:
        db_table = 'amenidad'


class Cheros(models.Model):
    cheros_id = models.AutoField(primary_key=True)
    perfil_user = models.ForeignKey('PerfilUser', models.DO_NOTHING, related_name='perfil')
    favorito_user = models.ForeignKey('PerfilUser', models.DO_NOTHING, related_name='favorito')

    class Meta:
        db_table = 'cheros'


class Ciudad(models.Model):
    ciudad_id = models.AutoField(primary_key=True)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento_id')
    nombre_ciudad = models.CharField(max_length=1024)

    class Meta:
        db_table = 'ciudad'


class Departamento(models.Model):
    departamento_id = models.AutoField(primary_key=True)
    pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais_id')
    nombre_depa = models.CharField(max_length=1024)

    class Meta:
        db_table = 'departamento'


class Foto(models.Model):
    foto_id = models.AutoField(primary_key=True)
    foto_lugar = models.ImageField(upload_to=publicacion_directory_path, blank=True, null=True)

    class Meta:
        db_table = 'foto'


class HistorialBusqueda(models.Model):
    busqueda_id = models.AutoField(primary_key=True)
    perfil = models.ForeignKey('PerfilUser', models.DO_NOTHING, db_column='perfil_id')
    busqueda = models.CharField(max_length=1024)
    fecha_busqueda = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'historial_busqueda'


class Hobbie(models.Model):
    hobbie_id = models.AutoField(primary_key=True)
    nombre_hobbie = models.CharField(max_length=1024)

    class Meta:
        db_table = 'hobbie'


class ListaAmenidad(models.Model):
    listamenidad_id = models.AutoField(primary_key=True)
    publicacion = models.ForeignKey('PublicacionAlquiler', models.DO_NOTHING, db_column='publicacion_id')
    amenidad = models.ForeignKey('Amenidad', models.DO_NOTHING, db_column='amenidad_id')

    class Meta:
        db_table = 'lista_amenidad'


class ListaFotos(models.Model):
    listafoto_id = models.AutoField(primary_key=True)
    publicacion = models.ForeignKey('PublicacionAlquiler', models.DO_NOTHING, db_column='publicacion_id')
    foto = models.ForeignKey('Foto', models.DO_NOTHING, db_column='foto_id')

    class Meta:
        db_table = 'lista_fotos'


class ListaPreferencia(models.Model):
    listapref_id = models.AutoField(primary_key=True)
    perfil = models.ForeignKey('PerfilUser', models.DO_NOTHING, db_column='perfil_id')
    preferencia = models.ForeignKey('Preferencia', models.DO_NOTHING, db_column='preferencia_id')

    class Meta:
        db_table = 'lista_preferencia'


class Listadohobbies(models.Model):
    listhobbies_id = models.AutoField(primary_key=True)
    perfil = models.ForeignKey('PerfilUser', models.DO_NOTHING, db_column='perfil_id')
    hobbie = models.ForeignKey('Hobbie', models.DO_NOTHING, db_column='hobbie_id')

    class Meta:
        db_table = 'listadohobbies'


class Pais(models.Model):
    pais_id = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=1024)

    class Meta:
        db_table = 'pais'


class PerfilUser(models.Model):
    perfil_id = models.AutoField(primary_key=True)
    ciudad = models.ForeignKey('Ciudad', models.DO_NOTHING, db_column='ciudad_id')
    email = models.CharField(max_length=1024)
    passwrd = models.CharField(max_length=1024)
    nombre_user = models.CharField(max_length=1024)
    apellidos_user = models.CharField(max_length=1024)
    edad = models.IntegerField(blank=True, null=True)
    biografia = models.CharField(max_length=1024, blank=True, null=True)
    telefono = models.CharField(max_length=1024, blank=True, null=True)
    username = models.CharField(max_length=1024)
    user_facebook = models.CharField(max_length=1024, blank=True, null=True)
    user_insta = models.CharField(max_length=1024, blank=True, null=True)
    user_twitter = models.CharField(max_length=1024, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to=usuario_directory_path, blank=True, null=True)
    genero = models.CharField(max_length=1024)

    class Meta:
        db_table = 'perfil_user'
    
    def __str__(self):
        return self.nombre_user


class Preferencia(models.Model):
    preferencia_id = models.AutoField(primary_key=True)
    nombre_preferencia = models.CharField(max_length=1024)

    class Meta:
        db_table = 'preferencia'


class PublicacionAlquiler(models.Model):
    publicacion_id = models.AutoField(primary_key=True)
    perfil = models.ForeignKey('PerfilUser', models.DO_NOTHING, db_column='perfil_id')
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


class VentaAlquiler(models.Model):
    venta_id = models.AutoField(primary_key=True)
    perfil = models.ForeignKey('PerfilUser', models.DO_NOTHING, db_column='perfil_id')
    publicacion = models.ForeignKey('PublicacionAlquiler', models.DO_NOTHING, db_column='publicacion_id')
    fecha_venta = models.DateField()
    comision = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'venta_alquiler'

