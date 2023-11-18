from django.db import models

class Receptor(models.Model):
    nombre = models.CharField(max_length=255)
    identificacion_tributaria = models.CharField(max_length=20)  # Ejemplo: RUC, CI
    direccion = models.CharField(max_length=255, null=True, blank=True) # Opcional, dependiendo del caso de uso
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    tipo_documento_identidad = models.CharField(max_length=20, null=True, blank=True) # Ejemplo: CI, RUC, pasaporte
    numero_documento_identidad = models.CharField(max_length=50, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    codigo_postal = models.CharField(max_length=10, null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True) # En caso de ser un receptor extranjero

    def __str__(self):
        return self.nombre

