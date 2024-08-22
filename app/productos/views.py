from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from . import usuarios
from .forms import ProductoForm
from .models import Producto
from django.shortcuts import redirect
from .models import Carro
# from models import cliente 
# from .forms import ClienteForm




lista = usuarios.usuarios
# lista = ['Limon', 'Cereza', 'Tamarindo', 'Fresa', 'Coco',]

def renderizar_consulta(request):
    return render(request, 'productos/consulta.productos.html',{'lista':lista})

def renderizar_entrada(request):
    return render(request, 'productos/entrada.productos.html')

def renderizar_salida(request):
    return render(request, 'productos/salida.productos.html')

def renderizar_home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})
  

def exito(request):
    return render(request, 'productos/exito.html')


def renderizar_create(request):
    mensaje = ''
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mensaje = 'Datos gardados correctamente'
        else:
            mensaje = 'Error al guardar los datos' + str(form.errors)
    else:
        form = ProductoForm()
    return render(request, 'productos/entrada.productos.html', {'mensaje':mensaje})



def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/consulta.productos.html', {'productos': productos})

def ver_carrito(request):
    carro = Carro(request)
    return render(request, 'productos/ver_carrito.html', {'carro': carro})


def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carro = Carro(request)
    carro.agregar(producto)
    return redirect('ver_carrito')

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carro = Carro(request)
    carro.eliminar(producto)
    return redirect('ver_carrito')

def restar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carro = Carro(request)
    carro.restar_producto(producto)
    return redirect('ver_carrito')

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('ver_carrito')

def carrito_total(request):
    carro = Carro(request)
    return {'carrito_total': carro.contar_productos()}


# def lista_clientes(request):
#     clientes = cliente.objects.all()
#     return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

# def detalle_cliente(request, pk):
#     cliente = get_object_or_404(cliente, pk=pk)
#     return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente})

# def crear_cliente(request):
#     if request.method == 'POST':
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_clientes')
#     else:
#         form = ClienteForm()
#     return render(request, 'clientes/formulario_cliente.html', {'form': form})

# def editar_cliente(request, pk):
#     cliente = get_object_or_404(cliente, pk=pk)
#     if request.method == 'POST':
#         form = ClienteForm(request.POST, instance=cliente)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_clientes')
#     else:
#         form = ClienteForm(instance=cliente)
#     return render(request, 'clientes/formulario_cliente.html', {'form': form})

# def eliminar_cliente(request, pk):
#     cliente = get_object_or_404(cliente, pk=pk)
#     if request.method == 'POST':
#         cliente.delete()
#         return redirect('lista_clientes')
#     return render(request, 'clientes/confirmar_eliminacion.html', {'cliente': cliente})