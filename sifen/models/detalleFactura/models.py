from django.db import models
from sifen.models.factura.models import Factura

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='detalles')
    descripcion = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=2)
    descuento = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    impuesto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Puede ser una referencia a un modelo de Impuesto si es más complejo
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)  # Calculado como cantidad * precio_unitario - descuento + impuesto

    def __str__(self):
        return f"{self.descripcion} en factura {self.factura.cdc}"
