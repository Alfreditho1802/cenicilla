from django import forms
from .models import *

canales_status=[
    (1,'L'),
    (2,'A'),
    (3,'B'),
    (4,'H'),
    (5,'S'),
    (6,'V')
]

class N_ref(forms.Form):#form para la imagen de referencia 
    nombre=forms.CharField(max_length=30,widget=forms.TextInput(attrs={
    'class': 'form-control ' , 'placeholder': 'Nombre'}))
    img_ref=forms.ImageField()
    #img_ref.widget.attrs.update({'class':'btn btn-primary'})

class Datos(forms.Form):
    nombre=forms.CharField(max_length=30,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Nombre Dataset'}))
    parte_infectada=forms.CharField(max_length=30,required=False,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Parte infectada'}))
    color=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Color'}))
    forma=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Forma'}))
    localizacion=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Localizacion'}))
    humedad=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Humedad'}))
    enfermedad=forms.CharField(max_length=30,required=False,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Enfermedad'}))
    patogeno=forms.CharField(max_length=30,required=False,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Patógeno'}))
    referencia=forms.ModelChoiceField(Referencia.objects.all(),widget=forms.Select(attrs={
    'class': 'form-control '}))

class N_img(forms.Form):#form para la imagen de referencia 
    nombre=forms.CharField(max_length=30,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Nombre'}))
    img_org=forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    Data=forms.ModelChoiceField(Data.objects.all(),widget=forms.Select(attrs={
    'class': 'form-control'}))

class Form_Entrenamiento(forms.Form):
    nombre=forms.CharField(max_length=30,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Nombre'}))
    descripcion=forms.CharField(max_length=30,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Descripcion'}))
    #Iteraciones=forms.IntegerField(max_value=10,min_value=1,widget=forms.TextInput(attrs={
    #'class': 'form-control ', 'placeholder': 'Numero de iteraciones'}))
    umbral_minimo=forms.IntegerField(min_value=1,max_value=100,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Umbral minimo'}))
    umbral_par_media=forms.IntegerField(min_value=1,max_value=100,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Umbral de media y mediana'}))
    umbral_fusion=forms.IntegerField(min_value=1,max_value=100,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Umbral de fusión'}))
    umbral_poda=forms.IntegerField(min_value=15,max_value=90,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Umbral de poda'}))
    umbral_neuronas=forms.IntegerField(min_value=3,max_value=13,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Numero de neuronas'}))
    canal1=forms.ChoiceField(choices=canales_status,widget=forms.Select(attrs={
    'class': 'form-control ', 'placeholder': 'Umbral de poda'}))
    canal2=forms.ChoiceField(choices=canales_status,widget=forms.Select(attrs={
    'class': 'form-control ', 'placeholder': 'Umbral de poda'}))
    canal3=forms.ChoiceField(choices=canales_status,widget=forms.Select(attrs={
    'class': 'form-control ', 'placeholder': 'Umbral de poda'}))
    canal4=forms.ChoiceField(choices=canales_status,widget=forms.Select(attrs={
    'class': 'form-control ', 'placeholder': 'Umbral de poda'}))
    datos=forms.ModelChoiceField(Data.objects.all(),widget=forms.Select(attrs={
    'class': 'form-control ', 'placeholder': 'Umbral de poda'}))
    
    