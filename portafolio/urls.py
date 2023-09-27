from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.curriculum, name='curriculum'),
    path('habilidades/', ListHabilidadesView.as_view(), name='Habilidades'),
    path('aptitudes/', ListAptitudesView.as_view(), name='Aptitudes'),
    path('contacto-info/', ListContactoView.as_view(), name='Contacto'),
    path('referencias/', ListReferenciasView.as_view(), name='Referencias'),
    path('experiencias/', ListExperienciasView.as_view(), name='Experiencias'),
    path('experiencia-detail/<int:pk>/', DetailExperienciaView.as_view(), name='experiencia_detail'),
    path('aptitud/<int:pk>/delete/', DeleteAptitudView.as_view(), name='delete_aptitud'),
    path('crear_aptitud/', CreateAptitudView.as_view(), name='crear_aptitud'),
    path('aptitud/<int:pk>/editar/', EditAptitudView.as_view(), name='editar_aptitud'),
    path('contacto/<int:pk>/delete/', DeleteContactView.as_view(), name='delete_contacto'),
    path('crear_contacto/', CreateContactView.as_view(), name='crear_contacto'),
    path('contacto/<int:pk>/editar/', EditContactView.as_view(), name='editar_contacto'),
    path('crear_habilidad/', CreateHabilitiesView.as_view(), name='crear_habilidad'),
    path('habilidad/<int:pk>/delete/', DeleteHabilitiesView.as_view(), name='delete_habilidad'),
    path('habilidad/<int:pk>/editar/', EditHabilitiesView.as_view(), name='editar_habilidad'),
    path('crear_referencia/', CreateReferenceView.as_view(), name='crear_referencia'),
    path('referencia/<int:pk>/delete/', DeleteReferenceView.as_view(), name='delete_referencia'),
    path('referencia/<int:pk>/editar/', EditReferenceView.as_view(), name='editar_referencia'),
    path('create_experience/', CreateExperienceView.as_view(), name='create_experience'),
    path('experience/<int:pk>/delete/', DeleteExperienceView.as_view(), name='delete_experience'),
    path('experience/<int:pk>/edit/', EditExperienceView.as_view(), name='edit_experience'),
]