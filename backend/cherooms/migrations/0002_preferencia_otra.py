# Generated by Django 4.0.5 on 2022-11-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cherooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferencia',
            name='otra',
            field=models.CharField(default='null', max_length=1024),
            preserve_default=False,
        ),
    ]
