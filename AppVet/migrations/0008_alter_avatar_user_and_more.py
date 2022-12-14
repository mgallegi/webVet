# Generated by Django 4.0.6 on 2022-09-23 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppVet', '0007_alter_datosmascota_apellidopropietariomascota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='datosmascota',
            name='apellidoPropietarioMascota',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppVet.datospropietario'),
        ),
    ]
