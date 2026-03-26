from core.permissions import IsEnterprise
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from services.models import Services
from services.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated, IsEnterprise]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "service_name": ["exact", "icontains"],
    }


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    permission_classes = [IsAuthenticated, IsEnterprise]
    serializer_class = ServiceSerializer
