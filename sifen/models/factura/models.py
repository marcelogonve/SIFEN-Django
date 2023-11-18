from django.db import models
from sifen.models.emisor.models import Emisor
from sifen.models.receptor.models import Receptor

class Factura(models.Model):
    emisor = models.ForeignKey(Emisor, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    cdc = models.CharField(max_length=50) # Código de control
    fecha_emision = models.DateField()
    estado = models.CharField(max_length=50) # Ejemplo: emitida, cancelada, pagada. Dependiendo del estado recibido por el SIFEN
    numero_factura = models.CharField(max_length=50)
    numero_timbrado = models.CharField(max_length=50)
    tipo_factura = models.CharField(max_length=50) # Ejemplo: electrónica, tradicional.
    moneda = models.CharField(max_length=10) # Ejemplo: PYG
    tipo_cambio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_sin_impuestos = models.DecimalField(max_digits=15, decimal_places=2)
    total_impuestos = models.DecimalField(max_digits=15, decimal_places=2)
    total_con_impuestos = models.DecimalField(max_digits=15, decimal_places=2)
    condiciones_pago = models.TextField(null=True, blank=True) # Ejemplo: Contado, crédito a 30 días, etc.
    observaciones = models.TextField(null=True, blank=True)

    # datos_factura = models.JSONField() # TODO: En desuso de momento. Para cualquier otro dato relevante.

    def __str__(self):
        return f"Factura {self.cdc} - {self.estado}"
