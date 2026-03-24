from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

import shortuuid


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role='CLIENT', **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, role='ADMIN', **extra_fields)


class User(AbstractUser):
    id = models.CharField(
        primary_key=True,
        max_length=22,
        default=shortuuid.uuid,
        editable=False,
        unique=True
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ('ADMIN', 'Admin'),
            ('ENTERPRISE', 'Enterprise'),
            ('CLIENT', 'Client'),
        ],
        default='CLIENT'
    )

    REQUIRED_FIELDS = ["name"]
    USERNAME_FIELD = "email"
    username = None

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['name']
