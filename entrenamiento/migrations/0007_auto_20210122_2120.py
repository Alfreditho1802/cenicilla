# Generated by Django 3.0.5 on 2021-01-23 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamiento', '0006_auto_20210119_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrenamiento_som',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='entrenamiento_som',
            name='pesos',
        ),
        migrations.AddField(
            model_name='data',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='enfermedad',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='forma',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='humedad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='localizacion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='parte_infectada',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='patogeno',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
