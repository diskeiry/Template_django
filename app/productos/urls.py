from django.urls import path
from . import views

urlpatterns = [
    path('consulta/', views.renderizar_consulta, name='consulta'),
    path('entrada/', views.renderizar_entrada, name='entrada'),
    path('salida/', views.renderizar_salida, name='salida')
]


