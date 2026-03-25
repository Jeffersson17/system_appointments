from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from enterprise.models import Enterprise
from enterprise.serializers import EnterpriseSerializer


class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "company_name": ["exact", "icontains"],
        "owner_name": ["exact", "icontains"],
    }


class EnterpriseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
