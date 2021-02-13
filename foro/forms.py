from django import forms
from .models import *

class Form_Foro(forms.Form):
    nombre=forms.CharField(max_length=30,widget=forms.TextInput(attrs={
    'class': 'form-control'}))

class Form_Mensaje(forms.Form):
    mensaje=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    'class': 'form-control','placeholder': 'Mensaje nuevo'}))