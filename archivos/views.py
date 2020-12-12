from django.shortcuts import render,redirect
from .models import Archivos_Bases
from .forms import Nuevo_archivo
from django.contrib.auth.models import User
from django.views.generic import CreateView
# Create your views here.
class nuevo_archivo(CreateView):
    model=Archivos_Bases
    template_name='archivos/nuevo.html'
    form_class=Nuevo_archivo
    def post(self,request,*args,**kwargs):
        self.form_class=Nuevo_archivo(request.POST,request.FILES)
        if self.form_class.is_valid():
            Archivos=Archivos_Bases()
            Archivos.nombre_archivo=request.POST.get('nombre_archivo')
            Archivos.archivo=request.FILES.get('archivo')
            Archivos.descripcion=request.POST.get('descripcion')
            us=User.objects.get(username=request.user)
            Archivos.id_user=us
            Archivos.save()
            return redirect('usuarios:mostrar')
        else:
            return render(request,self.template_name,context={'form':self.form_class})

