# Generated by Django 4.1.3 on 2022-11-20 00:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cherooms', '0021_remove_perfiluser_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialbusqueda',
            name='fecha_busqueda',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 18, 59, 1, 736253)),
        ),
    ]
