from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

Lista=[(0,'Técnico'),(1,'Administrador'),]

class registrar(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'is_superuser'
        ]
        labels={
            'username':'Correo',
            'first_name':'Nombres',
            'last_name':'Apellidos',
            'is_superuser':'admin'

        }
class Nuevo_usuario(forms.Form):
    Nombres=forms.CharField(label='Nombres',widget=forms.TextInput(attrs={
    'class': 'form-control', 'placeholder': 'Nombre'}))
    Apellidos=forms.CharField(label='Apellidos',widget=forms.TextInput(attrs={
    'class': 'form-control', 'placeholder': 'Apellidos'}))
    Tipo=forms.ChoiceField(choices=Lista,label='Tipo de Usuario',
    widget=forms.Select(attrs={'class': 'form-control'}))
    Correo=forms.EmailField(widget=forms.TextInput(attrs={
    'class': 'form-control', 'placeholder': 'Correo'}))
    Password=forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-control', 'placeholder': 'Password'}),label='Contraseña')
    Validar_pass=forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-control', 'placeholder': 'Password'}),label='Validar Contraseña')

class Editar_usuario(forms.Form):
    first_name=forms.CharField(label='Nombres',widget=forms.TextInput(attrs={
    'class': 'form-control', 'placeholder': 'Nombre'}))
    last_name=forms.CharField(label='Apellidos',widget=forms.TextInput(attrs={
    'class': 'form-control', 'placeholder': 'Apellidos'}))
    is_superuser=forms.ChoiceField(choices=Lista,label='Tipo de Usuario',
    widget=forms.Select(attrs={'class': 'form-control'}))
    username=forms.CharField(label='Correo',widget=forms.TextInput(attrs={
    'class': 'form-control', 'placeholder': 'Correo'}))

class Login_user(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(Login_user,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control mx-sm-3'
        self.fields['username'].widget.attrs['placeholder']='Correo Electronico'
        self.fields['password'].widget.attrs['class']='form-control mx-sm-3'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'
