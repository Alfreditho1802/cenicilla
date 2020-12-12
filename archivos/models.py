from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
"""
Construccion del modelos para subir archivos por parte de los técnicos 
"""
class Archivos_Bases(models.Model):
    id_Archivo=models.AutoField(primary_key=True)
    nombre_archivo=models.CharField(max_length=30,blank=False,null=False)
    archivo=models.FileField(upload_to='archivos',null=True,blank=True)
    descripcion=models.CharField(max_length=100,blank=False,null=False)
    subida=models.DateField(default=datetime.now())
    id_user=models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_archivo

    class Meta:
        ordering=['id_Archivo']
        verbose_name='Archivo'
        verbose_name_plural='Archivos'