from appointments.models import Appointment
from rest_framework import viewsets, generics
from appointments.serializers import AppointmentSerializer
from rest_framework.permissions import AllowAny


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AppointmentSerializer
