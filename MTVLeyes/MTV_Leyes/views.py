from django.shortcuts import render
from errno import EADDRNOTAVAIL
from urllib.request import DataHandler
from django.template import loader
from django.http import HttpResponse
from django.template import Template
from django.template import Context
import datetime
from .models import Familiar

# Create your views here.
def mtvleyes (request):
    nombre = "Giaccomo"
    apellido = "Pezzolo"
    nacimiento = datetime.date(1850,1, 13)
    parentesco = "Bisabuelo"
    edad = 172
    europeo = True
    email = "eltanogiacco@hotmail.com"

    instancia = Familiar( nombre = nombre, apellido = apellido, nacimiento= nacimiento,  parentesco = parentesco, edad = edad, europeo = europeo, email = email)
    instancia.save()
    #diccionario = {"nombre": nombre, "apellido":apellido, "nacimiento" : nacimiento, "parentesco": parentesco, "edad": edad, "europeo": europeo, "email": email}
    #plantilla = loader.get_template("template.html")
    #documento= plantilla.render(diccionario)
    familiares_list = Familiar.objects.all()
    return render (request, "template.html", {"mtvleyes" : familiares_list}) #HttpResponse(documento)

# Create your views here.
