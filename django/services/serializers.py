from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from enterprise.serializers import EnterpriseSerializer
from services.models import Services


class ServiceSerializer(serializers.ModelSerializer):
    enterprise = EnterpriseSerializer(read_only=True)

    class Meta:
        model = Services
        fields = ["id", "service_name", "price", "duration", "image_service", "description", "enterprise"]

    def create(self, validated_data):
        user = self.context["request"].user
        if user.role not in ["ENTERPRISE", "ADMIN"]:
            raise PermissionDenied("Você não tem permissão para criar um serviço.")
        if user.role == "ENTERPRISE":
            validated_data["enterprise"] = user.enterprise
        service = Services.objects.create(**validated_data)
        return service
