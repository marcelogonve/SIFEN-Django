from django.db import models

class Emisor(models.Model):
    nombre = models.CharField(max_length=255)
    identificacion_tributaria = models.CharField(max_length=20) # Ejemplo: RUC, CI
    direccion = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    codigo_pais = models.CharField(max_length=5) # Ejemplo: PY
    tipo_documento_identidad = models.CharField(max_length=20) # Ejemplo: CI, RUC, pasaporte
    numero_documento_identidad = models.CharField(max_length=50) # Ejemplo: 1234567
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    actividad_economica = models.CharField(max_length=255, null=True, blank=True)

    # datos_adicionales = models.JSONField(null=True, blank=True) # TODO: Para cualquier otro dato relevante. En desuso por ahora.

    def __str__(self):
        return self.nombre
