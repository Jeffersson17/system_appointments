from django.urls import path
from appointments.views import AppointmentDetailView


urlpatterns = [
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
]
