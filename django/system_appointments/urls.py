from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from clients.views import ClientViewSet
from enterprise.views import EnterpriseViewSet
from services.views import ServiceViewSet
from user.views import UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"services", ServiceViewSet)
router.register(r"enterprises", EnterpriseViewSet)
router.register(r"clients", ClientViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
