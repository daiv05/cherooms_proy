# Generated by Django 4.1.3 on 2022-11-19 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cherooms', '0005_remove_perfiluser_passwrd_perfiluser_last_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialbusqueda',
            name='fecha_busqueda',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 16, 31, 42, 741106)),
        ),
    ]