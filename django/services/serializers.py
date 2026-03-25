from rest_framework import serializers

from services.models import Services
from enterprise.serializers import EnterpriseSerializer


class ServiceSerializer(serializers.ModelSerializer):
    enterprise = EnterpriseSerializer(read_only=True)
    class Meta:
        model = Services
        fields = ["id", "service_name", "price", "duration", "image_service", "description", "enterprise"]
