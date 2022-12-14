# Generated by Django 4.1.3 on 2022-11-20 01:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cherooms', '0023_alter_historialbusqueda_fecha_busqueda'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfiluser',
            old_name='is_superuser',
            new_name='admin',
        ),
        migrations.AddField(
            model_name='perfiluser',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historialbusqueda',
            name='fecha_busqueda',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 19, 2, 30, 375959)),
        ),
    ]
