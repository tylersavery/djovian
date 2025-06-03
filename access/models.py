from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return self.email

    bio = models.TextField(blank=True, null=True)
    avatar = models.FileField(blank=True, null=True)

    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    state = models.CharField(max_length=32, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    zipcode = models.CharField(max_length=16, blank=True, null=True)

    @property
    def avatar_url(self) -> str | None:
        return self.avatar.url if self.avatar else None
