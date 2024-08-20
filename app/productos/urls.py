from django.contrib import admin
from django.urls import path
from . import views 



urlpatterns = [
    path('consulta/', views.listar_productos, name='consulta'),
    path('entrada/', views.renderizar_entrada, name='entrada'),
    path('salida/', views.renderizar_salida, name='salida'),
    path('crear/', views.renderizar_create, name='crear'),
    path('exito/', views.exito, name='exito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('limpiar/', views.limpiar_carro, name='limpiar_carro'),
    

]