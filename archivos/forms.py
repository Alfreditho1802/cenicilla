from django import forms
from .models import *

class Nuevo_archivo(forms.Form):
    nombre_archivo=forms.CharField(max_length=30,widget=forms.TextInput(attrs={
    'class': 'form-control'}))
    archivo=forms.FileField()
    descripcion=forms.CharField(max_length=30,widget=forms.TextInput(attrs={
    'class': 'form-control'}))
