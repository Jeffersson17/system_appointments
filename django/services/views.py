from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from services.models import Services
from services.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "service_name" : ["exact", "icontains"],
    }



class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
