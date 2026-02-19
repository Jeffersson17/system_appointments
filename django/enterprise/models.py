import shortuuid

from django.db import models


class Enterprise(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=22,
        default=shortuuid.uuid,
        editable=False,
        unique=True
    )
    company_name = models.CharField(max_length=255, unique=True)
    owner_name = models.CharField(max_length=255)
    logotipo = models.ImageField(upload_to='enterprise/logos/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Enterprise"
        verbose_name_plural = "Enterprises"
        ordering = ['company_name']

    def __str__(self):
        return self.company_name


