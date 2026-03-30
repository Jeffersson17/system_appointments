from appointments.views import AppointmentDetailView
from django.urls import path

urlpatterns = [
    path("appointments/<int:pk>/", AppointmentDetailView.as_view(), name="appointment-detail"),
]
