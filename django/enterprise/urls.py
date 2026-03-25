from django.urls import path

from enterprise.views import EnterpriseDetailView

urlpatterns = [
    path("enterprise/<int:pk>/", EnterpriseDetailView.as_view(), name="enterprise-detail"),
]
