# Generated by Django 4.0.6 on 2022-09-28 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppVet', '0013_alter_avatar_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenMascota', models.ImageField(blank=True, null=True, upload_to='mascotas')),
                ('mascota', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppVet.datosmascota')),
            ],
        ),
    ]
