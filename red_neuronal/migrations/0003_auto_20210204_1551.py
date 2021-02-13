# Generated by Django 3.0.5 on 2021-02-04 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamiento', '0008_imagenes_som'),
        ('red_neuronal', '0002_auto_20210204_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='red_neuronal',
            name='id_data',
        ),
        migrations.AddField(
            model_name='red_neuronal',
            name='id_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entrenamiento.Data'),
        ),
        migrations.RemoveField(
            model_name='red_neuronal',
            name='id_som',
        ),
        migrations.AddField(
            model_name='red_neuronal',
            name='id_som',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entrenamiento.Entrenamiento_Som'),
        ),
    ]