from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {"name": ["exact", "icontains"], "email": ["exact", "icontains"]}


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
