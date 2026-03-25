from django.urls import path

from clients.views import ClientDetailView

urlpatterns = [
    path("client/<int:pk>/", ClientDetailView.as_view(), name="client-detail"),
]
