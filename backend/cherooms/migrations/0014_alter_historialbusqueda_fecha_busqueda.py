# Generated by Django 4.1.3 on 2022-11-20 00:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cherooms', '0013_perfiluser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialbusqueda',
            name='fecha_busqueda',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 18, 40, 53, 413771)),
        ),
    ]