import shortuuid
from django.db import models

from enterprise.models import Enterprise


class Services(models.Model):
    id = models.CharField(primary_key=True, default=shortuuid.uuid, max_length=22, editable=False, unique=True)
    service_name = models.CharField(max_length=255)
    image_service = models.ImageField(upload_to="services/images/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    description = models.TextField(null=True, blank=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name="services")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["service_name"]

    def __str__(self):
        return self.service_name
