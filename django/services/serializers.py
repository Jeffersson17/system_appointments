from services.models import Services
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['__all__']
