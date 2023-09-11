from django.urls import path
from . import views
from .views import ListAptitudesView, ListHabilidadesView, ListContactoView, ListReferenciasView, ListExperienciasView, DetailExperienciaView

urlpatterns = [
    path('', views.curriculum, name='curriculum'),
    path('habilidades/', ListHabilidadesView.as_view(), name='Habilidades'),
    path('aptitudes/', ListAptitudesView.as_view(), name='Aptitudes'),
    path('contacto-info/', ListContactoView.as_view(), name='Contacto'),
    path('referencias/', ListReferenciasView.as_view(), name='Referencias'),
    path('experiencias/', ListExperienciasView.as_view(), name='Experiencias'),
    path('experiencia-detail/<int:pk>/', DetailExperienciaView.as_view(), name='experiencia_detail'),
]