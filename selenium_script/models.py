from django.db import models


class Datos(models.Model):
    numero = models.TextField(null=True, blank=True)
    expediente = models.TextField(null=True, blank=True)
    unidad_fiscalizable = models.TextField(null=True, blank=True)
    nombre_razon_social = models.TextField(null=True, blank=True)
    categoria = models.TextField(null=True, blank=True)
    region = models.TextField(null=True, blank=True)
    estado = models.TextField(null=True, blank=True)
    detalle = models.TextField(null=True, blank=True)