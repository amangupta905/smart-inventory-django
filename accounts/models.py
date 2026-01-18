from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('sales', 'Sales'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


# Create your models here.
