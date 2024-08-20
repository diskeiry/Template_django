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


def __str__(self):
        return self.nombre

# Create your models here.



class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro']={}
        # else:
        self.carro = carro

    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
               "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad']=value['cantidad']+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session['carro']=self.carro
        self.session.modified=True

    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["precio"] = float(value["precio"]) - producto.precio
                value['cantidad']=value['cantidad']-1
                if value['cantidad']<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session['carro']={}
        self.session.modified=True

    def contar_productos(self):
        return sum(item['cantidad'] for item in self.carro.values())
                   