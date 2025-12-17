import shortuuid

from enterprise.models import Enterprise

from django.db import models


class Clients(models.Model):
    id = models.CharField(
        primary_key=True,
        default=shortuuid.uuid,
        max_length=22,
        editable=False,
        unique=True
    )
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name='clients')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

