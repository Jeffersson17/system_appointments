from rest_framework import generics, viewsets

from enterprise.models import Enterprise
from enterprise.serializers import EnterpriseSerializer


class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer


class EnterpriseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
