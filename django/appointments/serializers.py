from appointments.models import Appointment
from rest_framework import serializers


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

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
