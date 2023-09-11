from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Aptitudes, Habilidades, Contacto, Referencias, Experiencias, Perfil

# Create your views here.

def curriculum(request):
    
    aptitudes = Aptitudes.objects.all()
    habilidades = Habilidades.objects.all()
    contacto = Contacto.objects.all()
    referencia = Referencias.objects.all()
    experiencia = Experiencias.objects.all()
    perfil = Perfil.objects.all()
    
    context = {
        'aptitudes': aptitudes,
        'habilidades': habilidades,
        'contacto': contacto,
        'referencia': referencia,
        'experiencia': experiencia,
        'perfil': perfil,
    }
    
    return render(request, 'portafolio/curriculum.html', context)

# Vistas basadas en clases de los modelos para Listar

class ListContactoView(ListView):
    model = Contacto
    template_name = 'portafolio/contacto_info.html'
    context_object_name = 'contacto'

class ListAptitudesView(ListView):
    model = Aptitudes
    template_name = 'portafolio/aptitudes.html' 
    context_object_name = 'aptitudes' 
    
class ListHabilidadesView(ListView):
    model = Habilidades
    template_name = 'portafolio/habilidades.html'
    context_object_name = 'habilidades'
    
class ListReferenciasView(ListView):
    model = Referencias
    template_name = 'portafolio/referencias.html'
    context_object_name = 'referencia'
    
class ListExperienciasView(ListView):
    model = Experiencias
    template_name = 'portafolio/experiencias.html'
    context_object_name = 'experiencia'
    
class DetailExperienciaView(DetailView):
    model = Experiencias
    template_name = 'portafolio/experiencia_detail.html'
    context_object_name = 'experiencia'
    
    #def get_object(self, queryset=None):
        #return Experiencia.objects.get(pk=self.kwargs['pk'])