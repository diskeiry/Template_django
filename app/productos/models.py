from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.URLField(blank=True, null=True)

class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class pedido(models.Model):
    ESTADO_PEDIDO = [
        ('P', 'Pendiente'),
        ('C', 'Enviado'),
        ('R', 'Entregado'),
    ]

    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1,choices=ESTADO_PEDIDO,default='P')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    Productos = models.ManyToManyField(Producto, through='PedidoProducto')

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()




# Create your models here.
