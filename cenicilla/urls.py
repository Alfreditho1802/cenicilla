"""cenicilla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import Login,logoutUser
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',include(('usuarios.urls','usuarios'))),
    path('entrenamiento/',include(('entrenamiento.urls','entrenamiento'))),
    path('archivos/',include(('archivos.urls','archivos'))),
    path('foro/',include(('foro.urls','foro'))),
    path('analisis/',include(('analisis.urls','analisis'))),
    path('red_neuronal/',include(('red_neuronal.urls','red_neuronal'))),
    #urls del sistema
    path('accounts/login/',Login.as_view(),name='login'),
    path('logout/',login_required(logoutUser),name='logout'),
    #path('accounts/',include('django.contrib.auth.urls'))template_name='registration/password_reset_form.html',
    path('reset_password/',views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete',views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('cambiar_pass',views.PasswordChangeView.as_view(),name='cambiar')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
