from django.urls import path
from . import views

urlpatterns = [
    path('listado_productos/', views.listado_productos, name='listado_productos'),
    path('listado_proveedores/', views.listado_proveedores, name='listado_proveedores'),
    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('nuevo_proveedor/', views.nuevo_proveedor, name='nuevo_proveedor'),
]