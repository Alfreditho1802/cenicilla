# Generated by Django 3.0.5 on 2020-11-11 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Foro',
            fields=[
                ('id_Foro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('id_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Foro',
                'verbose_name_plural': 'Foros',
                'ordering': ['id_Foro'],
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id_mensaje', models.AutoField(primary_key=True, serialize=False)),
                ('mensaje', models.CharField(max_length=30)),
                ('id_Foro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foro.Foro')),
                ('id_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'mensaje',
                'verbose_name_plural': 'mensajes',
                'ordering': ['id_mensaje'],
            },
        ),
    ]