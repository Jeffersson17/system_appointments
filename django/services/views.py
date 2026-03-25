from rest_framework import viewsets

from services.models import Services
from services.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
