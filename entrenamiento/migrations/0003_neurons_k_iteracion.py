# Generated by Django 3.0.5 on 2020-12-21 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamiento', '0002_neurons_id_entrenamiento_som'),
    ]

    operations = [
        migrations.AddField(
            model_name='neurons',
            name='k_iteracion',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
