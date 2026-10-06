from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if user.role == "ADMIN":
            return queryset
        if user.role == "CLIENT":
            return queryset.filter(client=user.client)
        return queryset.filter(enterprise=user.enterprise)


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AppointmentSerializer
