from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre_completo = models.CharField(max_length=100)
    legajo = models.CharField(max_length=4)
    telefono = models.CharField(max_length=10)

# Create -> POST
# Read -> GET
# Update -> PUT
# Delete -> DELETE