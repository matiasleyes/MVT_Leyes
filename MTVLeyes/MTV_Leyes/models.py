import email
from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacimiento = models.DateTimeField()
    parentesco = models.CharField(max_length=40)
    edad = models.IntegerField()
    europeo = models.BooleanField()
    email = models.CharField(max_length=40)