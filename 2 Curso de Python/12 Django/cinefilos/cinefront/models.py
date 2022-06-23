from tkinter import CASCADE
from django.db import models

# Create your models here.

class Director(models.Model):
    nombre          = models.CharField(max_length=32)
    nacimiento      = models.DateField(auto_now=False, auto_now_add=False)
    nacionalidad    = models.CharField(max_length=64)
    biografia       = models.TextField()

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    nombre      = models.CharField(max_length=512)
    resumen     = models.TextField()
    director    = models.ForeignKey(Director, on_delete=models.CASCADE)
    duracion    = models.DurationField()
    lanzamiento = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nombre