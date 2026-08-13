from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "first_name": ["exact", "icontains"],
        "last_name": ["exact", "icontains"],
        "phone_number": ["exact", "icontains"],
    }

    def perform_destroy(self, instance):
        # Ao deletar uma instância de cliente, também deletamos o usuário associado a ela
        user = instance.user
        instance.delete()  # Deleta a instância do cliente
        user.delete()  # Deleta o usuário associado ao cliente


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
