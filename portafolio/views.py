from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Aptitudes, Habilidades, Contacto, Referencias, Experiencias, Perfil
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.decorators import login_required

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

# CRUD DE CONTACTOS

class ListContactoView(ListView):
    model = Contacto
    template_name = 'portafolio/contacto_info.html'
    context_object_name = 'contacto'

class DeleteContactView(DeleteView):
    model = Contacto
    success_url = reverse_lazy('Contacto')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class CreateContactView(CreateView):
    model = Contacto
    template_name = 'portafolio/crear_contacto.html'
    form_class = ContactoForm  
    success_url = reverse_lazy('Contacto')
    
class EditContactView(UpdateView):
    model = Contacto
    template_name = 'portafolio/editar_contacto.html'
    form_class = ContactoForm 
    success_url = reverse_lazy('Contacto')
    
# CRUD DE HABILIDADES

class ListHabilidadesView(ListView):
    model = Habilidades
    template_name = 'portafolio/habilidades.html'
    context_object_name = 'habilidades'
    
class DeleteHabilitiesView(DeleteView):
    model = Habilidades
    success_url = reverse_lazy('Habilidades')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class CreateHabilitiesView(CreateView):
    model = Habilidades
    template_name = 'portafolio/crear_habilidad.html'
    form_class = HabilidadForm  
    success_url = reverse_lazy('Habilidades')
    
class EditHabilitiesView(UpdateView):
    model = Habilidades
    template_name = 'portafolio/editar_habilidad.html'
    form_class = HabilidadForm 
    success_url = reverse_lazy('Habilidades')   
    

# CRUD DE REFERENCIAS 

class ListReferenciasView(ListView):
    model = Referencias
    template_name = 'portafolio/referencias.html'
    context_object_name = 'referencia'
    
class DeleteReferenceView(DeleteView):
    model = Referencias
    success_url = reverse_lazy('Referencias')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class CreateReferenceView(CreateView):
    model = Referencias
    template_name = 'portafolio/crear_referencia.html'
    form_class = ReferenciaForm  
    success_url = reverse_lazy('Referencias')
    
class EditReferenceView(UpdateView):
    model = Referencias
    template_name = 'portafolio/editar_referencia.html'
    form_class = ReferenciaForm 
    success_url = reverse_lazy('Referencias')   
       

# CRUD DE EXPERIENCIAS

class ListExperienciasView(ListView):
    model = Experiencias
    template_name = 'portafolio/experiencias.html'
    context_object_name = 'experiencia'
    
class DetailExperienciaView(DetailView):
    model = Experiencias
    template_name = 'portafolio/experiencia_detail.html'
    context_object_name = 'experiencia'
    
class DeleteExperienceView(DeleteView):
    model = Experiencias  
    success_url = reverse_lazy('Experiencias')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class CreateExperienceView(CreateView):
    model = Experiencias  
    template_name = 'portafolio/crear_experiencia.html'
    form_class = ExperienciaForm
    success_url = reverse_lazy('Experiencias')

class EditExperienceView(UpdateView):
    model = Experiencias  
    template_name = 'portafolio/editar_experiencia.html'
    form_class = ExperienciaForm
    success_url = reverse_lazy('Experiencias')

# CRUD DE APTITUDES

class ListAptitudesView(ListView):
    model = Aptitudes
    template_name = 'portafolio/aptitudes.html' 
    context_object_name = 'aptitudes'
    
class DeleteAptitudView(DeleteView):
    model = Aptitudes
    success_url = reverse_lazy('Aptitudes')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class CreateAptitudView(CreateView):
    model = Aptitudes
    template_name = 'portafolio/crear_aptitud.html'
    form_class = AptitudForm  
    success_url = reverse_lazy('Aptitudes')
    
class EditAptitudView(UpdateView):
    model = Aptitudes
    template_name = 'portafolio/editar_aptitud.html'
    form_class = AptitudForm 
    success_url = reverse_lazy('Aptitudes')