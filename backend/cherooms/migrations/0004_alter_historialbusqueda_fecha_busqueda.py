# Generated by Django 4.1.3 on 2022-11-19 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cherooms', '0003_alter_foto_foto_lugar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialbusqueda',
            name='fecha_busqueda',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 12, 54, 31, 302189)),
        ),
    ]