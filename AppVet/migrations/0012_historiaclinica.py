# Generated by Django 4.0.6 on 2022-09-23 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppVet', '0011_alter_datosmascota_apellidopropietariomascota'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaConsulta', models.DateField()),
                ('sexoMascota', models.CharField(max_length=30)),
                ('pesoMascota', models.FloatField()),
                ('enfermedadPreviaMascota', models.CharField(max_length=250)),
                ('vacunasMascotas', models.CharField(max_length=100)),
                ('comidaMascota', models.CharField(max_length=100)),
                ('temperaturaMascota', models.FloatField()),
                ('motivoConsulta', models.CharField(max_length=250)),
                ('diagnosticoMascota', models.CharField(max_length=350)),
                ('nombreMascota', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppVet.datosmascota')),
                ('veterinarioMascota', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppVet.datosveterinarios')),
            ],
        ),
    ]