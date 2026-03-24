from django.db import models

import shortuuid


class Enterprise(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=22,
        default=shortuuid.uuid,
        editable=False,
        unique=True
    )
    company_name = models.CharField(max_length=255, unique=True)
    user = models.OneToOneField(
        'user.User',
        on_delete=models.CASCADE,
        related_name='enterprise'
    )
    owner_name = models.CharField(max_length=255)
    logotipo = models.ImageField(upload_to='enterprise/logos/', null=True, blank=True)

    class Meta:
        verbose_name = "Enterprise"
        verbose_name_plural = "Enterprises"
        ordering = ['company_name']

    def __str__(self):
        return self.company_name
