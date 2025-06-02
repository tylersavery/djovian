from django.conf import settings
from django.db import models

from project.models import AbstractModel
from access.models import User


class Example(AbstractModel):

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="example/", blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta(AbstractModel.Meta):
        ordering = ["-created_at"]
