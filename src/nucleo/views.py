from django.http import     HttpResponse
from django.shortcuts import render
# Create your views here.


def saludar (request):
    return HttpResponse('Hola desde Django!')
def saludar_etiqueta(request):
    return HttpResponse('<h1> hola desde la app</h1>')