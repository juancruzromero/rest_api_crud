from empleado.viewsets import EmpleadoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('empleado', EmpleadoViewset )