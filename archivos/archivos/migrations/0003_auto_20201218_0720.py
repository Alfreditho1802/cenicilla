# Generated by Django 3.0.5 on 2020-12-18 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0002_auto_20201212_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivos_bases',
            name='subida',
            field=models.DateField(default=datetime.datetime(2020, 12, 18, 7, 20, 46, 633912)),
        ),
    ]
