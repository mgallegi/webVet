# Generated by Django 4.0.6 on 2022-09-29 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVet', '0014_mascota'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosmascota',
            name='imagenMascota',
            field=models.ImageField(blank=True, null=True, upload_to='mascotas'),
        ),
        migrations.DeleteModel(
            name='Mascota',
        ),
    ]