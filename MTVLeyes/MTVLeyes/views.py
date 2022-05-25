from errno import EADDRNOTAVAIL
from urllib.request import DataHandler
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.template import Template
from django.template import Context
import datetime
from MTV_Leyes.models import Familiar

# Create your views here.
def mtvleyes (self):
    nombre = "Giaccomo"
    apellido = "Pezzolo"
    nacimiento = datetime.date(1850,1, 13)
    parentesco = "Bisabuelo"
    edad = 172
    europeo = True
    email = "eltanogiacco@hotmail.com"

    instancia = Familiar( nombre = nombre, apellido = apellido, nacimiento= nacimiento,  parentesco = parentesco, edad = edad, europeo = europeo, email = email)
    instancia.save()
    diccionario = {"nombre": nombre, "apellido":apellido, "nacimiento" : nacimiento, "parentesco": parentesco, "edad": edad, "europeo": europeo, "email": email}
    plantilla = loader.get_template("template.html")
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)
