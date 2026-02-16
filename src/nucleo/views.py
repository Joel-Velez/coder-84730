from django.http import     HttpResponse
from django.shortcuts import render
# Create your views here.


def saludar (request):
    return HttpResponse('Hola desde Django!')
def saludar_etiqueta(request):

    return HttpResponse('<h1> hola desde la app</h1>')

def index(request):
    return render(request, 'nucleo/index.html', {'titulo': 'Proyecto : django'})

def tirar_dado(request):
    from datetime import datetime
    from random import randint  
    
    tiro_de_dado = randint(1,6)

    if tiro_de_dado == 6:
        mensaje = f'has tirado {tiro_de_dado} y has ganado'
    else:
        mensaje = f'has tirado {tiro_de_dado} y has perdido'
    datos = {
        'titulo': 'Tirar dado',
        'mensaje': mensaje,
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return render(request, 'nucleo/dado.html', datos)