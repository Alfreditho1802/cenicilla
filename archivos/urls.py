from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('nuevo/',login_required(nuevo_archivo.as_view()),name='nuevo_archivo'),
]