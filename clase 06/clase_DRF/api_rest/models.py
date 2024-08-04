from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre      = models.CharField(max_length=30)
    apellidos   = models.CharField(max_length=50)
    curso       = models.CharField(max_length=50)
    correo      = models.CharField(max_length=200)
    descripcion = models.TextField()
    
    def __str__(self) -> str:
        return self.nombre + ', ' + self.apellidos + ' desc:. ' + self.descripcion