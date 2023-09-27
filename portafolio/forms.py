from django import forms
from .models import *

class AptitudForm(forms.ModelForm):
    class Meta:
        model = Aptitudes
        fields = ['nombre']

class ContactoForm(forms.ModelForm):
    class Meta: 
        model = Contacto
        fields = ['telefono', 'correo']
        
class HabilidadForm(forms.ModelForm):
    class Meta: 
        model = Habilidades
        fields = ['nombre']

class ReferenciaForm(forms.ModelForm):
    class Meta: 
        model = Referencias
        fields = ['nombre', 'puesto', 'empresa', 'telefono']
        
class ExperienciaForm(forms.ModelForm):
    class Meta: 
        model = Experiencias
        fields = ['nombre_empresa_proyecto', 'fecha_inicio', 'fecha_fin', 'descripcion']