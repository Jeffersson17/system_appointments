from appointments.models import Appointment
from rest_framework import serializers
from clients.serializers import ClientSerializer
from enterprise.serializers import EnterpriseSerializer
from services.serializers import ServiceSerializer


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
