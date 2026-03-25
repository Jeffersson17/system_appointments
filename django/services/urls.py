from django.urls import path

from services.views import ServiceDetailView

urlpatterns = [
    path("services/<int:pk>/", ServiceDetailView.as_view(), name="service-detail"),
]
