# Generated by Django 4.0.6 on 2022-09-29 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppVet', '0015_datosmascota_imagenmascota_delete_mascota'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosmascota',
            name='imagenMascota',
        ),
        migrations.CreateModel(
            name='ImagenMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='mascotas')),
                ('mascota', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppVet.datosmascota')),
            ],
        ),
    ]