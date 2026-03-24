import shortuuid

from enterprise.models import Enterprise

from django.db import models


class Client(models.Model):
    id = models.CharField(
        primary_key=True,
        default=shortuuid.uuid,
        max_length=22,
        editable=False,
        unique=True
    )
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(
        'user.User', 
        on_delete=models.CASCADE, 
        related_name='client'
    )
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    enterprise = models.ForeignKey(
        Enterprise, 
        on_delete=models.CASCADE, 
        related_name='clients'
    )

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

