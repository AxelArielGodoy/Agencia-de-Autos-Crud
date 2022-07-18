from django.db import models

# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    modelo = models.IntegerField()


class Blog(models.Model):
    titulo= models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    contenido = models.TextField(max_length=100)
    fecha_creacion =models.DateField(null=True)
    # imagen = models.ImageField(upload_to='autos', null=True, blank=True)
    imagen = models.ImageField(null=True)
    
    def __str__(self):
        return self.titulo