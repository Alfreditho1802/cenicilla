# Generated by Django 3.0.5 on 2020-12-18 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0003_auto_20201218_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivos_bases',
            name='subida',
            field=models.DateField(default=datetime.datetime(2020, 12, 18, 7, 23, 13, 926812)),
        ),
    ]