from rest_framework import serializers

from clients.models import Client
from enterprise.serializers import EnterpriseSerializer
from user.serializers import UserSerializer


class ClientSerializer(serializers.ModelSerializer):
    enterprise = EnterpriseSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'enterprise', 'user']
