from core.permissions import IsEnterprise
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from enterprise.models import Enterprise
from enterprise.serializers import EnterpriseSerializer


class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = [IsAuthenticated, IsEnterprise]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "company_name": ["exact", "icontains"],
        "owner_name": ["exact", "icontains"],
    }

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.role == "ADMIN":
            return Enterprise.objects.all()
        return Enterprise.objects.filter(user=user)

    def perform_destroy(self, instance):
        # Ao deletar uma instância de empresa, também deletamos o usuário associado a ela
        user = instance.user
        instance.delete() # Deleta a instância da empresa
        user.delete()  # Deleta o usuário associado à empresa


class EnterpriseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = [IsAuthenticated, IsEnterprise]
