from django.db import models

# Create your models here.

class Aptitudes(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Habilidades(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    telefono = models.CharField(max_length=15) 
    correo = models.EmailField()
    
    def __str__(self):
        return self.telefono
    
class Referencias(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=15) 
    empresa = models.CharField(max_length=15) 
    telefono = models.CharField(max_length=15)

class Experiencias(models.Model):
    nombre_empresa_proyecto = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_empresa_proyecto
    
class Perfil(models.Model):
    nombre = models.CharField(max_length=100) 
    profesion = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.nombre

