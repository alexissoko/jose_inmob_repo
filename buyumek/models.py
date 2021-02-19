from django.db import models

# Create your models here.
class Propiedad(models.Model):
    nombre = models.CharField(max_length=128)
    tipo = models.CharField(max_length=128)
    ambientes = models.IntegerField(blank=True, null=True)
    modalidad = models.CharField(max_length=512, blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    
    """
    from buyumek.models import Propiedad
    propiedad2 = Propiedad(
    nombre="Obispo Trejo 3",
    tipo="local",
    modalidad="Alquiler",
    precio=23000.00
    )
    propiedad1.save()
    """