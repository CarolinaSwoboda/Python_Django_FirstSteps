from django.shortcuts import render
from django.http import HttpResponse
from App_Coder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre = "Pyhton", camada = "11112")
    curso.save()
    documento = f"El curso es: {curso.nombre} y la camada es: {curso.camada}"
    return HttpResponse(documento)
