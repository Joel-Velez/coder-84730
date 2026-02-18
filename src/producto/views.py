from django.shortcuts import render
from . import models

# Create your views here.
def producto_list(request):
    productos = models.Categoria.objects.all()
    return render(request, 'producto/producto_list.html', {'productos': productos})