from django import forms
from entrenamiento.models import Entrenamiento_Som,Data
potencias=[
    (64,64),
    (32,32),
    (16,16)

]
class nueva_red(forms.Form):
    nombre=forms.CharField(max_length=40,widget=forms.TextInput(attrs={
    'class': 'form-control','placeholder':'Nombre'}))
    epoca=forms.IntegerField(min_value=0,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Epoca'}))
    pasos=forms.IntegerField(min_value=0,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Pasos'}))
    pasos_validacion=forms.IntegerField(min_value=0,widget=forms.TextInput(attrs={
    'class': 'form-control ', 'placeholder': 'Pasos de validacion'}))
    #potencias de dos
    batch_size=forms.ChoiceField(choices=potencias,widget=forms.Select(attrs={
    'class': 'form-control '}))
    f1=forms.ChoiceField(choices=potencias,widget=forms.Select(attrs={
    'class': 'form-control '}))
    f2=forms.ChoiceField(choices=potencias,widget=forms.Select(attrs={
    'class': 'form-control '}))
    #modelo a recibir 
    som=forms.ModelChoiceField(Entrenamiento_Som.objects.all(),empty_label=('Ninguno'),widget=forms.Select(attrs={
    'class': 'form-control '}),required=False)
    som1=forms.ModelChoiceField(Entrenamiento_Som.objects.all(),empty_label=('Ninguno'),widget=forms.Select(attrs={
    'class': 'form-control '}),required=False)
    data=forms.ModelChoiceField(Data.objects.all(),empty_label=('Ninguno'),widget=forms.Select(attrs={
    'class': 'form-control '}),required=False)
    data1=forms.ModelChoiceField(Data.objects.all(),empty_label=('Ninguno'),widget=forms.Select(attrs={
    'class': 'form-control '}),required=False)