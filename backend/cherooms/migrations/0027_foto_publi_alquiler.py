# Generated by Django 4.1.3 on 2022-11-27 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cherooms', '0026_alter_ciudad_nombre_ciudad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='publi_alquiler',
            field=models.ForeignKey(blank=True, db_column='publicacion_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cherooms.publicacionalquiler'),
        ),
    ]
