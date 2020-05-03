from rest_framework import viewsets
from . import models
from . import serializers

class EmpleadoViewset(viewsets.ModelViewSet):
    queryset = models.Empleado.objects.all()
    serializer_class = serializers.EmpleadoSerializer