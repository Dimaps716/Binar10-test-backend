from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    Nombre = models.CharField(max_length=15, null=True)
    Apellido =models.CharField(max_length=10, null=True)
    Email = models.CharField(max_length=50, unique=True, null=True)
    Cedula = models.IntegerField( null=True)
    Img = models.ImageField()
    Pais = models.CharField(max_length=50)
    Entidad_de_salud = models.CharField(max_length=80)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


    class Meta:
        ordering = ['-created']

    def _str_(self):
        return self .Nombre

