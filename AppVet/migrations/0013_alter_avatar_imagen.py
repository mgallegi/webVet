# Generated by Django 4.0.6 on 2022-09-28 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVet', '0012_historiaclinica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
