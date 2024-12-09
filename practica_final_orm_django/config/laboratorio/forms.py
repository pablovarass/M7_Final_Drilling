from django import forms

from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']
        labels = {
            'nombre': 'Nombre del laboratorio',
            'ciudad': 'Ciudad del laboratorio',
            'pais': 'Pais del laboratorio'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','required': True}),
            'ciudad': forms.TextInput(attrs={'class':'form-control','required': True}),
            'pais': forms.TextInput(attrs={'class':'form-control','required': True})
            }
        
class DirectorGeneralForm(forms.ModelForm):
    class Meta:
        model = DirectorGeneral
        fields = ['nombre', 'especialidad', 'laboratorio']
        labels = {
            'nombre': 'Nombre del director general',
            'especialidad': 'Especialidad del director general',
            'laboratorio': 'Laboratorio del director general'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','required': True}),
            'especialidad': forms.TextInput(attrs={'class':'form-control','required': True}),
            'laboratorio': forms.Select(attrs={'class':'form-control','required': True})
            }        

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'laboratorio', 'fecha_fabricacion', 'precio_costo', 'precio_venta']
        labels = {
            'nombre': 'Nombre del producto',
            'laboratorio': 'Laboratorio del producto',
            'fecha_fabricacion': 'Fecha de fabricación del producto',
            'precio_costo': 'Precio de costo del producto',
            'precio_venta': 'Precio de venta del producto'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'laboratorio': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'fecha_fabricacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True, 'min': '2015-01-01'}),
            'precio_costo': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
        }

