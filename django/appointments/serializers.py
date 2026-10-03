from appointments.models import Appointment
from rest_framework import serializers
from clients.serializers import ClientSerializer
from enterprise.serializers import EnterpriseSerializer
from services.serializers import ServiceSerializer
from rest_framework.exceptions import PermissionDenied


class AppointmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    enterprise = EnterpriseSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = ["scheduled_at", "observation", "status", "created_at", "client", "enterprise", "service"]

    def validate(self, data):
        user = self.context["request"].user
        if user.role == "CLIENT":
            client = user.client
            queryset = Appointment.objects.filter(client=client, status="SCHEDULED").exists()
            if self.instance:
                queryset = queryset.exclude(id=self.instance.id)
            if queryset.exists():
                raise serializers.ValidationError({"detail": "Você já possui um agendamento ativo."})
        return data

    def create(self, validated_data):
        user = self.request.user
        if user.role != "CLIENT":
            raise PermissionDenied("Apenas clientes podem criar agendamentos.")
        validated_data["client"] = user.client
        validated_data["enterprise"] = user.enterprise
        return super().create(validated_data)