from django import forms
from .models import Producto
# from .models import cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4,'cols': 40}),
            'precio': forms.NumberInput(attrs={'step': '0:01'}),
            'stock': forms.NumberInput(attrs={'min': '0'}),
            'imagen': forms.URLInput(attrs={'placeholder': 'URL de la imagen (opcional)'}),
        }

# class ClienteForm(forms.ModelForm):
#     class Meta:
#         model = cliente
#         fields = ['nombre', 'email', 'direccion', 'telefono', 'fecha_creacion']
#         widgets = {
#             'direccion': forms.Textarea(attrs={'rows': 4,'cols': 40}),
#             'telefono': forms.NumberInput(attrs={'min': '0'}),
#         }