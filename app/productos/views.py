from django.shortcuts import render
from django.http import request
# Create your views here.
def renderizar_consulta(request):
    return render(request, 'productos/consulta.productos.html')

def renderizar_entrada(request):
    return render(request, 'productos/entrada.productos.html')

def renderizar_salida(request):
    return render(request, 'productos/salida.productos.html')

def renderizar_home(request):
    return render(request, 'home.html')