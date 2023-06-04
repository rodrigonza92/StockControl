from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import (CreateView)

from compra.forms import ProductoForm
from compra.models import Producto, Proveedor

#Listado de Productos
def listado_productos(request):
    productos = Producto.objects.all()
    context = {
        'productos':productos
    }
    return render(request, 'compra/listado_productos.html', context)

#Bonus (No obligatorio)
def listado_proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {
        'proveedores':proveedores
    }
    return render(request, 'compra/listado_proveedores.html', context)

def nuevo_producto(request):
    proveedores = Proveedor.objects.all()
    context = {
        'proveedores':proveedores
    }
    if request.POST:
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        stock_actual = request.POST['stock_actual'] 
        proveedor_id = request.POST['proveedor']

        Producto.objects.create(
            nombre = nombre,
            precio=precio,
            stock_actual=stock_actual,
            proveedor_id=proveedor_id,
        )
        return redirect('listado_productos')
    
    return render(request, 'compra/nuevo_producto.html', context)


def nuevo_proveedor(request):
    if request.POST:
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        dni = request.POST['dni']

        Proveedor.objects.create(
            nombre = nombre,
            apellido = apellido,
            dni = dni,
        )
        return redirect('listado_proveedores')
    return render(request, 'compra/nuevo_proveedor.html')