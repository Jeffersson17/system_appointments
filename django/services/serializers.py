from rest_framework import serializers

from enterprise.serializers import EnterpriseSerializer
from services.models import Services


class ServiceSerializer(serializers.ModelSerializer):
    enterprise = EnterpriseSerializer(read_only=True)

    class Meta:
        model = Services
        fields = ["id", "service_name", "price", "duration", "image_service", "description", "enterprise"]
