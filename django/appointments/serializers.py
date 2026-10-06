from appointments.models import Appointment
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from clients.serializers import ClientSerializer
from enterprise.serializers import EnterpriseSerializer
from services.models import Services
from services.serializers import ServiceSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    enterprise = EnterpriseSerializer(read_only=True)
    service_detail = ServiceSerializer(source="service", read_only=True)
    service = serializers.PrimaryKeyRelatedField(
        queryset=Services.objects.all(),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Appointment
        fields = [
            "id",
            "scheduled_at",
            "observation",
            "status",
            "created_at",
            "client",
            "enterprise",
            "service",
            "service_detail",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["service"] = data.pop("service_detail", None)
        return data

    def validate(self, data):
        user = self.context["request"].user
        if user.role == "CLIENT":
            client = user.client
            queryset = Appointment.objects.filter(client=client, status="SCHEDULED")
            if self.instance:
                queryset = queryset.exclude(id=self.instance.id)
            if queryset.exists():
                raise serializers.ValidationError({"detail": "Você já possui um agendamento ativo."})
        return data

    def create(self, validated_data):
        user = self.context["request"].user
        if user.role != "CLIENT":
            raise PermissionDenied("Apenas clientes podem criar agendamentos.")
        validated_data["client"] = user.client
        validated_data["enterprise"] = user.client.enterprise
        return super().create(validated_data)
