from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    ruc_ci = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nombre
