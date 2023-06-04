from django import forms
from compra.models import Producto, Proveedor

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('__all__')

    def clean_precio(self):
        precio = self.cleaned_data['precio']

        if precio < 0:
            raise forms.ValidationError('Ingrese un precio válido.')

        return precio

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('__all__')
    
    def clean_dni(self):
        dni = self.cleaned_data['dni']

        if dni > 99999999 or dni < 1000000:
            raise forms.ValidationError('Ingrese un DNI válido.')
        
        return dni