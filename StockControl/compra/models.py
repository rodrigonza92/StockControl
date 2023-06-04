from django.db import models

class Proveedor(models.Model):
    """
    Modelo que representa un Proveedor

    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} {self.dni}"
    
class Producto(models.Model):
    """
    Modelo que representa un Producto

    """
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey (
        Proveedor,
        related_name='proveedor',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.nombre} {self.precio} {self.stock_actual} {self.proveedor}"