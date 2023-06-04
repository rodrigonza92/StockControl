from django.contrib import admin
from compra.models import Producto, Proveedor

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ("id", "nombre", "precio", "stock_actual", "proveedor")
    search_fields = ("nombre", "precio", "stock_actual", "proveedor",)
    list_filter = ("nombre", "precio", "stock_actual", "proveedor",)

class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor
    list_display = ("id", "nombre", "apellido", "dni")
    search_fields = ("nombre", "apellido", "dni",)
    list_filter = ("nombre", "apellido", "dni",)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
